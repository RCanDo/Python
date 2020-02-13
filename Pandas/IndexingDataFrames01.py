"""
project: help
title: Selecting and ordering columns in pandas.DataFrame
subtitle: based on  http://pandas.pydata.org/pandas-docs/stable/indexing.html#basics
ver: 0.1
author: kasprark; arkadiusz.kasprzyk@tieto.com
date: Sun Jan 21 15:16:33 2018


"""
## •

%reset
import importlib ## may come in handy

import numpy as np
import pandas as pd

#%%

df = pd.DataFrame( np.random.randn(8, 10), columns=list('ABCDEFGHIJ') )
df

#%%
'''
Q: How to put the first column at the end or v/v i.e. last elment at the beginning?
'''

#%%
'''
Before this let's see how Index works.
'''
col = df.columns
col
type(col)  ## pandas.core.indexes.base.Index

## sometimes it behaves like list
col1 = col[:6]; col1
col2 = col[4:]; col2

col1[::-1]
col1[range(4,-1,-1)]

## sometimes somewhat different
col1 + col2
## while
list(col1) + list(col2)

## Indices works with set operators
col1 | col2
col2 | col1   ## the same final order -- alphabetical...
col1[::-1] | col2[::-1]  ## !!!
col[::-1] | col2[::-1]  ## !!!
## hence | operator results always in alphabetical order !!!

col1 ^ col2               ## symmetric difference
col1[::-1] ^ col2         ## symmetric difference
col1[::-1] ^ col2[::-1]   ## symmetric difference
## in all cases alphabetical order !!!

col1.difference(col2)           ## normal difference
col1[::-1].difference(col2)         ## normal difference
## alphabetical order !!!

col1 & col2
col & col2
col[::-1] & col2          ## EXCEPTION: order of the first Index preserved !!!

#%%
## 1. using names
df['C']
type(df['C'])  ##  pandas.core.series.Series

df[['C']]
type(df[['C']])  ## pandas.core.frame.DataFrame, i.e. one-column DataFrame

df[['C', 'H']]
df[['H', 'C']]
df[['H', 'C', 'A']]
df[['A', 'A', 'A','B']]

## using slices is possible only via .loc
df.loc[:,'A':'B']
df.loc[:,'B':'E']
## more on this later

## Answer to Q:
df[['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'A']]
## This is only possible if columns' names are known in advance
## and is obviously tedious if there are many columns.


#%%
## 1. using column Indices via column Index
col[1:5]
df[col[1:5]]
df[ col[ [1,1,3,2,5] ] ]  ## notice 3 []
df[col[-1]]    ## a Series
df[[col[-1]]]  ## a DataFrame
df[col[::-1]]
df[col[::2]]
## ...

## it works also with .loc
df.loc[:,col[1:5]]
df.loc[:, col[ [1,1,3,2,5] ] ]  ## notice 3 []
df.loc[:,col[-1]]    ## a Series
df.loc[:,[col[-1]]]  ## a DataFrame
df.loc[:,col[::-1]]
df.loc[:,col[::2]]

###############
## Answer to Q:
col = df.columns;  k = len(col)
df[col[1:k] | [col[0]]]  ## logical operations on Indexes
## FAILED !!! Set operators on Indices results in alphabetical order...

## so it may only be done like this
col = df.columns;  k = len(col)
df[col[ list(range(1,k)) + [0] ]]
## what is not elegant

## as noticed above may be also used with .loc

#%%
df[col[[0,1,3,7,2]]]

#%%
## 2. Turning Index into List 
coll = list(df.columns); coll
df[coll]

coll[1]
coll[:3]
coll[::-2]

## within df
df[coll[1]]
df[coll[:3]]
df[coll[::-2]]


## but choosing some random elements is not straightforward:
coll[0,1,3,7,2]    ## TypeError: list indices must be integers or slices, not tuple
coll[[0,1,3,7,2]]  ## TypeError: list indices must be integers or slices, not list

# BUT
col[[0,1,3,7,2]]

## solution
[ coll[k] for k in [0,1,3,7,2] ]
df[[ coll[k] for k in [0,1,3,7,2] ]]
## ugly...

## solution
[ col[k] for k in [0,1,3,7,2] ]  
df[[ col[k] for k in [0,1,3,7,2] ]]
## so there is no point of doing list() from col

###############
## Answer to Q:
coll = list(df.columns);  k = len(coll)
df[[ coll[k] for k in list(range(1,k)) + [0] ]]

# or
col = df.columns;  k = len(col)
df[[ col[k] for k in list(range(1,k)) + [0] ]]


## but this is simpler:                 #!#!#!#!#!#!#!
coll = list(df.columns)
df[ coll[1:] + [coll[0]] ]


## notice that this cannot be done
col = df.columns
df[ col[1:] + [col[0]] ]                #!!! KeyError "None of [Index(['BA', 'CA', 'DA', ...

## you may also use .append() and .pop()
coll = list(df.columns)
coll.append(coll.pop(0))   ## must be in separate line !!! doesn't work inside [ ]
df[ coll ]

#%% 
## 3. turning Index into collections.deque which is kind of list fast on appending elements on both sides
##    (list is slow on adding/removing at the beginning of it)
from collections import deque   ## https://docs.python.org/3.6/library/collections.html#collections.deque

## deque has method .rotate() not available for standard python's lists
cold = deque(col); cold
type(cold)
cold.rotate(); cold     ## rotating n steps to the right (n>0) or left (n<0) 

cold = deque(col)
cold.rotate(1); cold    ## default value n=1 -- rotate right

cold = deque(col)
cold.rotate(-1); cold    ## rotate left

###############
## Answer to Q:
cold = deque(df.columns); cold
cold.rotate(-1); list(cold)         ## must be in separate line !!! doesn't work inside [ ]
df[list(cold)]
df[cold]

#%%
## using .loc[]
df.loc[:,['A','A','B','H']]
df.loc[:,'B':'D']

col    ## Index
df.loc[:,col[:3]]
df.loc[:,col[[1,1,1,3]]]
##...


###############
## Answer to Q: already done above
df.loc[:,['B','C','D','E','F','G','H','I','J','A']]

## or
col = df.columns; k=len(col)
df.loc[:,col[ list(range(1,k)) + [0] ]]

## or
coll = list(df.columns)
df.loc[:, coll[1:] + [coll[0]] ]

## or
coll = list(df.columns)
coll.append(coll.pop(0)) 
df.loc[:, coll ]


#%%
## When using .iloc[] you may use (and must!) columns position directly, 
## without referencing to their names

df.iloc[:,[1,3,5]]
df.iloc[:,[1,1,1,0,4,7]]
df.iloc[:,1:6]
df.iloc[:,:6]

###############
## Answer to Q: 
k = (df.shape)[1]
df.iloc[:, list(range(1,k)) + [0] ]



