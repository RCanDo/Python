# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Categorical data
subtitle:
version: 1.0
type: tutorial
keywords: [., NumPy, Pandas]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Pandas 2.2 User Guide
      chapter:
      link: https://pandas.pydata.org/docs/user_guide/categorical.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "..py"
    path: "D:/ROBOCZY/Python/Pandas/User Guide/"
    date: 2024-12-28
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.com
              - arek@staart.pl
"""

#%%
import numpy as np
import pandas as pd

from pycando.builtin import flatten, paste
from pycando.ak import data_frame
from pycando.config import pandas_options

# %%  # Object creation
"""
# Object creation
"""
# %%  ## Series creation
"""
## Series creation

Categorical Series or columns in a DataFrame can be created in several ways:
"""
# %% 1. By specifying  dtype="category"  when constructing a Series:
s = pd.Series(["a", "b", "c", "a"], dtype="category")
s
# 0    a
# 1    b
# 2    c
# 3    a
# dtype: category
# Categories (3, object): ['a', 'b', 'c']

# %% 2. By converting an existing Series or column to a category dtype:
df = pd.DataFrame({"A": ["a", "b", "c", "a"]})
df["B"] = df["A"].astype("category")
df
#    A  B
# 0  a  a
# 1  b  b
# 2  c  c
# 3  a  a
df.dtypes
# A      object
# B    category
# dtype: object

# %% 3. By using special functions, such as cut(), which groups data into discrete bins.
# See the example on tiling in the docs: https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-tile-cut

df = pd.DataFrame({"value": np.random.randint(0, 100, 20)})
labels = ["{0} - {1}".format(i, i + 9) for i in range(0, 100, 10)]
df["group"] = pd.cut(df.value, range(0, 105, 10), right=False, labels=labels)
df.head()
#    value    group
# 0     65  60 - 69
# 1     49  40 - 49
# 2     56  50 - 59
# 3     43  40 - 49
# 4     43  40 - 49
df.dtypes
# value       int64
# group    category
# dtype: object
df['group'].value_counts()
# group
# 60 - 69    5
# 40 - 49    5
# 70 - 79    3
# 90 - 99    2
# 80 - 89    2
# 50 - 59    2
# 20 - 29    1
# 0 - 9      0
# 10 - 19    0
# 30 - 39    0
# Name: count, dtype: int64

# %% 4. By passing a pandas.Categorical object to a Series or assigning it to a DataFrame.

raw_cat = pd.Categorical(
    ["a", "b", "c", "a"], categories=["b", "c", "d"], ordered=False
)
# [NaN, 'b', 'c', NaN]
# Categories (3, object): ['b', 'c', 'd']
s = pd.Series(raw_cat)
s
# 0    NaN
# 1      b
# 2      c
# 3    NaN
# dtype: category
# Categories (3, object): ['b', 'c', 'd']

df = pd.DataFrame({"A": ["a", "b", "c", "a"]})
df["B"] = raw_cat
df
#    A    B
# 0  a  NaN
# 1  b    b
# 2  c    c
# 3  a  NaN

df.dtypes
# A      object
# B    category
# dtype: object

#%%  ## DataFrame creation
"""
## DataFrame creation

Similar to the previous section where a single column was converted to categorical,
all columns in a DataFrame can be batch converted to categorical either during or after construction.

This can be done during construction by specifying dtype="category" in the DataFrame constructor:
"""
df = pd.DataFrame({"A": list("abca"), "B": list("bccd")}, dtype="category")
df.dtypes
# A    category
# B    category
# dtype: object

"""
Note that the categories present in each column differ;
the conversion is done column by column, so only labels present in a given column are categories:
"""
df["A"]
# 0    a
# 1    b
# 2    c
# 3    a
# Name: A, dtype: category
# Categories (3, object): ['a', 'b', 'c']

df["B"]
# 0    b
# 1    c
# 2    c
# 3    d
# Name: B, dtype: category
# Categories (3, object): ['b', 'c', 'd']

"""
Analogously, all columns in an existing DataFrame can be batch converted using DataFrame.astype():
"""
df = pd.DataFrame({"A": list("abca"), "B": list("bccd")})
df.dtypes
# A    object
# B    object
# dtype: object

df_cat = df.astype("category")                  # !
df_cat.dtypes
# A    category
# B    category
# dtype: object

"""
This conversion is likewise done column by column:
"""
df_cat["A"]
# 0    a
# 1    b
# 2    c
# 3    a
# Name: A, dtype: category
# Categories (3, object): ['a', 'b', 'c']

df_cat["B"]
# 0    b
# 1    c
# 2    c
# 3    d
# Name: B, dtype: category
# Categories (3, object): ['b', 'c', 'd']

#%%  ## Controlling behavior
"""
## Controlling behavior

