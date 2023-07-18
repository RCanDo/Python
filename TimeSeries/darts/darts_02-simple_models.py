#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: darts library
subtitle: Training forecasting models and making predictions - simple modelling
version: 1.0
type: tutorial
keywords: [time series, darts, data, data frame]
description: |
    Simple modelling.
remarks:
todo:
sources:
    - title: Quickstart
      chapter: Training forecasting models and making predictions
      link: https://unit8co.github.io/darts/quickstart/00-quickstart.html#Training-forecasting-models-and-making-predictions
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    date: 2023-02-04
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from darts import TimeSeries
from darts.datasets import AirPassengersDataset

from common.config import pandas_options
pandas_options()

# %%
series = AirPassengersDataset().load()
plt.figure('AirPassengersDataset')
series.plot()

# %% Creating a training and validation series
train, val = series.split_before(pd.Timestamp("19580101"))
train.end_time()    # !!!
val.start_time()

train.plot(label="training")
val.plot(label="validation")

# %% Training forecasting models and making predictions

# %% Playing with toy models

from darts.models import NaiveSeasonal

model_1 = NaiveSeasonal(K=1)
# In its most naive form, when K=1, this model simply always repeats the last value of the training series:

model_1     # <darts.models.forecasting.baselines.NaiveSeasonal at 0x7f2cc0117070>
dir(model_1)

model_1.fit(train)
# predict() takes in argument the number of time steps (after the end of the training series) over which to forecast:
forecast_1 = model_1.predict(36)
type(forecast_1)    # darts.timeseries.TimeSeries
forecast_1

plt.figure()
series.plot(label="actual")
forecast_1.plot(label="naive forecast (K=1)")

# %% K=5
model_2 = NaiveSeasonal(K=5)
model_2.fit(train)
forecast_2 = model_2.predict(36)

plt.figure()
series.plot(label="actual")
forecast_2.plot(label="naive forecast (K=5)")

# %% Inspect Seasonality

from darts.utils.statistics import plot_acf, check_seasonality
plot_acf(train, m=12, alpha=0.05)

# %%
for m in range(2, 25):
    is_seasonal, period = check_seasonality(train, m=m, alpha=0.05)
    if is_seasonal:
        print("There is seasonality of order {}.".format(period))
# There is seasonality of order 12.

help(check_seasonality)     # ???
# If `m` is None, we work under the assumption that there is a unique seasonality period, which is inferred
# from the Auto-correlation Function (ACF).      HOW ???
check_seasonality(train)            # True, 12
check_seasonality(train, m=12)      # True, 12
check_seasonality(train, m=2)       # False, 2
check_seasonality(train, m=10)      # False, 10

# %% less naive model
model_3 = NaiveSeasonal(K=12)
model_3.fit(train)
forecast_3 = model_3.predict(36)

series.plot(label="actual")
forecast_3.plot(label="naive forecast (K=12)")

# %% add drift
from darts.models import NaiveDrift
# This model simply produces linear predictions, with a slope
# that is determined by the first and last values of the training set

model_nd = NaiveDrift()
model_nd.fit(train)
forecast_nd = model_nd.predict(36)
forecast_nd[0]   # != 0

forecast_c = forecast_nd + forecast_3 - train.last_value()

series.plot()
forecast_3.plot(label="seasonal")
forecast_nd.plot(label="drift")
forecast_c.plot(label="combined")

(forecast_nd + forecast_3).plot(label="not moved")

# forecast_nd_b = model_nd.historical_forecasts(train[:3])
# ! ValueError: Train series only contains 2 elements but Naive drift model model requires at least 3 entries

forecast_nd_b = model_nd.historical_forecasts(train)
forecast_nd_b.plot(label="historical drift")

# %%
# https://unit8co.github.io/darts/generated_api/darts.models.forecasting.baselines.html#darts.models.forecasting.baselines.NaiveDrift.historical_forecasts
dir(model_nd)
help(model_nd.historical_forecasts)

# %%
model_nd.model_params   # OrderedDict()  -- empty !!!??? :(

# %% Computing error metrics
from darts.metrics import mape
print(
    "Mean absolute percentage error for the combined naive drift + seasonal: {:.2f}%.".format(
        mape(series, forecast_c)
    )
)

