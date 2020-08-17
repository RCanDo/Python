# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Time series / date functionality
subtitle:
version: 1.0
type: tutorial
keywords: [., NumPy, Pandas]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Pandas 1.1 User Guide
      chapter:
      link: https://pandas.pydata.org/docs/user_guide/timeseries.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "14-time_series_and_dates.py"
    path: "D:/ROBOCZY/Python/Pandas/User Guide/"
    date: 2019-11-13
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
from rcando.ak.builtin import flatten, paste
from rcando.ak.nppd import data_frame
import os

"""
PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"
"""

os.chdir(PYWORKS + "/Pandas/User Guide/")
print(os.getcwd())

#%%
import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)

#%%
#%% Intro
import datetime as dt

dti = pd.to_datetime(['1/1/2018', np.datetime64('2018-01-01'), dt.datetime(2018, 1, 1)])
dti

dti = pd.date_range('2018-01-01', periods=3, freq='H')
dti

dti = dti.tz_localize('UTC')
dti

dti.tz_convert('US/Pacific')

#%%
idx = pd.date_range('2018-01-01', periods=5, freq='H')

ts = pd.Series(range(len(idx)), index=idx)
ts

ts.resample('2H').mean()

#%%
day1 = pd.Timestamp('2018-01-05')
day1.day_name()

day2 = day1 + pd.Timedelta('1 day')
day2.day_name()

day3 = day1 + pd.offsets.BDay()
day3.day_name()

#%%
#%% Overview
# https://pandas.pydata.org/docs/user_guide/timeseries.html#overview




#%%



#%%



#%%