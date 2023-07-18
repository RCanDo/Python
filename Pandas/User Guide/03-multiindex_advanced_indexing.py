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
import numpy as np
import pandas as pd

from utils.builtin import flatten, paste
from utils.ak import data_frame

#%%
#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

# other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500
# the same

#%% Creating a MultiIndex (hierarchical index) object
#%%
arr = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
       ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
arr

#%%  (*)  !!!
# construct a MultiIndex directly and automatically
# without use of MultiIndex...()

arr
s = pd.Series(np.random.randn(8), index=arr)
s

df = pd.DataFrame(np.random.randn(8, 4), index=arr)
df

#%% BUT 'automatically' doesn't work for NumPy arrays or DataFrames

#! 1. different orientation
pd.Series(np.random.randn(8), index=np.array(arr))    #! ValueError: Length of passed values is 8, index implies 2.

#! 2. even after transposition it's not multiindex
pd.Series(np.random.randn(8), index=np.array(arr).T)  # not MultiIndex

pd.Series(np.random.randn(8), index=\
          pd.DataFrame({'first': ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                        'second': ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']})
         )                                            # not MultiIndex

#%%
#%% via  MultiIndex...()

#%% .from_arrays()
arr   #! it's a raw list of lists !
index0 = pd.MultiIndex.from_arrays(arr, names=['first', 'second'])
index0

s0 = pd.Series(np.random.randn(8), index=index0)
s0

#! but it's the same as (*) above
pd.Series(np.random.randn(8), index=arr)


#%% .from_tuples()
tuples = list(zip(*arr))
tuples

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index

s = pd.Series(np.random.randn(8), index=index)
s

#!!! BUT
pd.Series(np.random.randn(8), index=tuples)


#%% from NumPy arrays
nparr = np.array(arr)
nparr
index1 = pd.MultiIndex.from_arrays(nparr, names=['first', 'second'])
index1

#!!! be aware of
index = pd.MultiIndex.from_arrays(nparr.T)
index   #! NO !!!

#!!! no need for numpy(arr)
pd.MultiIndex.from_arrays(arr, names=['first', 'second'])   # OK !


#%% .from_frame()

index_df = pd.DataFrame({'first': ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                         'second': ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']})

index1 = pd.MultiIndex.from_frame( index_df )
index1

s1 = pd.Series(np.random.randn(8), index=index1)
s1

df = pd.DataFrame(np.random.randn(8, 4), index=index1)
df

#%% .from_frame()
df0 = pd.DataFrame([['bar', 'one'],
                   ['bar', 'two'],
                   ['foo', 'one'],
                   ['foo', 'two']],
                   columns=['first', 'second'])
df0

pd.MultiIndex.from_frame(df0)

## .to_frame()
pd.MultiIndex.from_frame(df0).to_frame()   #!!! self-indexed data frame

#%% .from_product()
iterables = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]
index = pd.MultiIndex.from_product(iterables, names=['first', 'second'])
index

pd.MultiIndex.from_product([range(2), range(3), range(3)], names=['d', 'p', 'q'])

#%% 'directly'
midx1 = pd.MultiIndex(levels=[['zero', 'one'], ['x', 'y']],
                     codes=[[1, 1, 0, 0], [1, 0, 1, 0]])
midx1

#%%
midx2 = pd.MultiIndex(levels=[['zero', 'one'], ['x', 'y']],
                     codes=[[1, 1, 0, 0, 1], [1, 0, 1, 0, 1]])
midx2

#%%  (2)
# NOTICE the meaning of `levels` -- NOT names of index's levels !!!
# but names of each index's level values !!! i.e. 'levels' like possible values of categorical variable
# For names of index's levels is `names` !!!

midx1.to_frame()

midx3 = pd.MultiIndex(levels=[['zero', 'one'], ['x', 'y']],
                     codes=[[1, 1, 0, 0], [1, 0, 1, 0]],
                     names=['level_0', 'level_1'])
midx3
midx3.to_frame()
midx3.to_frame(name=['a', 'b'])

# btw:
midx3.to_frame(index=False)
midx3.to_frame(index=False, name=['a', 'b'])

#%%
index.names
s.index.names
df.index.names

pd.MultiIndex.from_arrays(arr).levels

index.levels    #!!!

dir(index)  # ! a lot !

#%% BY THE WAY
df.sample(5)
df.sample(1, axis=1)

#%%
# This index can back any axis of a pandas object,
# and the number of levels of the index is up to you:

df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=arr)
df

df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
df

pd.DataFrame(np.random.rand(6, 6), index=index[:6], columns=index[:6])

df.sample(5, axis=1)

#%%
with pd.option_context('display.multi_sparse', False):
    print(df)

#%% Reconstructing the level labels
#%%
# The method get_level_values() will return a vector of the labels
# for each location at a particular index's level:

index
index.get_level_values()  #! TypeError: get_level_values() missing 1 required positional argument: 'level'
index.get_level_values(level=0)
index.get_level_values(1)
index.get_level_values('second')

#!!! Notice that `level` here (like ) has a differet meaning then in
index.levels   # like levels of the categorical variable

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
df.xs('one', axis=1, level='second')    # very complicated
df.xs('one', 1, 'second')    #
df.xs('one', axis=1, level=1)    # very complicated
df.xs('one', 1, 1)    #

#??? HOW TO SWAP LEVELS within DF ???
df.swaplevel(axis=1)
df.swaplevel(axis=1)['one']

#%% Defined levels
#%%
"""
The MultiIndex keeps all the defined levels (values) of an index,
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

new_df = df[['foo', 'qux']].remove_unused_levels()  #! AttributeError: 'DataFrame' object has no attribute 'remove_unused_levels'
# so a lot of coding to get part of df with MI pruned :(

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

""" !!!
The reindex() method of Series/DataFrames can be called with another MultiIndex,
or even a list or array of tuples:
"""
index
index[:3]
s.reindex(index[:3])   #!!!
s.reindex([('foo', 'two'), ('bar', 'one'), ('qux', 'one'), ('baz', 'one'), ('a', 'b')])  # NaN for ('a', 'b')

s[index[:3]]          # OK
s[index[:3]].index    # OK - pruned
s[index[:3]].index.levels    # this is not pruned, see above .remove_unused_levels()

# BUT
s[[('foo', 'two'), ('bar', 'one'), ('qux', 'one'), ('baz', 'one'), ('a', 'b')]]  #! KeyError: "[('a', 'b')] not in index"
# so we need .reindex() !

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
df.xs('one', axis=0, level='second')    # very complicated
df.xs('one', 0, 'second')    # very complicated
df.xs('one', 0, 1)    # very complicated

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
df.loc[[('bar', 'two'), ('qux', 'one')]].index.levels   # all levels - not pruned !

"""Note
It is important to note that tuples and lists are not treated identically in pandas
when it comes to indexing.
Whereas a tuple is interpreted as one multi-level key, a list is used to specify several keys.
Or in other words, tuples go 'horizontally' (traversing levels),
lists go 'vertically' (scanning levels).
"""

#%%
"""
Importantly, a list of tuples indexes several complete MultiIndex keys,
whereas a tuple of lists refer to several values within a level:
"""
s = pd.Series([1, 2, 3, 4, 5, 6],
              index=pd.MultiIndex.from_product([["A", "B"], ["c", "d", "e"]]))
s

s.loc[[("A", "c"), ("B", "d")]]  # list of tuples ~= only given combinations of levels

s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists ~= all combinations of levels

#%%
#%%  Using slicers
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#using-slicers

def mklbl(prefix, n):
    return ["%s%s" % (prefix, i) for i in range(n)]

mklbl('A', 4)

#%%
miindex = pd.MultiIndex.from_product([mklbl('A', 4),
                                      mklbl('B', 2),
                                      mklbl('C', 4),
                                      mklbl('D', 2)])
miindex

#%%
micolumns = pd.MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'),
                                       ('b', 'foo'), ('b', 'bah')],
                                      names=['lvl0', 'lvl1'])
micolumns

#%%
dfmi = pd.DataFrame(np.arange(len(miindex) * len(micolumns))
                      .reshape((len(miindex), len(micolumns))),
                    index=miindex, columns=micolumns)
dfmi

#%%
dfmi0 = dfmi.sample(11)
dfmi0
dfmi0.index.levels  # all levels from original df -- not pruned !


dfmi0.loc['A1']
dfmi0.loc['A1'].index
dfmi0.loc['A1'].index.levels


dfmi0.loc[:, 'a']
dfmi0.loc[:, 'a'].columns
dfmi0.loc[:, 'a'].columns.levels    #! AttributeError: 'Index' object has no attribute 'levels'
# because  dfmi0.loc[:, 'a'].columns  is Index  NOT  MultiIndex...    Jizaz!!!!
# and it became Index as using .loc[] for slicing  index's levels  ARE DROPPED !!!

dfmi0.loc['B1']   #! KeyError: 'B1'
dfmi0.loc[('A1', 'B1')]
dfmi0.loc[('A1', 'B1')].index           #!!!  some index's levels are dropped !!!
dfmi0.loc[('A1', 'B1')].index.levels    # but all levels (values) of non-dropped _index's levels_ are present !!!

dfmi0.xs('B1', level=1)
dfmi0.xs('B1', 0, 1)        #  xs(key, axis=0, level=None, drop_level: 'bool_t' = True)
dfmi0.xs('B1', 0, 1, False)      #  xs(key, axis=0, level=None, drop_level: 'bool_t' = True)

dfmi0.xs('B1', 0, 1).index.levels       #!!! as above

#%%
dfmi.sort_index()
dfmi = dfmi.sort_index().sort_index(axis=1)
dfmi

#%%
dfmi.loc[(slice('A1', 'A3')), :]
dfmi.loc[(slice('A1', 'A3'), slice(None)), :]
#!!! slices are inside tuple !!!
dfmi.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :]
dfmi.loc[(slice('A1', 'A3'), slice('B1', 'B1'), ['C1', 'C3']), :]
dfmi.loc[(slice('A1', 'A3'), slice('B1'), ['C1', 'C3']), :]  # slice('B1') doesn't work as expected BUT
dfmi.loc[(slice('A1', 'A3'), slice('B0'), ['C1', 'C3']), :]  # OK, because:

# slics('A1') means the same as slice('A0', 'A1')
# i.e. everything from beginning up to 'A1'
dfmi.loc[(slice('A1')), :]

dfmi.loc[(slice('A1', 'A3'), slice('B0')), :]
dfmi.loc[(slice(None), slice('B0')), :]
dfmi.loc[(slice(None), slice('B1')), :]  # everything
dfmi.loc[(slice(None), slice('B1', 'B1')), :]  # B1 ok
dfmi.loc[(slice(None), ['B1']), :]  # OK

# slicing must be done from the outermost level - cannot ommit one... :(
dfmi.loc[(slice('B0')), :]  # everything
dfmi.loc[(slice('C1')), :]  # everything
dfmi.loc[['C1', 'C3'], :]     #! KeyError: "['C1' 'C3'] not in index"
dfmi.loc[(['C1', 'C3']), :]   #! KeyError: "['C1' 'C3'] not in index"

dfmi.loc[(slice(None), slice(None), ['C1', 'C3']), :]   # OK

dfmi.loc['A1', (slice(None), 'foo')]

#%%  !!!
# You can use pandas.IndexSlice to facilitate a more natural syntax using :,
# rather than using slice(None).

idx = pd.IndexSlice                                         # !!!

dfmi.loc[idx[:, :, ['C1', 'C3']], idx[:, 'foo']]
dfmi.loc[idx[:, :, ['C1', 'C3'], :], idx[:, 'foo']]

#%%
# Using a boolean indexer you can provide selection related to the values.

mask = dfmi[('a', 'foo')] > 200
dfmi.loc[idx[mask], idx[:, 'foo']]
dfmi.loc[idx[mask, :], idx[:, 'foo']]
dfmi.loc[idx[mask, ['C1', 'C3']], idx[:, 'foo']]   # NO! empty - one level ommited
dfmi.loc[idx[mask, :, ['C1', 'C3']], idx[:, 'foo']]   # OK

#%%
# You can also specify the axis argument to .loc to interprete the passed slicers on a single axis.

dfmi.loc(axis=0)[:, :, ['C1', 'C3']]                        #!!!
dfmi.loc[idx[:, :, ['C1', 'C3']], :]
dfmi.loc[(slice(None), slice(None), ['C1', 'C3']), :]

#%%  !!!
#%% Furthermore, you can set the values using the following methods.
df2 = dfmi.copy()
df2.loc(axis=0)[:, :, ['C1', 'C3']] = -10
df2

#%% You can use a right-hand-side of an __alignable__ (?) object as well.
df2 = dfmi.copy()
df2.loc[idx[:, :, ['C1', 'C3']], :] = df2 * 1000            #!!!
df2

#%%
#%% Cross-section
"""
The xs() method of DataFrame additionally takes a level argument to make selecting
data at a particular level of a MultiIndex easier.
"""
df = pd.DataFrame(np.random.randn(8, 3),
                  index = pd.MultiIndex.from_product(
                          [['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
                          names=['first', 'second']
                          ),
                  columns = list('ABC'))
df

#%%
df['one']  #! KeyError
df.loc['one'] #! KeyError
df.loc[(slice(None), 'one')]  #! KeyError
df.loc[(slice(None), 'one'), :]  #! OK
df.loc[idx[:, 'one'], :]         #! OK

# almost! the same with .xs()  Cross Section
df.xs('one', level='second')
#! NOTICE THE DIFF IN the number of displayed columns levels
df.xs('one', level='second').index   # no second level !!!
df.loc[idx[:, 'one'], :].index       # both levels present !!!

#! You can pass drop_level=False to xs to retain the level that was selected.
df.xs('one', level='second', drop_level=False)

#%% on the columns
dft = df.T
dft.xs('one', level='second')           #! Error -- default axis=0
dft.xs('one', level='second', axis=1)
dft.loc[:, idx[:, 'one']]
dft.xs('one', level='second', axis=1, drop_level=False)

#%%
dft
dft.xs(('one', 'bar'), level=('second', 'first'), axis=1)
type(dft.xs(('one', 'bar'), level=('second', 'first'), axis=1))  # DF !!!
# does NOT collapse to Series !!!

dft.loc[:, ('bar', 'one')]    # pd.Series !!!
dft.loc[:, idx['bar', 'one']] # pd.Series !!!

#%%
#%% Advanced reindexing and alignment
#%%
"""
Using the parameter level in the reindex() and align() methods of pandas objects
is useful to broadcast values across a level. For instance:
"""
midx = pd.MultiIndex(levels=[['zero', 'one'], ['x', 'y']],
                     codes=[[1, 1, 0, 0], [1, 0, 1, 0]])
midx

#%%
df = pd.DataFrame(np.random.randn(4, 2), index=midx)
df
df.index
df.columns   # RangeIndex(start=0, stop=2, step=1)       #!!!

df2 = df.mean(level=0)
df2

df.mean(level=1)
df.mean(level=1, axis=1)  #! ValueError: level > 0 or level < -1 only valid with MultiIndex
df.mean(axis=1)   # OK

#%%
df2
df2.index
df.index

df2.reindex()          # nothing changed
df2.reindex(df.index)  # only NaN
df2.reindex(df.index, level=0)    # OK

#%% aligning  ??? very strange!
df_aligned, df2_aligned = df.align(df2, level=0)
df_aligned    # == df
df2_aligned   # == df2.reindex(df.index, level=0)

#%% Swapping levels
df
df.swaplevel(0, 1, axis=0)
df.swaplevel(axis=0)         # ok
df.swaplevel(0, 1, axis=0).loc[['x'], :]
df.swaplevel(axis=0).loc[['x'], :]

#%% Reordering levels
# The reorder_levels() method generalizes the swaplevel method,
# allowing you to permute the hierarchical index levels in one step:
df.reorder_levels([1, 0], axis=0)

#%%
#%% Renaming names of an Index or MultiIndex
"""
The rename() method is used to rename the labels of a MultiIndex,
and is typically used to rename the columns of a DataFrame.
The columns argument of rename allows a dictionary to be specified
that includes only the columns you wish to rename.
"""
df.rename(columns={0: "col0", 1: "col1"})
df.rename(index={"one": "two", "y": "z"})
df.rename_axis(index=['abc', 'def'])
df.rename_axis(columns="Cols")

#%%
# When working with an Index object directly, rather than via a DataFrame,
# Index.set_names() can be used to change the names.

mi = pd.MultiIndex.from_product([[1, 2], ['a', 'b']], names=['x', 'y'])
mi
mi.rename("L0", level=0)
mi.rename(['X', 'Y'])

mi.set_names('Q', level=1)
mi.set_names(['p', 'q'])

#%%
mi.levels[0]
# You cannot set the names of the MultiIndex via a level.
mi.levels[0].name = "name via level"  #! RuntimeError:


#%%
#%% Sorting a MultiIndex
#%%

mdi = pd.MultiIndex.from_product([['bar', 'baz', 'foo', 'qux'], ['one', 'two']])
tuples = mdi.to_numpy()
tuples
np.random.shuffle(tuples)
mdish = pd.MultiIndex.from_tuples(tuples)
mdish
#%%  .sort_index()
s = pd.Series(np.random.randn(8), index=mdish)
s
s.sort_index()
s.sort_index(level=0)
s.sort_index(level=1)

#%% using level name
s.index.set_names(['l0', 'l1'], inplace=True)                 #!!! inplace=True !!!
s
s.sort_index(level='l0')
s.sort_index(level='l1')

#%%
dft
dft.sort_index(level=1, axis=1)

#%% !!! INDEX SHOULD BE SORTED !!!
"""
Indexing will work even if the data are not sorted, but will be rather inefficient
(and show a PerformanceWarning).
It will also return a copy of the data rather than a view:
"""
dfm = pd.DataFrame({'jim': [0, 0, 1, 1],
                    'joe': ['x', 'x', 'z', 'y'],
                    'jolie': np.random.rand(4)})
dfm

dfm = dfm.set_index(['jim', 'joe'])
dfm

dfm.loc[(1, 'z')]  #! PerformanceWarning: indexing past lexsort depth may impact performance.

"""
Furthermore, if you try to index something that is not fully lexsorted, this can raise:
"""
dfm.loc[(0, 'y'):(1, 'z')]  #! UnsortedIndexError: 'Key length (2) was greater than MultiIndex lexsort depth

"""
The is_lexsorted() method on a MultiIndex shows if the index is sorted,
and the lexsort_depth property returns the sort depth:
"""
dfm.index.is_lexsorted()   # False
dfm.index.lexsort_depth    # 1  i.e. only 1 level is sorted  (?)


dfm = dfm.sort_index()     #!!! THIS SHOULD BE ALWAYS DONE !!!   ???
dfm
dfm.index.is_lexsorted()   # True
dfm.index.lexsort_depth    # 2  i.e. both levels are sorted  (?)

dfm
dfm.loc[(0, 'y'):(1, 'z')]

#%%
#%%  Take methods
#%%  https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#take-methods
"""
Similar to NumPy ndarrays, pandas Index, Series, and DataFrame also provides
the take() method that retrieves elements along a given axis at the given indices.
The given indices must be either a list or an ndarray of integer index positions.
take() will also accept negative integers as relative positions to the end of the object.
"""
index = pd.Index(np.random.randint(0, 1e4, 10))
index

pos = [0, 9, 3]
index[pos]              # Index
index.take(pos)         # Index

s = pd.Series(np.random.randn(10))
s
s[pos]
s.take(pos)

#%%
df = pd.DataFrame(np.random.randn(5, 3))
df
df.take([1, 4, 3])
df.iloc[[1, 4, 3], ]

df.take([2, 0], axis=1)
df.iloc[:, [2, 0]]
df.take([2, 0], axis=0)

#%% !!!
"""
take() method on pandas objects are not intended to work on boolean indices
and may return unexpected results.
"""
arr = np.random.randn(10)
arr
arr.take([False, False, True, True])   # turned into 0, 1

ss = pd.Series(np.random.randn(10))
ss.take([False, False, True, True])    # turned into 0, 1
ss.iloc[[0, 1]]

#%%
"""
The take method handles a narrower range of inputs, it can offer performance that
is a good deal faster than fancy indexing.
"""
arr = np.random.randn(int(1e5), 5)
arr
idx = np.arange(int(1e5))
idx

%timeit arr[idx]
# 4.87 ms ± 465 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
%timeit arr.take(idx, axis=0)
# 3.8 ms ± 607 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)



#%%
#%% Index types
"""
Documentation about DatetimeIndex and PeriodIndex are shown
[here](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-overview).
and documentation about TimedeltaIndex is found
[here](https://pandas.pydata.org/pandas-docs/stable/user_guide/timedeltas.html#timedeltas-index)

In the following sub-sections we will highlight some other index types.
"""

#%%
#%% CategoricalIndex

from pandas.api.types import CategoricalDtype

df = pd.DataFrame({'A': np.arange(6), 'B': list('aabbca')})
df

df['B'] = df['B'].astype(CategoricalDtype(list('cab')))  #! 'cab'
df
df.dtypes
df['B'].cat.categories

#%%
df2 = df.set_index('B')
df2.index

df2.loc['a']
df2.loc['b']
df2.loc['d']   # KeyError: 'd'

df2.loc['a'].index   # ... categories=['c', 'a', 'b'] ...
df2.sort_index()     #  c, a, b

df2.groupby(level=0).sum()
df2.groupby(level=0).sum().index   # ... categories=['c', 'a', 'b'] ...

#%% Reindexing

df3 = pd.DataFrame({'A': np.arange(3),
                    'B': pd.Series(list('abc')).astype('category')})
df3 = df3.set_index('B')
df3

df3.reindex(['a', 'e'])
df3.reindex(['a', 'e']).index

df3.reindex(pd.Categorical(['a', 'e'], categories=list('abc')))
df3.reindex(pd.Categorical(['a', 'e'], categories=list('abc'))).index

#%% !!!
pd.Categorical(np.random.choice(list('abc'), 100, replace=True))
# ... Categories (3, object): [a, b, c]
# pd.Categorical sorts cats by default; to give different order:
pd.Categorical(np.random.choice(list('abc'), 100, replace=True),
               categories=list('cab'))   #!!!
# Categories (3, object): [c, a, b]

#%%
"""!!! Warning !!!
Reshaping and Comparison operations on a CategoricalIndex must have the same categories
or a TypeError will be raised.
"""
df4 = pd.DataFrame({'A': np.arange(2), 'B': pd.Categorical(list('ba'))})  #! 'ba'
df4
df4.dtypes

df4 = df4.set_index('B')
df4.index    # ... categories=['a', 'b'] ...    why not 'b', 'a' ???
# see above: pd.Categorical sorts cats by default...

df5 = pd.DataFrame({'A': np.arange(2), 'B': pd.Categorical(list('bc'))})
df5
df5 = df5.set_index('B')

pd.concat([df4, df5]) #! TypeError: categories must match existing categories when appending


#%%
#%% Int64Index and RangeIndex
"""
Int64Index and RangeIndex

Int64Index is a fundamental basic index in pandas.
This is an immutable array implementing an ordered, sliceable set.

RangeIndex is a sub-class of Int64Index that provides the default index for all NDFrame objects.
RangeIndex is an optimized version of Int64Index that can represent
a monotonic ordered set.
These are analogous to Python range types.
"""


#%%
#%% Float64Index
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#float64index
"""
By default a Float64Index will be automatically created when passing floating,
or mixed-integer-floating values in index creation.
This enables a pure label-based slicing paradigm that makes [], ix, loc
for scalar indexing and slicing work exactly the same.
"""
idx = pd.Index([1.5, 2, 3, 4.5, 5])
idx

ss = pd.Series(range(5), index=idx)
ss

#%% Scalar selection for [],.loc will always be label based
ss[3]
ss[3.0]
ss[1]  #! KeyError
ss[1.5]
ss[4]  #! KeyError
ss[4.5]

ss.iloc[1]
ss.iloc[4]

ss[2:4]         # by label
ss.loc[2:4]     # by label
ss.iloc[2:4]    # positional

# In float indexes, slicing using floats is allowed
ss[2.1:4.6]
ss.loc[2.1:4.6]
ss[2.1:4.5]
ss[3:4.5]

#%%  Example
"""
Imagine that you have a somewhat irregular timedelta-like indexing scheme,
but the data is recorded as floats.
This could, for example, be millisecond offsets.
"""
dfir = pd.concat([pd.DataFrame(np.random.randn(5, 2),
                               index=np.arange(5) * 250.0,
                               columns=list('AB')),
                  pd.DataFrame(np.random.randn(6, 2),
                               index=np.arange(4, 10) * 250.1,
                               columns=list('AB'))])
dfir

#%%
dfir[0:1000.4]
dfir.loc[0:1001, 'A']
dfir.loc[1000.4]
dfir[0:1e3]

dfir.iloc[0:5]


#%%
#%% IntervalIndex
#%%
pd.Interval(1, 2)                  # Interval(1, 2, closed='right')
pd.Interval(1, 2, closed='left')   # Interval(1, 2, closed='left')
pd.Interval(1, 2, closed='neither')
pd.Interval(1, 2, closed='both')
1 in pd.Interval(1, 2, closed='both')  # True

pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4])

#%%
"""
The IntervalIndex allows some unique indexing
and is also used as a return type for the categories in cut() and qcut()
"""
df = pd.DataFrame({'A': [1, 2, 3, 4]},
                   index=pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4]))
df

#%%
df[[True, False, False, True]]
df.iloc[[0, 3]]

#%%
"""
Label based indexing via  .loc  along  the edges  of an interval
works as you would expect, selecting that particular interval.
"""
df.loc[2]
df.loc[[2, 3]]
df.loc[1:3]

# If you select a label contained within an interval,
# this will also select the interval.
df.loc[2.5]
df.loc[7/3]
df.loc[np.array([3, 4, 5])/2]

# Selecting using an Interval will only return exact matches
# (starting from pandas 0.25.0).

df.loc[pd.Interval(1, 2)]
df.loc[pd.Interval(.5, 1.5)]  # KeyError: Interval(0.5, 1.5, closed='right')

# Selecting all Intervals that overlap a given Interval can be performed
#using the overlaps() method to create a boolean indexer.

idxr = df.index.overlaps(pd.Interval(.5, 2.5))
idxr
df[idxr]

#%%
#%% Binning data with  cut()  and  qcut()
#%%
"""
cut() and qcut() both return a Categorical object, and the bins they create
are stored as an IntervalIndex in its .categories attribute.
"""
c = pd.cut(range(4), bins=2)
c
c.categories   # IntervalIndex(...)

"""
cut() also accepts an IntervalIndex for its bins argument,
which enables a useful pandas idiom.
First, We call cut() with some data and bins set to a fixed number,
to generate the bins.
Then, we pass the values of .categories as the bins argument in subsequent
calls to cut(), supplying new data which will be binned into the same bins.
"""
pd.cut([0, 3, 5, 1], bins=c.categories)

c = pd.qcut(np.random.randn(100), 10)   # quantiles
c
c.categories
c.value_counts()

pd.cut(np.random.randn(100), bins=c.categories).value_counts()

#%%
#%% Generating ranges of intervals
"""
If we need intervals on a regular frequency, we can use the interval_range() function
to create an IntervalIndex using various combinations of start, end, and periods.
The default frequency for interval_range is a 1 for numeric intervals,
and calendar day for datetime-like intervals:
"""

pd.interval_range(start=0, end=5)
pd.interval_range(start=pd.Timestamp('2020-05-04'), periods=4)
pd.interval_range(end=pd.Timedelta('3 days'), periods=3)

"""
Specifying start, end, and periods will generate a range of evenly spaced intervals
from start to end inclusively,
with periods number of elements in the resulting IntervalIndex:
"""
pd.interval_range(start=0, end=6, periods=4)
pd.interval_range(pd.Timestamp('2018-01-01'),
                  pd.Timestamp('2018-02-28'), periods=3)

"""
Additionally, the closed parameter can be used to specify which side(s)
the intervals are closed on.
Intervals are closed on the right side by default.
"""
pd.interval_range(start=0, end=4, closed='both')
pd.interval_range(start=0, end=4, closed='neither')

"""
The freq parameter can used to specify non-default frequencies,
and can utilize a variety of frequency aliases with datetime-like intervals:
"""
pd.interval_range(start=0, periods=5, freq=1.5)
pd.interval_range(start=pd.Timestamp('2020-05-04'), periods=4, freq='W')
pd.interval_range(start=pd.Timedelta('0 days'), periods=3, freq='9H')

#%%



#%%
#%% Miscellaneous indexing FAQ
#%% https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#miscellaneous-indexing-faq



#%%
