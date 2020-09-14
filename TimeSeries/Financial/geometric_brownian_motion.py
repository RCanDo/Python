#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Geometric Brownian motion
subtitle:
version: 1.0
type: example
keywords: [Geometric Brownion Motion, Ito integral, Wiener process]
description: |
remarks:
todo:
sources:
    - title: Geometric Brownian motion
      link: https://en.wikipedia.org/wiki/Geometric_Brownian_motion
      date: 2020-07-28
      usage: |
         Theoretical intro; code example.
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: geometric_brownian_motion.py
    path: D:/ROBOCZY/Python/TimeSeries/Financial/
    date: 2020-09-11
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import rcando as ak
import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/TimeSeries/Financial/")
print(os.getcwd())

#%%
import numpy as np
import pandas as pd

#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

#%% other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500         # the same

#%%
#%%
"""Geometric Brownian Motion

dS_t = \mu S_t dt + \sigma S_t dW_t
W_t - Wiener Process (Brownian motion) 
dW_t ~ N(0, dt)   N(mean, variance)

leeds to solution (Ito):

S_T = S_0 \exp{ (\mu - \sigma^2 / 2 )T + \sigma W_T }
    ~= S_0 \exp{ \Sigma_t^T (\mu - \sigma^2 / 2 )dt + \sigma dW_t }
    ~= S_0 \Pi_t^T \exp{ (\mu - \sigma^2 / 2 )dt + \sigma dW_t }
"""

#%%
import matplotlib.pyplot as plt

#%% seed 
# np.random.seed(1)   # seed from source
# really random seed (from date)
np.random.seed(ak.htr(1e7))

#%%
mu = 1
n = 50
dt = 0.1
S0 = 100

n * dt  # == T

sigma = np.arange(0.8, 2, 0.2)

# dt increments dSt
dSt = np.exp(
    (mu - sigma ** 2 / 2) * dt
    + sigma * np.random.normal(0, np.sqrt(dt), size=(len(sigma), n)).T
)
dSt = np.vstack([np.ones(len(sigma)), dSt])
ST = S0 * dSt.cumprod(axis=0)

plt.plot(ST)
plt.legend(np.round(sigma, 2))
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.title(
    "Realizations of Geometric Brownian Motion with different variances\n $\mu=1$"
)
plt.show()

#%%