#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: ARIMA Model – Complete Guide to Time Series Forecasting in Python
subtitle:
version: 1.0
type: tutorial
keywords: [ARIMA, time series, prediction, forecasting, ACF, PACF, seasonal, trend, unit root test]
description: |
    Tutorial on Time Series - basics.
remarks:
todo:
    - prediction for NEW API version
sources:
    - title: ARIMA Model – Complete Guide to Time Series Forecasting in Python
      link: https://www.machinelearningplus.com/time-series/arima-model-time-series-forecasting-python/
      date: 2019-02-18
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
    name: 02-ARIMA.py
    path: D:/ROBOCZY/Python/TimeSeries/Classical/
    date: 2020-09-01
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% 
#from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 120})

#%%
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.expand_frame_repr', False)

#%%
# Import as Dataframe (Australian Drug Sales)

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/wwwusage.csv', names=['value'], header=0)
df.shape     # 100, 1
df.head()
df.count()
df.isna().sum()  # 0 OK
df.plot()

ss0 = df.value

#%% 5. How to find the order of differencing (d) in ARIMA model
import statsmodels.api as sm
import statsmodels.stats as st   
"""
better use  sm.stats  as e.g. there is everything from  st.diagnostic
"""
import statsmodels.tsa.api as ts
import statsmodels.tsa.stattools as tst
import statsmodels.graphics.tsaplots as tsp

"""
dir(ts)
dir(st)
dir(tsp)
"""
#%% testing stationarity -- Augmented Dickey-Fuller test
# H0: there is a Unit Root == series is NONstatioary

help(tst.adfuller)
sm.webdoc(tst.adfuller)         # in browser
res = tst.adfuller(ss0)
res  # (adf, pvalue, usedlag, nobs, critical values (1%, 5%, 10%), icbest, resstore)
res[1]  # p-value
## pvalue > .05 thus cannot reject H0 == series is NONstationary

#%%
fig, axes = plt.subplots(3, 2) #, sharex=True)

# original series
axes[0, 0].plot(ss0);  axes[0, 0].set_title('Origial Series')
tsp.plot_acf(ss0, lags=50, ax=axes[0, 1])

# 1st diff
ss1 = df.value.diff().dropna()
axes[1, 0].plot(ss1);  axes[1, 0].set_title('1st diff')
tsp.plot_acf(ss1, lags=50, ax=axes[1, 1])

# 1st diff
ss2 = ss1.diff().dropna()
axes[2, 0].plot(ss2);  axes[2, 0].set_title('2nd diff')
tsp.plot_acf(ss2, lags=50, ax=axes[2, 1])


#%% Ljung-Box test for White Noise Q(m)
# https://support.numxl.com/hc/en-us/articles/115001099806-How-do-I-test-whether-a-given-time-series-is-just-white-noise-
# H0: r1 = r2 = ... = rM = 0 i.e. autocorr. up to lag M is 0 
#     i.e. we have (weak) WN.
# Q(m) >= p-val == cannot reject H0 == we have WN.
# Q(m) < p-val  == we reject H0     == we DO NOT have WN

sm.webdoc(sm.stats.acorr_ljungbox)
sm.stats.acorr_ljungbox(ss0, lags = 20, return_df=True)
# or from st.diagnostic. (yeah! it's a mess...)
st.diagnostic.acorr_ljungbox(ss0, lags = 20, return_df=True)  
"""
If lags is an integer then this is taken to be the largest lag that is included, 
the test result is reported for all smaller lag length. 
If lags is a list or array, 
then all lags are included up to the largest lag in the list, 
however only the tests for the lags in the list are reported.
"""
sm.stats.acorr_ljungbox(ss0, lags = [1, 5, 20], return_df=True)
# it's certainly NOT a WN

