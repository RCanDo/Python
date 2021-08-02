#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Reshaping And Pivot Tables
subtitle:
version: 1.0
type: tutorial
keywords: [cut, get_dummies, melt, factorize, crosstab, stack, pivot_table, NumPy, Pandas]
description: |
remarks:
todo:
sources:
    - title: Pandas 0.25.3 User Guide
      chapter: Reshaping And Pivot Tables
      link: https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "05-reshaping_and_pivot_tables.py"
    path: "D:/ROBOCZY/Python/Pandas/User Guide/"
    date: 2019-11-13
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

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.max_seq_items', None)

#%% Examples   https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html#examples
#%%
"""
In this section, we will review frequently asked questions and examples.

The Guide is below.

The column names and relevant column values are named to correspond with
how this DataFrame will be pivoted in the answers below.
"""

#%%
np.random.seed([3, 1415])
n=20
cols = np.array(['key', 'row', 'item', 'col'])

df = cols + pd.DataFrame( (np.random.randint(5, size=(n, 4))
                          // [2, 1, 2, 1]).astype(str) )
df.columns = cols
df

df = df.join(pd.DataFrame(np.random.randn(n, 2).round(2)).add_prefix("val"))
df

#%% Pivoting with single aggregations
"""
Suppose we wanted to pivot df such that the col values are columns,
row values are the index, and the mean of val0 are the values?
"""

pd.pivot_table(df, values='val0', columns='col', index='row', aggfunc='mean')

pd.pivot_table(df, values='val0', columns='col', index='row',
               aggfunc=sum, fill_value=0)


print(pd.pivot_table(df, values='val0', columns='col', index='row',
               aggfunc=sum).to_string(na_rep="."))

pd.pivot_table(df, values='val0', columns='col', index='row',
               aggfunc="size", fill_value=0)

pd.pivot_table(df, values='val0', columns='col', index='row',
               aggfunc=len, fill_value=0)

pd.pivot_table(df, values='val0', columns='col', index='row',
               aggfunc=[sum, len], fill_value=0)

pd.pivot_table(df, values='val0', columns='col', index='row',
               aggfunc=[sum, len, "mean"], fill_value=0)

pd.pivot_table(df, values=['val0', 'val1'], columns='col', index='row',
               aggfunc=sum, fill_value=0)

pd.pivot_table(df, values=['val0', 'val1'], columns='col', index='row',
               aggfunc=sum, fill_value=0, margins=True)

pd.pivot_table(df, values=['val0', 'val1'], columns='col', index='row',
               aggfunc=[sum, len], fill_value=0)


pd.pivot_table(df, values='val0', columns=['col', 'item'], index='row',
               aggfunc=sum, fill_value=0)

pd.pivot_table(df, values='val0', columns=['col', 'item'], index='row',
               aggfunc=sum, fill_value=0, margins=True)


#%% Exploding a list-like column

keys = ['panda1', 'panda2', 'panda3']
values = [['eats', 'shoots'], ['shoots', 'leaves'], ['eats', 'leaves']]
df = pd.DataFrame({'keys': keys, 'values': values})
df

#%%
df['values'].explode()  # -> Series
df.explode('values')

#%%
s = pd.Series([[1, 2, 3], 'foo', [], ['a', 'b']])
s
s.explode()

#%%
df = pd.DataFrame([{'var1': 'a,b,c', 'var2': 1},
                   {'var1': 'd,e,f', 'var2': 2}])
df

df.var1.str.split(',')

df = df.assign(var1=df.var1.str.split(','))
df
df.explode('var1')

#%%
#%% GUIDE

#%% Reshaping by pivoting DataFrame objects
#%%
import pandas.util.testing as tm

tm.N = 3

df = tm.makeTimeDataFrame()
N, K = df.shape

df
df.shape
df.to_numpy()
df.to_numpy().ravel()
df.to_numpy().ravel('F')  # order='C' - row-wise - last index changing fastest - C-style
                          #       'F' - column-wise - first index changing fastest - Fortran style
help(np.ravel)

np.asarray(df.columns)
np.asarray(df.columns).repeat(N)
np.tile(np.asarray(df.index), K)

#%%
def unpivot(df):
    N, K = df.shape
    data = {'value': df.to_numpy().ravel('F'),
            'variable': np.asarray(df.columns).repeat(N),
            'date': np.tile(np.asarray(df.index), K)}
    return pd.DataFrame(data, columns=['date', 'variable', 'value'])

# what the pandas' function ???

#%%
df0 = tm.makeTimeDataFrame()
df0

df = unpivot(df0)
df

# NOTICE THE DIFFERENCE !!! (melt() and stack() described below)
df0.melt()
df0.melt().index
df0.stack()
df0.stack().index   # MultiIndex !

#%%
df[df['variable'] == 'A']

#%%
df.pivot(index='date', columns='variable', values='value')
pd.pivot(df, index='date', columns='variable', values='value')

# `values` are all other columns
df.pivot(index='date', columns='variable')  # Ok

#%%

dfx = df
dfx['X1'] = dfx['value'] * 2
dfx
# `values` are all other columns
dfx_piv = dfx.pivot(index='date', columns='variable')
dfx_piv
dfx_piv.columns   # MultiIndex

dfx_piv['X1']

dfx.pivot(index='date', columns='variable', values=['value', 'X1'])

#%%
# but default `index` is row_number
df.pivot(columns='variable', values='value')  # strange...

# while `columns` has no default
df.pivot(index='date', values='value')        #!  KeyError: None

# hence DO NOT RELY ON DEFAULTS !!!

#%% BUT you cannot indicate more columns nor sth like multiIndex:
dfx.pivot(index='date', columns=['variable'], values=['value', 'X1'])
# KeyError: 'Level variable not found'
dfx.pivot(index=['date'], columns='variable', values=['value', 'X1'])
# ValueError: ...

#%% try sth like multiIndex
df
df2 = df
df2['time'] = np.random.randint(10, 13, 120)
df2

df2.pivot(index='date', columns='variable')  # Ok
df2.pivot(index='date', columns='variable', values='value')  # Ok

# multiIndex
df2.pivot(index=['date', 'time'], columns='variable')  #! ValueError: Length mismatch: Expected ...
# PITY!!!

"""
Use pd.pivot_table() !!! which is more flexible
"""


#%%
#%% stack - unstack
# uses 'multiindex'

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
tuples

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df

stacked = df.stack()
stacked

df.stack(level=0)
df.stack(level=1)  # IndexError: Too many levels: Index has only 1 level, not 2

#%%

stacked
stacked.unstack()
stacked.unstack(1)
stacked.unstack(0)
stacked.unstack('second')
stacked.unstack('first')

#%% stack and unstack methods implicitly sort the index levels involved

index = pd.MultiIndex.from_product([[2, 1], ['a', 'b']])
index
df = pd.DataFrame(np.random.randn(4), index=index, columns=['A'])
df
df.sort_index()
df.unstack()
df.unstack().stack()
all(df.unstack().stack() == df.sort_index())

#%% Multiple levels

columns = pd.MultiIndex.from_tuples([
            ('A', 'cat', 'long'), ('B', 'cat', 'long'),
            ('A', 'dog', 'short'), ('B', 'dog', 'short')],
            names=['exp', 'animal', 'hair_length']
          )
columns

#%%

df = pd.DataFrame(np.random.randn(4, 4), columns=columns)
df

df.index
df.columns

df.stack()
df.stack(0)
df.stack(1)
df.stack(2)
df.stack([0,2])
df.stack(['exp', 'hair_length'])

#%%

columns = pd.MultiIndex.from_tuples([('A', 'cat'), ('B', 'dog'),
                                     ('B', 'cat'), ('A', 'dog')],
                                    names=['exp', 'animal'],
                                    )
columns

index = pd.MultiIndex.from_product([('bar', 'baz', 'foo', 'qux'),
                                    ('one', 'two')],
                                    names=['first', 'second'])
index

df = pd.DataFrame(np.random.randn(8, 4), index=index, columns=columns)
df

df.sort_index()
df.sort_index(axis=1)

#%%

df.stack('exp')

df2 = df.iloc[[0, 1, 2, 4, 5, 7]]
df2

df2.stack()
df2.stack(0)
df2.stack(1)

#%%

df3 = df.iloc[[0, 1, 4, 7], [1, 2]]
df3

df3.unstack()
df3.unstack(0)

df3.unstack(fill_value=0)

#%%
#%% melt

cheese = pd.DataFrame({'first': ['John', 'Mary'],
                       'last': ['Doe', 'Bo'],
                       'height': [5.5, 6.0],
                       'weight': [130, 150]})
cheese

cheese.melt()
cheese.melt(id_vars=['first', 'last'])
cheese.melt(id_vars=['first', 'last'], var_name='quantity')

#%%

dfc = cheese.melt(id_vars=['first', 'last'], var_name='quantity')
dfc
dfc.columns
dfc.pivot(index='first', columns='quantity', values='value')
dfc.pivot(index='first', columns='quantity')

#%% BUT
dfc.pivot(index='first', columns=['quantity'], values='value') #! KeyError: 'Level quantity not found'
dfc.pivot(index='first', columns=['last', 'quantity'], values=['value']) #! ...

#%% pd.wide_to_long()
#%%

dft = pd.DataFrame({"A1970": {0: "a", 1: "b", 2: "c"},
                    "A1980": {0: "d", 1: "e", 2: "f"},
                    "B1970": {0: 2.5, 1: 1.2, 2: .7},
                    "B1980": {0: 3.2, 1: 1.3, 2: .1},
                    "X": dict(zip(range(3), np.random.randn(3)))
                   })
dft

dft["id"] = dft.index
dft

dftw = pd.wide_to_long(dft, ["A", "B"], i="id", j="year")
dftw
dftw.index

# !?!?!?!?!? magic!

#%% Combining with stats and GroupBy
#%%
df
df.stack()
df.stack().mean()
df.stack().mean(1)
df.stack().mean(axis=1)
df.stack().mean(1).unstack()

df.groupby(axis=1, level=1)
df
df.groupby(axis=1, level=1).mean()
df.groupby(level=1).mean()

df.stack()
df.stack().groupby(level=1).mean()

df.mean()
df.mean(axis=0)
df.mean(axis=1)
df.mean().unstack()


#%% Pivot tables
#%%
"""
While pivot() provides general purpose pivoting with various data types
(strings, numerics, etc.), pandas also provides pivot_table()
for pivoting with _aggregation_ of numeric data.

It takes a number of arguments:

    data: a DataFrame object.
    values: a column or a list of columns to aggregate.
    index: a column, Grouper, array which has the same length as data,
        or list of them.
        Keys to group by on the pivot table index.
        If an array is passed, it is being used in the same manner
        as column values.
    columns: a column, Grouper, array which has the same length as data,
        or list of them.
        Keys to group by on the pivot table column.
        If an array is passed, it is being used in the same manner
        as column values.
    aggfunc: function to use for aggregation, defaulting to numpy.mean().
"""
#%%
from datetime import datetime

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 6,
                   'B': ['A', 'B', 'C'] * 8,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 4,
                   'D': np.random.randint(0, 10, 24),
                   'E': np.random.randint(0, 100, 24),
                   'F': [datetime(2019, i, 1) for i in range(1, 13)]
                        + [datetime(2019, i, 15) for i in range(1, 13)]
                  })