In the examples above where we passed dtype='category', we used the default behavior:
    Categories are inferred from the data.
    Categories are unordered.
To control those behaviors, instead of passing 'category', use an instance of  CategoricalDtype.
"""
from pandas.api.types import CategoricalDtype

s = pd.Series(["a", "b", "c", "a"])
cat_type = CategoricalDtype(categories=["b", "c", "d"], ordered=True)
cat_type        # CategoricalDtype(categories=['b', 'c', 'd'], ordered=True, categories_dtype=object)
type(cat_type)  # pandas.core.dtypes.dtypes.CategoricalDtype

s_cat = s.astype(cat_type)
s_cat
# 0    NaN
# 1      b
# 2      c
# 3    NaN
# dtype: category
# Categories (3, object): ['b' < 'c' < 'd']

"""  !!!
Similarly, a CategoricalDtype can be used with a DataFrame to ensure that
!  categories are consistent among all columns.
"""
from pandas.api.types import CategoricalDtype

df = pd.DataFrame({"A": list("abca"), "B": list("bccd")})
cat_type = CategoricalDtype(categories=list("abcd"), ordered=True)
cat_type        # CategoricalDtype(categories=['a', 'b', 'c', 'd'], ordered=True, categories_dtype=object)
type(cat_type)  # pandas.core.dtypes.dtypes.CategoricalDtype

df_cat = df.astype(cat_type)
df_cat["A"]
# 0    a
# 1    b
# 2    c
# 3    a
# Name: A, dtype: category
# Categories (4, object): ['a' < 'b' < 'c' < 'd']

df_cat["B"]
# 0    b
# 1    c
# 2    c
# 3    d
# Name: B, dtype: category
# Categories (4, object): ['a' < 'b' < 'c' < 'd']

"""
To perform table-wise conversion,
where all labels in the entire DataFrame are used as categories for each column,
the categories parameter can be determined programmatically by
"""
categories = pd.unique(df.to_numpy().ravel())
categories
# array(['a', 'b', 'c', 'd'], dtype=object)

"""
If you already have codes and categories,
you can use the `.from_codes()` constructor to save the factorize step during normal constructor mode:
"""
splitter = np.random.choice([0, 1], 5, p=[0.5, 0.5])
splitter

cats = pd.Categorical.from_codes(splitter, categories=["train", "test"])
cats
# ['test', 'test', 'test', 'test', 'train']
# Categories (2, object): ['train', 'test']
type(cats)          # pandas.core.arrays.categorical.Categorical

s = pd.Series(cats)
s
# 0     test
# 1     test
# 2     test
# 3     test
# 4    train
# dtype: category
# Categories (2, object): ['train', 'test']

#%%  ## Regaining original data
"""
## Regaining original data

To get back to the original Series or NumPy array, use
"""
Series.astype(original_dtype)    # or
np.asarray(categorical)

# %%
s = pd.Series(["a", "b", "c", "a"])
s
# 0    a
# ...
# 3    a
# dtype: object
s2 = s.astype("category")
s2
# 0    a
# ...
# 3    a
# dtype: category
# Categories (3, object): ['a', 'b', 'c']

s2.astype(str)
# 0    a
# ...
# 3    a
# dtype: object

np.asarray(s2)
# array(['a', 'b', 'c', 'a'], dtype=object)

"""  Notes
In contrast to R’s `factor` function:

1. categorical data is not converting input values to strings;
   categories will end up the same data type as the original values.
2. there is currently no way to assign/change labels at creation time.
   Use `categories` to change the categories after creation time.
"""
#%%  # CategoricalDtype
"""
# CategoricalDtype

A categorical’s type is fully described by
    categories: a sequence of unique values and no missing values
    ordered: a boolean