#%% together
plt.rcParams.update({'figure.figsize': (7, 5), 'figure.dpi': 120})
for i, df_ in enumerate([ss0, ss1, ss2]):
    print(i)
    print(tst.adfuller(df_))
    print(sm.stats.acorr_ljungbox(df_, lags=[1, 2, 3, 4, 5, 10, 30], return_df=True))
    fig, axes = plt.subplots(3, 1)
    fig.suptitle(f'ss{i}')
    axes[0].plot(df_)
    tsp.plot_acf(df_, lags=int(len(df_)/4), ax=axes[1])
    tsp.plot_pacf(df_, lags=int(len(df_)/4), ax=axes[2])
    
"""!!! REMARK
Box & Jenkis (1976, p.33) suggests that for ACF (PACF)
N >= 50 and h <= N/4 
(we have N=100 and took h <= n/4)
"""
    
#%% How much to diff ?
#!!!   conda install -c saravji pmdarima
from pmdarima.arima.utils import ndiffs
ndiffs(ss0, test='adf')   # 2    -- Augmented Dickey-Fuller  (unit root exists)
ndiffs(ss0, test='kpss')  # 0    -- KPSS                     (trend stationarity)
ndiffs(ss0, test='pp')    # 2    -- Philips-Perron           (integrated 1)
"""
make it just with  statsmodels  as pmdairma uses it too
References: R's auto_arima ndiffs function: https://bit.ly/2Bu8CHN
everything copied from R's adf.test(), kpss.test(), pp.test()
look R help for basic info and references on these tests.
"""

#%% 6. How to find the order of the AR term (p)

#%% 7. How to find the order of the MA term (q)

#%% 8. How to handle if a time series is slightly under or over differenced
"""
It may happen that your series is slightly under differenced, 
that differencing it one more time makes it slightly over-differenced.
How to handle this case?

If your series is slightly under differenced, 
adding one or more additional AR terms usually makes it up. 
Likewise, if it is slightly over-differenced, try adding an additional MA term.
"""

#%% 9. How to build the ARIMA Model
from statsmodels.tsa.arima_model import ARIMA   # or
from statsmodels.tsa.api import ARIMA           # the same
# what is exactly
ts.ARIMA
"""!!!
FutureWarning: 
statsmodels.tsa.arima_model.ARMA and 
statsmodels.tsa.arima_model.ARIMA have been deprecated in favor of 
statsmodels.tsa.arima.model.ARIMA 
(note the .  between arima and model) and
statsmodels.tsa.SARIMAX. 
These will be removed after the 0.12 release.
"""

#%% arima 1, 1, 2
#%%
arima112 = ts.ARIMA(ss0, order=(1,1,2))
help(arima112.fit)
arima112_fit = arima112.fit()
arima112_fit.summary()

#%% some checks (for fun)
from scipy import stats
N = stats.norm()          # normal distribution
z = 1.1202/1.290; z
2*(1-N.cdf(z))
z = 0.6351/0.257; z
2*(1-N.cdf(z))
z = 0.5287/0.355; z
2*(1-N.cdf(z))
z = 0.0010/0.321; z
2*(1-N.cdf(z))

#%% density estimator (for residuals in this case)
# https://www.statsmodels.org/stable/examples/notebooks/generated/kernel_density.html
resids112 = arima112_fit.resid[1:]   # the 1st el is (wrongly!) ss0[0]

help(sm.nonparametric.KDEUnivariate)
dens112 = sm.nonparametric.KDEUnivariate(resids112)
dens112.fit()
dir(dens112)
"""!!! REMARK
dens112.density  is an array without any index indicating the support !!!
i.e. index is just positional 0, 1, ..., N-1.
Use  x=dens112.support
"""

fig, axes = plt.subplots(2, 1)
axes[0].plot(resids112); axes[0].set_title("residuals")
axes[1].plot(dens112.support, dens112.density); axes[1].set_title("density")

#%% White Noise and Normality checks
from scipy import stats
help(stats.shapiro)          # normality (via order statistics)
stats.shapiro(resids112)     # test statistic, p-value
# looks like normal

