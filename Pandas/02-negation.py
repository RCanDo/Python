# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Negation in numpy and pandas
subtitle:
version: 1.0
type: examples
keywords: [negation, bool, dtype, DataFrame, pd.Series, np.array, NumPy, Pandas]
description: |
remarks:
todo:
sources:
    - title:
      link: https://stackoverflow.com/questions/15998188/how-can-i-obtain-the-element-wise-logical-not-of-a-pandas-series
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "02-negation.py"
    path: "D:/ROBOCZY/Python/Pandas/"
    date: 2020-03-14
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
              - akasp666@google.com
"""

#%%
import numpy as np
import pandas as pd

#%%
s = pd.Series([True, True, False, True])
s
~s
-s
np.invert(s)
pd.np.invert(s)

#%%
%timeit ~s
# 84.5 µs ± 2.06 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%timeit (-s)
# 93.8 µs ± 907 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

%timeit np.invert(s)
# 105 µs ± 1.65 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

#%% in numpy

arr = np.array([True, False, True])
arr
np.invert(arr)
~arr  # ok

-arr  #! TypeError: The numpy boolean negative, the `-` operator, is not supported,
      # use the `~` operator or the logical_not function instead.

np.invert([True, False, True])
np.invert((True, False, True))
np.invert({True, False, True})   #! TypeError: bad operand type for unary ~: 'set'

#%%
df = pd.DataFrame({'A':[True, False, False], 'B':[True, False, True]})
df.dtypes

~df
-df
np.invert(df)
pd.np.invert(df)

#%% beware of NaNs
"""
just wanted to add a warning that your mask needs to be dtype 'bool', not 'object'.
Ie your mask can't have ever had any nan's. !!!
See here - even if your mask is nan-free now, it will remain 'object' type.

The inverse of an 'object' series won't throw an error,
instead you'll get a garbage mask of ints that won't work as you expect.
"""
df = pd.DataFrame({'A':[True, False, np.nan], 'B':[True, False, True]})
df.dtypes
~df['A']      #! TypeError: bad operand type for unary ~: 'float'

df.dropna(inplace=True)
df.dtypes
~df['A']      #! no error but col A is still object==string hence ~ gives int...

df['A'].astype('bool')
~df['A'].astype('bool')

df['A'].astype('int')
~df['A'].astype('int')  # what we have already seen


#%% beware of strange behaviour of  pd.to_numeric()
df
df.dtypes

pd.to_numeric(df['A'])  # bool! ???
~pd.to_numeric(df['A'])  # OK but strange way
# it' better to use .astype(col)

pd.to_numeric(pd.to_numeric(df['A']))   # bool! ???
# so you cannot cast bool to numeric using pd.to_numeric() ...
pd.to_numeric(df['B'])  # bool! ???

# USE .astype()  !!!

#%%



#%%



#%%



#%%