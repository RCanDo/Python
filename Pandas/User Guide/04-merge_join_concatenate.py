# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Merge, join, and concatenate
subtitle:
version: 1.0
type: tutorial
keywords: [merge, join, concatenate, NumPy, Pandas]
description: |
remarks:
todo:
sources:
    - title: Pandas 0.25.3 User Guide
      chapter: Merge, join, and concatenate
      link: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "04-merge_join_concatenate.py"
    path: "D:/ROBOCZY/Python/Pandas/User Guide/"
    date: 2019-11-16
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
#%%
from rcando.ak.builtin import flatten, paste
from rcando.ak.nppd import data_frame
import os, json

ROOTS = json.load(open('roots.json'))
WD = os.path.join(ROOTS['Works'], "Python/Pandas/User Guide/")
os.chdir(WD)

print(os.getcwd())

#%%
import numpy as np
import pandas as pd

#%% Concatenating objects
#%%
"""
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])
"""

abcd = list('ABCD')
df1 = data_frame(abcd, list(range(4)))
df1
df2 = data_frame(abcd, list(range(4, 8)))
df2
df3 = data_frame(abcd, list(range(8, 12)))
df3

dfx = data_frame(abcd, list(range(4)), columns=list('WXYZ'))
dfx

#%%

frames = [df1, df2, df3]

result = pd.concat(frames)
result

pd.concat(frames, axis=1)

#%%%

pd.concat(objs, axis=0, join='outer', ignore_index=False, keys=None,
          levels=None, names=None, verify_integrity=False, copy=True)
"""
objs : a sequence or mapping of Series or DataFrame objects.
    If a dict is passed, the sorted keys will be used as the keys argument,
    unless it is passed, in which case the values will be selected (see below).
    Any None objects will be dropped silently unless they are all None
    in which case a ValueError will be raised.
axis : {0, 1, …}, default 0. The axis to concatenate along.
join : {‘inner’, ‘outer’}, default ‘outer’. How to handle indexes on other axis(es).
    Outer for union and inner for intersection.
ignore_index : boolean, default False. If True, do not use the index values
    on the concatenation axis. The resulting axis will be labeled 0, …, n - 1.
    This is useful if you are concatenating objects where the concatenation axis
    does not have meaningful indexing information.
    Note the index values on the other axes are still respected in the join.
keys : sequence, default None. Construct hierarchical index using the passed keys
    as the outermost level. If multiple levels passed, should contain tuples.
levels : list of sequences, default None.
    Specific levels (unique values) to use for constructing a MultiIndex.
    Otherwise they will be inferred from the keys.
names : list, default None. Names for the levels in the resulting hierarchical index.
verify_integrity : boolean, default False. Check whether the new concatenated axis
    contains duplicates. This can be very expensive relative to the actual data concatenation.
copy : boolean, default True. If False, do not copy data unnecessarily.

Without a little bit of context many of these arguments don’t make much sense.
Let’s revisit the above example.
"""

#%%
"""
Suppose we wanted to associate specific keys with each of the pieces of the chopped up DataFrame.
We can do this using the keys argument:
"""

result = pd.concat(frames, keys=list('xyz'))
result
result.loc['y']

#%%
df4 = data_frame(list('BDF'), [2, 3, 6, 7])
df4.index = [1,2,3,4]
df4
pd.concat([df1, df4])
pd.concat([df1, df4], axis=0)
pd.concat([df1, df4], axis=0, join='inner')
pd.concat([df1, df4], axis=1)
pd.concat([df1, df4], 1)
pd.concat([df1, df4], 1, 'inner')
pd.concat([df1, df4], 1, 'left') #! ValueError: Only can inner (intersect) or outer (union) join the other axis
pd.concat([df1, df4], axis=1, join='inner')
pd.concat([df1, df4], axis=1, sort=False)       ## default in future versions
pd.concat([df1, df4], axis=1, sort=True)

#%% !!! .reindex(), .reindex_like()  vs  df.indx = new_index_labels

df4.reindex(df1.index)   #!!!
#!!! do not confuse .reindex() / .reindex_like()  with  df.index = new_index_labels
# this is NOT replacing labels of index but aligning to the given one; thus NaNs appear!
df4  # not changed
df4.reindex([0, 1, 4, 5])
df4.reindex_like(df1)   # works on both index and columns !