sm.stats.jarque_bera(resids112)   # JBstatistic, p-value, skew, kurtosis
# looks like Normal

help(sm.stats.acorr_ljungbox)
sm.stats.acorr_ljungbox(resids112, lags = [1,2,3,4,5,10], return_df=True) 
# looks like White Noise

help(sm.stats.acorr_breusch_godfrey) 
sm.stats.acorr_breusch_godfrey(arima112_fit, )  
## The default value of nlags after v0.12, is min(10, nobs//5). 
# (Lagrange multiplier test statistic,  The p-value for Lagrange multiplier test, \
#  The value of the f statistic for F test,  The pvalue for F test)
# so no serial correlation up to `lags` - WhiteNoise
 
help(sm.stats.durbin_watson)
sm.stats.durbin_watson(resids112)   # 1.98
""" from help
The test statistic is approximately equal to 2*(1-r) where ``r`` is the
sample autocorrelation of the residuals. 

!!! our case:
Thus, for r == 0, indicating no serial correlation, the test statistic equals 2. 

This statistic will always be between 0 and 4. 
The closer to 0 the statistic, the more evidence for positive serial correlation. 
The closer to 4, the more evidence for negative serial correlation.

NOTICE that this function returns no p-values...
Here they are:
"""
from rcando.copies.dwtest import durbin_watson_test
durbin_watson_test(resids112, X=...)    # X regressors must be given ... :(
# a long story...


#%%  arima 1, 1, 1 
#%%
arima111 = ts.ARIMA(ss0, order=(1,1,1))
arima111_fit = arima111.fit()
arima111_fit.summary()

#%% simpler way of getting the density plot is by using pd.DataFrame utility
resids = pd.DataFrame(arima111_fit.resid[1:])
fig, axes = plt.subplots(2, 1)
resids.plot(title="residuals", ax=axes[0])
resids.plot(title="density", ax=axes[1], kind='kde')

# residuals almost identical in both models!

#%%
dir(arima111_fit)
arima111_fit.plot_predict()  # NICE
arima111_fit.plot_diagnostics() #! AttributeError: 'ARIMAResults' object has no attribute 'plot_diagnostics'
#! we've made some diagostics above by hand; BUT compare below:


#%% NEW API IS DIFFERENT !!!
"""!!! Notice that 
statsmodels.tsa.arima_model.ARIMA  and
statsmodels.tsa.arima.model.ARIMA
have different API
"""
from statsmodels.tsa.arima.model import ARIMA as ARIMAnew
arima111new = ARIMAnew(ss1, order=(1, 1, 1))
arima111new_fit = arima111new.fit()
dir(arima111new_fit)
arima111new_fit.plot_predict() #! AttributeError: 'ARIMAResults' object has no attribute 'plot_predict' 
arima111new_fit.plot_diagnostics()  # very nice plot summarising what we've done above by hand

#!??? BUT HOW TO PLOT PREDICTIONS ??? 
import statsmodels.tsa.arima as tsarima
dir(tsarima)
dir(tsarima.model)
dir(tsarima.tools)

help(arima111new_fit.predict)
arima111new_pred = arima111new_fit.predict()
arima111new_pred

plt.figure()
plt.plot(ss0)
plt.plot(arima111new_pred)    # ooops... where is the trend ???
plt.plot(arima111new_pred.cumsum() + ss0[0])    # it is NOT the copy of original series
#! It was done by hand! Is there faster method like old .plot_predict()  ???
## on the other hand
plt.plot(ss0.diff()[1:])


arima111new_fit.forecast()     # prediction of the future values
arima111new_fit.forecast(3)    # prediction of the future values

#%%
arima111new_pred = arima111new_fit.predict(dynamic=80)
arima111new_pred

plt.figure()
plt.plot(ss0)
plt.plot(arima111new_pred)    # ooops... where is the trend ???
plt.plot(arima111new_pred.cumsum() + ss0[0])    # it is NOT the copy of original series
#! It was done by hand! Is there faster method like old .plot_predict()  ???
## on the other hand
plt.plot(ss0.diff()[1:])

