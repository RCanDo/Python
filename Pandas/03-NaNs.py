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
import math as m

# %%
                    None  |  float('nan')  |  np.nan  |  pd.NA  |  float('inf')  |  np.inf  |   ""
                             float('NaN')     np.NaN
                             float('NAN')     np.NAN

np.isnan            ERR!!!    True             True       <NA>      False            False     ERR!!!
np.isinf            ERR!      False            False      <NA>      True             True      ERR!
np.isfinite         ERR!      False            False      <NA>      False            False     ERR!
# math has exactly the same functionality as numpy i.e. one may substitute  m. for np. everywhere
# pandas
pd.isna             True      True             True       True      False            False     False
pd.isnull           True      True             True       True      False            False     False
pd.notna            False     False            False      False     True             True      True
pd.notnull          False     False            False      False     True             True      True

np.isnan("qq")  # ! TypeError: ufunc 'isnan' not supported for the input types,
            # and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

#%% Python's None (serving as NULL in e.g. SQL -- NO!!!)

None
type(None)    # NoneType

# None is singleton:
None == None  # True
None is None  # True

a = None
a is None     # True
a == None     # True

#!!! hence it is NOT like NULL !!!

#%% Python's NaN is a float !!! -- it's almost like NULL in SQL

nn = float('nan')
type(nn)  # float

# aliases
float('NaN')
float('NAN')

# nan is NOT singleton
nn is float('nan')  # False

# moreover it is NOT equal to itself!
nn == nn           # False  -- like NULL
nn != nn           # True   -- NOT like NULL
nn is nn           # True

# use  math  module to check for Python's NaN
m.isnan(nn)    # True
# or  numpy
np.isnan(nn)   # True

# %% BUT
# !!!  the most DANGEROUS AND ANNOYING THING:
m.isnan(a)     # ! TypeError: must be real number, not NoneType
np.isnan(a)    # ! TypeError: ufunc 'isnan' not supported for the input types,
            # and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''

# !!!  moreover, there is not way in  numpy  or  math  for checking for  pure Pythons'  None
m.isnull(a)    # ! AttributeError: module 'math' has no attribute 'isnull'
np.isnull(a)   # ! AttributeError: module 'numpy' has no attribute 'isnull'
# i.e.
# !!! there is NO  np.isnull()  or  math.isnull()

# %% in Pandas
pd.isnan(nn)   # ! AttributeError: module 'pandas' has no attribute 'isnan'

pd.isna(nn)    # True  !!!
pd.isnull(nn)  # True           there is NO  np.isnull()  or  math.isnull()

pd.isna(a)     # True
pd.isnull(a)   # True

# moreover
pd.notna(nn)    # False
pd.notnull(nn)  # False

pd.notna(a)     # False
pd.notnull(a)   # False

#%%
#%% np.nan

np.nan          # nan
type(np.nan)    # float
# aliases
np.NaN
np.NAN

npnan = np.nan

# np.nan is NOT singleton
npnan == npnan   # False !
# but almost
npnan is np.nan   # True
npnan is npnan   # True

npnan == nn      # False
npnan is nn      # False

np.isnan(npnan)  # True
m.isnan(npnan)   # True

np.isinf(npnan)  # False
np.isfinite(npnan)  # false
# more on inf below

# %% math.nan
m.nan           # nan
type(m.nan)     # float

# this is NOT the same thing as np.nan (also not a singleton)
np.nan is m.nan     # False
np.nan == m.nan     # False
m.nan == nn     # False

# but serves exactly the same way
# ...

# %%
# !!!  there is no Pandas nan
pd.nan  # ! AttributeError: module 'pandas' has no attribute 'nan'

# but there are all necessary utils for checking nans and None !:
pd.isnull(None)  # True
pd.isnull(a)     # True
pd.isnull(nn)    # True
pd.isnull(npnan)    # True !!!

pd.isna(None)

# and there is
pd.NA            # <NA>
type(pd.NA)      # pandas._libs.missing.NAType
# in pd.Series  it works as  np.nan
# see below


# %%
# %%  infinity

z = float('inf')
type(z)     # float

# it's singleton
z == z  # True
z is z  # True

m.isinf(z)      # True
m.isfinite(z)   # False

np.isinf(z)         # True
np.isfinite(z)      # False

# %% in  Pandas  no utils for  infinity
pd.isinf(z)         #! AttributeError: module 'pandas' has no attribute 'isinf'
pd.isfinite(z)      #! AttributeError: module 'pandas' has no attribute 'isinf'