pd.concat([df1, df4.reindex(df1.index)], axis=1)   # kind of a "left join"
pd.concat([df1, df4], axis=1).reindex(df1.index)   # "

# renaming
df4.index = df1.index
df4 # all vaues retained -- ony labels of index changed!
# now
pd.concat([df1, df4], 1)

#%% .append() == .concat(., axis=0)
df1.append(df2)

# In the case of DataFrame, the indexes must be disjoint
# but the columns do not need to be:
df1.append(df4, sort=False)

#%%
df1.append([df2, df3])
df1.append([df2, df3, df4])

#%% Ignoring indexes on the concatenation axis
# i.e. new index after concatenation

pd.concat([df1, df4], ignore_index=False)  # default
pd.concat([df1, df4], ignore_index=True)
pd.concat([df1, df4], ignore_index=True, sort=False)

df1.append(df4, ignore_index=True, sort=False)

#%% Concatenating with mixed ndims
# You can concatenate a mix of Series and DataFrame objects.
# The Series will be transformed to DataFrame with the column name
# as the name of the Series.
s1 = pd.Series(['X0', 'X1', 'X2', 'X3'], name='X')
s1
pd.concat([df1, s1])
pd.concat([df1, s1], axis=1)
df1.assign(X=s1)
df1.assign(X=s1, X2=s1)
df1
pd.concat([df1, s1, s1], axis=1)

# If unnamed Series are passed they will be numbered consecutively.
s2 = pd.Series(['_0', '_1', '_2', '_3'])
pd.concat([df1, s1, s2, s1, s2, s2], axis=1)

# Passing ignore_index=True will drop all name references.
pd.concat([df1, s1], axis=1, ignore_index=True)

#%% More concatenating with group keys¶

s3 = pd.Series([0, 1, 2, 3], name='foo')
s4 = pd.Series([0, 1, 2, 3])
s5 = pd.Series([0, 1, 4, 5])
pd.concat([s3, s4, s5], axis=1)

pd.concat([s3, s4, s5], axis=1, keys=['red', 'blue', 'yellow'])

#%%
pd.concat(frames, keys=['x', 'y', 'z'])

pieces = {'x': df1, 'y': df2, 'z': df3}
pieces
result = pd.concat(pieces, keys=['z', 'y'])
result
# The MultiIndex created has levels that are constructed from the passed keys
# and the index of the DataFrame pieces:
result.index
result.index.levels

#%%
"""
If you wish to specify other levels (as will occasionally be the case),
you can do so using the levels argument:
"""
result = pd.concat(pieces, keys=['x', 'y', 'z'],
                   levels=[['z', 'y', 'x', 'w']],
                   names=['group_key'])
result
result.index.levels
"""
This is fairly esoteric, but it is actually necessary for implementing things
like GroupBy where the order of a categorical variable is meaningful.
"""

#%% Appending rows to a DataFrame

s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])
df1.append(s2, ignore_index=True)
df1.append(s2)  #! TypeError: Can only append a Series if ignore_index=True or if the Series has a name

pd.concat([df1, s2], axis=0)  # no
pd.concat([df1, s2], axis=0, ignore_index=True)  # no

s3 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'X', 'Y'])
df1.append(s3, ignore_index=True)

#%% You can also pass a list of dicts or Series:

dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4},
         {'A': 5, 'B': 6, 'C': 7, 'Y': 8}]

df1.append(dicts, ignore_index=True, sort=False)
df1.append(dicts, ignore_index=True)