#!!! this is another NONsense
# THERE IS REALLY STH. WRONG WITH NEW API !!!
# or maybe I don't uderstand sth... :(

#%% go back to old API
help(arima111_fit.plot_predict)

arima111_fit.plot_predict(start=80)

fig, ax = plt.subplots()
plt.plot(ss0)
arima111_fit.plot_predict(start=80, ax=ax, plot_insample=False)
arima111_fit.plot_predict(start=80, dynamic=True, ax=ax, plot_insample=False)

#%%
help(arima111_fit.plot_predict)
"""
When you set dynamic=False the in-sample lagged values are used for prediction.
That is, the model gets trained up until the previous value to make the next prediction. 
This can make the fitted forecast and actuals look artificially good.
"""
arima111_fit.plot_predict()
arima111_fit.plot_predict(dynamic=False)
#??? NO difference...
"""
REMARK: It doesn't look similar to the predictions made above for new API (by hand) !!!
WHY ???
"""

arima111_fit.plot_predict(dynamic=True)     # NONSENSE !!! 
"""
there is sth. more to this:
dynamic=True without any further arguments gives prediction based only
on the first element, probably on top of the trend or integrated... ???
find it out !!!
see:
"""
fig, ax = plt.subplots()
plt.plot(ss0)
arima111_fit.plot_predict(start=10, ax=ax, plot_insample=False)
arima111_fit.plot_predict(start=10, dynamic=True, ax=ax, plot_insample=False)
arima111_fit.plot_predict(start=50, dynamic=True, ax=ax, plot_insample=False)
arima111_fit.plot_predict(start=57, dynamic=True, ax=ax, plot_insample=False)
arima111_fit.plot_predict(start=80, dynamic=True, ax=ax, plot_insample=False)

#%%
#%% 10. How to do find the optimal ARIMA model manually 
# using Out-of-Time Cross validation

train0 = ss0[:85]
test0 = ss0[85:]

#%% by hand
mod = ts.ARIMA(train0, order=(1,1,1))
help(mod.fit)
fit = mod.fit(disp=-1)   # disp < 0 means no output to terminal on algorithms work

fc, se, conf = fit.forecast(15, alpha=.05)
fc
se
conf

fc_df = pd.DataFrame(conf, index=test0.index, columns=['lower', 'upper'])
fc_df['fc'] = fc #pd.Series(fc, index=test0.index)
fc_df

plt.figure(figsize=(7, 5), dpi=120)
plt.title("Forecasts vs Actual")
plt.plot(train0, label='training')
plt.plot(test0, label='test')
plt.plot(fc_df.fc, label='forecast')
plt.fill_between(fc_df.index, fc_df.lower, fc_df.upper, color='k', alpha=.15)
plt.legend(loc="upper left", fontsize=8)
plt.show()

#%%
#%% use MY module 
import rcando as ak
        
#%%
#arimas = SearchARIMA(train0, test0, 1, 1, 1)
arimas = ak.SearchARIMA(train0, test0, 3, 2, 3)
arimas.models
arimas.pvalues
arimas.statistics
arimas.summary
print(arimas.summary.to_string(na_rep=""))

#%%
arimas.get_model((3,2,2)).forecast(15, True)
arimas[(3,2,2)].forecast(15, True)
arimas[(3,2,2)].test(test0, True)

#%% the same as
mod = ak.ModelARIMA(train0, order=(3,2,2))
mod.forecast(15, True)
mod.test(test0, True)

#%% the same with dates
zz0 = pd.Series(ss0.values, index = pd.date_range(start='2020-01-01', freq='D', periods=len(ss0)))
train0 = zz0[:85]
test0 = zz0[85:]

arimas = ak.SearchARIMA(train0, test0, 3, 2, 2)
arimas[(3,2,2)].forecast(15, True)
arimas[(3,2,2)].test(test0, True)