This information can be stored in a CategoricalDtype.
The categories argument is optional,
which implies that the actual categories should be inferred from whatever is present in the data
when the pandas.Categorical is created.
The categories are assumed to be unordered by default.
"""
from pandas.api.types import CategoricalDtype

CategoricalDtype(["a", "b", "c"])
# CategoricalDtype(categories=['a', 'b', 'c'], ordered=False, categories_dtype=object)

CategoricalDtype(["a", "b", "c"], ordered=True)
# CategoricalDtype(categories=['a', 'b', 'c'], ordered=True, categories_dtype=object)

CategoricalDtype()
# CategoricalDtype(categories=None, ordered=False, categories_dtype=None)

"""
A CategoricalDtype can be used in any place pandas expects a dtype.
For example  pandas.read_csv(),  pandas.DataFrame.astype(), or in the Series constructor.

Note
As a convenience, you can use the string 'category' in place of a CategoricalDtype
when you want the default behavior of the categories being unordered,
and equal to the set values present in the array.
In other words,  `dtype='category'`  is equivalent to `dtype=CategoricalDtype()`.
"""
# %%  ## Equality semantics
"""
## Equality semantics

Two instances of CategoricalDtype compare equal whenever they have the same categories and order.
When comparing two unordered categoricals, the order of the categories is not considered.
"""
c1 = CategoricalDtype(["a", "b", "c"], ordered=False)

# Equal, since order is not considered when ordered=False
c1 == CategoricalDtype(["b", "c", "a"], ordered=False)
# True

# Unequal, since the second CategoricalDtype is ordered
c1 == CategoricalDtype(["a", "b", "c"], ordered=True)
# False

"""  !!!
All instances of CategoricalDtype compare equal to the string 'category'.
"""
c1 == "category"
# True

# %%  ## Description
"""
## Description

Using describe() on categorical data will produce similar output to a Series or DataFrame of type string.
"""
cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat": cat, "s": ["a", "c", "c", np.nan]})

df.describe()
#        cat  s
# count    3  3
# unique   2  2
# top      c  c
# freq     2  2

df["cat"].describe()
# count     3
# unique    2
# top       c
# freq      2
# Name: cat, dtype: object      !!!  that's not good  !!!

df["s"].describe()
# count     3
# unique    2
# top       c
# freq      2
# Name: s, dtype: object

# %%
# %%  # Working with categories
"""
# Working with categories

Categorical data has a categories and a ordered property,
which list their possible values and whether the ordering matters or not.
These properties are exposed as
"""
s.cat.categories
s.cat.ordered
"""
If you don’t manually specify categories and ordering, they are inferred from the passed arguments.
"""
s = pd.Series(["a", "b", "c", "a"], dtype="category")
s.cat.categories    # Index(['a', 'b', 'c'], dtype='object')
s.cat.ordered       # False

"""
It’s also possible to pass in the categories in a specific order:
"""
s = pd.Series(pd.Categorical(["a", "b", "c", "a"], categories=["c", "b", "a"]))
s.cat.categories    # Index(['c', 'b', 'a'], dtype='object')
s.cat.ordered       # False
"""
New categorical data are not automatically ordered.
You must explicitly pass `ordered=True` to indicate an ordered Categorical.
"""
# %%
"""
The result of `unique()` is not always the same as `Series.cat.categories`,
because `Series.unique()` has a couple of guarantees, namely that it returns categories in the order of appearance,
and it only includes values that are actually present.
"""
s = pd.Series(list("babc")).astype(CategoricalDtype(list("abcd")))
s
# 0    b
# 1    a
# 2    b
# 3    c
# dtype: category
# Categories (4, object): ['a', 'b', 'c', 'd']

s.cat.categories    # Index(['a', 'b', 'c', 'd'], dtype='object')
s.unique()
# ['b', 'a', 'c']
# Categories (4, object): ['a', 'b', 'c', 'd']

# %%  ## Renaming categories
"""
## Renaming categories  `s.cat.rename_categories()`
"""

s = pd.Series(["a", "b", "c", "a"], dtype="category")
s
# 0    a
# 1    b
# 2    c
# 3    a
# dtype: category
# Categories (3, object): ['a', 'b', 'c']

new_categories = ["Group %s" % g for g in s.cat.categories]

s = s.cat.rename_categories(new_categories)
s
# 0    Group a
# 1    Group b
# 2    Group c
# 3    Group a
# dtype: category
# Categories (3, object): ['Group a', 'Group b', 'Group c']

# You can also pass a dict-like object to map the renaming

s = s.cat.rename_categories({'Group a': "x", 'Group b': "y", 'Group c': "z"})
s
# 0    x
# 1    y
# 2    z
# 3    x
# dtype: category
# Categories (3, object): ['x', 'y', 'z']

"""
Note
In contrast to R’s factor, categorical data can have categories of other types than string.
"""
# %%
"""
Categories must be unique or a ValueError is raised:
"""
s = s.cat.rename_categories([1, 1, 1])      # ! ValueError: Categorical categories must be unique

"""
Categories must also NOT be NaN or a ValueError is raised:
"""
s = s.cat.rename_categories([1, 2, np.nan]) # !ValueError: Categorical categories cannot be null

# %%  ## Appending new categories
"""
## Appending new categories