#%% Database-style DataFrame or named Series joining/merging
#%%

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
"""
left: A DataFrame or named Series object.

right: Another DataFrame or named Series object.

how: One of 'left', 'right', 'outer', 'inner'.
    Defaults to inner. See below for more detailed description of each method.

on: Column or index level names to join on.
    Must be found in both the left and right DataFrame and/or Series objects.
    If not passed and left_index and right_index are False,
    the intersection of the columns in the DataFrames and/or Series
    will be inferred to be the _join keys_.

left_on: Columns or index levels from the left DataFrame or Series to use as keys.
    Can either be column names, index level names, or arrays with length
    equal to the length of the DataFrame or Series.

right_on: Columns or index levels from the right DataFrame or Series to use as keys.
    Can either be column names, index level names, or arrays with length
    equal to the length of the DataFrame or Series.

left_index: If True, use the index (row labels) from the left DataFrame or Series
    as its join key(s).
    In the case of a DataFrame or Series with a MultiIndex (hierarchical),
    the number of levels must match the number of join keys from the right
    DataFrame or Series.

right_index: Same usage as left_index for the right DataFrame or Series

sort: Sort the result DataFrame by the join keys in lexicographical order.
    Defaults to True, setting to False will improve performance substantially
    in many cases.

suffixes: A tuple of string suffixes to apply to overlapping columns.
    Defaults to ('_x', '_y').

copy: Always copy data (default True) from the passed DataFrame or named Series objects,
    even when reindexing is not necessary.
    Cannot be avoided in many cases but may improve performance / memory usage.
    The cases where copying can be avoided are somewhat pathological
    but this option is provided nonetheless.

indicator: Add a column to the output DataFrame called `_merge`
    with information on the source of each row.
    `_merge` is Categorical-type and takes on a value of 'left_only'
    for observations whose merge key only appears in 'left' DataFrame or Series,
    'right_only' for observations whose merge key only appears in 'right'
    DataFrame or Series, and 'both' if the observation’s merge key is found in both.

validate : string, default None. If specified, checks if merge is of specified type.

        “one_to_one” or “1:1”: checks if merge keys are unique in both
            left and right datasets.
        “one_to_many” or “1:m”: checks if merge keys are unique in left dataset.
        “many_to_one” or “m:1”: checks if merge keys are unique in right dataset.
        “many_to_many” or “m:m”: allowed, but does not result in checks.
"""

#%%

dfl = data_frame(list('KAB'), range(4), columns=['key', 'A', 'B'])
dfl

dfr = data_frame(list('KCD'), range(4), columns=['key', 'C', 'D'])
dfr

pd.merge(dfl, dfr, on='key')

#%%
dfl2 = pd.concat([dfl,
                  pd.Series(paste('K', list('0012')), name='key1'),
                  pd.Series(paste('K', list('0101')), name='key2')],
                 axis=1)
dfr2 = pd.concat([dfr,
                  pd.Series(paste('K', list('0112')), name='key1'),
                  pd.Series(paste('K', list('0000')), name='key2')],
                 axis=1)
dfl2
dfr2

#%%
pd.merge(dfl2, dfr2, on=['key', 'key2'])
pd.merge(dfl2, dfr2, on=['key1', 'key2'])

#%%
"""
 Merge method 	SQL Join Name 	    Description
 left 	        LEFT OUTER JOIN 	Use keys from left frame only
 right 	        RIGHT OUTER JOIN 	Use keys from right frame only
 outer 	        FULL OUTER JOIN 	Use union of keys from both frames
 inner      	INNER JOIN 	        Use intersection of keys from both frames (default)
"""

pd.merge(dfl2, dfr2, on=['key1', 'key2'], how='left')
pd.merge(dfl2, dfr2, on=['key1', 'key2'], how='right')
pd.merge(dfl2, dfr2, on=['key1', 'key2'], how='inner')
pd.merge(dfl2, dfr2, on=['key1', 'key2'], how='outer')

#%% duplicate keys
left  = pd.DataFrame({'A': [1, 2], 'B': [2, 2]})
right = pd.DataFrame({'A': [4, 5, 6], 'B': [2, 2, 2]})
left
right
pd.merge(left, right, on='B', how='outer')

#%% validate="..." -- Checking for duplicate keys
left  = pd.DataFrame({'A': [1, 2], 'B': [1, 2]})
right = pd.DataFrame({'A': [4, 5, 6], 'B': [2, 2, 2]})
left
right
pd.merge(left, right, on='B', how='outer')

pd.merge(left, right, on='B', how='outer', validate="one_to_one")
#! MergeError: Merge keys are not unique in right dataset; not a one-to-one merge
pd.merge(left, right, on='B', how='outer', validate="1:1")

pd.merge(left, right, on='B', how='outer', validate="one_to_many")
pd.merge(left, right, on='B', how='outer', validate="1:m")
# OK

