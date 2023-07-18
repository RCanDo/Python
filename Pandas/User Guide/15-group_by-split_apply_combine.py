# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Group By: split-apply-combine
subtitle:
version: 1.0
type: tutorial
keywords: [groupby, NumPy, Pandas]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Pandas 0.25.3 User Guide
      chapter: Group By: split-apply-combine
      link: https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "15-group_by-split_apply_combine.py"
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
import numpy as np
import pandas as pd

#%%  see the file  04-merge_join_concatenate.py

from utils.builtin import paste
from utils.ak.nppd import data_frame

#%% Splitting an object into groups
#%%
"""
pandas objects can be split on any of their axes.

!!! The abstract definition of grouping is to provide a _mapping_ of labels to group names.  !!!

To create a GroupBy object (more on what the GroupBy object is later),
you may do the following:
"""

df = pd.DataFrame([('bird', 'Falconiformes', 389.0),
                   ('bird', 'Psittaciformes', 24.0),
                   ('mammal', 'Carnivora', 80.2),
                   ('mammal', 'Primates', np.nan),
                   ('mammal', 'Carnivora', 58)],
                index=['falcon', 'parrot', 'lion', 'monkey', 'leopard'],
                columns=('class', 'order', 'max_speed'))
df

#%%
dfg = df.groupby('class')
dfg
dfg.sum()
dfg.max()
dfg.min()
dfg.count()
dfg.std()
dfg.mean()

#%%
dir(dfg)
dfg.get_group('bird')
dfg.groups

#%%
dfg = df.groupby('order')
dfg.sum()
dfg = df.groupby('order', axis='columns')
dfg.sum()   # ValueError: len(index) != len(labels)

df.groupby(['class', 'order']).sum()
df.groupby(['class', 'order']).count()

#%%
"""
The _mapping_ can be specified many different ways:

A Python function, to be called on each of the axis labels.

A list or NumPy array of the same length as the selected axis.

A dict or Series, providing a label -> group name mapping.

For DataFrame objects, a string indicating a column to be used to group.
    Of course df.groupby('A') is just syntactic sugar for df.groupby(df['A']),
    but it makes life simpler.

For DataFrame objects, a string indicating an index level to be used to group.

A list of any of the above things.

Collectively we refer to the grouping objects as the _keys_.
"""
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
df
df.dtypes

#%% grouping by series (for df by some of its columns)

dfg = df.groupby('A')
dfg.count()
dfg.nunique()

# any aggregate -- outer functions:
dfg.agg(len)
dfg.agg(lambda x: sum(np.log(abs(x))))
dfg.agg(lambda x: (len(x), len(x)**2))
dfg.agg(lambda x: (min(x), max(x)))

dfg = df.groupby(['A', 'B'])
dfg.count()
dfg.nunique()                                                                   #!!!
dfg.sum()
dfg.sum().unstack('B')                                                          #!!!

#%%
# series may be grouped too, eg. by another series:
s1 = pd.Series(np.random.randn(12))
s2 = pd.Series(['a']*4 +['b']*5 + ['c']*3)
sg = s1.groupby(s2)
sg
sg.agg(len)
sg.count()
sg.sum()

# or just by list
sg = s1.groupby(['a']*4 +['b']*5 + ['c']*3)
sg.agg(len)
sg.count()
sg.sum()

# or by index (see below)

sg.groups
sg.groups.keys()
s1[sg.groups['a']]
sg.get_group('a')

#%%
"""
Note
A string passed to groupby may refer to either a column or an index level.
If a string matches both a column name and an index level name,
a ValueError will be raised.
"""
#%%
"""
If we also have a MultiIndex on columns A and B,
we can group by all but the specified columns.
"""
df
df2 = df.set_index(list('AB'))
df2

df2g = df2.groupby(level='B')
df2g.sum()
df2g = df2.groupby(level=df2.index.names.difference(['B']))
df2g.sum()

df2.groupby('A').sum()
df2.groupby(list('A')).sum()

#%%
"""
These will split the DataFrame on its index (rows). We could also split by the columns:
"""
def get_letter_type(letter):
    if letter.lower() in 'aeiouy':
        return 'vowel'
    else:
        return 'consonant'

