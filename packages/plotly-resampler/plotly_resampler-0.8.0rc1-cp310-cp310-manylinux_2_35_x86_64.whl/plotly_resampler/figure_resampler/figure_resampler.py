# -*- coding: utf-8 -*-
"""
``FigureResampler`` wrapper around the plotly ``go.Figure`` class.

Creates a web-application and uses ``dash`` callbacks to enable dynamic resampling.

"""

from __future__ import annotations

__author__ = "Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost"

import warnings
from typing import Tuple, List

import dash
import plotly.graph_objects as go
from dash import Dash
from jupyter_dash import JupyterDash
from plotly.basedatatypes import BaseFigure
from trace_updater import TraceUpdater

from ..aggregation import AbstractSeriesAggregator, EfficientLTTB
from .figure_resampler_interface import AbstractFigureAggregator
from .utils import is_figure, is_fr


class FigureResampler(AbstractFigureAggregator, go.Figure):
    """Data aggregation functionality for ``go.Figures``."""

    def __init__(
        self,
        figure: BaseFigure | dict = None,
        convert_existing_traces: bool = True,
        default_n_shown_samples: int = 1000,
        default_downsampler: AbstractSeriesAggregator = EfficientLTTB(),
        resampled_trace_prefix_suffix: Tuple[str, str] = (
            '<b style="color:sandybrown">[R]</b> ',
            "",
        ),
        show_mean_aggregation_size: bool = True,
        convert_traces_kwargs: dict | None = None,
        verbose: bool = False,
        show_dash_kwargs: dict | None = None,
    ):
        """Initialize a dynamic aggregation data mirror using a dash web app.

        Parameters
        ----------
        figure: BaseFigure
            The figure that will be decorated. Can be either an empty figure
            (e.g., ``go.Figure()``, ``make_subplots()``, ``go.FigureWidget``) or an
            existing figure.
        convert_existing_traces: bool
            A bool indicating whether the high-frequency traces of the passed ``figure``
            should be resampled, by default True. Hence, when set to False, the
            high-frequency traces of the passed ``figure`` will not be resampled.
        default_n_shown_samples: int, optional
            The default number of samples that will be shown for each trace,
            by default 1000.\n
            .. note::
                * This can be overridden within the :func:`add_trace` method.
                * If a trace withholds fewer datapoints than this parameter,
                  the data will *not* be aggregated.
        default_downsampler: AbstractSeriesDownsampler
            An instance which implements the AbstractSeriesDownsampler interface and
            will be used as default downsampler, by default ``EfficientLTTB`` with
            _interleave_gaps_ set to True. \n
            .. note:: This can be overridden within the :func:`add_trace` method.
        resampled_trace_prefix_suffix: str, optional
            A tuple which contains the ``prefix`` and ``suffix``, respectively, which
            will be added to the trace its legend-name when a resampled version of the
            trace is shown. By default a bold, orange ``[R]`` is shown as prefix
            (no suffix is shown).
        show_mean_aggregation_size: bool, optional
            Whether the mean aggregation bin size will be added as a suffix to the trace
            its legend-name, by default True.
        convert_traces_kwargs: dict, optional
            A dict of kwargs that will be passed to the :func:`add_traces` method and
            will be used to convert the existing traces. \n
            .. note::
                This argument is only used when the passed ``figure`` contains data and
                ``convert_existing_traces`` is set to True.
        verbose: bool, optional
            Whether some verbose messages will be printed or not, by default False.
        show_dash_kwargs: dict, optional
            A dict that will be used as default kwargs for the :func:`show_dash` method. 
            Note that the passed kwargs will be take precedence over these defaults.

        """
        # Parse the figure input before calling `super`
        if is_figure(figure) and not is_fr(figure):
            # A go.Figure
            # => base case: the figure does not need to be adjusted
            f = figure
        else:
            # Create a new figure object and make sure that the trace uid will not get
            # adjusted when they are added.
            f = self._get_figure_class(go.Figure)()
            f._data_validator.set_uid = False

            if isinstance(figure, BaseFigure):
                # A base figure object, can be;
                # - a go.FigureWidget
                # - a plotly-resampler figure: subclass of AbstractFigureAggregator
                # => we first copy the layout, grid_str and grid ref
                f.layout = figure.layout
                f._grid_str = figure._grid_str
                f._grid_ref = figure._grid_ref
                f.add_traces(figure.data)
            elif isinstance(figure, dict) and (
                "data" in figure or "layout" in figure # or "frames" in figure  # TODO
            ):
                # A figure as a dict, can be;
                # - a plotly figure as a dict (after calling `fig.to_dict()`)
                # - a pickled (plotly-resampler) figure (after loading a pickled figure)
                # => we first copy the layout, grid_str and grid ref
                f.layout = figure.get("layout")
                f._grid_str = figure.get("_grid_str")
                f._grid_ref = figure.get("_grid_ref")
                f.add_traces(figure.get("data"))
                # `pr_props` is not None when loading a pickled plotly-resampler figure
                f._pr_props = figure.get("pr_props")
                # `f._pr_props`` is an attribute to store properties of a
                # plotly-resampler figure. This attribute is only used to pass
                # information to the super() constructor. Once the super constructor is
                # called, the attribute is removed.

                # f.add_frames(figure.get("frames")) TODO
            elif isinstance(figure, (dict, list)):
                # A single trace dict or a list of traces
                f.add_traces(figure)

        self._show_dash_kwargs = show_dash_kwargs if show_dash_kwargs is not None else {}

        super().__init__(
            f,
            convert_existing_traces,
            default_n_shown_samples,
            default_downsampler,
            resampled_trace_prefix_suffix,
            show_mean_aggregation_size,
            convert_traces_kwargs,
            verbose,
        )

        if isinstance(figure, AbstractFigureAggregator):
            # Copy the `_hf_data` if the previous figure was an AbstractFigureAggregator
            # and adjust the default `max_n_samples` and `downsampler`
            self._hf_data.update(
                self._copy_hf_data(figure._hf_data, adjust_default_values=True)
            )

            # Note: This hack ensures that the this figure object initially uses
            # data of the whole view. More concretely; we create a dict
            # serialization figure and adjust the hf-traces to the whole view
            # with the check-update method (by passing no range / filter args)
            with self.batch_update():
                graph_dict: dict = self._get_current_graph()
                update_indices = self._check_update_figure_dict(graph_dict)
                for idx in update_indices:
                    self.data[idx].update(graph_dict["data"][idx])

        # The FigureResampler needs a dash app
        self._app: JupyterDash | Dash | None = None
        self._port: int | None = None
        self._host: str | None = None

    def show_dash(
        self,
        mode=None,
        config: dict | None = None,
        graph_properties: dict | None = None,
        **kwargs,
    ):
        """Registers the :func:`update_graph` callback & show the figure in a dash app.

        Parameters
        ----------
        mode: str, optional
            Display mode. One of:\n
              * ``"external"``: The URL of the app will be displayed in the notebook
                output cell. Clicking this URL will open the app in the default
                web browser.
              * ``"inline"``: The app will be displayed inline in the notebook output
                cell in an iframe.
              * ``"jupyterlab"``: The app will be displayed in a dedicated tab in the
                JupyterLab interface. Requires JupyterLab and the ``jupyterlab-dash``
                extension.
            By default None, which will result in the same behavior as ``"external"``.
        config: dict, optional
            The configuration options for displaying this figure, by default None.
            This ``config`` parameter is the same as the dict that you would pass as
            ``config`` argument to the `show` method.
            See more https://plotly.com/python/configuration-options/
        graph_properties: dict, optional
            Dictionary of (keyword, value) for the properties that should be passed to
            the dcc.Graph, by default None.
            e.g.: {"style": {"width": "50%"}}
            Note: "config" is not allowed as key in this dict, as there is a distinct
            ``config`` parameter for this property in this method.
            See more https://dash.plotly.com/dash-core-components/graph
        **kwargs: dict
            Additional app.run_server() kwargs. e.g.: port, ...
            Also note that these kwargs take precedence over the ones passed to the
            constructor via the ``show_dash_kwargs`` argument.

        """
        graph_properties = {} if graph_properties is None else graph_properties
        assert "config" not in graph_properties.keys()  # There is a param for config
        # 1. Construct the Dash app layout
        app = JupyterDash("local_app")
        app.layout = dash.html.Div(
            [
                dash.dcc.Graph(
                    id="resample-figure", figure=self, config=config, **graph_properties
                ),
                TraceUpdater(
                    id="trace-updater", gdID="resample-figure", sequentialUpdate=False
                ),
            ]
        )
        self.register_update_graph_callback(app, "resample-figure", "trace-updater")

        # 2. Run the app
        if (
            mode == "inline"
            and "height" not in kwargs
        ):
            # If app height is not specified -> re-use figure height for inline dash app
            #  Note: default layout height is 450 (whereas default app height is 650)
            #  See: https://plotly.com/python/reference/layout/#layout-height
            fig_height = self.layout.height if self.layout.height is not None else 450
            kwargs["height"] = fig_height + 18

        # kwargs take precedence over the show_dash_kwargs
        kwargs = {**self._show_dash_kwargs, **kwargs}

        # Store the app information, so it can be killed
        self._app = app
        self._host = kwargs.get("host", "127.0.0.1")
        self._port = kwargs.get("port", "8050")

        app.run_server(mode=mode, **kwargs)

    def stop_server(self, warn: bool = True):
        """Stop the running dash-app.

        Parameters
        ----------
        warn: bool
            Whether a warning message will be shown or  not, by default True.

        .. attention::
            This only works if the dash-app was started with :func:`show_dash`.
        """
        if self._app is not None:

            old_server = self._app._server_threads.get((self._host, self._port))
            if old_server:
                old_server.kill()
                old_server.join()
                del self._app._server_threads[(self._host, self._port)]
        elif warn:
            warnings.warn(
                "Could not stop the server, either the \n"
                + "\t- 'show-dash' method was not called, or \n"
                + "\t- the dash-server wasn't started with 'show_dash'"
            )

    def register_update_graph_callback(
        self, app: dash.Dash, graph_id: str, trace_updater_id: str
    ):
        """Register the :func:`construct_update_data` method as callback function to
        the passed dash-app.

        Parameters
        ----------
        app: Union[dash.Dash, JupyterDash]
            The app in which the callback will be registered.
        graph_id:
            The id of the ``dcc.Graph``-component which withholds the to-be resampled
            Figure.
        trace_updater_id
            The id of the ``TraceUpdater`` component. This component is leveraged by
            ``FigureResampler`` to efficiently POST the to-be-updated data to the
            front-end.

        """
        app.callback(
            dash.dependencies.Output(trace_updater_id, "updateData"),
            dash.dependencies.Input(graph_id, "relayoutData"),
            prevent_initial_call=True,
        )(self.construct_update_data)

    def _get_pr_props_keys(self) -> List[str]:
        # Add the additional plotly-resampler properties of this class
        return super()._get_pr_props_keys() + ["_show_dash_kwargs"]

    def _ipython_display_(self):
        # To display the figure inline as a dash app
        self.show_dash(mode="inline")