pd.merge(left, right, on='B', how='outer', validate="m:1")
#! MergeError: Merge keys are not unique in right dataset; not a many-to-one merge

#%% The merge indicator
"""
merge() accepts the argument `indicator`.
If True, a Categorical-type column called '_merge' will be added to the output object
that takes on values:
Observation Origin 	                _merge value
Merge key only in 'left' frame 	    left_only
Merge key only in 'right' frame 	right_only
Merge key in both frames 	        both
"""

df1 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
df1
df2
pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')


#%% Merge dtypes
#%%
...

#%% Merging will preserve category dtypes of the mergands.
# See also the section on categoricals.

from pandas.api.types import CategoricalDtype
X = pd.Series(np.random.choice(['foo', 'bar'], size=(10,)))
X = X.astype(CategoricalDtype(categories=['foo', 'bar']))
Y = np.random.choice(['one', 'two', 'three'], size=(10,))

dfl = pd.DataFrame({'X': X, 'Y': Y})
dfl
dfl.dtypes

dfr = pd.DataFrame( {
          'X': pd.Series(['foo', 'bar'], dtype=CategoricalDtype(['foo', 'bar'])),
          'Z': [1, 2] } )
dfr
dfr.dtypes

result = pd.merge(dfl, dfr, how='outer')
result
result.dtypes

"""
Note
The category dtypes must be exactly the same,
meaning the same categories and the ordered attribute.
Otherwise the result will coerce to object dtype.

Note
Merging on category dtypes that are the same can be quite performant
compared to object dtype merging.
"""

#%% Joining on index
#%%
dfl = data_frame(list('AB'), list('012'))
dfl.index = paste('K', list('012'))
dfr = data_frame(list('CD'), list('023'))
dfr.index = paste('K', list('023'))
dfl
dfr

dfl.join(dfr)  # .join() == merge( on=index )
dfl.join(dfr, how='outer')
dfl.join(dfr, how='inner')

# the same result via merge()
pd.merge(dfl, dfr, left_index=True, right_index=True)
pd.merge(dfl, dfr, left_index=True, right_index=True, how='inner')
pd.merge(dfl, dfr, left_index=True, right_index=True, how='outer')
pd.merge(dfl, dfr, left_index=True, right_index=True, how='left')
pd.merge(dfl, dfr, left_index=True, right_index=True, how='right')

#%% Joining key columns on an index
"""
join() takes an optional on argument which may be a column or multiple column names,
which specifies that the passed DataFrame is to be aligned on that column in the DataFrame.
These two function calls are completely equivalent:

left.join(right, on=key_or_keys)
pd.merge(left, right, left_on=key_or_keys, right_index=True,
      how='left', sort=False)

Obviously you can choose whichever form you find more convenient.
For many-to-one joins (where one of the DataFrame’s is already indexed by the join key),
using join may be more convenient.
"""

dfl = data_frame(list('AB'), range(4))
dfl['key'] = ['K0', 'K1']*2
dfl

dfr = data_frame(list('CD'), [0, 1])
dfr.index = ['K0', 'K1']
dfr

dfl.join(dfr, on='key')
pd.merge(dfl, dfr, left_on='key', right_index=True, how='left', sort=False)

#%% To join on multiple keys, the passed DataFrame must have a MultiIndex:

dfl = data_frame(list('AB'), range(4))
dfk = pd.DataFrame({'key1': paste('K', list('0012')),
                    'key2': paste('K', list('0101'))})
dfl = dfl.join(dfk)
dfl

midx = pd.MultiIndex.from_arrays([paste('K', list('0122')),
                                  paste('K', list('0001'))])
midx
dfr = data_frame(list('CD'), range(4))
dfr.index = midx
dfr

dfl.join(dfr, on=['key1', 'key2'])
dfl.join(dfr, on=['key1', 'key2'], how='inner')

#%% Joining a single Index to a MultiIndex
"""
You can join a singly-indexed DataFrame with a level of a MultiIndexed DataFrame.
The level will match on the name of the index of the singly-indexed frame
against a level name of the MultiIndexed frame.
"""
dfl = data_frame(list('AB'), range(3))
dfl.index = pd.Index(paste('K', range(3)), name='key')

dfr = data_frame(list('CD'), range(4))
dfr.index = pd.MultiIndex.from_arrays([paste('K', list('0122')),
                                       paste('Y', list('0123'))],
                                      names=['key', 'Y'])