Appending categories can be done by using the add_categories() method:
"""
s = pd.Series(["a", "b", "c", "a"], dtype="category")
s = s.cat.add_categories([4])

s.cat.categories    # Index(['a', 'b', 'c', 4], dtype='object')
s
# 0    a
# 1    b
# 2    c
# 3    a
# dtype: category
# Categories (4, object): ['a', 'b', 'c', 4]

"""
## Removing categories  `s.cat.remove_categories()`

Values which are removed are replaced by  `np.nan`:
"""
s = s.cat.remove_categories(['c'])
s
# 0      a
# 1      b
# 2    NaN
# 3      a
# dtype: category
# Categories (3, object): [4, 'a', 'b']

"""
## Removing unused categories
"""
s.cat.remove_unused_categories()
# 0      a
# 1      b
# 2    NaN
# 3      a
# dtype: category
# Categories (2, object): ['a', 'b']

# %%  ## Setting categories
"""
## Setting categories

If you want to do remove and add new categories in one step (which has some speed advantage),
or simply set the categories to a predefined scale, use  `set_categories()`.
"""
s = pd.Series(["one", "two", "four", "-"], dtype="category")
s
# 0     one
# 1     two
# 2    four
# 3       -
# dtype: category
# Categories (4, object): ['-', 'four', 'one', 'two']

s = s.cat.set_categories(["one", "two", "three", "four"])
s
# 0     one
# 1     two
# 2    four
# 3     NaN
# dtype: category
# Categories (4, object): ['one', 'two', 'three', 'four']

"""  !!!
Be aware that Categorical.set_categories() cannot know whether some category is omitted intentionally
or because it is misspelled or (under Python3) due to a type difference
(e.g., NumPy S1 dtype and Python strings).
This can result in surprising behaviour!
"""

# %%  # Sorting and order
"""
# Sorting and order

If categorical data is ordered (`s.cat.ordered == True`),
then the order of the categories has a meaning and certain operations are possible.
If the categorical is unordered, .min()/.max() will raise a TypeError.
"""
s = pd.Series(pd.Categorical(["c", "b", "a", "c"], ordered=False))
s
# 0    c
# 1    b
# 2    a
# 3    c
# dtype: category
# Categories (3, object): ['a', 'b', 'c']       !!! notice the alphabetical "order"

# !!! sorting of unordered means alphabetical order:
s = s.sort_values()
s
# 2    a
# 1    b
# 0    c
# 3    c
# dtype: category
# Categories (3, object): ['a', 'b', 'c']

s.cat.ordered   # False

s.min(), s.max()
# ! TypeError: Categorical is not ordered for operation min;
#   you can use .as_ordered() to change the Categorical to an ordered one

from pandas.api.types import CategoricalDtype

s = pd.Series(["d", "b", "a", "d"]).astype(CategoricalDtype(ordered=True))
s
# 0    d
# 1    b
# 2    a
# 3    d
# dtype: category
# Categories (3, object): ['a' < 'b' < 'd']    !!! alphabetical order is default
s = s.sort_values()
s
# 2    a
# 1    b
# 0    d
# 3    d
# dtype: category
# Categories (3, object): ['a' < 'b' < 'd']

s.cat.ordered   # True

s.min(), s.max()
# ('a', 'd')

# add new category to ordered – always to the "top" or as "the highest"/"last" category, and in the given order
s.cat.add_categories(['c', '0'])
# ...
# dtype: category
# Categories (4, object): ['a' < 'b' < 'd' < 'c', '0']       !!!  important  !!!

"""
You can set categorical data to be ordered by using as_ordered() or unordered by using as_unordered().
These will by default return a new object.
"""
s = pd.Series(pd.Categorical(["c", "b", "a", "c"], ordered=False))
s.cat.as_ordered()
# 0    c
# 1    b
# 2    a
# 3    c
# dtype: category
# Categories (3, object): ['a' < 'b' < 'c']

s.cat.as_unordered()
# 0    c
# 1    b
# 2    a
# 3    c
# dtype: category
# Categories (3, object): ['a', 'b', 'c']

"""
Sorting will use the order defined by categories, not any lexical order present on the data type.
This is even true for strings and numeric data:
"""
s = pd.Series([1, 2, 3, 1], dtype="category")
s = s.cat.set_categories([2, 3, 1], ordered=True)
s
# 0    1
# 1    2
# 2    3
# 3    1
# dtype: category
# Categories (3, int64): [2 < 3 < 1]

s = s.sort_values()
s
# 1    2
# 2    3
# 0    1
# 3    1
# dtype: category
# Categories (3, int64): [2 < 3 < 1]

s.min(), s.max()
# (2, 1)
s.cat.categories    # Index([2, 3, 1], dtype='int64')     sort order

# %%  ## Reordering
"""
## Reordering

