#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Time Series Analysis in Python – A Comprehensive Guide with Examples
subtitle:
version: 1.0
type: tutorial
keywords: [time series, prediction, forecasting, ACF, PACF, seasonal, trend, unit root test]
description: |
    Tutorial on Time Series - basics.
remarks:
todo:
sources:
    - title: Time Series Analysis in Python – A Comprehensive Guide with Examples
      link: https://pandas.pydata.org/docs/user_guide/timeseries.html#time-series-related-instance-methods/
      date: 2019-02-13
      authors:
          - nick: selva86
            fullname: Selva Prabhakaran
            email:
      usage: |
          not only copy
    - link: https://github.com/selva86/datasets
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-intro.py
    path: D:/ROBOCZY/Python/TimeSeries/Classical/
    date: 2020-08-29
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% 1. What is a Time Series?

#%% 2. How to import time series in python?
from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

#%%
# Import as Dataframe (Australian Drug Sales)

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'])
df.head()

#%%
ss = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')
ss.head()
type(ss)     # df

#%% 3. What is panel data?
# it is ts with additional variables
# dataset source: https://github.com/rouseguy
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/MarketArrivals.csv')
df = df.loc[df.market=='MUMBAI', :]
df.head()

#%% 4. Visualizing a time series

# Time series data source: fpp pacakge in R.
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')

# Draw Plot
def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16, 5), dpi=dpi)
    #plt.plot(x, y, color='r')              # mpl.colors.BASE_COLORS
    #plt.plot(x, y, color='tab:red')        # mpl.colors.TABLEAU_COLORS
    plt.plot(x, y, color='xkcd:red')       # mpl.colors.XKCD_COLORS
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

plot_df(df, x=df.index, y=df.value,
        title='Monthly anti-diabetic drug sales in Australia from 1992 to 2008.')

#%% Since all values are positive, you can show this on both sides of the Y axis
# to emphasize the growth. (???)

# Import data
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/AirPassengers.csv',
                 parse_dates=['date'])
x = df['date'].values
y1 = df['value'].values
# Plot
fig, ax = plt.subplots(1, 1, figsize=(16,5), dpi= 120)
plt.fill_between(x, y1=y1, y2=-y1, alpha=0.5, linewidth=2, color='seagreen')
plt.ylim(-800, 800)
plt.title('Air Passengers (Two Side View)', fontsize=16)
plt.hlines(y=0, xmin=np.min(df.date), xmax=np.max(df.date), linewidth=.5)
plt.show()

#%% Seasonal Plot of a Time Series

#%% Import Data
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')
df.head()
type(df.index)     # pandas.core.indexes.datetimes.DatetimeIndex
df.index.year      # no datetime accessor `.dt` needed

df2 = df.reset_index(inplace=False)
df2.head(10)
type(df2.date)
df2.date.dt.year   # .dt accessor needed

#%% but it's all nonsense:
# data
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'])
df.head()

type(df.date)  # pandas.core.series.Series
df.date.dt.year    # Series
[d.year for d in df.date]  # list

# year, month columns
df['year'] = df.date.dt.year
df['month'] = df.date.dt.month
years = df['year'].unique()

# colors
np.random.seed(100)
mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

#%%

plt.figure(figsize=(16, 12), dpi=80)
for i, y in enumerate(years):
    #if i > 0:
    plt.plot('month', 'value', data=df.loc[df.year==y, :],
             color=mycolors[i], label=y)
    plt.text(12.2, df.loc[df.year==y, 'value'][-1:].values[0],
             y, fontsize=12, color=mycolors[i])

# Decoration
plt.gca().set(xlim=(1-.1, 12.1), ylim=(2, 30),
              ylabel='$Drug Sales$', xlabel='$Month$')
plt.yticks(fontsize=12, alpha=.7)
plt.title("Seasonal Plot of Drug Sales Time Series", fontsize=20)

#%% Boxplot of Month-wise (Seasonal) and Year-wise (trend) Distribution

fig, axes = plt.subplots(1, 2, figsize=(20, 7), dpi=80)
sns.boxplot(x='year', y='value', data=df, ax=axes[0])
sns.boxplot(x='month', y='value', data=df.loc[~df.year.isin([1991, 2008]), :])

axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18)
axes[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize=18)

#%% 5. Patterns in a time series
fig, axes = plt.subplots(1, 3, figsize=(20, 4), dpi=100)

pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/guinearice.csv', parse_dates=['date'], index_col='date')\
  .plot(title='Trend Only', legend=False, ax=axes[0])

pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/sunspotarea.csv', parse_dates=['date'], index_col='date')\
  .plot(title='Seasonality Only', legend=False, ax=axes[1])

pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/AirPassengers.csv', parse_dates=['date'], index_col='date')\
  .plot(title='Trend and Seasonality', legend=False, ax=axes[2])


#%%
"""
How to diffentiate between a ‘cyclic’ vs ‘seasonal’ pattern?

If the patterns are not of fixed calendar based frequencies, then it is cyclic.
Because, unlike the seasonality, cyclic effects are typically influenced
by the business and other socio-economic factors.
"""

#%% 6. Additive and multiplicative time series
"""
Additive time series:
Value = Base Level + Trend + Seasonality + Error

Multiplicative Time Series:
Value = Base Level x Trend x Seasonality x Error
"""


#%% 7. How to decompose a time series into its components?
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')
df.head()

#plt.rcParams.update({'figure.figsize': (10, 10)})   # ?

#%%
# multiplicative decomposition
res_m = seasonal_decompose(df['value'],
                                model='multiplicative', extrapolate_trend='freq')
# additive decomposition
res_a = seasonal_decompose(df['value'],
                                model='additive', extrapolate_trend='freq')
"""
extrapolate_trend='freq' takes care of any missing values in the trend and residuals
at the beginning of the series.
"""
#%%
res_m
dir(res_m)
res_m.nobs
res_m.observed
res_m.seasonal
res_m.trend
res_m.resid
res_m.weights
res_m.plot().suptitle('Multiplicative Decompose', fontsize=12)

## check if it's really multiplicative decomposition
df_m = res_m.seasonal * res_m.trend * res_m.resid
df_m.head()
all(df_m == df)    # True  OK !!!

#%%
res_a
dir(res_a)
res_a.nobs
res_a.observed
res_a.seasonal
res_a.trend
res_a.resid
res_a.weights
res_a.plot().suptitle('Additive Decompose', fontsize=12)

## check if it's really multiplicative decomposition
df_a = res_m.seasonal + res_m.trend + res_m.resid
df_a.head()
all(df_a == df)    # True  OK !!!

#%% 8. Stationary and Non-Stationary Time Series

#%% 9. How to make a time series stationary?
"""
You can make series stationary by:
    Differencing the Series (once or more)  !!!
    Take the log of the series
    Take the nth root of the series
    Combination of the above
"""

#%% 10. How to test for stationarity?
"""!!! Unit Root Tests
There are multiple implementations of Unit Root tests like:

    Augmented Dickey Fuller test (ADH Test)
    Kwiatkowski-Phillips-Schmidt-Shin – KPSS test (trend stationary)
    Philips Perron test (PP Test)

"""
from statsmodels.tsa.stattools import adfuller, kpss

#%% ADF Test
"""
The most commonly used is the ADF test, where the null hypothesis is the time series
possesses a unit root and is non-stationary.
So, id the P-Value in ADH test is less than the significance level (0.05),
you reject the null hypothesis.
"""
adf_test = adfuller(df.value, autolag='AIC')
adf_test
print(f'ADF Statistic: {adf_test[0]}')
print(f'p-value: {adf_test[1]}')
for key, value in adf_test[4].items():
    print('Critial Values:')
    print(f'   {key}, {value}')

#%% KPSS Test
"""
The KPSS test, on the other hand, is used to test for trend stationarity.
The null hypothesis and the P-Value interpretation is just the opposite of ADH test.
"""
kpss_test = kpss(df.value, regression='c')
print('\nKPSS Statistic: %f' % kpss_test[0])
print('p-value: %f' % kpss_test[1])
for key, value in kpss_test[3].items():
    print('Critial Values:')
    print(f'   {key}, {value}')

#%% 11. What is the difference between white noise and a stationary series?
randvals = np.random.randn(1000)
pd.Series(randvals).plot(title='Random White Noise', color='k')

#%% 12. How to detrend a time series?
"""
1. Subtract the line of best fit from the time series.
   The line of best fit may be obtained from a linear regression model
   with the time steps as the predictor.
   For more complex trends, you may want to use quadratic terms (x^2) in the model.

2. Subtract the trend component obtained from time series decomposition we saw earlier.

3. Subtract the mean

4. Apply a filter like
    - Baxter-King filter (statsmodels.tsa.filters.bkfilter) or
    - Hodrick-Prescott Filter (statsmodels.tsa.filters.hpfilter)
      to remove the moving average trend lines or the cyclical components.
"""