df
dfg = df.groupby(get_letter_type, axis=1)
dfg

dfg.count()

dfg.agg(lambda x: sum(map(lambda i: isinstance(i, str), x)))
dfg.agg(lambda x: sum(map(lambda i: isinstance(i, float), x))) ## ???

#%% grouping by index
"""
pandas Index objects support duplicate values.
If a non-unique index is used as the group key in a groupby operation,
all values for the same index value will be considered to be in one group
and thus the output of aggregation functions will only contain unique index values:
"""
lst = [1, 2, 3]*2
ss = pd.Series([1, 2, 3, 10, 20, 30], lst)
ss
ss[1]
ss[:1]
ss[2]
ss[:2]
ss[:5]
ss[3]
ss[3][:1]

ssg = ss.groupby(level=0)
ssg.count()
ssg.nunique()
ssg.last()
ssg.first()
ssg.sum()

"""
Note that no splitting occurs until it’s needed.
Creating the GroupBy object only verifies that you’ve passed a valid mapping.

Note
Many kinds of complicated data manipulations can be expressed in terms of GroupBy operations
(though can’t be guaranteed to be the most efficient).
You can get quite creative with the label mapping functions.
"""

#%% GroupBy sorting
"""
By default the group keys are sorted during the groupby operation.
You may however pass sort=False for potential speedups:
"""
df2 = pd.DataFrame({'X': ['B', 'B', 'A', 'A'], 'Y': [1, 2, 3, 4]})
df2
df2.groupby(['X']).sum()
df2.groupby(['X'], sort=False).sum()

#%%%
"""
Note that groupby will preserve the order in which observations are sorted within each group.
For example, the groups created by groupby() below are in the order
they appeared in the original DataFrame:
"""
df3 = pd.DataFrame({'X': ['A', 'B', 'A', 'B'], 'Y': [1, 4, 3, 2]})
df3
df3.groupby(['X']).get_group('B')

#%% GroupBy object attributes
"""
The groups attribute is a dict
whose keys are the computed unique groups and corresponding   # ???
values being the axis labels belonging to each group.         # ???
In the above example we have:
"""
df
df.groupby('A').groups
df.groupby(get_letter_type, axis=1).groups

dfg = df.groupby(['A', 'B'])
dfg.groups

#%%
df = pd.DataFrame(  [
        ["2000-01-01", 42.849980, 157.500553, "male"],
        ["2000-01-02", 49.607315, 177.340407, "male"],
        ["2000-01-03", 56.293531, 171.524640, "male"],
        ["2000-01-04", 48.421077, 144.251986, "female"],
        ["2000-01-05", 46.556882, 152.526206, "male"],
        ["2000-01-06", 68.448851, 168.272968, "female"],
        ["2000-01-07", 70.757698, 136.431469, "male"],
        ["2000-01-08", 58.909500, 176.499753, "female"],
        ["2000-01-09", 76.435631, 174.094104, "female"],
        ["2000-01-10", 45.306120, 177.540920, "male"]
        ],
    columns=["date", "height", "weight", "gender"] )
df
df.dtypes
## it's always better to keep proper types
df['date'] = df['date'].astype('datetime64')
# or
df['date'] = pd.to_datetime(df['date'])

df = df.set_index('date')
df
df.dtypes    #!

dfg = df.groupby('gender')
dfg.groups
#
dfg.gender
#  <pandas.core.groupby.generic.SeriesGroupBy object at 0x7fdac45e1040>
dfg.height
dfg.weight

dfg.mean()

#%% GroupBy with MultiIndex
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
ss = pd.Series(np.random.randint(0, 10, 8), index=index)
ss

ssg = ss.groupby(level=0)
ssg.sum()
ssg.min()
ssg.max()

ssg = ss.groupby(level=1)
ssg.sum()

ssg = ss.groupby(level=[0, 1])
ssg.sum()

ssg = ss.groupby(level='second')
ssg.sum()

ssg = ss.groupby(['first', 'second'])
ssg.sum()