df

#%%
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])

pd.pivot_table(df, values='D', index=['B'], columns=['A', 'C'],
               aggfunc=np.sum)

pd.pivot_table(df, values=['D', 'E'], index=['B'], columns=['A', 'C'],
               aggfunc=np.sum)

#%%
"""
If the values column name is not given, the pivot table will include all of the data
that can be aggregated in an additional level of hierarchy in the columns:
"""
pd.pivot_table(df, index=['B'], columns=['A', 'C'], aggfunc=np.sum)
pd.pivot_table(df, index=['B'], columns=['A', 'C'], aggfunc=np.min)

#%%
"""Also, you can use Grouper for index and columns keywords.
For detail of Grouper, see
[Grouping with a Grouper specification](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby-specify).
"""
pd.pivot_table(df, values='D', columns='C',
               index=pd.Grouper(freq='M', key='F'))

# .to_string()
table = pd.pivot_table(df, index=['A', 'B'], columns=['C'])
table
print(table.to_string(na_rep=''))

"""
Note that pivot_table is also available as an instance method on DataFrame,
    i.e. DataFrame.pivot_table().
"""

#%% Adding margins

pd.pivot_table(df, values=['D'], index=['B'], columns=['A'],
               aggfunc=np.sum, margins=True)

pd.pivot_table(df, values=['D'], index=['B'], columns=['A', 'C'],
               aggfunc=np.sum, margins=True)

