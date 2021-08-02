#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: date & time
subtitle:
version: 1.0
type: tutorial
keywords: [date, time]
description: |
    About dates and time
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title:     # title of the book or internet page
      chapter:   # if necessary
      pages:     # if necessary
      link: https://the_page/../xxx.domain
      date:    # date of issue or last edition of the page
      authors:
          - nick:
            fullname:
            email:
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: D:/ROBOCZY/Python/datetime
    date: 2021-04-27
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

ROOTS = json.load(open('roots.json'))
WD = os.path.join(ROOTS['Works'], "Python/Pandas/User Guide/")   #!!! adjust
os.chdir(WD)

print(os.getcwd())

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


# %% However, some style checkers like Flake may complain on #%% - there should be space after #

""" run the whole block
in Spyder: Shift+Enter or the icon: green arrow with red arrow
"""

# %%

"""
Interactive work style is very useful when debugging or learning.

Of course the block delimiters are allowed in Python (it's just the comment)
thus the whole file may be smoothly run.
"""