#%% Grouping DataFrame with Index levels and columns

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])

df = pd.DataFrame({'A': [1, 1, 1, 1, 2, 2, 3, 3],
                   'B': np.arange(8)},
                    index=index)
df

#%% Grouping DataFrame with Index levels and columns
"""
A DataFrame may be grouped by
!!!  a combination of columns and index levels
by specifying the column names as strings and the index levels as  pd.Grouper()  objects.
"""
df.groupby([pd.Grouper(level=1), 'A']).sum()
df.groupby([pd.Grouper(level='second'), 'A']).sum()
df.groupby(['second', 'A']).sum()     ## .Grouper() not needed when index levels are named

#%% DataFrame column selection in GroupBy
"""
Once you have created the GroupBy object from a DataFrame,
you might want to do something different for each of the columns.
Thus, using [] similar to getting a column from a DataFrame, you can do:
"""
df = pd.DataFrame({ 'A': paste('a', list('000011112222')),
                    'B': paste('b', list('012012012012')),
                    'C': paste('c', list('001122001122')),
                    'X': np.random.randint(0, 5, 12),
                    'Y': np.random.randint(10, 15, 12)
                  })
df

grouped = df.groupby(['A'])
grouped.sum()
grouped.groups

grouped_C = grouped['C']
grouped_C
grouped_C.count()
grouped_C.sum()
# This is mainly syntactic sugar for the alternative and much more verbose:
df['C'].groupby(df['A']).sum()
df['C'].groupby(df['A']).count()

grouped_B = grouped['B']
grouped_B.count()
grouped_B.sum()


#%% Iterating through groups
#%%
"""
With the GroupBy object in hand, iterating through the grouped data is very natural
and functions similarly to itertools.groupby():
"""

grouped = df.groupby('A')
grouped.groups
grouped.groups['a1']

for name, group in grouped:      # !!!
    print(name)
    print(group)

#%%
for name, group in df.groupby(['A', 'B']):
    print(name)
    print(group)

# See [Iterating through groups](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-iterating-label).

#%% Selecting a group
#%%

grouped.get_group('a2')

df.groupby(['A', 'B']).get_group(('a2', 'b2'))


#%% Aggregation
#%%
"""
Once the GroupBy object has been created, several methods are available
to perform a computation on the grouped data.
These operations are similar to the
[aggregating API](https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#basics-aggregate) ,
[window functions API](https://pandas.pydata.org/pandas-docs/stable/user_guide/computation.html#stats-aggregate),
and [resample API](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-aggregate).
"""

df

dfg = df.groupby('A')
dfg.size()             # Series
dfg.describe()

dfg.aggregate(sum)
dfg.agg(sum)
dfg.sum()
dfg.agg(sum).reset_index()

dfg = df.groupby('A', as_index=False)
dfg.agg(sum)
dfg.size()             # Series

#%%
dfgab = df.groupby(['A', 'B'])
dfgab.sum()
dfgab.size()             # Series
dfgab.describe()

dfgab.aggregate(sum)
dfgab.sum()
dfgab.sum().reset_index()

dfgab = df.groupby(['A', 'B'], as_index=False)                                  #!!!
dfgab.sum()
dfgab.size()             # Series

#%%
dfg.agg([sum, np.mean, np.std])
dfg['X'].agg([sum, np.mean, np.std])

dfg.agg([sum, np.mean, np.std]).rename(columns={'sum':'agg1', 'mean':'agg2', 'std':'agg3'})
# cannot be done via list:
dfg.agg([sum, np.mean, np.std]).rename(columns=['agg1', 'agg2', 'agg3']) #! TypeError: 'list' object is not callable

#%%
dfg.agg([sum, sum])  #! SpecificationError: Function names must be unique, found multiple named sum
# but you may use lambdas
dfg.agg([lambda x: min(x),
         lambda x: np.mean(x)])
# so this will work
dfg.agg([lambda x: min(x),
         lambda x: min(x)])

