#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: darts library
subtitle: LinearRegressionModel
version: 1.0
type: tutorial
keywords: [time series, darts, data, data frame]
description: |
    How LinearRegressionModel works - case study
remarks:
todo:
sources:
    - title: LinearRegressionModel API
      link: https://unit8co.github.io/darts/generated_api/darts.models.forecasting.linear_regression_model.html#linear-regression-model
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    date: 2023-03-06
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

from utils.config import pandas_options
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


# %% output_chunk_length
# %%
from darts.models import LinearRegressionModel, NBEATSModel

# %%
model = LinearRegressionModel()
# ! ValueError: At least one of `lags`, `lags_future_covariates` or `lags_past_covariates` must be not None.

# %%
model = LinearRegressionModel(lags=1)
model.fit(train)
model.extreme_lags
# (-1, 1, None, None, None)
# (minimum target lag, maximum target lag,
#  min past covariate lag,
#  min future covariate lag, max future covariate lag)
model.model_params
# OrderedDict([('lags', 1),
#              ('lags_past_covariates', None),
#              ('lags_future_covariates', None),
#              ('output_chunk_length', 1),
#              ('add_encoders', None),
#              ('likelihood', None),
#              ('quantiles', None),
#              ('random_state', None),
#              ('multi_models', True)])

plt.figure("lags=1")
series.plot()
train.plot()

pred_10 = model.predict(n=10)
pred_10.plot(label="10")

pred_8 = model.predict(n=8)
pred_8.plot(label="8")

pred_5 = model.predict(n=5)
pred_5.plot(label="5")

pred_4 = model.predict(n=4)
pred_4.plot(label="4")

pred_3 = model.predict(n=3)
pred_3.plot(label="3")

pred_2 = model.predict(n=2)
pred_2.plot(label="2")

pred_2 = model.predict(n=1)
pred_2.plot(label="1")

# %%
model = LinearRegressionModel(
    lags=7, output_chunk_length=5,
    lags_past_covariates=6,
    lags_future_covariates=[3, 4])
model.extreme_lags
# (-7, 5,  -6,  -3, 4)

model = LinearRegressionModel(lags=3, output_chunk_length=2)
model.extreme_lags
# (-3, 2, None, None, None)

model = LinearRegressionModel(lags=[3, 5], lags_past_covariates = 4, output_chunk_length=7)
# ! ValueError: Every element of `lags` must be a strictly negative integer. Given: [3, 5].
model = LinearRegressionModel(lags=[-3, -5], lags_past_covariates = 4, output_chunk_length=7)
model.extreme_lags
# (-5, 7,  -4,  None, None)

model = LinearRegressionModel(lags=[-3, -5], lags_future_covariates = [-4, 6], output_chunk_length=7)
model.extreme_lags
# (-5, 7, None, -4, 6)

model = NBEATSModel(input_chunk_length=10, output_chunk_length=7)
model.extreme_lags
# (-10, 7, None, None, None)

model = NBEATSModel(input_chunk_length=10, output_chunk_length=7, lags_future_covariates=[4, 6])
# ! ValueError: Invalid model creation parameters. Model `NBEATSModel` has no args/kwargs `['lags_future_covariates']`
# https://unit8co.github.io/darts/generated_api/darts.models.forecasting.nbeats.html

model = LinearRegressionModel(input_chunk_length=10, output_chunk_length=7, lags_future_covariates=[4, 6])
# ! TypeError: LinearRegression.__init__() got an unexpected keyword argument 'input_chunk_length'
# ...

# %%
model = LinearRegressionModel(lags=7, output_chunk_length=5)
model.fit(train)

model.extreme_lags
# (-7, 5, None, None, None)
model.model_params
model.model

plt.figure("5")
series.plot()
train.plot()

pred_10 = model.predict(n=10)
pred_10.plot(label="10")

pred_8 = model.predict(n=8)
pred_8.plot(label="8")

pred_5 = model.predict(n=5)
pred_5.plot(label="5")

pred_4 = model.predict(n=4)
pred_4.plot(label="4")

pred_3 = model.predict(n=3)
pred_3.plot(label="3")

pred_2 = model.predict(n=2)
pred_2.plot(label="2")

pred_2 = model.predict(n=1)
pred_2.plot(label="1")

# %%
model = LinearRegressionModel(lags=7, output_chunk_length=3)
model.fit(train)

model.extreme_lags
# (-7, 3, None, None, None)
# (minimum target lag, maximum target lag,
#  min past covariate lag,
#  min future covariate lag, max future covariate lag)
model.model_params
model.model

