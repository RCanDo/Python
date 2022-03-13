#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:47:51 2022

@author: arek
"""
#%%
import numpy as np
import pandas as pd
df1 = pd.DataFrame({'a': np.random.randint(9, size=9), 'b': np.random.randint(9, size=9)},
                   index = np.random.choice(16, 9, replace=False))
df2 = pd.DataFrame({'c': np.random.randint(9, size=9), 'd': np.random.randint(9, size=9)},
                   index = np.random.choice(16, 9, replace=False))
df1
df2

#%%
pd.concat([df1, df2])
pd.concat([df1, df2], ignore_index=True)

pd.concat([df1, df2], axis=1)
pd.concat([df1, df2], axis=1, ignore_index=True)
pd.concat([df1, df2])

#%%