Reordering the categories is possible via the
    Categorical.reorder_categories()  and the
    Categorical.set_categories()  methods.
For Categorical.reorder_categories(), all old categories must be included in the new categories
and no new categories are allowed.
This will necessarily make the sort order the same as the categories order.
"""
s = pd.Series([1, 2, 3, 1], dtype="category")
s = s.cat.reorder_categories([2, 3, 1], ordered=True)
s
# 0    1
# 1    2
# 2    3
# 3    1
# dtype: category
# Categories (3, int64): [2 < 3 < 1]

s = s.sort_values()
s
# 1    2
# 2    3
# 0    1
# 3    1
# dtype: category
# Categories (3, int64): [2 < 3 < 1]
s.min(), s.max()        # (np.int64(2), np.int64(1))

"""
Note the difference between assigning new categories and reordering the categories:
the first renames categories and therefore the individual values in the Series,
but if the first position was sorted last, the renamed value will still be sorted last.
Reordering means that the way values are sorted is different afterwards,
but not that individual values in the Series are changed.

If the Categorical is not ordered,  Series.min()  and  Series.max()  will raise TypeError.
Numeric operations like +, -, *, / and operations based on them
(e.g. Series.median(), which would need to compute the mean between two values if the length of an array is even)
do not work and raise a TypeError.
"""

# %%  ## Multi column sorting
"""
## Multi column sorting

A categorical dtyped column will participate in a multi-column sort in a similar manner to other columns.
The ordering of the categorical is determined by the categories of that column.
"""
dfs = pd.DataFrame(
    {
        "A": pd.Categorical(
            list("bbeebbaa"),
            categories=["e", "a", "b"],
            ordered=True,
        ),
        "B": [1, 2, 1, 2, 2, 1, 2, 1],
    }
)

dfs.sort_values(by=["A", "B"])
#    A  B
# 2  e  1
# 3  e  2
# 7  a  1
# 6  a  2
# 0  b  1
# 5  b  1
# 1  b  2
# 4  b  2

"""
Reordering the categories changes a future sort.
"""
dfs["A"] = dfs["A"].cat.reorder_categories(["a", "b", "e"])

dfs.sort_values(by=["A", "B"])
#    A  B
# 7  a  1
# 6  a  2
# 0  b  1
# 5  b  1
# 1  b  2
# 4  b  2
# 2  e  1
# 3  e  2

# %%  # Comparisons
"""
# Comparisons

Comparing categorical data with other objects is possible in three cases:
1. Comparing equality (== and !=) to a list-like object (list, Series, array, …)
   of the same length as the categorical data.
2. All comparisons (==, !=, >, >=, <, and <=) of categorical data to another categorical Series,
   when ordered==True and the categories are the same.
3. All comparisons of a categorical data to a scalar.
All other comparisons, especially “non-equality” comparisons of two categoricals with different categories
or a categorical with any list-like object, will raise a TypeError.