#%% Named aggregation
"""
To support column-specific aggregation with control over the output column names,
pandas accepts the special syntax in GroupBy.agg(), known as “named aggregation”, where
- The  keywords  are the  output column names
- The  values  are  tuples  whose first element is the  column  to select
  and the second element is the  aggregation  to apply to that column.
  Pandas provides the pandas.NamedAgg namedtuple with the fields ['column', 'aggfunc']
  to make it clearer what the arguments are.
  As usual, the aggregation can be a callable or a string alias.
"""
animals = pd.DataFrame({'kind': ['cat', 'dog', 'cat', 'dog'],
                        'height': [9.1, 6.0, 9.5, 34.0],
                        'weight': [7.9, 7.5, 9.9, 198.0]})
animals

#%%
animals_kind = animals.groupby("kind")

animals_kind.agg(
        min_height=pd.NamedAgg(column='height', aggfunc='min'),
        max_height=pd.NamedAgg(column='height', aggfunc='max'),
        average_weight=pd.NamedAgg(column='weight', aggfunc=np.mean)
        )

#%% pandas.NamedAgg is just a namedtuple. Plain tuples are allowed as well.
animals_kind.agg(min_height=('height', 'mean'),
                 max_height=('height', 'max'),
                 average_weight=('weight', np.mean),
                )
#%% If your desired output column names are not valid python keywords,
# construct a dictionary and unpack the keyword arguments
animals_kind.agg(**{'total weight': pd.NamedAgg('weight', sum),
                    'mean weight': ('weight', np.mean)})

#%% agg for Series -- no more need for column name within agg
animals_kind['height'].agg(min_height='min', max_height='max')
animals_kind.height.agg(**{'min height':min, 'max height':max})

#%%  when output names are not important you may simply write

# for DataFrames
animals_kind.agg({'height': min, 'weight': max})
# now the dict keys indicate columns not an output names

# for Series
animals_kind.height.agg([min, max])

#%% Cython-optimized aggregation functions
"""
Some common aggregations, currently only sum, mean, std, and sem,
have optimized Cython implementations:
"""
animals_kind.sum()
animals_kind.mean()
animals_kind.std()
animals_kind.sem()


#%% Transformation¶
#%%
"""
The transform method returns an object that is indexed the same (same size)
as the one being grouped. The transform function must:

    - Return a result that is either the same size as the group chunk
      or broadcastable to the size of the group chunk
      (e.g., a scalar, grouped.transform(lambda x: x.iloc[-1])).
    - Operate column-by-column on the group chunk.
      The transform is applied to the first group chunk using chunk.apply.
    - Not perform in-place operations on the group chunk.
      Group chunks should be treated as _immutable_,
      and changes to a group chunk may produce unexpected results.
      For example, when using `fillna`, inplace must be False
      (grouped.transform(lambda x: x.fillna(inplace=False))).
    - (Optionally) operates on the entire group chunk.
      If this is supported, a fast path is used starting from the second chunk.

For example, suppose we wished to standardize the data within each group:
"""

#%%
idx = pd.date_range('1999-10-01', periods=1100)
ts = pd.Series(np.random.normal(.5, 2, 1100), idx)
ts.head(10)
ts.tail()
ts.count()   # 1100
ts[ts>0].count()
ts[ts<0].count()

ts.rolling(window=100, min_periods=100).mean().dropna()

transformed = ts.groupby(lambda x: x.year).transform(lambda x: (x-x.mean()) / x.std())
transformed

#%% We would expect the result to now have mean 0 and standard deviation 1
# within each group, which we can easily check:
tsg = ts.groupby(lambda x: x.year)
tsg.mean()
tsg.std()

transg = transformed.groupby(lambda x: x.year)
transg.mean()
transg.std()

#%% We can also visually compare the original and transformed data sets.
comp_df = pd.DataFrame({'original': ts, 'transformed': transformed})
comp_df.plot()

#%% Transformation functions that have lower dimension outputs
# are broadcast to match the shape of the input array.

tsg_t1 = tsg.transform(lambda x: x.max() - x.min())
tsg_t1.name = "max - min"
comp_df.join(tsg_t1).plot()

#%% Alternatively, the built-in methods could be used to produce the same outputs.
ts_max = tsg.transform(max)
ts_min = tsg.transform(min)
ts_range = ts_max - ts_min
ts_range.name = 'ts range'
comp_df.join(ts_range).plot()

