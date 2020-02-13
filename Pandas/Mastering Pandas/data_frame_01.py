# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:01:49 2019

@author: kasprark
"""

import numpy as np
import pandas as pd

#%%

data0 = {'a':[0, 1, 3], 'b':[1, 0.1, 0.01], 'c':[10, 12, 34]}
idx0 = ['2013-Q1', '2013-Q2', '2013-Q3']
df0 = pd.DataFrame(data0, idx0)
df0

#%% this have different output:
data1 = {'a':{0, 1, 3}, 'b':{1, 0.1, 0.01}, 'c':{10, 12, 34}}
#idx1 = {'2013-Q1', '2013-Q2', '2013-Q3'}
idx1 = ['2013-Q1', '2013-Q2', '2013-Q3']
df1 = pd.DataFrame(data1, idx1)
df1

#%% but (very tedious...)
data2 = {'a':{'2013-Q1':0, '2013-Q2':1, '2013-Q3':3}, 
         'b':{'2013-Q1':1, '2013-Q2':0.1, '2013-Q3':0.01}, 
         'c':{'2013-Q1':10, '2013-Q2':12, '2013-Q3':34}}
df2 = pd.DataFrame(data2)
df2

#%%

df0 == df2

#%%

data3 = {'idx': ['2013-Q1', '2013-Q2', '2013-Q3'], 'a':[0, 1, 3], 'b':[1, 0.1, 0.01], 'c':[10, 12, 34]}
df3 = pd.DataFrame(data3)
df3.set_index('idx')          # NOT IN PLACE!!!
df3
df3 = df3.set_index('idx')
df3

#%%



