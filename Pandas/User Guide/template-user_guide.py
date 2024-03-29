# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title:
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
      link: https://pandas.pydata.org/pandas-docs/stable/user_guide/___.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "..py"
    path: "D:/ROBOCZY/Python/Pandas/User Guide/"
    date: 2020-08-17
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




#%%




#%%




#%%




#%%