#%% try the same by month
tsgm = ts.groupby(lambda x: x.month)
tsgm_t1 = tsgm.transform(lambda x: x.max() - x.min())
tsgm_t1.name = 'months'
comp_df.join(tsgm_t1).plot()

#%% sth little different
months_range_df = pd.DataFrame({'max': tsgm.transform(max),
                                'min': tsgm.transform(min)})
months_range_df.plot()
comp_df.join(months_range_df).plot()

#%%
#%% replace missing data with the group mean.
#%%

#%% first try to generate data with NaN
# for problems with NaN see 'ex01-pd.dtypes.py'

r=10; c=3; nnans=7
arr = np.random.randint(0, r*c, (r, c)).astype("float32")
arr.dtype

rows = np.random.randint(0, r, (nnans,))
cols = np.random.randint(0, c, (nnans,))
arr[rows, cols] = np.nan    # ok but only because we set dtype=float32
                            # otherwise there would be an error!
                            # in numpy NaN may only be for floats... BAD!!!

df = pd.DataFrame(arr)
df.dtypes   # not good having floats for int...
for c in df.columns: df[c] = df[c].astype(pd.Int16Dtype())
df
# so Pandas accept NaN for int types but they are Pandas' ints!!!

#!!! there's really no shorter way !!!

#%% back to replacing missing data
df
countries = np.array(['SK', 'CZ', 'HG', 'PL'])
key = countries[np.random.randint(0, 4, 10)]

dfg = df.groupby(key)
dfg.groups
dfg.get_group('PL')
dfg.count()    # non NA counts !

dfgt = dfg.transform(lambda x: x.fillna(x.mean()))
dfgt

#%% check if both means are equall
dfg.mean()
dfgt.groupby(key).mean()

# NA counts should differ
dfg.count()
dfgt.groupby(key).count()


dfg.size()
dfgt.groupby(key).size()

#%%
"""
Some functions will automatically transform the input when applied to a GroupBy object,
but returning an object of the same shape as the original.
Passing as_index=False will not affect these transformation methods.
For example: fillna, ffill, bfill, shift..
"""
df
dfg.fillna()    # empty df ...
dfg.fillna(-1)  # empty...
dfg.transform(lambda x: x.fillna(-1))
# BUT
dfg.ffill()  # forward fill
dfg.bfill()  # backward fill
dfg.shift()  # shift everything within group by n steps, first entries becoming NA

#%%
#%% New syntax to window and resample operations
"""
Working with the  resample, expanding or rolling  operations on the groupby level
used to require the application of helper functions.
However, now it is possible to use resample(), expanding() and rolling()
as methods on groupbys.
The example below will apply the rolling() method on the samples of the column B based on the groups of column A.
"""
df = pd.DataFrame({'A': [1]*10 + [5]*10,
                   'B': np.arange(20)})
df
#%%
dfga = df.groupby('A')
dfga.groups

dfga.rolling(4)
dfga.rolling(4).B
dfga.rolling(4).B.mean()
#??? do it in opposie direction ???

dfga.expanding()
dfga.expanding().sum()    ## cumsum within window

#%%
"""
Suppose you want to use the resample() method to get a daily frequency
 in each group of your dataframe and wish to complete the missing values
 with the ffill() method.
"""
df_re = pd.DataFrame({'date': pd.date_range(start='2016-01-01', periods=4, freq='W'),
                      'group': [1, 1, 2, 2],
                      'val': [5, 6, 7, 8]}).set_index('date')
df_re

df_re.groupby('group').resample('1D').ffill()


# %%
df_re = pd.DataFrame({'date': pd.date_range(start='2016-01-01', periods=72, freq='H'),
                      'group': np.random.choice([0, 1], 72),
                      'val': np.random.sample(size=72)}).set_index('date')
df_re

df_re.groupby('group').resample('1D').agg(**{'val': pd.NamedAgg(column='val', aggfunc=np.mean)})

#%%
#%% Filtration
# https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#filtration



#%%