pd.pivot_table(df, values=['D', 'E'], index=['B'], columns=['A'],
               aggfunc=np.sum, margins=True)

pd.pivot_table(df, values=['D', 'E'], index=['B'], columns=['A'],
               aggfunc=len, margins=True)

#%% Cross tabulations
#%%
"""
Use crosstab() to compute a cross-tabulation of two (or more) factors.
By default crosstab computes a frequency table of the factors unless
an array of values and an aggregation function are passed.

It takes a number of arguments

    index: array-like, values to group by in the rows.
    columns: array-like, values to group by in the columns.
    values: array-like, optional, array of values to aggregate according to the factors.
    aggfunc: function, optional,
        If no values array is passed, computes a frequency table.
    rownames: sequence, default None, must match number of row arrays passed.
    colnames: sequence, default None, if passed, must match number of column arrays passed.
    margins: boolean, default False,
        Add row/column margins (subtotals)
    normalize: boolean, {‘all’, ‘index’, ‘columns’}, or {0,1}, default False.
        Normalize by dividing all values by the sum of values.

Any Series passed will have their name attributes used unless row or column names
for the cross-tabulation are specified
"""
foo, bar, dull, shiny, one, two = 'foo', 'bar', 'dull', 'shiny', 'one', 'two'

a = np.array([foo, foo, bar, bar, foo, foo], dtype=object)
b = np.array([one, one, two, one, two, one], dtype=object)
c = np.array([dull, dull, shiny, dull, dull, shiny], dtype=object)
a, b, c