#%% Using scipy: Subtract the line of best fit
from scipy import signal
data_detr_1 = signal.detrend(df.value)
plt.plot(data_detr_1)
# no good...

#%% Using statmodels: Subtracting the Trend Component.
# already done above
data_detr_2 = df.value - res_m.trend
data_detr_2.plot(title='Drug Sales detrended by subtracting the trend component', fontsize=16)

#%% ... other methods ???


#%% 13. How to deseasonalize a time series?
"""
1. Take a moving average with length as the seasonal window.
   This will smoothen in series in the process.

2. Seasonal difference the series (subtract the value of previous season
   from the current value)

3. Divide the series by the seasonal index obtained from STL decomposition
"""

#%% Subtracting the Trend Component.

# multiplicative
data_des_m = df.value / res_m.seasonal
plt.plot(data_des_m)
plt.plot(title="Drug Sales Deseasonlized", fontsize=12)

# additive
data_des_a = df.value - res_a.seasonal
plt.plot(data_des_a)

#%% differentiate with given step (lag = 12)

plt.plot(df.diff(1))
plt.plot(df.diff(12))
plt.plot(df.diff(1).diff(12))

#%% 14. How to test for seasonality of a time series?
"""
The common way is to plot the series and check for repeatable patterns in fixed time intervals. So, the types of seasonality is determined by the clock or the calendar:

    Hour of day
    Day of month
    Weekly
    Monthly
    Yearly

However, if you want a more definitive inspection of the seasonality,
use the Autocorrelation Function (ACF) plot (explained below).

Formal test
[CHTest](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.CHTest.html#pmdarima.arima.CHTest)
"""
from pandas.plotting import autocorrelation_plot
autocorrelation_plot(df)

#%% 15. How to treat missing values in a time series?
"""
Some effective ways of imputation are:

1. Forward fill
2. Backward Fill
3. Linear Interpolation
4. Quadratic interpolation
5. Mean of nearest neighbors
6. Mean of seasonal counterparts

To measure the imputation performance,
I manually introduce missing values to the time series,
impute it with above approaches
and then measure the mean squared error of the imputed against the actual values.
"""

#%%
fig, axes = plt.subplots(7, 1, sharex=True, figsize=(10, 12))
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'], index_col='date').head(100)
dfm = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10_missings.csv', parse_dates=['date'], index_col='date').head(100)

...[a lot of code]

#%%
"""
You could also consider the following approaches depending on how accurate you want
the imputations to be.

1. If you have explanatory variables use a prediction model like the random forest
   or k-Nearest Neighbors to predict it.
2. If you have enough past observations, forecast the missing values.
3. If you have enough future observations, backcast the missing values
4. Forecast of counterparts from previous cycles.
"""
#%% 16. What is autocorrelation and partial autocorrelation functions?
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Calculate ACF and PACF upto 50 lags
acf_50 = acf(df.value, nlags=50)
pacf_50 = pacf(df.value, nlags=50)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(16,3), dpi= 100)
plot_acf(df.value.tolist(), lags=50, ax=axes[0])
plot_pacf(df.value.tolist(), lags=50, ax=axes[1])

#%% 17. How to compute partial autocorrelation function?


#%% 18. Lag Plots
from pandas.plotting import lag_plot
plt.rcParams.update({'ytick.left' : False, 'axes.titlepad':10})

# Import
ss = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/sunspotarea.csv')
a10 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', )

# Plot
fig, axes = plt.subplots(1, 4, figsize=(10,3), sharex=True, sharey=True, dpi=100)
for i, ax in enumerate(axes.flatten()[:4]):
    lag_plot(ss.value, lag=i+1, ax=ax, c='firebrick')
    ax.set_title('Lag ' + str(i+1))

fig.suptitle('Lag Plots of Sun Spots Area \n(Points get wide and scattered with increasing lag -> lesser correlation)\n', y=1.15)

fig, axes = plt.subplots(1, 4, figsize=(10,3), sharex=True, sharey=True, dpi=100)
for i, ax in enumerate(axes[:4]):
    lag_plot(a10.value, lag=i+1, ax=ax, c='firebrick')
    ax.set_title('Lag ' + str(i+1))

fig.suptitle('Lag Plots of Drug Sales', y=1.05)
plt.show()

