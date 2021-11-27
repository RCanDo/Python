#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Outliers detection
subtitle:
version: 1.0
type: tutorial
keywords: [outliers, Z-score, IQR]
description: |
remarks:
todo:
sources:
    - title: Ways to Detect and Remove the Outliers
      chapter:
      pages:
      link: https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
      date: 2018-05-22
      authors:
          - nick:
            fullname: Natasha Sharma
            email:
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: outliers.py
    path: E:/ROBOCZY/Python/ML/
    date: 2021-11-03
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%%
import numpy as np
import pandas as pd

import sklearn.datasets as sd

import matplotlib.pyplot as plt
import seaborn as sb

#%%
boston = sd.load_boston()    #! DEPRECATED: load_boston is deprecated in 1.0 and will be removed in 1.2
dir(boston)
boston.data     # np.array
boston.target   # np.array

#create the dataframe
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
boston_df.shape # (506, 13)
boston_df.head()

#%%
sb.boxplot(x=boston_df['DIS'])

#%%
fig, ax = plt.subplots()
ax.scatter(boston_df['INDUS'], boston_df['TAX'])
ax.set_xlabel('INDUS')
ax.set_ylabel('TAX')

#%% Z-Score
"""
The Z-score is the signed number of standard deviations
by which the value of an observation or data point
is above the mean value of what is being observed or measured.
"""
from scipy.stats import zscore
zz = zscore(boston_df)
zz.shape   # (506, 13)   np.array
zz

zz = np.abs(zscore(boston_df))

threshold = 3
where = np.where(zz > 3)
where
# first array is for rows, second is for columns

zz[where]   # see NumPy fancy indexing

#%% IQR score
Q1 = boston_df.quantile(.25)
Q3 = boston_df.quantile(.75)
IQR = Q3 - Q1
IQR

(boston_df < (Q1 - 1.5 * IQR)) | (boston_df > (Q3 + 1.5 * IQR))

#%%
#%% removing outliers
boston_df_1 = boston_df[ (zz < 3).all(axis=1) ]
boston_df_1.shape       # (415, 13)

#%%


#%%


#%%


#%%