#%%
pd.crosstab(a, b)
pd.crosstab(a, b, rownames='a', colnames='b')
pd.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])
pd.crosstab(a, [b, c])
pd.crosstab([a, b], c, rownames=['a', 'b'], colnames=['c'])

#%%
df = pd.DataFrame({'A': [1, 2, 2, 2, 2],
                   'B': [3, 3, 4, 4, 4],
                   'C': [1, 1, np.nan, 1, 1]})
df

pd.crosstab(df)  # TypeError: ...
pd.crosstab(df.A, df.B)
pd.crosstab(df.A, df.B, margins=True)
pd.crosstab(df.A, df.B, normalize=True)
pd.crosstab(df.A, df.B, normalize=True, margins=True)

pd.crosstab(df.A, df.B, normalize='columns')
pd.crosstab(df.A, df.B, normalize='columns', margins=True)
pd.crosstab(df.A, df.B, normalize='rows')   # ValueError: Not a valid normalize argument

pd.crosstab(df.A, df.B, values=df.C, aggfunc=np.sum)
pd.crosstab(df.A, df.B, values=df.C, aggfunc=np.sum, normalize=1)

pd.crosstab(df.A, df.B, values=df.C, aggfunc=len)
pd.crosstab(df.A, df.B, values=df.C, aggfunc=len, normalize=1)
print(pd.crosstab(df.A, df.B, values=df.C, aggfunc=len).to_string(na_rep=""))

#%%

foo = pd.Categorical(['a', 'b'], categories=['a', 'b', 'c'])
bar = pd.Categorical(['d', 'e'], categories=['d', 'e', 'f'])
pd.crosstab(foo, bar)
pd.crosstab(foo, bar, margins=True)

#%% cut()   Tiling ?

