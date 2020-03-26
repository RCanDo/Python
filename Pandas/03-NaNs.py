# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Missing values in Pandas and NumPy
subtitle:
version: 1.0
type: examples
keywords: [missing values, NaN, dtype, DataFrame, pd.Series, np.array, NumPy, Pandas]
description: |
    - there are lot of types of NaNs in python/pandas/numpy/...
    - pd.Series' logical cannot have NaNs !!!
    - such series is type-casted to 'object' i.e. 'str'
remarks:
todo:
sources:
    - title: Assigning a variable NaN in python without numpy
      link: https://stackoverflow.com/questions/19374254/assigning-a-variable-nan-in-python-without-numpy
    - title: Working with missing data [Pandas User Guide]
      link: https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
    - title: Handling Missing Data [Python Data Science Handbook]
      link: https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html
    - title:
      link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "03-NaNs.py"
    path: "~/Works/Python/Pandas/"
    date: 2020-03-24
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import numpy as np
import pandas as pd
import math

#%%
ss = pd.Series([True, False, None])
ss   # object !?!?!? but it's not a string!

type(ss[0])  # bool
type(ss[2])  # NoneType
ss[2] == None  # True

ssu = ss.unique()
ssu  # object
type(ssu[0]) # bool
type(ssu[2]) # NoneType

ss.value_counts(dropna=False)  # !!! no good...

#%%
ss = pd.Series([True, False, None, float('nan'), pd.NA])  # object!
ss  # object
type(ss[0])  # bool
type(ss[2])  # NoneType
type(ss[3])  # float
type(ss[4])  # pandas._libs.missing.NAType

ss[2] == None  # True
math.isnan(ss[3]) # True
math.isnan(ss[4]) # TypeError: must be real number, not NAType

ssu = ss.unique()
ssu
type(ssu[2])  # NoneType
type(ssu[3])  # float
type(ssu[4])  # pandas._libs.missing.NAType

ss.value_counts()
ss.value_counts(dropna=False)  # !!! no good... :
# True     3
# True     1
# False    1
# dtype: int64

#%% !!!
ss.unique(dropna=False)  # TypeError: unique() got an unexpected keyword argument 'dropna'
#??? HOW TO GET UNIQUES WITHOUT NANs ???
ss.unique()


#%%

pd.Series([True, False, pd.NA, pd.NA]).value_counts(dropna=False)
pd.Series([True, False, pd.NA, pd.NA]).astype('bool')  # TypeError: boolean value of NA is ambiguous
pd.Series([True, False, pd.NA, pd.NA]).astype('int')   # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NAType'

ss = pd.Series([True, False, pd.NA, pd.NA]).astype('str')
ss           # object
type(ss[0])  # str
type(ss[1])  # str
type(ss[2])  # str
type(ss[3])  # str

# so it was cast to 'str' and all elements are 'str' but it's 'object'...

#%%
ss = pd.Series([0, 1, 1, 0, pd.NA])
ss            # object
ss.dtype      # dtype('O')
type(ss)      # pandas.core.series.Series
type(ss[0])   # int
type(ss[1])   # int
type(ss[4])   # pandas._libs.missing.NAType

np.where(ss == 0)

ss.astype('object') == 1   # ok

#%%
data0 = pd.read_csv('~/Projects/Kaggle/IEEE-CIS_Fraud_Detection/data/train_transaction.csv')

#%%
import math

math.isnan(data0['M1'][1])
math.isnan(data0['M1'])

data0['M1']

set(data0['M1'].unique()) == {'T', 'F', np.nan}   # True



#%%



#%%
#%% Missing data in Pandas
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
df.iloc[1, 0]  # <NA>
type(df.iloc[1, 0])  # pandas._libs.missing.NAType
df.iloc[1, 0].dtype  # 'NAType' object has no attribute 'dtype'
dir(df.iloc[1, 0])   # only hiddens

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

#%% notice that one must use native Pandas integer type  `pd.Int16Dtype()`;
# Python's `int` is not allowed, for the same reason as above:
# NaNs are `float`s in basic Python as in NumPy (see `03-NaNs.py`):
df = pd.DataFrame(arr, columns=list('ABC'))
df
df.dtypes

for c in df.columns: df[c] = df[c].astype(int)  # ValueError: Cannot convert non-finite values (NA or inf) to integer


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
df.dtypes
# Notice that all columns remains int16 while we substituted np.nan which is float.
type(df.iloc[1, 0])   # pandas._libs.missing.NAType

# recreate df and try:
for r, c in zip(rows, cols): df.iloc[r, c] = float('nan')
df
#OK
df.dtypes
# as above!
# It's good but nevertheless there is huge mess with NaNs in Python/NumPy/Pandas

#%%