dfl
dfr
dfl.join(dfr, how='inner')

# This is equivalent but less verbose and more memory efficient / faster than this:
pd.merge(dfl.reset_index(), dfr.reset_index(), on=['key'], how='inner') \
    .set_index(['key', 'Y'])

#%% Joining with two MultiIndexes
"""
This is supported in a limited way, provided that the index for the right argument
is completely used in the join, and is a subset of the indices in the left argument,
as in this example:
"""

midxl = pd.MultiIndex.from_product([list('abc'), list('xy'), [1, 2]],
                                  names=['abc', 'xy', 'num'])
dfl = pd.DataFrame({'v1': range(12)}, index=midxl)

midxr = pd.MultiIndex.from_product([list('abc'), list('xy')],
                                  names=['abc', 'xy'])
dfr = pd.DataFrame({'v2': np.arange(1, 7)*100}, index=midxr)

print(dfl)
print(dfr)

#%%
dfl.join(dfr)
dfl.join(dfr, on=['abc'])  #! ValueError: len(left_on) must equal the number of levels in the index of "right"
dfl.join(dfr, on=['abc', 'xy'])   # OK

#%% If that condition is not satisfied, a join with two multi-indexes can be done
# using the following code:

dfl = data_frame(list('AB'), range(3))
dfl.index = pd.MultiIndex.from_arrays([paste('K', list('001')),
                                       paste('X', list('012'))],
                                      names=['key', 'X'])
print(dfl)

dfr = data_frame(list('CD'), range(4))
dfr.index = pd.MultiIndex.from_arrays([paste('K', list('0122')),
                                       paste('Y', list('0123'))],
                                      names=['key', 'Y'])
print(dfr)

#%%
pd.merge(dfl.reset_index(), dfr.reset_index(), on='key', how='inner') \
    .set_index(['key', 'X', 'Y'])

pd.merge(dfl.reset_index(), dfr.reset_index(), on='key', how='outer') \
    .set_index(['key', 'X', 'Y'])

#%% Merging on a combination of columns and index levels
"""
Strings passed as the on, left_on, and right_on parameters may refer to either
column names or index level names.
This enables merging DataFrame instances on a combination of index levels and columns
without resetting indexes.
"""
dfl = data_frame(list('AB'), range(4))
dfl.index = pd.Index(paste('K', list('0012')), name='key1')
dfl['key2'] = paste('K', list('0101'))
print(dfl)

dfr = data_frame(list('CD'), range(4))
dfr.index = pd.Index(paste('K', list('0122')), name='key1')
dfr['key2'] = paste('K', list('0001'))
print(dfr)

dfl.merge(dfr, on=['key1', 'key2'])
pd.merge(dfl, dfr, on=['key1', 'key2'])

"""
Note
When DataFrames are merged on a string that matches an index level in both frames,
the index level is preserved as an index level in the resulting DataFrame.

Note
When DataFrames are merged using only some of the levels of a MultiIndex,
the extra levels will be dropped from the resulting merge.
In order to preserve those levels, use .reset_index() on those level names
to move those levels to columns prior to doing the merge.

Note
If a string matches both a column name and an index level name,
then a warning is issued and the __column takes precedence__.
This will result in an ambiguity error in a future version.
"""

#%% Overlapping value columns
"""
The merge suffixes argument takes a tuple of list of strings to append
to overlapping column names in the input DataFrames
to disambiguate the result columns:
"""
dfl = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'v': [1, 2, 3]})
dfr = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'v': [4, 5, 6]})
pd.merge(dfl, dfr, on='k')
pd.merge(dfl, dfr, on='k', suffixes=['_l', '_r'])

#%% DataFrame.join() has lsuffix and rsuffix arguments which behave similarly.
dfl = dfl.set_index('k')
dfr = dfr.set_index('k')
print(dfl)
print(dfr)
dfl.join(dfr, lsuffix='_l', rsuffix='_r')

#%% Joining multiple DataFrames
# A list or tuple of DataFrames can also be passed to join() to join them together on their indexes.
dfr2 = pd.DataFrame({'v': [7, 8, 9]}, index=['K1', 'K1', 'K2'])
print(dfr2)
dfl.join([dfr, dfr2])