ages = np.array([10, 15, 13, 12, 23, 25, 28, 59, 60])
ages
pd.cut(ages, bins=3)
pd.cut(ages, bins=2)
pd.cut(ages, bins=2, include_lowest=True)

pd.cut(ages, bins=[0, 18, 35, 70])
pd.cut(ages, bins=[0, 18, 35])

c = pd.cut(ages, bins=3)
c
c.categories
pd.cut([25, 20, 50], bins=c.categories)

#%% Computing indicator / dummy variables
#%%

"""
To convert a categorical variable into a “dummy” or “indicator” DataFrame,
for example a column in a DataFrame (a Series) which has k distinct values,
can derive a DataFrame containing k columns of 1s and 0s using get_dummies():

It's also called 'one-hot-sth...'
"""

df = pd.DataFrame({'key': list('bbacab'), 'X': range(6)})
df

pd.get_dummies(df['key'])
pd.get_dummies(df.key)

#%%

dummies = pd.get_dummies(df.key, prefix="key")
dummies

df[['X']].join(dummies)   #!!!  DF.join(DF2)

#%% This function is often used along with discretization functions like cut:

values = np.random.random(10)
values

bins = np.linspace(0, 1, 6)
values_cut = pd.cut(values, bins=bins, include_lowest=True)
values_cut

pd.get_dummies(values_cut)

#%%
"""
get_dummies() also accepts a DataFrame.
By default all categorical variables (categorical in the statistical sense,
those with object or categorical dtype) are encoded as dummy variables.
"""
df = pd.DataFrame({'A': ['a', 'b', 'a'],
                   'B': ['c', 'c', 'b'],
                   'C': [10, 20, 30],
                   'P': ['r', 'q', 'p']
                   })
df

pd.get_dummies(df)
pd.get_dummies(df, columns=['A'])

"""
Notice that the B column is still included in the output, it just hasn’t been encoded.

???
You can _drop_ (how?) B before calling `get_dummies` if you don’t want to include it in the output.
"""

#%%
df2 = df
del df2['P']

pd.get_dummies(df2, prefix='prefix')
pd.get_dummies(df2, prefix=['from_A', 'from_B'])
pd.get_dummies(df2, prefix={'B': 'from_B', 'A': 'from_A'})

#%% avaiding colinearity i.e. dropping one level

ss = pd.Series(list('abcaa'))
ss

pd.get_dummies(ss)
pd.get_dummies(ss, drop_first=True)

#%% When a column contains only one level, it will be omitted in the result.

df = pd.DataFrame({'A': list('aaaaa'), 'B': list('ababc')})

pd.get_dummies(df)
pd.get_dummies(df, drop_first=True)

#%%
df = pd.DataFrame({'A': list('abc'), 'B':[1.1, 2.2, 3.3]})
df
pd.get_dummies(df, dtype=bool)
pd.get_dummies(df, dtype=bool).dtypes

#%% Factorizing values
#%%

ss = pd.Series(['A', 'A', np.nan, 'B', 3.14, np.inf])
ss

labels, uniques = pd.factorize(ss)
labels
uniques

df = pd.DataFrame(labels, columns=['X'])
pd.get_dummies(df, columns=['X'])

#%%
"""
Note that `factorize` is similar to `numpy.unique`,
but differs in its handling of NaN:

Note
The following numpy.unique will fail under Python 3 with a TypeError
because of an ordering bug. See also [here](https://github.com/numpy/numpy/issues/641).
"""
ss
pd.factorize(ss, sort=True)

np.unique(ss, return_inverse=True)

"""Note
If you just want to handle one column as a categorical variable (like R’s factor),
you can use
"""

df = pd.DataFrame({'A': ['a', 'b', 'a'],
                   'B': ['c', 'c', 'b'],
                   'C': [10, 20, 30],
                   })
df

df["cat_A"] = pd.Categorical(df["A"])
df
df.dtypes
# or
df["cat_A2"] = df["A"].astype("category")
df
df.dtypes

"""
For full docs on Categorical, see the Categorical introduction
https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#categorical
and the API documentation
"""
#%%

