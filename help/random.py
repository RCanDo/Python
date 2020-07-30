# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:27:25 2018

@author: kasprark


random examples
"""
#%%
import numpy as np

#%%


np.random.normal(50, 5, size=1000)

np.random.randn(8, 4)
np.random.rand(5)
np.random.rand(5, 5)
np.random.randint(-5, 5)
[ str(x) for x in np.random.choice( range(1980,2000), size=100, replace=True ) ]


#%%

x_sub, y_sub = zip(*np.random.sample(list(zip([1, 2, 3], [-1, -2, -3])), 2))

x_sub
y_sub

#%%

arr = [1,1,2,2,3,3]
np.random.shuffle(arr)   #!!! in place !!!
arr

arr = [1,1,2,2,3,3]
np.random.permutation(arr)   #! returns value ! OK!
arr

#%%
dir(np.random)

help(np.random.random_sample)

#%%
help(np.random.choice)

np.random.choice(list('abc'), 10, replace=True)
np.random.choice(['s1', 's2', 's3'], 10, replace=True)


#%%




#%%



