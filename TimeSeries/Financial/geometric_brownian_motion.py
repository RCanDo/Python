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

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando as ak
import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/TimeSeries/Financial/")
print(os.getcwd())

#%% Block delimiters allows to run separated blocks of code by one key-stroke
# e.g. Shift+Enter in Spyder

"""
Created on Sat May  2 09:13:27 2020

link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""

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
pd.set_option('max_colwidth', -1)
#pd.options.display.max_colwidth = 500         # the same


#%%
"""

dS_t = \mu S_t dt + \sigma S_t dW_t
W_t - Wiener Process (Brownian motion)

leeds to solution (Ito):

S_t = S_0 \exp{ (\mu - \sigma^2 / 2 )t + \sigma W_t }

"""


#%%
# Python code for the plot

import numpy as np
import matplotlib.pyplot as plt

#%% relly random seed (from date)
from datetime import datetime as dt
now = dt.now()
np.random.seed(int(np.log10(np.abs(np.prod(now.today().timetuple())))))

#%%
mu = 1
n = 50
dt = 0.1
x0 = 100
# np.random.seed(1)   # seed from source


sigma = np.arange(0.8, 2, 0.2)

x = np.exp(
    (mu - sigma ** 2 / 2) * dt
    + sigma * np.random.normal(0, np.sqrt(dt), size=(len(sigma), n)).T
)
x = np.vstack([np.ones(len(sigma)), x])
x = x0 * x.cumprod(axis=0)

plt.plot(x)
plt.legend(np.round(sigma, 2))
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.title(
    "Realizations of Geometric Brownian Motion with different variances\n $\mu=1$"
)
plt.show()

#%%