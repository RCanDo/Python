# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:48:00 2018

@author: kasprark
"""

%lsmagic

ll = list(range(5))
ll
ll2 = ll
ll2[2] = 5
ll

import numpy as np

a = np.array([1,2,3])
a
a.shape
a.T
np.shape(a.T)

a = np.array([[1,2,3]])
a
a.shape
a.T
a.T.shape

#%% 
a = 4
b=a
b

b=5
b
a

#%% but

a = [1,3,5]
b = a
b

b[1] = 0
b
a

#%%

a = (1,3,5)
b = a
b

b[1] = 0    ## TypeError: 'tuple' object does not support item assignment

#%%
import math
"%30.29f" % math.e
"%.29f" % math.e

"{:.30f}".format(np.e)
"{:.29f}".format(np.pi)

#%%
import pandas as pd
pd.read_csv()

#%%
np.random.normal(size=10)
list(np.random.normal(size=10))
pd.Series(np.random.normal(size=10))

import random as rnd
rnd.gauss(0,1)
rnd.normalvariate(0,1)

#%%
np.arange(5)