Any “non-equality” comparisons of categorical data with a Series, np.array, list or categorical data
with different categories or ordering will raise a TypeError
because custom categories ordering could be interpreted in two ways:
one with taking into account the ordering and one without.
"""
cat = pd.Series([1, 2, 3]).astype(CategoricalDtype([3, 2, 1], ordered=True))
cat_base = pd.Series([2, 2, 2]).astype(CategoricalDtype([3, 2, 1], ordered=True))
cat_base2 = pd.Series([2, 2, 2]).astype(CategoricalDtype(ordered=True))

cat
# 0    1
# 1    2
# 2    3
# dtype: category
# Categories (3, int64): [3 < 2 < 1]

cat_base
# 0    2
# 1    2
# 2    2
# dtype: category
# Categories (3, int64): [3 < 2 < 1]

cat_base2
# 0    2
# 1    2
# 2    2
# dtype: category
# Categories (1, int64): [2]

"""
Comparing to a categorical with the same categories and ordering or to a scalar works:
"""
cat > cat_base
# 0     True
# 1    False
# 2    False
# dtype: bool

cat > 2
# 0     True
# 1    False
# 2    False
# dtype: bool

"""
Equality comparisons work with any list-like object of same length and scalars:
"""
cat == cat_base
# 0    False
# 1     True
# 2    False
# dtype: bool

cat == np.array([1, 2, 3])
# 0    True
# 1    True
# 2    True
# dtype: bool

cat == 2
# 0    False
# 1     True
# 2    False
# dtype: bool

# %%
"""
This doesn’t work because the categories are not the same:
"""
cat > cat_base2     # ! TypeError: Categoricals can only be compared if 'categories' are the same.
"""
If you want to do a “non-equality” comparison of a categorical series with a list-like object which is not categorical data,
you need to be explicit and convert the categorical data back to the original values:
"""
base = np.array([1, 2, 3])
cat > base  # !TypeError: Cannot compare a Categorical for op __gt__ with type <class 'numpy.ndarray'>.
            # If you want to compare values, use 'np.asarray(cat) <op> other'.

np.asarray(cat) > base      # array([False, False, False])
np.asarray(cat) > np.array([2, 2, 2])  # array([False, False, True])    # not an order of  `cat`
"""
When you compare two unordered categoricals with the same categories, the order is not considered:
"""
c1 = pd.Categorical(["a", "b"], categories=["a", "b"], ordered=False)
c2 = pd.Categorical(["a", "b"], categories=["b", "a"], ordered=False)
c1 == c2
# array([ True,  True])

# %%  # Operations
"""
# Operations

