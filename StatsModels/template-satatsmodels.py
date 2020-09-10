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
    - title:
      chapter:ry
      pages:
      link: https://the_page/../xxx.domain
      date:
      authors:
          - nick:
            fullname:
            email:
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-xxx.py
    path: D:/ROBOCZY/Python/StatsModels/
    date: 2020-09-
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import rcando as ak
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
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)

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


# %%



#%%



#%%