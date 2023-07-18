#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: darts library
subtitle: Building and manipulating TimeSeries - TimeSeries object
version: 1.0
type: tutorial
keywords: [time series, darts, data, data frame]
description: |
    Data format and properties for `darts` library: TimeSeries object.
remarks:
todo:
sources:
    - title: Quickstart
      chapter: Building and manipulating TimeSeries
      link: https://unit8co.github.io/darts/quickstart/00-quickstart.html
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
plt.figure('AirPassengersDataset', layout="tight")
series.plot()

# %%
help(series.plot)
"""
plot(new_plot: bool = False,
     central_quantile: Union[float, str] = 0.5,
     low_quantile: Optional[float] = 0.05,
     high_quantile: Optional[float] = 0.95,
     default_formatting: bool = True,
     label: Union[str, Sequence[str], NoneType] = '',
     *args, **kwargs
)
method of darts.timeseries.TimeSeries instance
Plot the series.
This is a wrapper method around :func:`xarray.DataArray.plot()`.

Parameters
----------
new_plot:  bool = False,
    whether to spawn a new Figure
central_quantile:  Union[float, str] = 0.5,
    The quantile (between 0 and 1) to plot as a "central" value, if the series is stochastic (i.e., if
    it has multiple samples). This will be applied on each component separately (i.e., to display quantiles
    of the components' marginal distributions). For instance, setting `central_quantile=0.5` will plot the
    median of each component. `central_quantile` can also be set to 'mean'.
low_quantile:  Optional[float] = 0.05,
    The quantile to use for the lower bound of the plotted confidence interval. Similar to `central_quantile`,
    this is applied to each component separately (i.e., displaying marginal distributions). No confidence
    interval is shown if `confidence_low_quantile` is None (default 0.05).
high_quantile:  bool = True,
    The quantile to use for the upper bound of the plotted confidence interval. Similar to `central_quantile`,
    this is applied to each component separately (i.e., displaying marginal distributions). No confidence
    interval is shown if `high_quantile` is None (default 0.95).
default_formatting
    Whether or not to use the darts default scheme.
label
    A prefix that will appear in front of each component of the TimeSeries or a list of string of
    length the number of components in the plotted TimeSeries (default "").
args
    some positional arguments for the `plot()` method
kwargs
    some keyword arguments for the `plot()` method

"""

dir(series)
# https://unit8co.github.io/darts/generated_api/darts.timeseries.html
# https://unit8co.github.io/darts/userguide/covariates.html

# %%
series.head()
series.tail()
dir(series)
len(series)     # 144
series.shape    # ! AttributeError: 'TimeSeries' object has no attribute 'shape'
series.time_index

series[11:22]
series.columns      # Index(['#Passengers'], dtype='object', name='component')
series.components   # "
series.univariate_component(0)  # TimeSeries

df = series.pd_dataframe()
df.head()

# %% splitting
plt.figure('splitting')
series1, series2 = series.split_before(0.75)
series1.plot()
series2.plot()

# %% slicing:
series1, series2 = series[:-36], series[-36:]
series1.plot(True)      # new_plot == new figure
series2.plot()

# %% arithmetic operations:
help(TimeSeries.from_times_and_values)
noise = TimeSeries.from_times_and_values(
    times = series.time_index,
    values = np.random.randn(len(series)),
    columns = ["noise"]         # default is ["0", "1", ...]
)

plt.figure('noise')
noise.plot()

(series / 2 + 20 * noise - 10).plot()

# %% stacking
fig = plt.figure('stack')
(series / 50).stack(noise).plot()

# %%
noise.columns    # ['noise']
(series / 50).columns   # ['#Passengers']
(series / 50).stack(noise).columns   #  ['#Passengers', 'noise']

""" !!!
TimeSeries is intended to be immutable and most operations return new TimeSeries object.
https://unit8co.github.io/darts/userguide/timeseries.html#implementation

Thus, there is no way of adding new columns to TimeSeries;
ts['new_col'] = ...     doesn't work
!!! because TimeSeries is IMMUTABLE !!!
only ts.stack()  serves this purpose (or darts.concatenate() - see next cell)
but they return new TimeSeries object.
"""
help(series.stack)
"""
stack(other: 'TimeSeries') -> 'TimeSeries' method of darts.timeseries.TimeSeries instance
    Stacks another univariate or multivariate TimeSeries with the same time index on top of
    the current one (along the component axis).

    Return a new TimeSeries that includes all the components of `self` and of `other`.

    The resulting TimeSeries will have the same name for its time dimension as this TimeSeries, and the
    same number of samples.
"""
ts = series.stack(np.random.randn(len(series)))     #! AttributeError: 'numpy.ndarray' object has no attribute 'time_dim'
# hence it must be TimeSeries

# %%
from darts import concatenate

ts = concatenate([series, noise], axis=1)
ts.plot()

# %% mapping:
plt.figure('map 1')
series.map(np.log).plot()

ts = series.stack(series.map(np.log))
ts.columns  # ts = series.stack(np.random.randn(len(series)))

help(series.map)

# %% mapping on both timestamps and values:
plt.figure('map 2')
series.map(lambda ti, x: x / ti.days_in_month).plot()   # ti = series.time_index

type(series.time_index)  # Out[37]: pandas.core.indexes.datetimes.DatetimeIndex

# %% Adding some datetime attribute as an extra dimension (yielding a multivariate series):
help(series.add_datetime_attribute)

plt.figure('add_datetime_attribute')
series2 = (series / 20).add_datetime_attribute("month")
series2.plot()

series2.head()
series2.columns      # Index(['#Passengers', 'month'], dtype='object', name='component')
series2.components   # "
series2.univariate_component(0)     # TimeSeries
series2['#Passengers']              # the same "
series2.univariate_component(1)

df2 = series2.pd_dataframe()
df2.head()
df2.index           # DatetimeIndex(['1949-01-01', ... '1960-12-01'], dtype='datetime64[ns]', name='Month', freq='MS')
series2.time_index  # DatetimeIndex(['1949-01-01', ... '1960-12-01'], dtype='datetime64[ns]', name='Month', freq='MS')

# %% Adding some binary holidays component:
help(series.add_holidays)
# https://github.com/dr-prodigy/python-holidays#available-countries
s3 = (series / 200).add_holidays("US")
plt.figure('holidays')
s3.plot()
s3.head(33)

# %%
s3['holidays'].head(22)
dir(s3['holidays'])
s3['holidays'].values()
help(s3['holidays'].values)
s3['holidays'].all_values()
help(s3['holidays'].all_values)

# %% differencing:
plt.figure('diff')
series.diff().plot()

# %% Filling missing values (using a ``utils`` function).
# Missing values are represented by np.nan.
from darts.utils.missing_values import fill_missing_values

values = np.arange(50, step=0.5)
values[10:30] = np.nan
values[60:95] = np.nan
s4 = TimeSeries.from_values(values)
s4

plt.figure('missing_values')
(s4 - 10).plot(label="with missing values (shifted below)")
fill_missing_values(s4).plot(label="without missing values")

# %% Filling missing values for sth irregular
noise = np.random.randn(100)
noise2 = noise.copy()
noise2[10:30] = np.nan
noise2[60:95] = np.nan

noise = TimeSeries.from_values(noise, columns=["noise"])
noise2 = TimeSeries.from_values(noise2)
noise2 = fill_missing_values(noise2)

plt.figure('noise')
noise.plot()
noise2.plot(label="filled missing values")

# %%



