#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:10:45 2024

@author: arek
"""
# %%
import numpy as np
import pandas as pd

# %%
np.random.seed(1)
df = pd.DataFrame(
    {'A': list('abcdefgh'), 'B': range(8), 'C': np.random.randint(-8, 8, 8), 'D': np.random.sample(8)},
    index=[2,4,3,5,8,7,0,9])
df
"""
   A  B  C         D
2  a  0 -3  0.146756
4  b  1  3  0.092339
3  c  2  4  0.186260
5  d  3  0  0.345561
8  e  4  7  0.396767
7  f  5  1  0.538817
0  g  6  3  0.419195
9  h  7 -3  0.685220
"""
# %%
df[:4]
"""
   A  B  C         D
2  a  0 -3  0.146756
4  b  1  3  0.092339
3  c  2  4  0.186260
5  d  3  0  0.345561
"""
df.loc[:4]              # !!!
"""
   A  B  C         D
2  a  0 -3  0.146756
4  b  1  3  0.092339
"""
df.iloc[:4]
"""
   A  B  C         D
2  a  0 -3  0.146756
4  b  1  3  0.092339
3  c  2  4  0.186260
5  d  3  0  0.345561
"""

# %% boolean index -- on index by default
df.index.isin([3,7,9])
# array([False, False,  True, False, False,  True, False,  True])
df[df.index.isin([3,7,9])]
"""
   A  B  C         D
3  c  2  4  0.186260
7  f  5  1  0.538817
9  h  7 -3  0.685220
"""

df.loc[df.index.isin([3,7,9])]
df.iloc[df.index.isin([3,7,9])]
"""
   A  B  C         D
3  c  2  4  0.186260
7  f  5  1  0.538817
9  h  7 -3  0.685220
"""

# on columns
df.columns.isin(list('BC'))
# array([False,  True,  True, False])
df[df.columns.isin(list('BC'))]     # ! ValueError: Item wrong length 4 instead of 8.

df.loc[:, df.columns.isin(list('BC'))]
df.iloc[:, df.columns.isin(list('BC'))]
"""
   B  C
2  0 -3
4  1  3
3  2  4
5  3  0
8  4  7
7  5  1
0  6  3
9  7 -3
"""

# %%
df[[1,3]]       # ! KeyError: "None of [Index([1, 3], dtype='int64')] are in the [columns]"

df.loc[[1,3]]   # ! KeyError: '[1] not in index'
df.loc[[2,3]]
"""
   A  B  C         D
2  a  0 -3  0.146756
3  c  2  4  0.186260
"""

df.iloc[[1,3]]
"""
   A  B  C         D
4  b  1  3  0.092339
5  d  3  0  0.345561
"""
df.iloc[[2,3]]
"""
   A  B  C         D
3  c  2  4  0.186260
5  d  3  0  0.345561
"""

# %% on columns
df.loc[:,[2,3]]     # ! KeyError: "None of [Index([2, 3], dtype='int64')] are in the [columns]"
df.iloc[:,[2,3]]
"""
   C         D
2 -3  0.146756
4  3  0.092339
3  4  0.186260
5  0  0.345561
8  7  0.396767
7  1  0.538817
0  3  0.419195
9 -3  0.685220
"""
# %%

# %% other
#%%
%reset
import importlib ## may come in handy

import math as m
import numpy as np
import pandas as pd
import scipy as sp
import pylab as pl

#%%
pwd
cd D:/ROBOCZY/Python/Pandas
ls

#%%
'''
Basics
------
'''
dates = pd.date_range('1/1/2000', periods=8)
dates
dates[5]
dates[:5]
dates[[5]]

np.random.randn(8, 4)

df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df
df.mean()
df.median()
df.var()
df.min()
df.last('1D')  ## last period of TS

df - df.mean()

panel = pd.Panel({'one' : df, 'two' : df - df.mean()})
panel
panel[:,:,:]

s = df['A']
s
s[dates[5]]
type(s)  ## pandas.core.series.Series

sdf = df[['A']]
sdf
type(sdf)

panel['one']

#%%
df
df[['B', 'A']] = df[['A', 'B']]
df

## Warning: pandas aligns all AXES when setting Series and DataFrame from .loc, and .iloc.
## This will not modify df because the column alignment is before value assignment.

df.loc[:,['B', 'A']] = df[['A', 'B']]
df  ## nothing changed

## The correct way is to use raw values
df.loc[:,['B', 'A']] = df[['A', 'B']].values     ##!!!!!!!
df

#%%
'''
Attribute Access
----------------
You may access an index on a Series, column on a DataFrame,
and an item on a Panel directly as an _attribute_:
'''
sa = pd.Series([1,2,3],index=list('abc'))
sa
sa.b

dfa = df.copy()
dfa.A
type(dfa.A)

panel.one

x = pd.DataFrame({ 'x':[1,2,3], 'y':[3,4,5] })
x
x.iloc[2] = dict(x=9, y=99)
x
x.iloc[1] = {'x':0, 'y':-1}
x

#%%
'''
You can use _attribute_ access to _modify_ an existing element of a Series or column of a DataFrame,
but be careful; if you try to use attribute access to _create_ a new column,
it creates a new attribute rather than a new column.
In 0.21.0 and later, this will raise a UserWarning:
'''
x.x[0]=10; x
x.y[0:2]=1; x
x.y[0:2]=[3,4]; x
x.x=range(2); x  ## ERROR
x.x=range(3); x  ## OK

## BUT
x.z = range(3)   ## NO WARNING!!!
x      ## no column 'z'
x.z    ## .z is just another attribute

#%%
'''
Slicing ranges
--------------
'''