#%% there is also math's infinity
m.inf       # inf
m.log(0)    #! ValueError: math domain error  ... WHY NOT -inf ???
infty = m.inf
type(infty)     # float

# and numpy infinity
np.inf      # inf
# ! but NO Pandas infinity
pd.inf      # ! AttributeError: module 'pandas' has no attribute 'inf'

# singleton
infty == infty   # True
infty == m.inf   # True
infty is m.inf   # True
# math and numpy infinity are the same thing
m.inf == np.inf  # True

m.isinf(infty)   # True
m.isnan(infty)   # False

# %%
m.isinf(a)        #! TypeError: must be real number, not NoneType
m.isinf(nn)        # False  !!! NaN is NOT finite and NOT infinite !!!
m.isinf(infty)     # True

m.isfinite(a)     #! TypeError: must be real number, not NoneType
m.isfinite(nn)     # False  !!! NaN is NOT finite and NOT infinite !!!
m.isfinite(infty)  # False

#%% the same things in numpy

np.isnan(a)   #! TypeError: ...
np.isnan(nn)  # True
np.isnan(infty)  # False

np.isinf(a)      #! TypeError: ...
np.isinf(nn)     # False
np.isinf(infty)  # True

np.isfinite(a)    #! TypeError: ...
np.isfinite(nn)    # False
np.isfinite(infty) # False

# %% in pandas
pd.isna(a)       # True
pd.isna(nn)      # True
pd.isna(infty)   # False

pd.isnull(infty) # False

# %%
# %%


#%%
#%%
ss = pd.Series(range(3), dtype=int)
ss

ss[0] = None  # turned to NaN
ss            # dtype: float64
ss[0]         # nan
type(ss[0])   # numpy.float64

#%%
ss = pd.Series([True, False, True])
ss  # dtype: bool   OK

ss[0] = None    # turned to  ...  !!!
ss
# 0      NaN        !
# 1    False
# 2     True
# dtype: object     !!!    BUT NOT a string

ss[0]   # nan
type(ss[0])     # float
ss[1]
type(ss[1])     # bool

ss.isnull()
# 0     True
# 1    False
# 2    False
# dtype: bool
ss.notnull()

ss.isna()
# 0     True
# 1    False
# 2    False
# dtype: bool

ss[1] = np.nan
# 0     NaN
# 1     NaN
# 2    True
# dtype: object       !!!

#%%
ss = pd.Series([True, False, True])
ss

ss[0] = pd.NA
ss
# 0      NaN        !!!  it's NOT <NA> i.e. pandas._libs.missing.NAType; see below
# 1    False
# 2     True
# dtype: object     !!!
ss[0]   # nan
type(ss[0])     # float

ss.isna()
ss.notna()

#%%
# np.array() with NaNs see below

#%%
ss = pd.Series([True, False, None, float('nan'), pd.NA])  # object!
ss
# 0     True
# 1    False
# 2     None
# 3      NaN
# 4     <NA>            !!!  it's not just  NaN  as above; i.e. it's now proper  pandas._libs.missing.NAType
# dtype: object

type(ss[0])  # bool
type(ss[2])  # NoneType
type(ss[3])  # float
type(ss[4])  # pandas._libs.missing.NAType

ss[2] == None  # True
m.isnan(ss[2]) # ! TypeError: must be real number, not NoneType
m.isnan(ss[3]) # True
m.isnan(ss[4]) # ! TypeError: must be real number, not NAType

np.isnan(ss[2]) # !!! TypeError: ufunc 'isnan' not supported for the input types,
            # and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
np.isnan(ss[3]) # True
np.isnan(ss[4]) # <NA>

pd.isna(ss[2]) # True
pd.isna(ss[3]) # True
pd.isna(ss[4]) # True

pd.isnull(ss[2]) # True
pd.isnull(ss[3]) # True
pd.isnull(ss[4]) # True

ssu = ss.unique()
ssu     # array([True, False, None, nan, <NA>], dtype=object)
type(ssu[2])  # NoneType
type(ssu[3])  # float
type(ssu[4])  # pandas._libs.missing.NAType

ss.value_counts()
# True     1
# False    1
# Name: count, dtype: int64
ss.value_counts(dropna=False)  # !!! no good... :
# True     1
# False    1
# None     1
# NaN      1
# <NA>     1
# Name: count, dtype: int64

