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
keywords: [MultiIndex, NumPy, Pandas]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Pandas 0.25.3 User Guide
      chapter: 03 - Hierarchical indexing (MultiIndex)
      link: https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "03-multiindex_advanced_indexing.py"
    path: "D:/ROBOCZY/Python/Pandas/User Guide/"
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

# PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/Pandas/User Guide/")
print(os.getcwd())


#%%
import numpy as np
import pandas as pd

#%% Creating a MultiIndex (hierarchical index) object
#%%
arr = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
       ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

tuples = list(zip(*arr))
tuples

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index

s = pd.Series(np.random.randn(8), index=index)
s

#!!! BUT
pd.Series(np.random.randn(8), index=tuples)

#%%
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
pd.MultiIndex.from_product(iterables, names=['first', 'second'])

#%%
df = pd.DataFrame([['bar', 'one'], ['bar', 'two'],
                   ['foo', 'one'], ['foo', 'two']],
                   columns=['first', 'second'])
df

pd.MultiIndex.from_frame(df)

pd.MultiIndex.from_frame(df).to_frame()

#%% construct a MultiIndex automatically:

arr
s = pd.Series(np.random.randn(8), index=arr)
s

df = pd.DataFrame(np.random.randn(8, 4), index=arr)
df

#%%
index.names
s.index.names
df.index.names

index.levels

#%%
# This index can back any axis of a pandas object, 
# and the number of levels of the index is up to you:

df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
df

pd.DataFrame(np.random.rand(6, 6), index=index[:6], columns=index[:6])
#%%
with pd.option_context('display.multi_sparse', False):  
    print(df)

#%% Reconstructing the level labels
#%%
# The method get_level_values() will return a vector of the labels 
# for each location at a particular level:
    
index
index.get_level_values()  #! TypeError: get_level_values() missing 1 required positional argument: 'level'
index.get_level_values(level=0)
index.get_level_values(1)
index.get_level_values('second')

#!!! Notice that `level` here has a differet meaning then in
index.levels

#%% Basic indexing on axis with MultiIndex
#%%
""" 
One of the important features of hierarchical indexing is that 
you can select data by a “partial” label identifying a subgroup in the data. 
Partial selection “drops” levels of the hierarchical index in the result 
in a completely analogous way to selecting a column in a regular DataFrame:
"""
df
df['bar']  # level 0
df['one']  #! KeyError: 'one'  -- level 1
df['bar']['one']

s
s['qux']

# See 'Cross-section with hierarchical index' below
# for how to select on a deeper level. e.g.
df.xs('one', level='second', axis=1)    # very complicated

#??? HOW TO SWAP LEVELS within DF ???
df.swaplevel(axis=1)
df.swaplevel(axis=1)['one']
    
#%% Defined levels
#%%
"""
The MultiIndex keeps all the defined levels of an index, 
even if they are not actually used. 
When slicing an index, you may notice this. For example:
"""
df
df.columns
df.columns.names

df.columns.levels  #!

df[['foo', 'qux']]
df[['foo', 'qux']].columns.levels

"""
This is done to avoid a recomputation of the levels in order to make slicing 
highly performant. 
If you want to see only the used levels, you can use the get_level_values() method.
"""

df[['foo', 'qux']].columns.to_numpy()
df[['foo', 'qux']].columns.get_level_values(0)

"""
To reconstruct the MultiIndex with only the used levels, 
the remove_unused_levels() method may be used.
"""
new_mi = df[['foo', 'qux']].columns.remove_unused_levels()
new_mi
new_mi.levels
    
#%% Data alignment and using reindex
#%%
"""
Operations between differently-indexed objects having MultiIndex 
on the axes will work as you expect; 
data alignment will work the same as an Index of tuples:
"""
s
s[:-2]
s + s[:-2]
s + s[::2]

"""
The reindex() method of Series/DataFrames can be called with another MultiIndex, 
or even a list or array of tuples:
"""
index
index[:3]
s.reindex(index[:3])
s.reindex([('foo', 'two'), ('bar', 'one'), ('qux', 'one'), ('baz', 'one')])
    
#%% Advanced indexing with hierarchical index
#%%
df
df = df.T
df

df.loc[('bar', 'two')]
df.loc['bar', 'two']        #! this is shorthand which may lead to ambiguity !

df.loc[('bar', 'two'), 'A']

df.loc['bar']    # is a shorthand for
df.loc['bar',]
df.loc[('bar',),]

df.loc['one']    #! KeyError: 'one'

#!!! Again, as for columns:
df.xs('one', level='second', axis=0)    # very complicated

#??? HOW TO SWAP LEVELS within DF ???
df.swaplevel(axis=0)
df.swaplevel(axis=0).loc['one']

#%%
df.loc['baz':'foo']
df.loc[('baz', 'two'):('qux', 'one')]
df.loc[('baz', 'two'):'foo']            # all foos are taken!

#!!! Passing a list of labels or tuples works similar to reindexing:
df.loc[[('bar', 'two'), ('qux', 'one')]]
df.loc[[('bar', 'two'), ('qux', 'one')]].index

"""Note
It is important to note that tuples and lists are not treated identically in pandas 
when it comes to indexing. 
Whereas a tuple is interpreted as one multi-level key, a list is used to specify several keys. 
Or in other words, tuples go horizontally (traversing levels), 
lists go vertically (scanning levels).

???
"""

#%%
"""
Importantly, a list of tuples indexes several complete MultiIndex keys, 
whereas a tuple of lists refer to several values within a level:
"""
s = pd.Series([1, 2, 3, 4, 5, 6],
              index=pd.MultiIndex.from_product([["A", "B"], ["c", "d", "e"]]))
s

s.loc[[("A", "c"), ("B", "d")]]  # list of tuples

s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists

#%%  Using slicers
https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#using-slicers




#%%




#%%