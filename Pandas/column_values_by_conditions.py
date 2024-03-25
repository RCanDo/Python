#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
title:
version: 1.0
type: module
keywords: [conditions, lookup, select, apply, data frame, ...]
description: |
    How to construct a column in a data frame where values depend on values of other columns,
    or, more generally, where values depend on some conditions satisfied or not by values of other vectors.
content:
todo:
sources:
    - title: Creating a new column based on if-elif-else condition
      link: https://stackoverflow.com/questions/21702342/creating-a-new-column-based-on-if-elif-else-condition
remarks:
    - beware order of conditions ! (must be like in `if elif else`)
file:
    usage:
        interactive: False
        terminal: False
    date: 2021-11-05
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
# %%
import numpy as np
import pandas as pd

from utils.config import pandas_options
pandas_options()

# %%
# %%
N = 1000
y = np.random.choice(2, N, True, (.7, .3))
np.unique(y)

a = np.random.randint(-9, 9, N)
b = np.random.choice(list('abc'), N, True, (.5, .3, .2))
c = np.random.sample(N)
X = pd.DataFrame(dict(a=a, b=b, c=c))

X.head(99)


# %%  np.select()
conditions = [(X.a > 0) & (X.b == 'a'), X.c > 0.5,]
choices = ['A', 'B']
u1 = np.select(conditions, choices, default = 0)
u1
np.unique(u1, return_counts=True)

means1 = pd.Series(y).groupby(u1).mean()
means1

# %% new data
N0 = 100
a0 = np.random.randint(-9, 9, N0)
b0 = np.random.choice(list('abc'), N0, True, (.5, .3, .2))
c0 = np.random.sample(N0)
X0 = pd.DataFrame(dict(a=a0, b=b0, c=c0))
X0.index = np.random.randint(0, N0, N0)

conditions0 = [(X0.a > 0) & (X0.b == 'a'), X0.c > 0.5,]
choices0 = ['A', 'B']
u10 = pd.Series(np.select(conditions0, choices0, default = 0))
u10

y1_hat = means1[u10]
y1_hat.index = X0.index
y1_hat

# %%  no need to use default value via np.select()
conditions = [X.b == 'a', X.b == 'b', X.b == 'c']
choices = [0, 1, 2]
c1 = np.select(conditions, choices)
c1
np.unique(c1, return_counts=True)

# %%
# %%  .mask()
u2 = pd.Series(np.zeros(len(y))).astype(int)    # ~ default value / the rest
u2 = u2 \
    .mask(X.c > 0.5, 'B') \
    .mask((X.a > 0) & (X.b == 'a'), 'A')
u2
u2.value_counts()

means2 = pd.Series(y).groupby(u2).mean()
means2
means2['0']
means2['A']
means2['B']

# BTW
np.unique(u2, return_counts=True)   # ! TypeError: '<' not supported between instances of 'str' and 'int'   ???!!!
u2.values   # there are integer 0s and str 'A', 'B' in one array
u2.values.dtype     # dtype('O')  object
# this is why cannot compare (! while it's not essential for the function main task !)
np.unique(u2.values, return_counts=True)   # ! TypeError: '<' not supported between instances of 'str' and 'int'
np.unique(u2.values.astype(str), return_counts=True)
# (array(['0', 'A', 'B'], dtype='<U1'), array([396, 224, 380]))

# %%
# %%  direct substitution
u3 = pd.Series(np.zeros(len(y))).astype(int).astype(str)    # ~ default value / the rest
u3[(X.a > 0) & (X.b == 'a')] = 'A'
u3[X.c > 0.5] = 'B'

u3.value_counts()
np.unique(u3, return_counts=True)
# (array(['0', 'A', 'B'], dtype=object), array([396, 106, 498]))

# %%
