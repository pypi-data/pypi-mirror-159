"""Darts forecast class, representing a future forecast.

Is initialized with a number of time steps to forecast from the end of the
interface's target series.
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict
from darts import TimeSeries
from darts.metrics import mape, rmse
from darts.models.forecasting.forecasting_model import ForecastingModel
from darts.utils.statistics import extract_trend_and_seasonality, granger_causality_tests
from darts.utils.utils import ModelMode
from .utils import hex_to_rgba

DIMS = ("time", "component", "sample")
past_cov_support = set(["LinearRegression"])


class DartsForecast:
    """The Darts forecast class, representing a future forecast.

    An instance of a Darts forecast is produced from the Darts interface, which
    manages all the data used by backtests and forecasts. Initialize a forecast
    with reference to a model, and the model is deployed on the interface's
    data. See kwargs for values you can pass into the forecast.
    """

    model: ForecastingModel
    forecast: TimeSeries
    kwargs: Dict[str, any] = {
        "n": 10,
        "num_samples": 1,
    }

    def __init__(self, source, model: ForecastingModel, **kwargs):
        """Initialize a Darts forecast given a model and specifications.

        Once a forecast is run, its forecast is saved and it may be replotted
        or re-run at any point. This also allows you to change the covariates
        used in your interface and have them reflected in the forecast for the
        kwargs set in this forecast.

        Args:
            source (DartsInterface): The interface from which to draw data.
            model (ForecastingModel): A Darts model to use for predictions
            n (int) = 1: How many time steps to forecast
            num_samples (int) = 1: __description__
            ...
        """
        self.source = source
        # print(str(model))
        self.model_str = str(model)
        self.model = model
        #print(kwargs, self.kwargs, self.source)
        self.kwargs.update(kwargs)
        self.forecast = None
        self.residuals = None
        # print(self.kwargs)

    # runs the backtest using darts, and prints the MAPE
    def run(self, disable_future, series=None, **kwargs):
        _kwargs = (
            dict(
                past_covariates=self.source.past_covariates,
                future_covariates=self.source.future_covariates,
            )
        )
        _kwargs.update(kwargs)

        if disable_future:
            del _kwargs["future_covariates"]

        del_past = True 
        for model in past_cov_support:
            if model in self.model_str: 
                del_past = False
                break
        if del_past:
            del _kwargs["past_covariates"]

        if series:
            self.forecast = self.model.predict(
                series=series,
                **_kwargs,
                **self.kwargs,
            )
        else:
            self.forecast = self.model.predict(
                **_kwargs,
                **self.kwargs,
            )

        #print("finished forecasting... ", self.forecast)
        return self.forecast

    # ---------------------------------------------------------------------------- #
    #                                 VISUALIZATION                                #
    # ---------------------------------------------------------------------------- #

    # plotting the backtest shows actual vs. prediction
    def plot(
        self,
        components=None,
        actual_ts=None,
        future_begins_at=None,
        future_opacity: float = 0.1,
    ):
        residual_df = None
        # get the source fig
        title = "Forecast: {}".format(self.source.target_ts.time_index[-1])
        fig = self.source.plot(
            components,
            future_begins_at=future_begins_at
            if future_begins_at
            else self.source.target_ts.time_index[-1],
            future_opacity=future_opacity,
            title=title,
            with_residual_space=True,
        )

        # add residual trace
        if self.forecast and actual_ts:
            actual_sliced = actual_ts.slice_intersect(self.forecast)
            forecast_sliced = self.forecast.slice_intersect(actual_ts)

            # print(len(self.forecast), len(actual_sliced))

            if len(actual_sliced) > 0:
                self.mape = mape(forecast_sliced, actual_sliced).round(2)
                self.rmse = rmse(forecast_sliced, actual_sliced).round(2)
                # print("MAPE = {:.2f}%".format(self.mape))

                text = f"Forecast: {self.source.target_ts.time_index[-1]} - MAPE = {self.mape}%, RMSE = {self.rmse}"
                fig.update_layout(title_text=text)

                for _, (ca, c) in enumerate(
                    zip(
                        actual_sliced._xa.component[:10],
                        forecast_sliced._xa.component[:10],
                    )
                ):
                    comp_name = c.values
                    comp_name = "RESIDUALS: {}".format(str(c.values))
                    comp = forecast_sliced._xa.sel(component=c)
                    truth = actual_sliced._xa.sel(component=ca)

                    if comp.sample.size > 1:
                        prediction_series = comp.mean(dim=DIMS[2])
                    else:
                        prediction_series = comp.values[:, 0]

                    residuals = prediction_series - truth.values[:, 0]
                    try:
                        res = list(residuals.to_numpy().reshape(-1))
                    except:
                        res = list(residuals.reshape(-1))

                    # print(list(residuals.to_numpy().reshape(-1)))
                    residual_df = pd.DataFrame(
                        {"date": list(actual_sliced.time_index), "residual": res}
                    )

                    fig.append_trace(
                        go.Scatter(
                            x=actual_sliced.time_index,
                            y=residuals,
                            stackgroup="residual",
                            line=dict(color=px.colors.qualitative.Plotly[0]),
                            showlegend=False,
                            name=comp_name,
                        ),
                        row=2,
                        col=1,
                    )

                    fig.add_vline(
                        x=future_begins_at
                        if future_begins_at
                        else self.source.target_ts.time_index[-1],
                        line=dict(color="rgba(0,0,0,0.3)", dash="dot"),
                        row=2,
                        col=1,
                    )
                    break

        # add prediction trace
        for _, c in enumerate(self.forecast._xa.component[:10]):
            comp_name = c.values
            comp_name = "PRED: {}".format(str(c.values))
            comp = self.forecast._xa.sel(component=c)

            # print("sample size: ", comp.sample.size)

            if comp.sample.size > 1:
                prediction_series = comp.mean(dim=DIMS[2]).values[:]
            else:
                prediction_series = comp.values[:, 0]

            if comp.sample.size > 1:
                low_series = comp.quantile(q=0.05, dim=DIMS[2])
                high_series = comp.quantile(q=0.95, dim=DIMS[2])

                fig.append_trace(
                    go.Scatter(
                        x=np.concatenate(
                            [self.forecast.time_index, self.forecast.time_index[::-1]]
                        ),
                        y=np.concatenate(
                            [low_series.values[:], high_series.values[::-1]]
                        ),
                        mode="lines",
                        fill="toself",
                        name="5% - 95% Confidence Band",
                        hoveron="points",
                        line=dict(
                            width=1,
                            color="rgba"
                            + str(hex_to_rgba(px.colors.qualitative.T10[1], 0.4)),
                        ),
                        fillcolor="rgba"
                        + str(hex_to_rgba(px.colors.qualitative.T10[1], 0.2)),
                    ),
                    row=1,
                    col=1,
                )

            series_analysis = TimeSeries.from_times_and_values(
                self.forecast.time_index, prediction_series
            )
            trend, seasonality = extract_trend_and_seasonality(
                series_analysis, model=ModelMode.ADDITIVE
            )

            fig.append_trace(
                go.Scatter(
                    x=self.forecast.time_index,
                    y=prediction_series,
                    mode="lines",
                    name=comp_name,
                    line=dict(color=px.colors.qualitative.Plotly[8],),
                ),
                row=1,
                col=1,
            )

            fig.append_trace(
                go.Scatter(
                    x=self.forecast.time_index,
                    y=trend._xa.values[:, 0, 0],
                    mode="lines",
                    line=dict(color=px.colors.qualitative.Plotly[3],),
                    name="TREND: {}".format(comp_name),
                ),
                row=3,
                col=1,
            )

            fig.append_trace(
                go.Scatter(
                    x=self.forecast.time_index,
                    y=seasonality._xa.values[:, 0, 0],
                    mode="lines",
                    line=dict(color=px.colors.qualitative.Plotly[3],),
                    name="SEASONALITY: {}".format(comp_name),
                ),
                row=4,
                col=1,
            )

            fig["layout"]["xaxis"].update(autorange=True)

        if residual_df is None: residual_df = pd.DataFrame()
        # show the display
        return fig, residual_df