arimas.pvalues
arimas.statistics
arimas.summary
print(arimas.summary.to_string(na_rep=""))

#%% 11. Accuracy Metrics for Time Series Forecast
"""
The commonly used accuracy metrics to judge forecasts are:

    Mean Absolute Percentage Error (MAPE)
    Mean Error (ME)
    Mean Absolute Error (MAE)
    Mean Percentage Error (MPE)
    Root Mean Squared Error (RMSE)
    Lag 1 Autocorrelation of Error (ACF1)
    Correlation between the Actual and the Forecast (corr)
    Min-Max Error (minmax)

Typically, if you are comparing forecasts of two different series, 
the MAPE, Correlation and Min-Max Error can be used.
"""

# Accuracy metrics
def forecast_accuracy(forecast, actual):
    mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
    me = np.mean(forecast - actual)             # ME
    mae = np.mean(np.abs(forecast - actual))    # MAE
    mpe = np.mean((forecast - actual)/actual)   # MPE
    rmse = np.mean((forecast - actual)**2)**.5  # RMSE
    corr = np.corrcoef(forecast, actual)[0,1]   # corr
    mins = np.amin(np.hstack([forecast[:,None], 
                              actual[:,None]]), axis=1)
    maxs = np.amax(np.hstack([forecast[:,None], 
                              actual[:,None]]), axis=1)
    minmax = 1 - np.mean(mins/maxs)             # minmax
    acf1 = ts.acf(forecast - actual)[1]                      # ACF1
    return pd.Series({'mape':mape, 'me':me, 'mae': mae, 
            'mpe': mpe, 'rmse':rmse, 'acf1':acf1, 
            'corr':corr, 'minmax':minmax}).round(3)

fc_df, acc = arimas[(3,2,2)].test(test0)
acc
forecast_accuracy(fc_df.fc, test0)

# but all this already incorporated into
arimas.statistics

#%%
#%% 12. How to do Auto Arima Forecast in Python
"""
Like R’s popular auto.arima() function, the pmdarima package provides auto_arima() 
with similar functionality.

auto_arima() uses a stepwise approach to search multiple combinations of p,d,q parameters 
and chooses the best model that has the least AIC.
"""
# conda install pyramid-arima
import pmdarima as pm

model = pm.auto_arima(ss0, start_p=1, start_q=1, max_p=3, max_q=3,
                      m=1,         # frequency of series
                      test='adf',  # use adf_test to fid optimal `d`
                      d=None,      # let model determine `d`
                      seasonal=False, start_P=0, D=0, 
                      stepwise=True,
                      trace=True, error_action='ignore',
                      supress_warnings=True
                      )
print(model.summary())

#%% 13. How to interpret the residual plots in ARIMA model
model.plot_diagnostics()  
# looks like API of  statsmodels.tsa.arima.model  is used (new, not .arima_model - old)

#%% do some prediction
fc, confint = model.predict(n_periods=15, return_conf_int=True)
fc
confint

fc_df = pd.DataFrame(confint, columns=['upper', 'lower'])
fc_df['fc'] = fc
fc_df.index = np.arange(len(ss0), len(ss0)+15)

plt.plot(ss0)
plt.fill_between(fc_df.index, fc_df.lower, fc_df.upper, alpha=.15)
plt.plot(fc_df.fc)
plt.title("Forecast of ...")

#%%
#%% 14. How to automatically build SARIMA model in python
"""
The problem with plain ARIMA model is it does not support seasonality.

If your time series has defined seasonality, then, 
go for SARIMA which uses seasonal differencing.

Seasonal differencing is similar to regular differencing, but, 
instead of subtracting consecutive terms, you subtract the value from previous season.

So, the model will be represented as SARIMA(p,d,q)x(P,D,Q,X), 
where, P, D and Q are SAR, order of seasonal differencing 
and SMA terms respectively and 'X' is the frequency of the time series.

If your model has well defined seasonal patterns, 
then enforce D=1 for a given frequency ‘x’.

!!! Here’s some practical advice on building SARIMA model:
As a general rule, set the model parameters such that __D never exceeds one__!!! 
And the total differencing __‘d + D’ never exceeds 2__!!! 
Try to keep only either SAR or SMA terms if your model has seasonal components.

Let’s build an SARIMA model on 'a10' – the drug sales dataset.
"""
#%%
ss = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv',
                 parse_dates=['date'], index_col='date')
