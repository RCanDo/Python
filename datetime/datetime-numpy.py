#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: date & time in NumPy
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
      link: https://numpy.org/devdocs/reference/routines.datetime.html
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

import rcando.ak as ak
import os

ROOT = "E:/"
#ROOT = "~"
PYWORKS = os.path.join(ROOT, "ROBOCZY/Python")
##
WD = os.path.join(PYWORKS, "datetime")  ## adjust !!!
#DATA = os.path.join(ROOT, "Data/...")           ## adjust !!!

os.chdir(WD)
print(os.getcwd())

#%%
import numpy as np


#%%
# https://numpy.org/devdocs/reference/generated/numpy.busday_count.html#numpy.busday_count
# Number of weekdays in January 2011

np.busday_count('2011-01', '2011-02')
# 21

# Number of weekdays in 2011
np.busday_count('2011', '2012')
# 260

# Number of Saturdays in 2011
np.busday_count('2011', '2012', weekmask='Sat')
# 53

#%%



#%%