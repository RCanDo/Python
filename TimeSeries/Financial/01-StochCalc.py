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

import pandas as pd

#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", 500)
pd.set_option("display.max_rows", 100)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

#%%
#%%