# The metrics will compare only common slices of series when the two series are not aligned,
# and parallelize computation over a large number of pairs of series

# %%
# %% Quickly try out several models
from darts.models import ExponentialSmoothing, TBATS, AutoARIMA, Theta

def eval_model(model):
    model.fit(train)
    forecast = model.predict(len(val))
    print("model {} obtains MAPE: {:.2f}%".format(model, mape(val, forecast)))


eval_model(ExponentialSmoothing())
eval_model(TBATS())
eval_model(AutoARIMA())
eval_model(Theta())

# %%
# %% Searching for hyper-parameters with the Theta method

# Search for the best theta parameter, by trying 50 different values
thetas = 2 - np.linspace(-10, 10, 50)

mape_best = float("inf")
theta_best = 0

for theta in thetas:
    model_theta = Theta(theta)
    model_theta.fit(train)
    pred_theta = model_theta.predict(len(val))
    result = mape(val, pred_theta)

    if result < mape_best:
        mape_best = result
        theta_best = theta
        model_theta_best = model_theta

pred_theta_best = model_theta_best.predict(len(val))

print(
    "The MAPE is: {:.2f}, with theta = {}.".format(
        mape(val, pred_theta_best), theta_best
    )
)

# %% Backtesting: simulate historical forecasting

hist_fcast_theta = model_theta_best.historical_forecasts(
    series, start=0.6, forecast_horizon=3, verbose=True
)

series_start, _ = series.split_before(.6)
pd.concat(
   {"series": series.pd_dataframe(),
    "train": train.pd_dataframe(),
    "series_start": series_start.pd_dataframe(),
    "hist_fcast": hist_fcast_theta.pd_dataframe()
    },
   axis=1,
)
# !!! notice the 3-month gap between series_start and historical_fcast_theta (prediction)
# because the  `only_last` option is by default  True, i.e. only last point of pred is taken...
print()

series.plot(label="data")
hist_fcast_theta.plot(label="backtest 3-months ahead forecast (Theta)")
print("MAPE = {:.2f}%".format(mape(hist_fcast_theta, series)))

# %%
# So it seems that our best model on validation set is not doing so great anymore when we backtest it;
# overfitting ?

# To have a closer look at the errors, we can also use the backtest() method
# to obtain all the raw errors (say, MAPE errors) that would have been obtained by our model:

raw_errors = model_theta_best.backtest(
    series, start=0.6, forecast_horizon=3, metric=mape,
    reduction=None,     # == aggregate for all errors from all predictions;
    verbose=True
)

raw_errors      # it's a list !!! not a TimeSeries obj !!!
# because these are NOT residuals but MAPE values (or any other type of error)

len(raw_errors)  # 57 ~= 0.4 * 144

from darts.utils.statistics import plot_hist

plot_hist(
    raw_errors,
    bins=np.arange(0, max(raw_errors), 1),
    title="Individual backtest error scores (histogram)",
)

# %%
# Finally, using backtest() we can also get a simpler view of the average error over the historical forecasts:

average_error = model_theta_best.backtest(
    series, start=0.6, forecast_horizon=3, metric=mape,
    reduction=np.mean,  # this is actually the default
    verbose=True,
)

print("Average error (MAPE) over all historical forecasts: %.2f" % average_error)


# %% residuals
from darts.utils.statistics import plot_residuals_analysis

plot_residuals_analysis(model_theta_best.residuals(series))

# - residuals distribution is not centered at 0, which means that our Theta model is biased.
# - large ACF value at lag 12h indicates that the residuals contain information that was not used by the model.

# %%
# %% ExponentialSmoothing

model_es = ExponentialSmoothing(seasonal_periods=12)
historical_fcast_es = model_es.historical_forecasts(
    series, start=0.6, forecast_horizon=3, verbose=True
)

plt.figure()
series.plot(label="data")
historical_fcast_es.plot(label="backtest 3-months ahead forecast (Exp. Smoothing)")
print("MAPE = {:.2f}%".format(mape(historical_fcast_es, series)))
# MAPE = 4.45%

plot_residuals_analysis(model_es.residuals(series))

# The residual analysis reflects an improved performance:
# - distribution of the residuals centred at value 0,
# - the ACF values, although not insignificant, have lower magnitudes

# %%