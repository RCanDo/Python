#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 09:21:55 2022

@author: arek
"""
#%%
import numpy as np

#%%
"""
for 2d matrix make it 3d by repeating it depth-wise:
a = [[1, 2],
     [3, 4]]
a3 = [[[1,1], [2,2]],
      [[3,3], [4,4]]]
"""
a = np.array([[1, 2], [3, 4]])

# 0. one must first exapnd dims:
a0 = np.expand_dims(a, 2)
a0
# or
np.expand_dims(a, -1)
# or
a[:,:,np.newaxis]
# or
np.reshape(a, (2,2,1))

# 1
a3 = np.r_['2', a0, a0, a0]
a3
# or
np.r_['2,3,0', a, a, a]

# 2
a3 = np.stack(a0, 2)
a3

# 3
a3 = np.tile(a0, (1,1,3))
a3

# in one go (shortest solution)
a3 = np.tile(a[:,:,np.newaxis], (1,1,3))
a3

#%%
