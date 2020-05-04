# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: cut() and qcut()
subtitle:
version: 1.0
type: help examples
keywords: [cut, binning, Pandas, NumPy]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: pandas.cut
      link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html#pandas.cut
      usage: |
          not only copy
    - title:
      link:
"""


#%%
from rcando.ak.builtin import flatten, paste
from rcando.ak.nppd import data_frame
import os

PYWORKS = "D:/ROBOCZY/Python/Pandas"
# PYWORKS = "/home/arek/Works/Python/Pandas"

os.chdir(PYWORKS + "/User Guide/")
print(os.getcwd())


#%%
import numpy as np
import pandas as pd

#%%
pd.cut(x = [1, 2, 0, 4, 8, 2, 4, 0, -2],   # array-like
       bins = 3,        # [-3, 0, 3, 6, 10] / pd.IntervalIndex
       right = True,    # right closed?
       labels = None,   # array / False
       retbins = False, # bool  Whether to return the bins or not.
                        # Useful when bins is provided as a scalar.
       precision = 3,   # The precision at which to store and display the bins labels.
       include_lowest = False,  # bool  Whether the first interval should be left-inclusive or not.
       duplicates = 'raise'  # 'drop'  If bin edges are not unique, raise ValueError or drop non-uniques.
       )

#%% Examples
# Discretize into three equal-sized bins.

c = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)
c
c.categories
dir(c)
type(c)   # pandas.core.arrays.categorical.Categorical

c = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3, retbins=True)
c
type(c)   # tuple !!!
c[0]
c[1]  # array([0.994, 3., 5., 7.])   -- bins


pd.cut([0, 10], 10, retbins=True, include_lowest=True)[1]
# array([-0.01,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])

# Discovers the same bins, but assign them specific labels.
# Notice that the returned Categorical’s categories are labels and is ordered.
c = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3, labels=["bad", "medium", "good"])
c
# [bad, good, medium, medium, good, bad]
# Categories (3, object): [bad < medium < good]
type(c)   # pandas.core.arrays.categorical.Categorical

# labels=False  returns respective bin for every data point
pd.cut([1, 7, 5, 4, 6, 3], bins=3, labels=False)
# array([0, 2, 1, 1, 2, 0], dtype=int64)

# Passing a Series as an input returns a Series with categorical dtype:
s = pd.Series(np.array([2, 4, 6, 8, 10]))
pd.cut(s, 3)
# pd.Series,  dtype: category

s = pd.Series(np.array([2, 4, 6, 8, 10]), index=['a', 'b', 'c', 'd', 'e'])
pd.cut(s, 3)

# Passing a Series as an input returns a Series with mapping value.
# It is used to map numerically to intervals based on bins.

s = pd.Series(np.array([2, 4, 6, 8, 10]), index=['a', 'b', 'c', 'd', 'e'])

pd.cut(s, [0, 2, 4, 6, 8, 10])
pd.cut(s, [0, 2, 4, 6, 8, 10], labels=False)
pd.cut(s, [0, 2, 4, 6, 8, 10], labels=False, retbins=True)
# dtype: int64
pd.cut(s, [0, 2, 4, 6, 8, 10], labels=False, retbins=True, right=False)
# dtype: float64

# Use  duplicates='drop'  when bins is not unique
pd.cut(s, [0, 2, 4, 6, 10, 10], labels=False, retbins=True,
       right=False, duplicates='drop')

# Passing an IntervalIndex for bins results in those categories exactly.
# Notice that values not covered by the IntervalIndex are set to NaN.
# 0 is to the left of the first bin (which is closed on the right),
# and 1.5 falls between two bins.

bins = pd.IntervalIndex.from_tuples([(0, 1), (2, 3), (4, 5)])
pd.cut([0, 0.5, 1.5, 2.5, 4.5], bins)

#%%
#%%
pd.qcut(x,
        q,  # int - nr of quantiles; list-like of quantiles;
        labels,
        retbins,
        precision,
        deplicates
       )

#%%
pd.qcut(range(5), 4)
pd.qcut(range(5), 4, retbins=True)
pd.qcut(range(5), 3, retbins=True)

pd.qcut(range(5), 3, labels=["good", "medium", "bad"])

pd.qcut(range(5), 4, labels=False)  # numpy.ndarray

#%%
qq = pd.qcut(np.random.randn(100), 10)
dir(qq)
qq.value_counts()

pd.qcut(np.random.randn(1000), 10).value_counts()


#%%