#%% 19. How to estimate the forecastability of a time series?
"""
The ‘Approximate Entropy’ can be used to quantify the regularity and unpredictability
of fluctuations in a time series.
The higher the approximate entropy, the more difficult it is to forecast it.

Another better alternate is the ‘Sample Entropy’.
Sample Entropy is similar to approximate entropy but is more consistent
in estimating the complexity even for smaller time series.
"""
#%% Approximate_entropy
# https://en.wikipedia.org/wiki/Approximate_entropy
rand_small = np.random.randint(0, 100, size=36)
rand_big = np.random.randint(0, 100, size=136)

def ApEn(U, m, r):
    """Compute Aproximate entropy"""
    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m)] for i in range(N - m + 1)]
        C = [len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / (N - m + 1.0) for x_i in x]
        return (N - m + 1.0)**(-1) * sum(np.log(C))

    N = len(U)
    return abs(_phi(m+1) - _phi(m))

print(ApEn(ss.value, m=2, r=0.2*np.std(ss.value)))     # 0.651
print(ApEn(a10.value, m=2, r=0.2*np.std(a10.value)))   # 0.537

print(ApEn(rand_small, m=2, r=0.2*np.std(rand_small))) # 0.143
print(ApEn(rand_big, m=2, r=0.2*np.std(rand_big)))     # 0.716


#%% https://en.wikipedia.org/wiki/Sample_entropy
def SampEn(U, m, r):
    """Compute Sample entropy"""
    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m)] for i in range(N - m + 1)]
        C = [len([1 for j in range(len(x)) if i != j and _maxdist(x[i], x[j]) <= r]) for i in range(len(x))]
        return sum(C)

    N = len(U)
    return -np.log(_phi(m+1) / _phi(m))

print(SampEn(ss.value, m=2, r=0.2*np.std(ss.value)))      # 0.78
print(SampEn(a10.value, m=2, r=0.2*np.std(a10.value)))    # 0.41
print(SampEn(rand_small, m=2, r=0.2*np.std(rand_small)))  # 1.79
print(SampEn(rand_big, m=2, r=0.2*np.std(rand_big)))      # 2.42

#%% 20. Why and How to smoothen a time series?
"""
    Take a moving average
    Do a LOESS smoothing (Localized Regression)
    Do a LOWESS smoothing (Locally Weighted Regression)
"""

#%%
from statsmodels.nonparametric.smoothers_lowess import lowess
plt.rcParams.update({'xtick.bottom' : False, 'axes.titlepad':5})

# Import
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                  parse_dates=['date'], index_col='date')

# 1. Moving Average
df_ma = df.value.rolling(3, center=True, closed='both').mean()
df_ma
plt.plot(df)
plt.plot(df_ma)
plt.plot(df.value.rolling(12, center=True, closed='both').mean())

# 2. Loess Smoothing (5% and 15%)
# 0.05
lw05 = lowess(df.value, np.arange(len(df.value)), frac=0.05)
type(lw05)   # numpy.ndarray
lw05.shape   # 204, 2
#
df_lw05 = pd.DataFrame(lw05[:, 1], index=df.index, columns=['value'])

# 0.15
lw15 = lowess(df.value, np.arange(len(df.value)), frac=0.15)
df_lw15 = pd.DataFrame(lw15[:, 1], index=df.index, columns=['value'])

# Plot
fig, axes = plt.subplots(4,1, figsize=(7, 7), sharex=True, dpi=120)
df['value'].plot(ax=axes[0], color='k', title='Original Series')
df_ma.plot(ax=axes[1], title='Moving Average (3)')
df_lw05['value'].plot(ax=axes[2], title='Loess Smoothed 05%')
df_lw15['value'].plot(ax=axes[3], title='Loess Smoothed 15%')
fig.suptitle('How to Smoothen a Time Series', y=0.95, fontsize=14)
plt.show()

#%% 21. How to use Granger Causality test
# to know if one time series is helpful in forecasting another?
"""
Granger causality test is used to determine if one time series, say X,
will be useful to forecast another, say Y.

The Null hypothesis is: the X series (in the second column),
does not Granger cause the Y series (in the first column).
If the P-Values are less than a significance level (0.05)
then you reject the null hypothesis and conclude that
the said lag of X is indeed useful
"""

#%%
from statsmodels.tsa.stattools import grangercausalitytests
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])
df['month'] = df.date.dt.month
gct = grangercausalitytests(df[['value', 'month']], maxlag=2)

#%%


#%%


#%%