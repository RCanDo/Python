#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:40:20 2023

@author: arek
"""

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from darts import TimeSeries
from darts.datasets import AirPassengersDataset

from common.config import pandas_options
pandas_options()

# %% Machine learning and global models
"""
Darts has a rich support for machine learning and deep learning forecasting models; for instance:

    RegressionModel can wrap around any sklearn-compatible regression model to produce forecasts
    (it has its own section below).

    RNNModel is a flexible RNN implementation, which can be used like DeepAR.

    NBEATSModel implements the N-BEATS model.

    TFTModel implements the Temporal Fusion Transformer model.

    TCNModel implements temporal convolutional networks.

    …

In addition to supporting the same basic fit()/predict() interface as the other models,
these models are also global models, as they support being trained on multiple time series
(sometimes referred to as meta learning).

This is a key point of using ML-based models for forecasting:
more often than not, ML models (especially deep learning models) need to be trained on large amounts of data,
which often means a large amount of separate yet related time series.

In Darts, the basic way to specify multiple TimeSeries is using a Sequence of TimeSeries
(for instance, a simple list of TimeSeries).
"""

# %% A toy example with two series
"""
These models can be trained on thousands of series.
Here, for the sake of illustration, we will load two distinct series:
- the air traffic passenger count, and another series
- containing the number of pounds of milk produced per cow monthly.
We also cast our series to np.float32 as that will slightly speedup the training:
"""
from darts.datasets import AirPassengersDataset, MonthlyMilkDataset

series_air = AirPassengersDataset().load().astype(np.float32)
series_milk = MonthlyMilkDataset().load().astype(np.float32)

# set aside last 36 months of each series as validation set:
train_air, val_air = series_air[:-36], series_air[-36:]
train_milk, val_milk = series_milk[:-36], series_milk[-36:]

train_air.plot()
val_air.plot()
train_milk.plot()
val_milk.plot()

# %%
# let’s scale these two series between 0 and 1, as that will benefit most ML models. We will use a Scaler for this:

from darts.dataprocessing.transformers import Scaler

scaler = Scaler()
train_air_scaled, train_milk_scaled = scaler.fit_transform([train_air, train_milk])

plt.figure()
train_air_scaled.plot()
train_milk_scaled.plot()

# %% Using deep learning: example with N-BEATS
"""
Next, we will build an N-BEATS model.
This model can be tuned with many hyper-parameters (such as number of stacks, layers, etc).
Here, for simplicity, we will use it with default hyper-parameters.
The only two hyper-parameters that we have to provide are:

    input_chunk_length:
    this is the “lookback window” of the model,
    i.e. how many time steps of history the neural network takes as input to produce its output in a forward pass.

    output_chunk_length:
    this is the “forward window” of the model,
    i.e. how many time steps of future values the neural network outputs in a forward pass.

The random_state parameter is just here to get reproducible results.

Most neural networks in Darts require these two parameters.
Here, we will use multiples of the seasonality.
We are now ready to fit our model on our two series (by giving a list containing the two series to fit()):
"""
# %%
from darts.models import NBEATSModel

model = NBEATSModel(input_chunk_length=24, output_chunk_length=12, random_state=42)

model.fit([train_air_scaled, train_milk_scaled], epochs=50, verbose=True)

# %%
pred_air = model.predict(series=train_air_scaled, n=36)
pred_milk = model.predict(series=train_milk_scaled, n=36)

# scale back:
pred_air, pred_milk = scaler.inverse_transform([pred_air, pred_milk])

plt.figure(figsize=(10, 6))
series_air.plot(label="actual (air)")
series_milk.plot(label="actual (milk)")
pred_air.plot(label="forecast (air)")
pred_milk.plot(label="forecast (milk)")

# %%
"""
Our forecasts are actually not so terrible,
considering that we use one model with default hyper-parameters to capture both air passengers and milk production!

The model seems quite OK at capturing the yearly seasonality, but misses the trend for the air series.
In the next section, we will try to solve this issue using external data (covariates).
"""

# %% Covariates: using external data
"""
In addition to the target series (the series we are interested to forecast),
many models in Darts also accept covariates series in input.
Covariates are series that we do not want to forecast,
but which can provide helpful additional information to the models.
Both the targets and covariates can be multivariate or univariate.

There are two kinds of covariate time series in Darts:

    past_covariates
    are series not necessarily known ahead of the forecast time.
    Those can for instance represent things that have to be measured and are not known upfront.
    Models do not use the future values of past_covariates when making forecasts.

    future_covariates
    are series which are known in advance, up to the forecast horizon.
    This can represent things such as calendar information, holidays, weather forecasts, etc.
    Models that accept future_covariates will look at the future values (up to the forecast horizon) when making forecasts.

[covariates-highlevel.png]

Each covariate can potentially be multivariate.
If you have several covariate series (such as month and year values),
you should stack() or concatenate() them to obtain a multivariate series.

The covariates you provide can be longer than necessary.
Darts will try to be smart and slice them in the right way for forecasting the target,
based on the time indexes of the different series.
!!! You will receive an error if your covariates do not have a sufficient time span, though. !!!
"""
# %%
"""
Let’s now build some external covariates containing both monthly and yearly values for our air and milk series.
In the cell below, we use the
darts.utils.timeseries_generation.datetime_attribute_timeseries()
function to generate series containing the month and year values,
and we concatenate() these series along the "component" axis in order to obtain one covariate series
with two components (month and year), per target series.
For simplicity, we directly scale the month and year values to have them between (roughly) 0 and 1:
"""
# %%
from darts import concatenate
from darts.utils.timeseries_generation import datetime_attribute_timeseries as dt_attr

air_covs = concatenate(
    [
        dt_attr(series_air.time_index, "month", dtype=np.float32) / 12,
        (dt_attr(series_air.time_index, "year", dtype=np.float32) - 1948) / 12,
    ],
    axis="component",
)

milk_covs = concatenate(
    [
        dt_attr(series_milk.time_index, "month", dtype=np.float32) / 12,
        (dt_attr(series_milk.time_index, "year", dtype=np.float32) - 1962) / 13,
    ],
    axis="component",
)

air_covs.plot()
milk_covs.plot()
plt.title(
    "one multivariate time series of 2 dimensions, containing covariates for the air series:"
);

# %%
"""
Not all models support all types of covariates.
NBEATSModel supports only past_covariates.
Therefore, even though our covariates represent calendar information and are known in advance,
we will use them as past_covariates with N-BEATS.
To train, all we have to do is give them as past_covariates to the fit() function, in the same order as the targets:
"""
# %%
model = NBEATSModel(input_chunk_length=24, output_chunk_length=12, random_state=42)

model.fit(
    [train_air_scaled, train_milk_scaled],
    past_covariates=[air_covs, milk_covs],
    epochs=50,
    verbose=True,
);

# %%
"""
Then to produce forecasts, we again have to provide our covariates as past_covariates to the predict() function.
Even though the covariates time series also contains “future” values of the covariates up to the forecast horizon,
the model will not consume those future values, because it uses them as past covariates (and not future covariates).
"""
# %%
pred_air = model.predict(series=train_air_scaled, past_covariates=air_covs, n=36)
pred_milk = model.predict(series=train_milk_scaled, past_covariates=milk_covs, n=36)

# scale back:
pred_air, pred_milk = scaler.inverse_transform([pred_air, pred_milk])

plt.figure(figsize=(10, 6))
series_air.plot(label="actual (air)")
series_milk.plot(label="actual (milk)")
pred_air.plot(label="forecast (air)")
pred_milk.plot(label="forecast (milk)")

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
