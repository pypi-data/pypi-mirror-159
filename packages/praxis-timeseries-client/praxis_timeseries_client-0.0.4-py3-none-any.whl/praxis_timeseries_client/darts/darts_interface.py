"""
Darts Interface Class

Synthesizes covariate timeseries and target timeseries into a module for plotting
and running backtests and forecasts.
"""
from enum import Enum
from typing import Any, Optional, Union, List, Tuple, Dict

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from darts import TimeSeries
from darts.models.forecasting.forecasting_model import ForecastingModel
from darts.utils.statistics import (
    extract_trend_and_seasonality,
    granger_causality_tests,
)
from darts.utils.utils import ModelMode
from plotly.subplots import make_subplots

from .darts_backtest import DartsBacktest
from .darts_forecast import DartsForecast
from .utils import stack_timeseries

# ---------------------------------------------------------------------------- #
#                                     ENUMS                                    #
# ---------------------------------------------------------------------------- #


class DartsComponentType(Enum):
    """An enum for encoding types of components.

    Covariates are used in actual training of the model. Discretes are not
    necessarily timeseries, but rather just variables that can be plotted
    alongside the main Darts data."""

    PAST_COVARIATE = 1
    FUTURE_COVARIATE = 2
    PAST_DISCRETE = 3
    FUTURE_DISCRETE = 4


class DartsDiscreteComponent:
    """A wrapper around discrete variables"""

    df: pd.DataFrame
    type: DartsComponentType
    comp_name: str
    col_time: str
    col_value: str
    col_tooltip: str
    mask: Any

    # -------------------------------- PROPERTIES -------------------------------- #

    @property
    def time_col(self) -> pd.DataFrame:
        return (
            self.df.loc[self.mask][self.col_time]
            if self.mask is not None
            else self.df[self.col_time]
        )

    @property
    def value_col(self) -> pd.DataFrame:
        return (
            self.df.loc[self.mask][self.col_value]
            if self.mask is not None
            else self.df[self.col_value]
        )

    @property
    def tooltip_col(self) -> pd.DataFrame:
        return (
            self.df.loc[self.mask][self.col_tooltip]
            if self.mask is not None
            else self.df[self.col_tooltip]
        )

    @property
    def plot_data(self) -> Dict[str, Any]:
        """Returns x, y, and hovertext for plotting in go.Scatter"""
        return dict(
            x=self.time_col,
            y=self.value_col,
            hovertext=self.tooltip_col,
            mode="markers",
            name="{}:{}".format(self.comp_name, self.col_value),
        )

    # ------------------------------- FUNCTIONALITY ------------------------------ #

    def __init__(
        self,
        key: str,
        df: pd.DataFrame,
        type: Union[str, DartsComponentType],
        time_col: str,
        value_col: str,
        tooltip_col: str,
        mask: Any = None,
    ):
        """Initializes a discrete component from a dict"""
        self.df = df
        self.comp_name = key
        self.col_time = time_col
        self.col_value = value_col
        self.col_tooltip = tooltip_col
        if isinstance(type, str):
            self.type = (
                DartsComponentType.PAST_DISCRETE
                if type == "past"
                else DartsComponentType.FUTURE_DISCRETE
            )
        else:
            self.type = type
        self.mask = mask

    def split_at(self, date) -> Tuple[Any, Any]:
        """Splits the discrete component at a specific time"""
        if isinstance(date, pd.Timestamp):
            date = date.to_datetime64()
        mask_before = self.time_col < date
        mask_after = self.time_col >= date
        return (
            DartsDiscreteComponent(
                key=self.comp_name,
                df=self.df,
                type=self.type,
                time_col=self.col_time,
                value_col=self.col_value,
                tooltip_col=self.col_tooltip,
                mask=mask_before,
            ),
            DartsDiscreteComponent(
                key=self.comp_name,
                df=self.df,
                type=self.type,
                time_col=self.col_time,
                value_col=self.col_value,
                tooltip_col=self.col_tooltip,
                mask=mask_after,
            ),
        )


