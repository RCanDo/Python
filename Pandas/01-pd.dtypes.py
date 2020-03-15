# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: DataFrame dtypes
subtitle:
version: 1.0
type: examples
keywords: [dtype, DataFrame, np.array, NumPy, Pandas]
description: |
remarks:
    - see also next file  02-negation.py
todo:
sources:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "ex01-pd.dtypes.py"
    path: "D:/ROBOCZY/Python/Pandas/"
    date: 2019-11-24
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
from builtin import flatten, paste
from nppd import data_frame

#%%
"""Conclusion:
Do not use np.array() if not necessary.
np.array() may contain only one type of data so it coerces everything into most general
type, usually 'str' (which is 'object' in pd.DataFrame).
"""

#%%

df = pd.DataFrame([[1, 2], [3, 4]]).add_prefix('V')
df
df.dtypes
"""
V0    int64
V1    int64
dtype: object
"""

df = pd.DataFrame([['a', 2], [3, 4]]).add_prefix('V')
df
df.dtypes
"""
V0    object    == str
V1     int64
dtype: object
"""

df = pd.DataFrame([['a', 2], ['b', 4]]).add_prefix('V')
df
df.dtypes
"""
V0    object    == str
V1     int64
dtype: object
"""

#%% when using np.array()
df = pd.DataFrame(np.array([[1, 2], [2, 4]])).add_prefix('V')
df.dtypes

# ok when using only numbers, BUT

#%% we get into troubles when mixing types
# np.array can contain only one type ('str' is most uiversal):

df = pd.DataFrame(np.array([['a', 2], ['b', 4]])).add_prefix('V')
df
df.dtypes
"""
V0    object
V1    object
dtype: object
"""

# we need to do manual conversions column by column... (no shortcuts!!!)
df['V0'] = df['V0'].astype('str')
df['V1'] = df['V1'].astype('int')

# notice that 'str' is the same as 'object';
# by default everything is 'object' i.e. 'str'.

#%% another way
df = pd.DataFrame(np.array([['a', 2], ['b', 4]])).add_prefix('V')
df['V1'] = pd.to_numeric(df['V1'])
df.dtypes
# NOTICE that there is NO method .to_str() nor .to_object() !!!
df['V1'] = pd.to_str(df['V1'])  #! AttributeError: module 'pandas' has no attribute 'to_str'
df['V1'] = pd.to_object(df['V1'])  #! AttributeError: module 'pandas' has no attribute 'to_object'

#??? So how to convert from 'int' to 'str' ???
# Only using .astype() method of columns (see above).

df = pd.DataFrame(np.array([[1, 2], [2, 4]])).add_prefix('V')
df.dtypes
df['V0'] = df['V0'].astype('str')


#%% sth more complicated

df = pd.DataFrame( [
        ["2000-01-01", 42,  1.5, "x"],
        ["2000-01-02", 49,  0.3, "y"],
        ["2000-01-03", 56, -2.1, "y"]],
       columns=['date', 'nr', 'value', 'label'])
df
df.dtypes
"""
date      object
nr         int64
value    float64
label     object
"""
## so pd.DataFrame inferes data types quite well - the only problem is with dates:
df['data'] = pd.to_datetime(df['date'])
df.dtypes
"""
date             object
nr                int64
value           float64
label            object
data     datetime64[ns]
"""
# the same as
df['data'] = df['date'].astype('datetime64')   #! tricky name!!!

#%% when using np.array() things become more complicated

df = pd.DataFrame(  np.array([
        ["2000-01-01", 42,  1.5, "x"],
        ["2000-01-02", 49,  0.3, "y"],
        ["2000-01-03", 56, -2.1, "y"]]),
       columns=['date', 'nr', 'value', 'label'])
df
df.dtypes
"""
date     object
nr       object
value    object
label    object
"""
# the best way to set the proper types is to write some loop:
types = ['datetime64', 'int', 'float', 'str']
for c, t in zip(df.columns, types):
    df[c] = df[c].astype(t)

df.dtypes
df

#%%
#%% Missing data
#%%
"""
Notice the following problem with NaN.
Create r x c tabe of random integers via np.
and replace some random entries with NaN
"""
r=10; c=3; nnans=7
arr = np.random.randint(0, r*c, (r, c))
arr
arr.dtype

rows = np.random.randint(0, r, (nnans,))
cols = np.random.randint(0, c, (nnans,))

arr[rows, cols] = np.nan  # ValueError: cannot convert float NaN to integer

"""
https://stackoverflow.com/questions/11548005/numpy-or-pandas-keeping-array-type-as-integer-while-having-a-nan-value/11548224
https://pandas.pydata.org/pandas-docs/stable/user_guide/gotchas.html#nan-integer-na-values-and-na-type-promotions
https://pandas.pydata.org/pandas-docs/stable/user_guide/integer_na.html#integer-na
"""
arr = arr.astype("float32")  # float is really not an integer... but there's no choice!
arr[rows, cols] = np.nan   # numpy fancy indexing
arr

#%% pd.DataFrame with NaNs...

#%% way 1. using np.array

df = pd.DataFrame(arr, columns=list('ABC'))
df
df.dtypes  # float32 what is quite innacurate...
# unfortunatelly one cannot change dtypes for all columns at once...
df.dtype = pd.Int16Dtype()
df.dtypes   # no chenges
# only in a loop (see above)

for c in df.columns: df[c] = df[c].astype(pd.Int16Dtype())
df.dtypes
df

#%%
df.iloc[3, 0]  # <NA>
type(df.iloc[3, 0])  # pandas._libs.missing.NAType
df.iloc[3, 0].dtype  # 'NAType' object has no attribute 'dtype'
dir(df.iloc[3, 0])   # only hiddens

dir(pd._libs.missing)

#%% at defnition

#! this didn't work but now it works!
df = pd.DataFrame(arr, dtype='Int16')
# old:  #! ValueError: failed to cast to 'Int16' (Exception was: data type not understood)
df
df.dtypes

# more canonic form
df = pd.DataFrame(arr, dtype=pd.Int16Dtype())
df
df.dtypes

#%% way 2. column by column
df = pd.DataFrame(
        {'A': pd.Series(np.random.randint(0, 100, 10), dtype=pd.Int16Dtype()),
         'B': pd.Series(np.random.randint(0, 100, 10), dtype=pd.Int16Dtype()),
         'C': pd.Series(np.random.randint(0, 100, 10), dtype=pd.Int16Dtype())
        })
df
df.dtypes

df.iloc[rows, cols] = np.nan
df
#! ooops... It doesn't work like numpy fancy indexing
# let's recreate the matrix, and run sth more traditional

for r, c in zip(rows, cols): df.iloc[r, c] = np.nan
df
#OK

#%%