type(ss)     # df
ss.head()
dd = ss.value
dd

#%%
fig, axes = plt.subplots(3, 1, figsize=(10, 5), dpi=100, sharex=True)

#with axes[0] as a:                              #! AttributeError: __enter__
#    a.plot(dd, label='original')
#    a...

axes[0].plot(dd)
axes[0].set_title('original series')

axes[1].plot(dd.diff(1), label='diff 1')
axes[1].set_title('usual lag 1 differenncig ')

axes[2].plot(dd.diff(12), label='diff 12')
axes[2].set_title('seasonal lag 12 differenncig')

#%% 
import pmdarima as pm
smodel = pm.auto_arima(dd, start_p=1, start_q=1, max_p=3, max_q=3, 
                       test='adf', d=None,
                       seasonal=True, m=12,   # == X  frequency
                       start_P=0, D=1,
                       stepwise=True, trace=True,
                       error_action='ignore', supress_warnings=True
                       )
smodel.summary()

#%% forecast for the next 24 months
fc, confint = smodel.predict(n_periods=24, return_conf_int=True)

fc_df = pd.DataFrame(confint, columns=['lower', 'upper'])
fc_df['fc'] = fc
fc_df.index = pd.date_range(dd.index[-1], periods=24, freq='MS')

plt.plot(dd)
plt.plot(fc_df.fc)
plt.fill_between(fc_df.index, fc_df.lower, fc_df.upper, alpha=.15)
plt.title("Forecast of drug sales - SARIMA")


#%% 15. How to build SARIMAX Model with exogenous variable
from dateutils.parser import parse

sd = ts.seasonal_decompose(dd[-36:], model='multiplicative', extrapolate_trend='freq')
sd
dir(sd)

seasonal = sd.seasonal[-12:].to_frame()
seasonal['month'] = seasonal.index.month
seasonal

ss['month'] = ss.index.month
ss

# !!!
dfs = pd.merge(ss, seasonal, how='left', on='month')
dfs
dfs.index = ss.index
dfs.head()
dfs.tail()

#%%
sxmodel = pm.auto_arima(dfs[['value']], exogenous=dfs[['seasonal']], 
                       start_p=1, start_q=1, max_p=3, max_q=3, 
                       test='adf', d=None,
                       seasonal=True, m=12,   # == X  frequency
                       start_P=0, D=1,
                       stepwise=True, trace=True,
                       error_action='ignore', supress_warnings=True
                       )
sxmodel.summary()
"""
exogenous var coeff is very small and not signifficant at all..
"""

#%%
fc, confint = sxmodel.predict(n_periods=24, exogenous=dfs[['seasonal']].iloc[-24:],
                              return_conf_int=True)
fc
confint

#%%
fc_df = pd.DataFrame(confint, columns=['lower', 'upper'])
fc_df['fc'] = fc
fc_df.index = pd.date_range(dfs.index[-1], periods=24, freq='MS')
fc_df

#%%
plt.plot(dfs.value)
plt.plot(fc_df.fc)
plt.fill_between(fc_df.index, fc_df.lower, fc_df.upper, alpha=.15)

#%%
#%%  16. Practice Exercises
"""
In the AirPassengers dataset, go back 12 months in time and build the SARIMA forecast for the next 12 months.

    Is the series stationary? If not what sort of differencing is required?
    What is the order of your best model?
    What is the AIC of your model?
    What is the MAPE achieved in OOT cross-validation?
    What is the order of the best model predicted by auto_arima() method?
"""

#%% END