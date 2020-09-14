#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Stochastic Calculus with Python
subtitle:
version: 1.0
type: examples
keywords: [stochastic calculus, Geometric Brownian Motion, ]
description: |
remarks:    # additional notes worth emphasising
todo:
    - problem 1
    - problem 2   # and so on...
sources:
    - title: Stochastic Calculus with Python: Simulating Stock Price Dynamics
      link: https://jtsulliv.github.io/stock-movement/
      date: 2017-09-21
      authors:
          - nick:
            fullname: John Sullivan
            email: jtsulliv@gmail.com
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: D:/ROBOCZY/Python/TimeSeries/Financial
    date: 2020-09-10
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando as ak
import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/TimeSeries/Financial/")
print(os.getcwd())

#%% Block delimiters allows to run separated blocks of code by one key-stroke

import numpy as np
import pandas as pd

#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", 500)
pd.set_option("display.max_rows", 100)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

#%%
import matplotlib.pyplot as plt

#%%
#%% Wienner Proces / Brownion Motion
# see: geometric_brownion_motion.py 
#
def wiener(length: int=100, dt: float=.1, seed: int=None) -> pd.DataFrame:
    """
    Wiener Process (Brownion Motion)
    """
    N = int(length) - 1
    seed = ak.htr(1e7) if seed is None else seed  # really random seed
    np.random.seed(seed)
    dW = np.random.normal(0, np.sqrt(dt), N)
    dW = np.insert(dW, 0, 0.)
    W = np.cumsum(dW)
    df = pd.DataFrame({"W": W, "dW": dW}, index=np.cumsum([dt] * (N + 1)))
    return df

#%%
seed = 5
N = 100
dt = .1

W = wiener(N, dt)
W.shape   # (100, 2)
plt.plot(W)
W.plot()
plt.axhline(0, color='grey')

#%%
#%% GBM Exact Solution
def gbm(length: int=100, dt: float=.1, 
        mu: float=0, sigma: float=1, S0: float=1, seed: int=None):
    """
    Geometric Brownian Motion
    """
    W = wiener(length, dt, seed)
    drift = (mu - sigma**2 / 2) * np.linspace(dt, int(length * dt), length)
    diffusion = sigma * W.W
    W['S'] = S0 * np.exp(drift + diffusion)
    return W

#%%
length = 100
dt = .1
mu = .15
sigma = 0.4
S0 = 55.25

GBM = gbm(100, dt, mu, sigma, S0, 5)
GBM.shape     # 100, 3
GBM.head()
GBM.S.plot()

#%% 
import quandl
quandl.ApiConfig.api_key = "ohyXVxNAY_RAGnHv22pk"

start = '2016-01-01'
end = '2016-12-31'

data = quandl.get("WIKI/AMZN", start_date=start, end_date=end)
data.shape   # (252, 12)

data.head()
data.tail()

#%% 
opens = data.Open
opens.head()
opens.plot()

#%%

#%% estimation of drift and diffusion param
def daily_returns(ss):
    ss_lag = ss.shift()[1:]
    returns = (ss[1:] - ss_lag) / ss_lag
    return returns

returns = daily_returns(opens)
#%%
mu = np.mean(returns) #* 252
sigma = np.std(returns) #* np.sqrt(252)

""" ???
The mean of the returns are multiplied by the 252 trading days so that we can annualize returns. 
We’re going to build a model for a one year time horizon, 
but we could have easily converted to bi-annual, quarterly, or weekly returns. 
Similarly, the variance is also multiplied by 252.
"""

#%%
T = 252
dt = 1#.001
sim0 = gbm(T, dt, mu, sigma, opens[0], 22)
sim0.index = opens.index

opens.plot()
sim0.S.plot()

for k in range(4):
    sim_k = gbm(T, dt, mu, sigma, opens[0])
    sim_k.index = opens.index
    sim_k.S.plot()

#%%



#%%


#%%