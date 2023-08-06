"""Darts backtest class, representing a historical forecast.

Is initialized with a date, a forecast horizon, a stride, and various other
settings, and saves the eventual forecast so it can be replotted 
"""
from shutil import ExecError
from typing import Dict

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from darts import TimeSeries
from darts.metrics import mape, rmse
from darts.models.forecasting.forecasting_model import ForecastingModel
from darts.utils.statistics import extract_trend_and_seasonality
from darts.utils.utils import ModelMode

from .utils import hex_to_rgba

DIMS = ("time", "component", "sample")


class DartsBacktest:
    """The Darts backtest class, representing a historical forecast.

    An instance of a Darts backtest is produced from the Darts interface, which
    manages all the data used by backtests and forecasts. Initialize a backtest
    with reference to a model, and the model is deployed on the interface's
    data. See kwargs for values you can pass into the backtest.
    """

    model: ForecastingModel
    forecast: TimeSeries
    mape: float
    kwargs: Dict[str, any] = {
        "num_samples": 1,
        "train_length": None,
        "start": 0.5,
        "forecast_horizon": 1,
        "stride": 1,
        "retrain": True,
        "overlap_end": False,
        "last_points_only": True,
        "verbose": False,
    }

    def __init__(self, source, model: ForecastingModel, **kwargs):
        """Initialize a Darts backtest given a model and specifications.

        Once a backtest is run, its forecast is saved and it may be replotted
        or re-run at any point. This also allows you to change the covariates
        used in your interface and have them reflected in the backtest for the
        kwargs set in this backtest.

        Args:
            source (DartsInterface): The interface from which to draw data.
            model (ForecastingModel): A Darts model to use for predictions
            num_samples (int) = 1: __description__
            train_length (int) = None: If retraining the model, how many datapoints to use
            start (float or pd.Timestamp) = 0.5: When to begin the backtest
            forecast_horizon (int) = 1: How many time stamps to forecast at each stride
            stride (int) = 1: The stride of the backtest
            retrain (boolean) = False: Whether or not to retrain the model at each step
            ...
        """
        self.source = source
        self.model = model
        self.kwargs.update(kwargs)
        self.forecast = None

    # runs the backtest using darts, and prints the MAPE
    def run(self, **kwargs):
        _kwargs = (
            dict(
                past_covariates=self.source.past_covariates,
                future_covariates=self.source.future_covariates,
            )
        )
        _kwargs.update(kwargs)
        self.forecast = self.model.historical_forecasts(
            self.source.target_ts, **_kwargs, **(self.kwargs)
        )
        self.mape = mape(self.forecast, self.source.target_ts)
        self.rmse = rmse(self.forecast, self.source.target_ts)
        # print("MAPE = {:.2f}%".format(self.mape))
        return self.forecast

    # ---------------------------------------------------------------------------- #
    #                                 VISUALIZATION                                #
    # ---------------------------------------------------------------------------- #

    # plotting the backtest shows actual vs. prediction
    def plot(self, components=None, actual_ts=None, future_opacity: float = 0.5):
        residual_df = None
        # if the backtest hasn't been run, return an error
        if not self.forecast:
            raise ExecError("Please run the backtest before plotting it!")
        # get the source fig
        title = "Backtest: {} - MAPE = {:.2f}%, RMSE = {:.2f}".format(
            self.kwargs["start"], self.mape, self.rmse
        )
        fig = self.source.plot(
            components,
            future_begins_at=self.kwargs["start"],
            future_opacity=future_opacity,
            title=title,
            with_residual_space=True,
        )
        # add residual trace
        if self.forecast and actual_ts:
            actual_sliced = actual_ts.slice_intersect(self.forecast)

            # print(len(self.forecast), len(actual_sliced))
            for _, (ca, c) in enumerate(
                zip(actual_sliced._xa.component[:10], self.forecast._xa.component[:10])
            ):
                comp_name = c.values
                comp_name = "RESIDUALS: {}".format(str(c.values))
                comp = self.forecast._xa.sel(component=c)
                truth = actual_sliced._xa.sel(component=ca)

                if comp.sample.size > 1:
                    prediction_series = comp.mean(dim=DIMS[2])
                else:
                    prediction_series = comp.values[:, 0]

                residuals = prediction_series - truth.values[:, 0]
                residual_df = pd.DataFrame(
                    {
                        "date": list(actual_sliced.time_index),
                        "residual": list(residuals),
                    }
                )

                fig.append_trace(
                    go.Scatter(
                        x=actual_sliced.time_index,
                        y=residuals,
                        stackgroup="residual",
                        line=dict(color=px.colors.qualitative.Plotly[0], width=2),
                        showlegend=False,
                        name=comp_name,
                    ),
                    row=2,
                    col=1,
                )

                fig.add_vline(
                    x=self.kwargs["start"],
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

            print("sample size: ", comp.sample.size)

            prediction_series = comp.mean(dim=DIMS[2])

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
                    y=prediction_series.values[:],
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
