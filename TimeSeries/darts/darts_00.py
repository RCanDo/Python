#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://unit8co.github.io/darts/#forecasting-models
"""

# %%
import numpy as np
import pandas as pd
from darts import TimeSeries
from darts.datasets import AirPassengersDataset

# Read a pandas DataFrame
# df = pd.read_csv("AirPassengers.csv", delimiter=",")
# Create a TimeSeries, specifying the time and value columns
# series = TimeSeries.from_dataframe(df, "Month", "#Passengers")

series = AirPassengersDataset().load()

# Set aside the last 36 months as a validation series
train, val = series[:-36], series[-36:]

# %%
from darts.models import ExponentialSmoothing

model = ExponentialSmoothing()
model.fit(train)
prediction = model.predict(len(val), num_samples=1000)

# %%
import matplotlib.pyplot as plt

series.plot()
prediction.plot(label="forecast", low_quantile=0.05, high_quantile=0.95)
plt.legend()

# %%
from darts.datasets import ETTh2Dataset

series = ETTh2Dataset().load()[:10000][["MUFL", "LULL"]]
train, val = series.split_before(0.6)

train.n_timesteps   # 5999
val.n_timesteps     # 4001

# %%
from darts.ad import KMeansScorer

scorer = KMeansScorer(k=2, window=5)
scorer.fit(train)
anom_score = scorer.score(val)
anom_score      # 3991

# %%
from darts.ad import QuantileDetector

detector = QuantileDetector(high_quantile=0.99)
detector.fit(scorer.score(train))
binary_anom = detector.detect(anom_score)

# %%
import matplotlib.pyplot as plt

series.plot()
(anom_score / 2. - 100).plot(label="computed anomaly score", c="orangered", lw=3)
(binary_anom * 45 - 150).plot(label="detected binary anomaly", lw=4)

# %%
binary_anom     # ts
binary_anom.values()
binary_anom.values().tolist()

binary_anom.values().shape      # (3997, 1)
val.n_timesteps     # 4001

val[binary_anom.values()==1, :, 1]


# %%
ts = val['MUFL']
ts      # (4001,)

scorer = KMeansScorer(k=2, window=51)
detector = QuantileDetector(high_quantile=0.99)

scorer.fit(ts)
anomaly_score = scorer.score(ts)
anomaly_score       # ts  (3952, 1)

detector.fit(anomaly_score)
binary_anomalies = detector.detect(anomaly_score)
binary_anomalies    # ts  (3952, 1)

# ts.plot()
# (anomaly_score / 4 - 125000).plot(label="computed anomaly score", lw=3)
# (binary_anomalies * 50000 - 200000).plot(label="detected binary anomaly", lw=4)
# plt.show()

binary_anomalies_values = binary_anomalies.values()
outliers_indices = np.where(binary_anomalies_values == 1)[0]

ts_values = ts.values()
# We expect there to be very few outliers, thus we are using
# a standard loop instead of vectorization
for index in outliers_indices:
    ts_values[index] = np.nan

ts = TimeSeries.from_times_and_values(ts.time_index, ts_values)

# %%
