#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title:
subtitle:
version: 1.0
type: tutorial
keywords: []
description: |
    About ...
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title:
      chapter:
      link: https://docs.scipy.org/doc/scipy/tutorial/general.html
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: E:/ROBOCZY/Python/SciPy/
    date: 2021-10-21
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

#%%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

#%%
ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/SciPy/")   #!!! adjust
os.chdir(WD)

#%%
WD = os.getcwd()
print(WD)

#%% Block delimiters allows to run separated blocks of code by one key-stroke
# e.g. Shift+Enter in Spyder

import numpy as np
import pandas as pd

"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""
#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

# %% other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500
# the same

#%%
pd.options.display.width = 120

#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('dark_background')
# see `plt.style.available` for list of available styles

#!!! SciPy sub-packages need to be imported separately !!!
from scipy import linalg, stats, sparse

#%%
#%%
import numpy as np

rng = np.random.default_rng()   # Generator(PCG64) at 0x7F04F7B4A200
# may be used as  random_state=rng  but it's too much randomness
# we'd like to have reproducible results here so better resort to random_state as fixed numbers


from scipy.stats import norm

dist = norm(loc=2, scale=4)  # our "unknown" distribution

data = dist.rvs(size=100, random_state=1234)
plt.hist(data)

std_true = dist.std()      # the true value of the statistic
# 4.0

std_sample = np.std(data)  # the sample statistic
# 3.982739401341612

#%% We can calculate a 90% confidence interval of the statistic using bootstrap.

from scipy.stats import bootstrap

data = (data,)  # samples must be in a sequence

res = bootstrap(data, np.std, confidence_level=0.9)
res     # BootstrapResult(
        #   confidence_interval = ConfidenceInterval(low=3.508889643797191, high=4.697198500798465),
        #        standard_error = 0.3505826727429452
        #   )

print(res.confidence_interval)
# ConfidenceInterval(low=3.503351156364158, high=4.6698952294272145)
res.confidence_interval.low   # 3.503351156364158
res.confidence_interval.high  # ..

#%%
n_trials = 1000

ci_contains_true_std = 0

for i in range(n_trials):

   data = (dist.rvs(size=100, random_state=rng),)

   ci = bootstrap(data, np.std, confidence_level=0.9, n_resamples=1000,

                  random_state=rng).confidence_interval

   if ci[0] < std_true < ci[1]:

       ci_contains_true_std += 1

print(ci_contains_true_std)
875


....

#%%
#%%
from scipy.stats import t
t.ppf(.95, 100-1)

t.interval(.95, 100-1)
t.interval(.95, 9999)


norm.interval(.95)

# %%
from statsmodels.stats import proportion
dir()
help(proportion.proportion_confint)
ci = proportion.proportion_confint(13, 23, .05)
ci
p = 13/23
p
np.mean(ci)
