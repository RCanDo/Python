# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:46:41 2019

@author: staar
"""

import numpy as np
import pandas as pd

#%%

data = [[1, 2, 4], [4, 0, 10], [10, 20, 30]]
pd.DataFrame(data)

df = pd.DataFrame(data, index=list('pqr'), columns=list('XYZ'))
df
# pd.DataFrame.from_...(data, index=[], columns=[])

#%% columns as attributes
df.X

type(df.X)  # Series
df.X < 5    # Series boolean
list(df.X < 5)  # list

list(df.X)      # list
tuple(df.X)     # tuple
set(df.X)       # set

#%% directly -- uses names with precedence of cols

df['X']     # Series
df[['X']]   # DataFrame
df[['X', 'Z']]

#!!! ???
list(df[['X']])   # ['X']
tuple(df[['X']])  # ('X',)
set(df[['X']])    # {'X'}
#!!! ???

df['p']  #! no such col
# to choose row must use `:`
df[:'p'] #  row -- but in fact:
type(df[:'p'] )  #!  pandas.core.frame.DataFrame
df['p':'r']   # rows
df[['p':'r']]   #! invalid syntax

df[1]       #! cols
df[[0, 3]]  #! cols
df[:1]      #  rows  -> DF
df[1:2] > 0         # -> DF

df[['p', 'r']]  #! no such cols
# cannot choose specific rows... only ranges defined via `:`

# however, using boolean list references rows!!! (not cols! - even without `:`)
df[[True, False, True]]  # rows  boolean as list
df[df.X < 5]             # rows  boolean as Series

#!!! double indexing doesn't work directly !!!
df[:1, :]   #! invalid key
df['p', :]  #! invalid key
# boolean for cols
df[:, [True, False, True]]   #! invalid key
# boolean for rows
df[[True, False, True], :]   #! invalid key

#! cannot directly work on cols with booleans or numbers (column indexes)
# need sth more

#%% .loc[]
# names with precedence of rows

df.loc['p']        # row -> Series
df.loc[['p']]      # rows -> DF
df.loc[['p', 'r']] # rows -> DF

# double indexing works!
df.loc['q', :]     # -> Series
df.loc[['q'], :]   # -> DF
df.loc['q':'r', :] # -> DF

df.loc['X']        #! no such row
df.loc[:, 'X']     # -> Series
df.loc[:, ['X']]   # -> DF
df.loc[:, 'X':'Y'] # -> DF

df.loc[:, :]       # -> DF

#!!! numbers doesn't work with .loc[]
df.loc[1]    #!
df.loc[1, :]  #!
df.loc[:, 1]  #!

# booleans work!
df.loc[[True, False, True]]      # rows
df.loc[[True, False, True], :]   # rows
df.loc[[True, False, False], :]  # always -> DF

# booleans for columns works too!
df.loc[:, [True, False, True]]
df.loc[:, [True, False, False]]  # always -> DF

# on rows
df.loc[df.X < 5]                 # boolean as Series
df.loc[df.X < 5, :]              # boolean as Series
df.loc[list(df.X < 5)]           # boolean as list
df.loc[list(df.X < 5), :]        # boolean as list

# on columns
df.loc[:, [True, False, True]]   # boolean as list
df.loc[:, df.loc['q'] > 0]       # boolean as Series
# notice:
df.loc['q']       # -> Series
df.loc['q'] > 0   # -> Series

# but
df.loc[['q']]         # -> DF
df.loc[['q']] > 0     # -> DF  !!!
# also
df[1:2]         # -> DF
df[1:2] > 0     # -> DF
df.loc[:, df[1:2] > 0]  #!  Cannot index with multidimensional key !

#%% .iloc[]
# numbers with precedence of rows

df.iloc[0]    # -> Series
df.iloc[[0]]    # -> DF
df.iloc[[0, 2]]    # -> DF

df.iloc[0, :]    # -> Series
df.iloc[[0], :]    # -> DF
df.iloc[[0, 2], :]    # -> DF

df.iloc[:, 0]    # -> Series
df.iloc[:, [0]]    # -> DF
df.iloc[:, [0, 2]]    # -> DF

#!!! names doesn't work with .iloc[]
df.iloc['p']
df.iloc['p', :]
df.iloc[:, 'X']

# booleans work but only as list ! (cannot be Series... strange!)
df.iloc[[True, False, True]]
df.iloc[[True, False, False]]    # always -> DF
df.iloc[[True, False, True], :]

df.iloc[:, [True, False, True]]
df.iloc[:, [True, False, False]] # always -> DF

#! BUT
df.iloc[df.X < 5]        #!       boolean as Series
df.iloc[list(df.X < 5)]  # -> DF  boolean as list
df.iloc[df.X < 5, :]        #!       boolean as Series
df.iloc[list(df.X < 5), :]  # -> DF  boolean as list

df.iloc[1] > 0              # -> Series
df.iloc[:, df.iloc[1] > 0]         #!
df.iloc[:, list(df.iloc[1] > 0)]   # -> DF
df.iloc[:, list(df.iloc[1] == 0)]  # always -> DF

#%% .loc and .iloc for numeric names of rows
df
dfn = df
dfn.index = [0, 5, 10]
dfn

dfn[:1]
dfn[1:2]

# BUT
dfn.loc[0]  # ok
dfn.loc[1]  #! KeyError
dfn.iloc[1] #  -> Series
dfn.loc[5]  #  -> Series

dfn.loc[1, :]  #!
dfn.iloc[1, :] #  -> Series
dfn.loc[5, :]  #  -> Series

dfn.iloc[[1], :]   #  -> DF
dfn.loc[[5], :]    #  -> DF

#%% booleans
df > 5         # -> DF
df.X > 5       # -> Series
df['X'] > 5    # -> Series
df[['X']] > 5    # -> DF

df.loc['q']        # -> Series
df.loc['q'] > 5    # -> Series
df.loc[['q']]      # -> DF
df.loc[['q']] > 5  # -> DF

df.loc['q', :]        # -> Series
df.loc['q', :] > 5    # -> Series
df.loc[['q'], :]      # -> DF
df.loc[['q'], :] > 5  # -> DF



#%% .iat  .ix (depricated)
