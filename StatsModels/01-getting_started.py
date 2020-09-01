#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: StatsModels guide
subtitle:
version: 1.0
type: tutorial
keywords: [kw1, kw2, ..., kwn]
description: |
    Guide, examples, tutorial, etc...
remarks:
todo:
sources:
    - title: statsmodels v0.12.0
      chapter: Getting started
      link: https://www.statsmodels.org/stable/gettingstarted.html
      date:
      authors:
          - nick:
            fullname:
            email:
      usage: |
          not only copy
    - title: Patsy quickstart
      link: https://patsy.readthedocs.io/en/latest/quickstart.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-getting_started.py
    path: D:/ROBOCZY/Python/StatsModels/
    date: 2020-09-01
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
from rcando.ak.builtin import flatten, paste
from rcando.ak.nppd import data_frame
import os

PYWORKS = "D:/ROBOCZY/Python"
#PYWORKS = "~/Works/Python"

os.chdir(PYWORKS + "/StatsModels/")
print(os.getcwd())

#%%
import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices


#%%

"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""

pd.options.display.width = 0  # autodetects the size of your terminal window

pd.set_option('display.max_rows', 500)
pd.options.display.max_rows = 500         # the same
pd.options.display.max_colwidth = 500         # the same

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pd.set_option('display.max_rows', 500)   #!!!


# %% However, some style checkers like Flake may complain on #%% - there should be space after #

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

pd.set_option('display.precision', 2)

#%%
#%% how to import from various formats
# https://www.statsmodels.org/stable/iolib.html


# %%
# [Guerry data](https://vincentarelbundock.github.io/Rdatasets/doc/HistData/Guerry.html)
# [R datasets repo](https://github.com/vincentarelbundock/Rdatasets/ )

df = sm.datasets.get_rdataset("Guerry", "HistData").data
df.columns
cols = ['Department', 'Lottery', 'Literacy', 'Wealth', 'Region']
df = df[cols]
df[:5]
df.isna().sum()
df.isna().sum(1)
df.notna()
df.count()

df = df.dropna()
df

#%%
y, X = dmatrices('Lottery ~ Literacy + Wealth + Region', data=df, return_type='dataframe')
y
X

#%% https://www.statsmodels.org/stable/regression.html
mod = sm.OLS(y, X)
res = mod.fit()
res.summary()
dir(res)
res.params

#%% Diagnostics and specification tests
sm.stats.linear_rainbow(res)       # F-statistic , p-value.
help(sm.stats.linear_rainbow)
print(sm.stats.linear_rainbow.__doc__)

#%%
sm.graphics.plot_partregress('Lottery', 'Wealth', ['Region', 'Literacy'],
                             data=df, obs_labels=False)

#%% online (webbrowser) documentation
sm.webdoc()           # statsmodels web page - introduction
sm.webdoc('gls')
sm.webdoc(sm.GLS)
help(sm.GLS)
sm.webdoc(sm.OLS)
sm.webdoc(sm.OLS, stable=False)  # == development doc.

#%%