Apart from Series.min(), Series.max() and Series.mode(),
the following operations are possible with categorical data:
"""
# %% 1. Series methods
"""
Series methods like Series.value_counts() will use all categories,
even if some categories are not present in the data:
"""
s = pd.Series(pd.Categorical(["a", "b", "c", "c"], categories=["b", "c", "d", "a"]))

s.value_counts()
# c    2
# a    1
# b    1
# d    0
# Name: count, dtype: int64

# %% [ak]  value_counts & CategoricalIndex
s = pd.Series(pd.Categorical(list("abbbbcc") + [None]*3, categories=["c", "a", "b"], ordered=False))
svc = s.value_counts()
# frequency order
svc
# b    4
# c    2
# a    1
# Name: count, dtype: int64
svc.index   # CategoricalIndex(['b', 'c', 'a'], categories=['c', 'a', 'b'],  ordered=False,  dtype='category')
# categorical index but not ordered !
# yet sorting still possible
svc.sort_index()
svc[s.cat.categories]
# c    2
# a    1
# b    4
s.cat.categories    # Index(['c', 'a', 'b'], dtype='object')
sorted(s.cat.categories)    # ['a', 'b', 'c']
sorted(s.cat.categories, reverse=1)    # ['c', 'b', 'a']
sorted(svc.index)           # ['a', 'b', 'c']

# -------
# for ordered categorical
s = pd.Series(pd.Categorical(list("abbbbcc") + [None]*3, categories=["c", "a", "b"], ordered=True))
s
svc = s.value_counts()
# frequency order – not that of categories (None's are ignored)
svc
# b    4
# c    2
# a    1
# Name: count, dtype: int64
svc[s.cat.categories]
# c    2
# a    1
# b    4
s.value_counts()[s.cat.categories[::-1]]
# but the index is also ordered categorical with order inherited from original

# better use properties of index
svc.index   # !!! CategoricalIndex(['b', 'c', 'a'], categories=['c', 'a', 'b'],  ordered=True,  dtype='category')
svc.sort_index()
# c    2
# a    1
# b    4
# Name: count, dtype: int64
svc.sort_index(ascending=False)
# b    4
# a    1
# c    2
# Name: count, dtype: int64

s.cat.categories    # Index(['c', 'a', 'b'], dtype='object')
sorted(s.cat.categories)    # ['a', 'b', 'c']
sorted(svc.index)           # ['a', 'b', 'c']    even though  ordered=True   !!!


# add NA to categories (see below: # Missing data)
z = s.cat.add_categories(['<NA>']).fillna('<NA>')
# 0       a
# ...
# 9    <NA>
# dtype: category
# Categories (4, object): ['c' < 'a' < 'b' < '<NA>']         !!!  wow  !!!  important  !!!
zvc = z.value_counts()
zvc
# b       4
# <NA>    3
# c       2
# a       1
# Name: count, dtype: int64
zvc.index   # CategoricalIndex(['b', '<NA>', 'c', 'a'], categories=['c', 'a', 'b', '<NA>'], ordered=True, dtype='category')
zvc.sort_index()
# c       2
# a       1
# b       4
# <NA>    3
# Name: count, dtype: int64

zvc3 = zvc[:3]
zvc3
zvc3.index  # CategoricalIndex(['b', '<NA>', 'c'], categories=['c', 'a', 'b', '<NA>'], ordered=True, dtype='category')
zvc3.index.remove_unused_categories()
# CategoricalIndex(['b', '<NA>', 'c'], categories=['c', 'b', '<NA>'], ordered=True, dtype='category')

zvc3.index.to_list() # ['b', '<NA>', 'c']
zvc3.index = zvc3.index.set_categories(['b', 'c', '<NA>'], ordered=True)
zvc3.index  # CategoricalIndex(['b', '<NA>', 'c'], categories=['b', 'c', '<NA>'], ordered=True, dtype='category')
zvc3.sort_index()
# b       4
# c       2
# <NA>    3
# Name: count, dtype: int64

def na_last(xvc: pd.Series, na: str = '<NA>'):
    cats = cats0 = xvc.index.to_list()  # order from series not from index.categories
    if na in cats:
        cats.remove(na)
        cats += [na]
        xvc.index = xvc.index.set_categories(cats)
    return xvc.sort_index()



# %% 2. DataFrame methods
"""
DataFrame methods like DataFrame.sum() also show “unused” categories when observed=False.
"""
columns = pd.Categorical(
    ["One", "One", "Two"], categories=["One", "Two", "Three"], ordered=True
)

df = pd.DataFrame(
    data=[[1, 2, 3], [4, 5, 6]],
    columns=pd.MultiIndex.from_arrays([["A", "B", "B"], columns]),
).T
#        0  1
# A One  1  4
# B One  2  5
#   Two  3  6

df.groupby(level=1, observed=False).sum()
#        0  1
# One    3  9
# Two    3  6
# Three  0  0

"""
Groupby will also show “unused” categories when `observed=False`:
"""
cats = pd.Categorical(
    ["a", "b", "b", "b", "c", "c", "c"], categories=["a", "b", "c", "d"]
)
df = pd.DataFrame({"cats": cats, "values": [1, 2, 2, 2, 3, 4, 5]})
df.groupby("cats", observed=False).mean()
#       values
# cats
# a        1.0
# b        2.0
# c        4.0
# d        NaN

cats2 = pd.Categorical(["a", "a", "b", "b"], categories=["a", "b", "c"])
df2 = pd.DataFrame(
    {
        "cats": cats2,
        "B": ["c", "d", "c", "d"],
        "values": [1, 2, 3, 4],
    }
)
df2
#   cats  B  values
# 0    a  c       1
# 1    a  d       2
# 2    b  c       3
# 3    b  d       4

df2.groupby(["cats", "B"], observed=False).mean()
#         values
# cats B
# a    c     1.0
#      d     2.0
# b    c     3.0
#      d     4.0
# c    c     NaN
#      d     NaN

# %% 3. Pivot tables:

raw_cat = pd.Categorical(["a", "a", "b", "b"], categories=["a", "b", "c"])
df = pd.DataFrame({"A": raw_cat, "B": ["c", "d", "c", "d"], "values": [1, 2, 3, 4]})
df
#    A  B  values
# 0  a  c       1
# 1  a  d       2
# 2  b  c       3
# 3  b  d       4

pd.pivot_table(df, values="values", index=["A", "B"], observed=False)
#      values
# A B
# a c     1.0
#   d     2.0
# b c     3.0
#   d     4.0

# %%  [ak]  crosstab  &  CategoricalIndex
s = np.random.choice(list('abcd'), 33)
s = pd.Series(pd.Categorical(s, categories=list('dacb'), ordered=True))
s
z = np.random.choice(list('pqr'), 33)
z = pd.Series(pd.Categorical(z, categories=list('rpq'), ordered=True))
z
ct = pd.crosstab(s, z)
ct
# col_0  r  p  q
# row_0
# d      4  3  3
# a      3  1  1
# c      4  2  0
# b      4  3  5
ct.index  # CategoricalIndex(['d', 'a', 'c', 'b'], categories=['d', 'a', 'c', 'b'], ordered=True, dtype='category', name='row_0')
ct.columns  # CategoricalIndex(['r', 'p', 'q'], categories=['r', 'p', 'q'], ordered=True, dtype='category', name='col_0'

svc = s.value_counts()
svc     #
# b    12
# d    10
# c     6
# a     5
# Name: count, dtype: int64
# frequency order – not that of categories (None's are ignored)
zvc = z.value_counts()
zvc
# r    15
# p     9
# q     9
# Name: count, dtype: int64
ct0 = ct.loc[svc[:3].index, zvc[:2].index]
ct0
#    r  p
# b  4  3
# d  4  3
# c  4  2
ct0.index   # CategoricalIndex(['b', 'd', 'c'], categories=['d', 'a', 'c', 'b'], ordered=True, dtype='category')
ct0.columns # CategoricalIndex(['r', 'p'], categories=['r', 'p', 'q'], ordered=True, dtype='category')

# %%
....

# %%  # Getting data in/out
"""
# Getting data in/out

