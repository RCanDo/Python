# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:45:28 2018

@author: kasprark
"""

## http://pandas.pydata.org/pandas-docs/stable/indexing.html

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

