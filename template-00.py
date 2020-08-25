#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title:
subtitle:
version: 1.0
type:          # possible values: ...
keywords: [kw1, kw2, ..., kwn]   # there are always some keywords!
description: |
    Description of what is in the file.
    Detailed but do not make lectures here!
remarks:    # additional notes worth emphasising
    - eg. work interactively (in Spyder)
    - install PackageX first
    - etc.
todo:
    - problem 1
    - problem 2   # and so on...
sources:   # there may be more sources
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
          to what extent this source was used:
          is the file just copy from the source?
          or the main idea was taken from the source?
          or only some minor details of the algorithm were borrowed from the source
          (what details?)
          be conscise!
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: D:/ROBOCZY/Python/...
    date: 2020-08-
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import gym
import numpy as np

#%% Block delimiters allows to run separated blocks of code by one key-stroke
# e.g. Shift+Enter in Spyder

"""
Created on Sat May  2 09:13:27 2020

link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""

import pandas as pd

pd.options.display.width = 0  # autodetects the size of your terminal window

pd.set_option('display.max_rows', 500)
pd.options.display.max_rows = 500         # the same
pd.options.display.max_colwidth = 500         # the same

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pd.set_option('display.max_rows', 500)   #!!!


# %% However, some style checkers like Flake may complain on #%% - there should be space after #

""" run the whole block
in Spyder: Shift+Enter or the icon: green arrow with red arrow
"""

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

pd.set_option('display.precision', 2)


# %%

"""
Interactive work style is very useful when debugging or learning.

Of course the block delimiters are allowed in Python (it's just the comment)
thus the whole file may be smoothly run.
"""