# plt.figure("1")     # the same figure for comparison

pred_10 = model.predict(n=10)
pred_10.plot(label="10")

pred_8 = model.predict(n=8)
pred_8.plot(label="8")

pred_5 = model.predict(n=5)
pred_5.plot(label="5")

pred_4 = model.predict(n=4)
pred_4.plot(label="4")

pred_3 = model.predict(n=3)
pred_3.plot(label="3")

pred_2 = model.predict(n=2)
pred_2.plot(label="2")

# %%
model = LinearRegressionModel(lags=7)
model.fit(train)

model.extreme_lags
# (-7, 1, None, None, None)
# (minimum target lag, maximum target lag,
#  min past covariate lag,
#  min future covariate lag, max future covariate lag)
model.model_params
model.model

# plt.figure("1")     # the same figure for comparison

pred_10 = model.predict(n=10)
pred_10.plot(label="10")

pred_8 = model.predict(n=8)
pred_8.plot(label="8")

pred_5 = model.predict(n=5)
pred_5.plot(label="5")

pred_4 = model.predict(n=4)
pred_4.plot(label="4")

pred_3 = model.predict(n=3)
pred_3.plot(label="3")

pred_2 = model.predict(n=2)
pred_2.plot(label="2")

# %%
model = LinearRegressionModel(lags=7, output_chunk_length=10)
model.fit(train)

model.extreme_lags
# (-7, 10, None, None, None)
# (minimum target lag, maximum target lag,
#  min past covariate lag,
#  min future covariate lag, max future covariate lag)
model.model_params
model.model

# plt.figure("1")     # the same figure for comparison

pred_13 = model.predict(n=13)
pred_13.plot(label="13")

pred_10 = model.predict(n=10)
pred_10.plot(label="10")

# %% lags
# %%
model = LinearRegressionModel(lags=7, output_chunk_length=5)
model.fit(train)

model.extreme_lags
# (-7, 5, None, None, None)

plt.figure("lags")
series.plot()
train.plot()

pred_10 = model.predict(n=10)
pred_10.plot(label="10")

pred_8 = model.predict(n=8)
pred_8.plot(label="8")

pred_5 = model.predict(n=5)
pred_5.plot(label="5")

pred_4 = model.predict(n=4)
pred_4.plot(label="4")

pred_3 = model.predict(n=3)
pred_3.plot(label="3")

pred_2 = model.predict(n=2)
pred_2.plot(label="2")

# %%
model = LinearRegressionModel(lags=1, output_chunk_length=5)
model.fit(train)

model.extreme_lags
# (-1, 5, None, None, None)

pred_10 = model.predict(n=10)
pred_10.plot(label="10")

pred_8 = model.predict(n=8)
pred_8.plot(label="8")

pred_5 = model.predict(n=5)
pred_5.plot(label="5")

pred_4 = model.predict(n=4)
pred_4.plot(label="4")

pred_3 = model.predict(n=3)
pred_3.plot(label="3")

pred_2 = model.predict(n=2)
pred_2.plot(label="2")

# %% full
# %%
model = LinearRegressionModel(lags=12, output_chunk_length=12)
model.fit(train)

model.extreme_lags
# (-12, 12, None, None, None)

plt.figure("full")
series.plot()
train.plot()

pred_36 = model.predict(n=36)
pred_36.plot(label="36")

pred_24 = model.predict(n=24)
pred_24.plot(label="24")

pred = model.predict(n=12)
pred.plot(label="12")


# %%
model = LinearRegressionModel(lags=24, output_chunk_length=24)
model.fit(train)

model.extreme_lags
# (-1, 5, None, None, None)

plt.figure("full")
series.plot()
train.plot()

pred_36 = model.predict(n=36)
pred_36.plot(label="36")

pred_24 = model.predict(n=24)
pred_24.plot(label="24")

pred = model.predict(n=12)
pred.plot(label="12")

# %% one year shorter train data
train, val = series.split_before(pd.Timestamp("19570101"))

# %%
model = LinearRegressionModel(lags=24, output_chunk_length=24)
model.fit(train)

model.extreme_lags
# (-1, 5, None, None, None)

plt.figure("full")
series.plot()
train.plot()

pred_36 = model.predict(n=48)
pred_36.plot(label="36")

pred_24 = model.predict(n=24)
pred_24.plot(label="24")

pred = model.predict(n=12)
pred.plot(label="12")

# %%