# ---------------------------------------------------------------------------- #
#                                DARTS INTERFACE                               #
# ---------------------------------------------------------------------------- #


class DartsInterface:
    """An interface for using Darts to run forecasts, backtests, and view data.

    Initialize with a target timeseries to use, as well as covariates (past and future).
    Discrete variables (not necessarily timeseries) may also be supplied to enable
    deeper analysis into variance in the data. Once visualization is sastisfied,
    backtests and forecasts can be run using any model in a plug-and-play manner.

    Example usage:
    ```python
    train = TimeSeries.from_dataframe(df_train, time_col="date", value_cols=["meantemp"])
    train_past_covs = TimeSeries.from_dataframe(df_train, time_col="date", value_cols=["humidity", "wind_speed"])

    dbi = DartsForecasterInterface(train, past_covs_ts=train_past_covs)
    dbi.plot().show()
    ```"""

    today_time: pd.Timestamp
    target_ts: TimeSeries
    past_covariates: Optional[TimeSeries]
    future_covariates: Optional[TimeSeries]
    discrete_vars: Optional[Dict[str, DartsDiscreteComponent]]

    def __init__(
        self,
        target_ts: TimeSeries,
        past_covs_ts: Optional[Union[List[TimeSeries], TimeSeries]] = None,
        future_covs_ts: Optional[Union[List[TimeSeries], TimeSeries]] = None,
        discrete_vars: Optional[
            Dict[str, Union[Dict[str, Any], DartsDiscreteComponent]]
        ] = None,
        today_time: pd.Timestamp = None,
        causality_score: dict = {},
    ):
        """Initialize a Darts interface with a set of covariates and variables.

        If passing in a list of TimeSeries for either covariate input, the time
        range will be stripped to that of the first Time Series in the list, with
        its frequency. So to not lose any data, make sure you pass in the largest
        range timeseries first in the list."""
        self.target_ts = target_ts
        if past_covs_ts and isinstance(past_covs_ts, list):
            past_covs_ts = stack_timeseries(past_covs_ts)
        if future_covs_ts and isinstance(future_covs_ts, list):
            future_covs_ts = stack_timeseries(future_covs_ts)
        if discrete_vars and isinstance(discrete_vars, dict):
            self.discrete_vars = {
                k: DartsDiscreteComponent(key=k, **v)
                if not isinstance(v, DartsDiscreteComponent)
                else v
                for k, v in discrete_vars.items()
            }
        if not today_time:
            today_time = self.target_ts.time_index[-1]
        self.today_time = today_time
        self.past_covariates = past_covs_ts
        self.future_covariates = future_covs_ts
        self.causality_score = causality_score

    # ---------------------------------------------------------------------------- #
    #                                  PROPERTIES                                  #
    # ---------------------------------------------------------------------------- #

    @property
    def covariates(self) -> List[str]:
        """The list of all covariates in this interface, past and future"""
        covariates = []
        if self.past_covariates:
            covariates.extend(self.past_covariates.components.to_list())
        if self.future_covariates:
            covariates.extend(self.future_covariates.components.to_list())
        return covariates

    @property
    def discretes(self) -> List[str]:
        """The list of all discretes in this interface"""
        return list(self.discrete_vars.keys())

    def get_component_type(self, comp: str) -> DartsComponentType:
        """Gets the type of a component, throwing if not in this interface"""
        if self.past_covariates and comp in self.past_covariates.components:
            return DartsComponentType.PAST_COVARIATE
        elif self.future_covariates and comp in self.future_covariates.components:
            return DartsComponentType.FUTURE_COVARIATE
        elif self.discrete_vars and comp in self.discrete_vars:
            return self.discrete_vars[comp].type
        else:
            raise ValueError(
                "Component '{}' not in interface with covariates: {} and discretes: {}".format(
                    comp, self.covariates, self.discretes
                )
            )

    def get_component_plot_data(
        self, comp: str, future_begins_at: pd.Timestamp = None
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """Returns go.Scatter information for plotting a component"""
        traces = []
        annotation_text = None
        comp_type = self.get_component_type(comp)
        # split the past covariates before and after future
        if comp_type == DartsComponentType.PAST_COVARIATE:
            past_covariates_before = self.past_covariates
            past_covariates_after = None
            if future_begins_at < self.past_covariates.time_index[-1]:
                (
                    past_covariates_before,
                    past_covariates_after,
                ) = self.past_covariates.split_before(future_begins_at)
            traces.append(
                dict(
                    x=past_covariates_before.time_index,
                    y=past_covariates_before._xa.sel(component=comp).values[:, 0],
                    mode="lines",
                    name=comp,
                )
            )
            if past_covariates_after:
                traces.append(
                    dict(
                        x=past_covariates_after.time_index,
                        y=past_covariates_after._xa.sel(component=comp).values[:, 0],
                        mode="lines",
                        name=comp,
                    )
                )
            annotation_text = "[PAST COVARIATE] {}".format(comp)
        # past discretes are also split, but this is much more forgiving and won't throw error
        elif comp_type == DartsComponentType.PAST_DISCRETE:
            past_discretes_before, past_discretes_after = self.discrete_vars[
                comp
            ].split_at(future_begins_at)
            traces.append(past_discretes_before.plot_data)
            traces.append(past_discretes_after.plot_data)
            annotation_text = "[PAST DISCRETE] {}:{}".format(
                comp, self.discrete_vars[comp].col_value
            )
        # future covariates and discretes are returned as-is
        elif comp_type == DartsComponentType.FUTURE_COVARIATE:
            traces.append(
                dict(
                    x=self.future_covariates.time_index,
                    y=self.future_covariates._xa.sel(component=comp).values[:, 0],
                    mode="lines",
                    name=comp,
                )
            )
            annotation_text = "[FUTURE COVARIATE] {}".format(comp)
        elif comp_type == DartsComponentType.FUTURE_DISCRETE:
            traces.append(self.discrete_vars[comp].plot_data)
            annotation_text = "[FUTURE DISCRETE] {}:{}".format(
                comp, self.discrete_vars[comp].col_value
            )
        return traces, annotation_text

    def last_time(self, components: Optional[List[str]] = None) -> pd.Timestamp:
        """Gets the last possible time from covariates in a list"""
        if not components:
            components = self.covariates
        max_date = self.target_ts.end_time()
        for comp in components:
            comp_type = self.get_component_type(comp)
            end_time = None
            if (
                comp_type == DartsComponentType.PAST_DISCRETE
                or comp_type == DartsComponentType.FUTURE_DISCRETE
            ):
                continue
            elif comp_type == DartsComponentType.PAST_COVARIATE:
                end_time = self.past_covariates.end_time()
            else:
                end_time = self.future_covariates.end_time()
            if max_date < end_time:
                max_date = end_time
        return max_date

    # ---------------------------------------------------------------------------- #
    #                                  FORECASTING                                 #
    # ---------------------------------------------------------------------------- #

    def backtest(self, model: ForecastingModel, start: pd.Timestamp, **kwargs):
        """Creates a DartsBacktest and runs the backtest given a model.

        Args:
            model (ForecastingModel): Model to use for forecasting
            start (pd.Timestamp): When to begin the backtest

        Returns:
            DartsBacktest: A backtest instance representing a historical forecast.
        """
        return DartsBacktest(self, model, start=start, **kwargs)

    def forecast(self, model: ForecastingModel, n: int, **kwargs):
        """Creates a DartsForecast and runs the forecast given a model.

        Args:
            model (ForecastingModel): Model to use for forecasting
            n (int): How many time steps to forecast into

        Returns:
            DartsForecast: A forecast instance representing a future forecast.
        """
        return DartsForecast(self, model, n=n, **kwargs)

    # ---------------------------------------------------------------------------- #
    #                                 VISUALIZATION                                #
    # ---------------------------------------------------------------------------- #

    # plot the input timeseries.
    def plot(
        self,
        components: List[str] = None,
        future_begins_at: Optional[Union[pd.Timestamp, float]] = None,
        future_opacity: float = 0.4,
        title="Data Interface: Pre-forecast",
        with_residual_space: bool = False,
    ):
        """Plots the covariates and discretes

        Args:
            components (list, optional): An ordered list of components to plot. Defaults to None.
            split_at (pd.Timestamp, optional): When to denote the past-future split in the plot. Defaults to None.

        Returns:
            _type_: _description_
        """
        # if no covs passed in, display all covariates
        if components is None:
            components = [*self.covariates, *self.discretes]
        total_subplots = len(components) + 2 + int(with_residual_space)

        # keep track of the minimum and maximum date
        ts_begin = self.target_ts.start_time()
        ts_end = future_begins_at or self.today_time
        ts_future_end = self.last_time(components)

        # keep track of the color index
        i = 1
        cind = 0

        # begin building the subplots
        TARGET_HEIGHT = 240
        COMPONENT_HEIGHT = 60
        TOTAL_HEIGHT = TARGET_HEIGHT + COMPONENT_HEIGHT * total_subplots
        fig = make_subplots(
            rows=1 + total_subplots,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            row_heights=[
                TARGET_HEIGHT / TOTAL_HEIGHT,
                *([COMPONENT_HEIGHT / TOTAL_HEIGHT] * (total_subplots)),
            ],
        )

        # ---------------------------- TARGET PLOT --------------------------- #

        # split the target plot into before and after
        target_before = self.target_ts
        target_after = None
        if ts_end < self.target_ts.time_index[-1]:
            _, target_after = self.target_ts.split_before(ts_end)
            target_before, _ = self.target_ts.split_after(ts_end)

        # print(target_before)

        trend_before, seasonality_before = extract_trend_and_seasonality(
            target_before, model=ModelMode.ADDITIVE
        )
        trend_after, seasonality_after = None, None
        if target_after and len(target_after) > 14:
            trend_after, seasonality_after = extract_trend_and_seasonality(
                target_after, model=ModelMode.ADDITIVE
            )

        # plot up to the first 10 components
        for c in self.target_ts._xa.component[:10]:
            for j, (target_ts, trend_ts, seasonality_ts) in enumerate(
                zip(
                    [target_before, target_after],
                    [trend_before, trend_after],
                    [seasonality_before, seasonality_after],
                )
            ):
                if not target_ts:
                    continue
                comp_name = str(c.values)
                comp = target_ts._xa.sel(component=c)

                fig.append_trace(
                    go.Scatter(
                        x=target_ts.time_index,
                        y=comp.values[:, 0],
                        mode="lines",
                        line=dict(color=px.colors.qualitative.Plotly[cind % 10],width=1),
                        opacity=future_opacity if j > 0 else 1.0,
                        showlegend=(j == 0),
                        name="ACTUAL: {}".format(comp_name),
                    ),
                    row=1,
                    col=1,
                )

                if trend_ts and seasonality_ts:
                    comp_trend = trend_ts._xa
                    comp_seasonality = seasonality_ts._xa
                    # print(comp_trend.values.shape)
                    # print(comp.values[:, 0].shape)
                    # print(comp_trend.values[:, 0].shape)

                    fig.append_trace(
                        go.Scatter(
                            x=target_ts.time_index,
                            y=comp_trend.values[:, 0, 0],
                            mode="lines",
                            line=dict(color=px.colors.qualitative.Plotly[cind % 10],),
                            opacity=future_opacity if j > 0 else 1.0,
                            showlegend=(j == 0),
                            name="TREND: {}".format(comp_name),
                        ),
                        row=2 + int(with_residual_space),
                        col=1,
                    )

                    trendMax, trendMin = (
                        comp_trend.values[:, 0, 0].max(),
                        comp_trend.values[:, 0, 0].min(),
                    )

                    fig.append_trace(
                        go.Scatter(
                            x=target_ts.time_index,
                            y=comp_seasonality.values[:, 0, 0],
                            mode="lines",
                            line=dict(color=px.colors.qualitative.Plotly[cind % 10],),
                            opacity=future_opacity if j > 0 else 1.0,
                            showlegend=(j == 0),
                            name="SEASONALITY: {}".format(comp_name),
                        ),
                        row=3 + int(with_residual_space),
                        col=1,
                    )

                    # fix the range of the seasonality
                    trendRange = trendMax - trendMin
                    fig.update_yaxes(
                        range=[-trendRange * 0.55, trendRange * 0.55],
                        row=3 + int(with_residual_space),
                        col=1,
                    )
            i += 1
            cind += 1
        # annotate the target series
        fig.add_annotation(
            xref="x domain",
            yref="y domain",
            x=0.001,
            y=0.99,
            text="TARGET SERIES",
            showarrow=False,
            row=1,
            col=1,
        )

        if with_residual_space:
            fig.add_annotation(
                xref="x domain",
                yref="y domain",
                x=0.001,
                y=0.99,
                text="RESIDUAL",
                showarrow=False,
                row=2,
                col=1,
            )

        fig.add_annotation(
            xref="x domain",
            yref="y domain",
            x=0.001,
            y=0.99,
            text="TREND",
            showarrow=False,
            row=2 + int(with_residual_space),
            col=1,
        )

        fig.add_annotation(
            xref="x domain",
            yref="y domain",
            x=0.001,
            y=0.99,
            text="SEASONALITY",
            showarrow=False,
            row=3 + int(with_residual_space),
            col=1,
        )

        i += 2 + int(with_residual_space)
        # -------------------------- COMPONENTS PLOT ------------------------- #

        # now, plot each component on its own graph
        for comp in components:
            # get the component's plot data and annotation
            trace_data, annotation_text = self.get_component_plot_data(comp, ts_end)
            if comp in self.causality_score:
                annotation_text += f" (p-val {self.causality_score[comp].round(3)})"
            for j, trace_dict in enumerate(trace_data):
                # append the trace for before and future
                fig.append_trace(
                    go.Scatter(
                        **trace_dict,
                        opacity=future_opacity if j > 0 else 1.0,
                        showlegend=(j == 0),
                        line=dict(color=px.colors.qualitative.Plotly[cind % 10],width=1),
                    ),
                    row=i,
                    col=1,
                )

            # add the plot annotation
            fig.add_annotation(
                xref="x domain",
                yref="y domain",
                x=0.001,
                y=0.99,
                text=annotation_text,
                showarrow=False,
                row=i,
                col=1,
            )
            i += 1
            cind += 1

        # ------------------------- GRAPH APPEARANCE ------------------------- #

        # add a range selector
        fig.update_xaxes(
            # rangeslider_visible=True,
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
        )

        # remove the sliders and selectors for the other subplots
        # also add the vline
        for i in range(total_subplots + 1):
            fig.update_xaxes(
                showticklabels=True,
                rangeslider={"visible": False},
                rangeselector={"visible": False},
                row=i + 1,
                col=1,
            )
        fig.add_vrect(
            x0=ts_end,
            x1=ts_end,
            line=dict(color="rgba(0,0,0,0.7)", width=2), 
            opacity=1.0,
            annotation_text="CUTOFF",
            annotation_position="top left")

        # update the layout of the display, and show it
        fig.update_layout(
            margin=dict(l=5, r=5, t=30 if title and title != "" else 20, b=20),
            height=TOTAL_HEIGHT + 0.05* total_subplots * TOTAL_HEIGHT + (30 if title and title != "" else 20) + 20,
            title=title,
            hovermode="closest",
            xaxis=dict(
                range=[ts_begin, ts_future_end],
                gridcolor="rgba(0,0,0,0.1)"),
            yaxis=dict(gridcolor="rgba(0,0,0,0.1)",zerolinecolor="rgba(0,0,0,0.2)"),
            paper_bgcolor='rgba(0,0,0,0)',
            font_family="JetBrains Mono",
            # modebar_add=['select2d']
            # plot_bgcolor='rgba(0,0,0,0)',
        )

        return fig