#%% !!!
ss.unique(dropna=False)  # TypeError: unique() got an unexpected keyword argument 'dropna'
#??? HOW TO GET UNIQUES WITHOUT NANs ???
ss.unique()
# array([True, False, None], dtype=object)
ss.value_counts().index.values


# %% !!!  DO NOT CAST in advance  !!!
pd.Series([True, False, pd.NA, pd.NA]).astype('bool')  # ! TypeError: boolean value of NA is ambiguous
pd.Series([True, False, pd.NA, pd.NA]).astype('int')   # ! TypeError: int() argument must be a string, a bytes-like object or a number, not 'NAType'

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
#%% Missing data in Pandas
#%%
"""
Notice the following problem with NaN.
Create r x c tabe of random integers via np.
and replace some random entries with NaN
"""
np.random.seed(3)
r=10; c=3; nnans=7
arr = np.random.randint(0, r*c, (r, c))
arr
arr.dtype   # dtype('int64')

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
# array([[10., 24., 25.],
#        [nan, 24.,  8.],
#           ...
#        [24., nan, nan],
#        [26., 22.,  2.]], dtype=float32)


#%% pd.DataFrame with NaNs...

#%% way 1. using np.array

df = pd.DataFrame(arr, columns=list('ABC'))
df
#       A     B     C
# 0  10.0  24.0  25.0
# 1   NaN  24.0   8.0
#       ...
# 8  24.0   NaN   NaN
# 9  26.0  22.0   2.0

df.dtypes  # float32  what is quite innacurate...
# unfortunatelly one cannot change dtypes for all columns at once...
df.dtype = pd.Int16Dtype()
df.dtypes   # no chenges
# only in a loop (see above)

for c in df.columns: df[c] = df[c].astype(pd.Int16Dtype())
df.dtypes   # Int16   ok
df
#       A     B     C
# 0    10    24    25
# 1  <NA>    24     8
#       ...
# 8    24  <NA>  <NA>
# 9    26    22     2

#%%
df.iloc[1, 0]  # <NA>
type(df.iloc[1, 0])  # pandas._libs.missing.NAType
df.iloc[1, 0].dtype  # 'NAType' object has no attribute 'dtype'
dir(df.iloc[1, 0])   # only hiddens

# %%  all Pandas "missing" types  !!!
dir(pd._libs.missing)

#%% at defnition

#! this didn't work but now it works!
df = pd.DataFrame(arr, columns=list('ABC'), dtype='Int16')
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

df = pd.DataFrame(arr, columns=list('ABC'), dtype='int')  # works BUT
df.dtypes   # int32  -- Pandas type  not Python's int

# MOREOVER
df = pd.DataFrame(arr, columns=list('ABC'))
df.dtypes   # float32
# which we cannot change this way:
for c in df.columns: df[c] = df[c].astype(int)  #! ValueError: Cannot convert non-finite values (NA or inf) to integer
# only this
for c in df.columns: df[c] = df[c].astype(pd.Int16Dtype())
df.dtypes   # int16

#%% way 2. column by column
df = pd.DataFrame(
        {'A': pd.Series(np.random.randint(0, 100, 10), dtype=pd.Int16Dtype()),
         'B': pd.Series(np.random.randint(0, 100, 10), dtype=pd.Int16Dtype()),
         'C': pd.Series(np.random.randint(0, 100, 10), dtype=pd.Int16Dtype()),
        })
df

#%%
df.dtypes

df.iloc[rows, cols] = np.nan
df
#! ooops... It doesn't work like numpy fancy indexing

# let's recreate the matrix, and run sth more traditional

for r, c in zip(rows, cols): df.iloc[r, c] = np.nan
df
#OK
df.dtypes   # int16
# Notice that all columns remains int16 while we substituted np.nan which is float.
type(df.iloc[1, 0])   # pandas._libs.missing.NAType

# recreate df and try:
for r, c in zip(rows, cols): df.iloc[r, c] = float('nan')
df
#OK
df.dtypes
# as above!
# It's good but nevertheless there is huge mess with NaNs in Python/NumPy/Pandas

# recreate again:
for r, c in zip(rows, cols): df.iloc[r, c] = None
df
#OK
df.dtypes

#%%


#%%
data0 = pd.read_csv('~/Projects/Kaggle/IEEE-CIS_Fraud_Detection/data/train_transaction.csv')

#%%
import math

math.isnan(data0['M1'][1])
math.isnan(data0['M1'])

data0['M1']

set(data0['M1'].unique()) == {'T', 'F', np.nan}   # True

