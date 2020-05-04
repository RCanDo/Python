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
keywords: [, Pandas, NumPy]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Pandas ...
      chapter: ...
      link: https://pandas.pydata.org/pandas-docs/stable/...
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "0_-_.py"
    path: ".../Python/Pandas/User Guide/"
    date: 2020-04-11
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - arek@staart.pl
"""


#%%
from rcando.ak.builtin import flatten, paste
from rcando.ak.nppd import data_frame
import os

 PYWORKS = "D:/ROBOCZY/Python/Pandas"
# PYWORKS = "/home/arek/Works/Python/Pandas"

os.chdir(PYWORKS + "/User Guide/")
print(os.getcwd())


#%%
import numpy as np
import pandas as pd

#%% Creating a MultiIndex (hierarchical index) object
#%%