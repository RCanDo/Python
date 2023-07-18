#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: time series analysis
subtitle: Hourly Energy Consumption
version: 1.0
type: tutorial
keywords: [time series]
description: |
    Time Series analysis on example of Hourly Energy Consumption
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title:
      chapter:
      pages:
      link: https://www.youtube.com/watch?v=vV12dGe_Fho&t=88s
      authors:
          - nick:
            fullname: Rob Mulla
            email:
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: E:/ROBOCZY/Python/datetime
    date: 2021-04-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)
import os
from pathlib import Path

# internal libraries (under proper wd - root project folder)

# working directory set to [project_root] folder (where .git resides)
# !!! it's assumed THIS file is anywhere in [project_root] or deeper !!!
pth = Path().absolute()
while not list(pth.glob(".git")):
    pth = pth.parent
os.chdir(pth)

os.getcwd()

# %%
import numpy as np
import pandas as pd
import darts as ds
import matplotlib.pyplot as plt
import seaborn as sns

import xgboost as xgb

# %%
import common.builtin as bi
import common.data_utils as du
import common.df as cdf
import common.plots as pl
from common.project import Paths
from common.config import pandas_options
pandas_options()

# %%
df = pd.read_csv("../../Data/HourlyEnergyConsumption/PJME_hourly.csv")
cdf.info(df)    # 145366

df = df.set_index('Datetime')
df.head()
df.tail()
df.plot()

df.index = pd.to_datetime(df.index)

# %%
palette = sns.color_palette()
df.plot(style=".", color=palette[0], title="PJME Energy Use in MW")


# %%
ts = ds.TimeSeries.from_dataframe(df, time_col="Datetime", fill_missing_dates=True, freq='1h')
# ! ValueError: cannot reindex on an axis with duplicate labels

# %% test-train split
train = df[df.index < '2015-01-01']
test = df[df.index >= '2015-01-01']

len(train)  # 113926
len(test)   #  31440

# %%
