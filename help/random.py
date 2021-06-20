#! python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:27:25 2018

@author: kasprark

random examples
"""


#%%
import numpy as np

#%%
dir(np.random)

help(np.random.random_sample)
# Return random floats in the half-open interval [0.0, 1.0).
np.random.random_sample()
np.random.sample()             # just alias !
np.random.sample(5)
np.random.sample((5,))
np.random.sample((5,3))

# from interval [3, 5)
(5 - 3)*np.random.sample((5,3)) + 3

#! another alias !
np.random.rand(5)
np.random.rand(5, 3)
# but little different
np.random.sample(5,3)         #! ERROR


#%%
# random samples from a normal (Gaussian) distribution.
np.random.normal(10, 5, size=10)

# sample (or samples) from the "standard_normal" distribution.
np.random.randn(8, 4)

np.random.randint(-5, 5)
[ str(x) for x in np.random.choice( range(1980,2000), size=100, replace=True ) ]

#%%
# Generate a non-uniform random sample from np.arange(5) of size 3 without replacement:
np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])

np.random.choice(list('abcde'), 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])


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
help(np.random.choice)

random.choice(['Head',"Tail"])

np.random.choice(list('abc'), 10, replace=True)
np.random.choice(['s1', 's2', 's3'], 10, replace=True)


#%% 27. Shuffle
"""
This snippet can be used to randomize the order of the elements in a list.
Note that shuffle works in place, and returns None.
"""

from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo)
foo




#%%