You can write data that contains category dtypes to a HDFStore.
See here for an example and caveats: https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5-categorical

It is also possible to write data to and reading data from Stata format files.
See here for an example and caveats: https://pandas.pydata.org/docs/user_guide/io.html#io-stata-categorical

Writing to a CSV file will convert the data, effectively removing any information about the categorical
(categories and ordering).
So if you read back the CSV file you have to convert the relevant columns back to category
and assign the right categories and categories ordering.
"""
import io

s = pd.Series(pd.Categorical(["a", "b", "b", "a", "a", "d"]))
# rename the categories
s = s.cat.rename_categories(["very good", "good", "bad"])
# reorder the categories and add missing categories
s = s.cat.set_categories(["very bad", "bad", "medium", "good", "very good"])

df = pd.DataFrame({"cats": s, "vals": [1, 2, 3, 4, 5, 6]})

csv = io.StringIO()
df.to_csv(csv)

df2 = pd.read_csv(io.StringIO(csv.getvalue()))
df2
df2.dtypes
# Unnamed: 0     int64
# cats          object
# vals           int64
# dtype: object

df2["cats"]
# 0    very good
# 1         good
# 2         good
# 3    very good
# 4    very good
# 5          bad
# Name: cats, dtype: object

# Redo the category
df2["cats"] = df2["cats"].astype("category")
df2["cats"] = df2["cats"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])

df2.dtypes
# Unnamed: 0       int64
# cats          category
# vals             int64
# dtype: object

df2["cats"]
# 0    very good
# 1         good
# 2         good
# 3    very good
# 4    very good
# 5          bad
# Name: cats, dtype: category
# Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']

"""
The same holds for writing to a SQL database with to_sql.
"""

# %%  # Missing data
"""
# Missing data

pandas primarily uses the value np.nan to represent missing data.
It is by default not included in computations.
See the Missing Data section: https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data

Missing values should not be included in the Categorical’s categories, only in the values.
???  Instead, it is understood that NaN is different, and is always a possibility.
When working with the Categorical’s codes, missing values will always have a code of -1.
"""
s = pd.Series(["a", "b", np.nan, "a"], dtype="category")
# only two categories
s
# 0      a
# 1      b
# 2    NaN
# 3      a
# dtype: category
# Categories (2, object): ['a', 'b']

s.cat.codes
# 0    0
# 1    1
# 2   -1
# 3    0
# dtype: int8

"""
Methods for working with missing data, e.g. isna(), fillna(), dropna(), all work normally:
"""
s = pd.Series(["a", "b", np.nan], dtype="category")
s
# 0      a
# 1      b
# 2    NaN
# dtype: category
# Categories (2, object): ['a', 'b']

pd.isna(s)  # or
s.isna()
# 0    False
# 1    False
# 2     True
# dtype: bool

# %%
s.fillna("a")
# 0    a
# 1    b
# 2    a
# dtype: category
# Categories (2, object): ['a', 'b']

# !!! BUT:
s = pd.Series(["a", "b", np.nan, "a"], dtype="category")
s.fillna("c")       # !!! TypeError: Cannot setitem on a Categorical with a new category (c), set the categories first

# one must add category first, e.g.
s = s.cat.add_categories(['<NaN>'])
s = s.fillna("<NaN>")
s

# %%
