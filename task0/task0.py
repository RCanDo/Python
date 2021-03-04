#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:35:48 2021

@author: arek
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/task0/")
print(os.getcwd())

# %%
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 500)
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

pd.set_option('display.large_repr', 'truncate')

pd.set_option('display.precision', 3)

#%%

data = pd.read_csv("recruitment_task.csv")
data.head()
data.shape    # 150000, 48
data.columns

data.info()
"""
Only first five columns are not 'sparse'
('sparse' in the meaning of having majority of NULLs)
"""

data.count()

#%%
"""
It's easy here to set the 'sparsity' threshold 
"""
def columns_sparsity(df, threshold=.5):
    sparse_cols = df.apply(lambda col: col.isnull().sum() > df.shape[0] * threshold)
    sparse_cols = sparse_cols.index[sparse_cols].tolist()
    dense_cols = df.columns.difference(sparse_cols).tolist()
    return dense_cols, sparse_cols

dense_cols, sparse_cols = columns_sparsity(data)
print(dense_cols)
print(sparse_cols)

#%%
data.dtypes[dense_cols]
data.dtypes[sparse_cols]

#%%
data[dense_cols].count() 

from sklearn.impute import SimpleImputer
data[dense_cols] = SimpleImputer(strategy="constant", fill_value="NA").fit_transform(data[dense_cols])

for n, c in data.iloc[:,0:3].iteritems(): print("{:s} : ".format(n)); print(c.value_counts())

data.memory_usage().sum() / 1e6   ## 57.6 MB

#%%
#%% plots
group = data.iloc[:, 0]
plt.hist(group)
 
x1 = data.iloc[:, 1]
plt.hist(x1)

plt.hist([x1[group=="A"], x1[group=="B"]], histtype="bar")

plt.bar(data.iloc[:, 1])

#%%
gdata = data.groupby('group')
gdc1 = gdata.f1.value_counts()
gdc1[("A")]
gdc1[("B")]

plt.hist([gdc1[("A")], gdc1[("B")]], histtype='bar')

#%%
import plotly.express as px

#%%
x2 = data.iloc[:, 2]
plt.hist(x2[x2.notna()]) 

#%%

x3 = data.iloc[:, 3]
plt.plot(x3)
plt.hist(x3, bins=50)
plt.hist(x3[x3<50], bins=50)
plt.boxplot(x3)

x4 = data.iloc[:, 4]
plt.hist(x4, bins=100)
plt.hist(x4[x4<2e5], bins=100)
plt.boxplot(data.iloc[:, 4])

## END PLOTS

#%%
#%%
sdata = data[sparse_cols]
sdata_fsum = sdata.notna().sum(axis=1)
sdata_fsum.count()
sdata_fsum.value_counts()
sdata_fsum.value_counts()/sdata.shape[0]

#%%
(sdata < 0).sum(axis=0).sum()     # 0
(sdata == 0).sum(axis=0).sum()    # 0
(sdata > 0).sum(axis=0).sum()     # 150622

#%%
"""
## removing cases with two 'factor levels'
data2 = data1.loc[data_fsum==1,:]
data2.notna().sum(axis=1).value_counts()   ## OK
"""

#%%

data2 = data[dense_cols].copy()
data2['factor'] = sdata.apply(lambda r: r.index[r.notna()][0], axis=1)
data2['value'] = sdata.apply(lambda r: r[r.notna()][0], axis=1)
data2.head()

data2.memory_usage().sum() / 1e6   ## 8.4 MB

data_oh = pd.get_dummies(data2, columns=['f0', 'f1', 'factor'])
data_oh.columns
data_oh.shape


#%%
#%%


#%%



#%%



#%%



#%%



#%%