#%%
dfr3 = pd.DataFrame({'v': [-7, -8, -9]}, index=['K0', 'K2', 'K2'])
print(dfr3)
dfl.join([dfr, dfr2, dfr3])
# suffixes BAD !!!


#%% Merging together values within Series or DataFrame columns
#%%
"""
Another fairly common situation is to have two like-indexed (or similarly indexed) Series or DataFrame
objects and wanting to __“patch” values__ in one object
from values for matching indices in the other.
Here is an example:
"""
df1 = pd.DataFrame([[np.nan, 3., 5.], [-4.6, np.nan, np.nan],
                    [np.nan, 7., np.nan]])

df2 = pd.DataFrame([[-42.6, np.nan, -8.2], [-5., 1.6, 4]],
                   index=[1, 2])
print(df1)
print(df2)

df1.combine_first(df2)

#! do not confuse with
df1.update(df2)   # alters __non-NA__ values in place!
df1

#%% Timeseries friendly merging
#%%

#%% Merging ordered data
"""
A merge_ordered() function allows combining time series and other ordered data.
In particular it has an optional `fill_method` keyword to fill/interpolate missing data:
"""
dfl = pd.DataFrame({'k': ['K0', 'K1', 'K1', 'K2'],
                    'lv': [1, 2, 3, 4],
                    's': ['a', 'b', 'c', 'd']})
dfr = pd.DataFrame({'k': ['K1', 'K2', 'K4'],
                    'rv': [1, 2, 3]})
print(dfl)
print(dfr)

pd.merge_ordered(dfl, dfr, fill_method='ffill', left_by='s')

# ??? not very clear what's going on...

#%% Merging asof
"""
A merge_asof() is similar to an ordered left-join except that we match
on nearest key rather than equal keys.
For each row in the left DataFrame, we select the last row in the right DataFrame
whose on key is less than the left’s key.
Both DataFrames must be sorted by the key.

Optionally an asof merge can perform a group-wise merge.
This matches the by key equally, in addition to the nearest match on the on key.

For example; we might have trades and quotes and we want to asof merge them.
"""

trades = pd.DataFrame({
    'time': pd.to_datetime(['20160525 13:30:00.023',
                            '20160525 13:30:00.038',
                            '20160525 13:30:00.048',
                            '20160525 13:30:00.048',
                            '20160525 13:30:00.048']),
    'ticker': ['MSFT', 'MSFT', 'GOOG', 'GOOG', 'AAPL'],
    'price': [51.95, 51.95, 720.77, 720.92, 98.00],
    'quantity': [75, 155, 100, 100, 100]},
     columns=['time', 'ticker', 'price', 'quantity'])


quotes = pd.DataFrame({
    'time': pd.to_datetime(['20160525 13:30:00.023',
                            '20160525 13:30:00.023',
                            '20160525 13:30:00.030',
                            '20160525 13:30:00.041',
                            '20160525 13:30:00.048',
                            '20160525 13:30:00.049',
                            '20160525 13:30:00.072',
                            '20160525 13:30:00.075']),
    'ticker': ['GOOG', 'MSFT', 'MSFT', 'MSFT', 'GOOG', 'AAPL', 'GOOG', 'MSFT'],
    'bid': [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
    'ask': [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03]},
    columns=['time', 'ticker', 'bid', 'ask'])

#%%
trades
quotes

pd.merge_asof(trades, quotes, on='time', tolerance=pd.Timedelta('2ms'))

# By default we are taking the asof of the quotes.
pd.merge_asof(trades, quotes, on='time', by='ticker')

# We only asof within 2ms between the quote time and the trade time.
pd.merge_asof(trades, quotes, on='time', by='ticker', tolerance=pd.Timedelta('2ms'))

#%%
"""
We only asof within 10ms between the quote time and the trade time
and we exclude exact matches on time.
Note that though we exclude the exact matches (of the quotes),
prior quotes do propagate to that point in time.
"""

pd.merge_asof(trades, quotes, on='time', by='ticker',
              tolerance=pd.Timedelta('10ms'),
              allow_exact_matches=False)

pd.merge_asof(trades, quotes, on='time', by='ticker',
              tolerance=pd.Timedelta('10ms'))
