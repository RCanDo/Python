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

#%%
help(np.random.randint)
# ONLY UNIFORM distribution;
#! use np.random.choice() for arbitrary distributions on set of elements of any types

np.random.randint(-5, 5)

np.random.randint(2, size=10)  # array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])
np.random.randint(1, size=10)  # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# Generate a 2 x 4 array of ints between 0 and 4, inclusive:
np.random.randint(5, size=(2, 4))   # array([[4, 0, 2, 1], [3, 2, 2, 0]])

# Generate a 1 x 3 array with 3 different upper bounds
np.random.randint(1, [3, 5, 10])    # array([2, 2, 9]) # random

# Generate a 1 by 3 array with 3 different lower bounds
np.random.randint([1, 5, 7], 10)    # array([9, 8, 7]) # random

# Generate a 2 by 4 array using broadcasting with dtype of uint8
np.random.randint([1, 3, 5, 7], [[10], [20]], dtype=np.uint8)   # array([[ 8,  6,  9,  7],  [ 1, 16,  9, 12]], dtype=uint8)

#%%
help(np.random.choice)
#! use np.random.choice() for arbitrary distributions on set of elements of any types

# Generate a non-uniform random sample from np.arange(5) of size 3 without replacement:
np.random.choice(5, 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])

np.random.choice(list('abcde'), 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])

np.random.choice(range(5), 3, replace=False, p=[0.1, 0, 0.3, 0.6, 0])

[ str(x) for x in np.random.choice( range(1980, 2000), size=100, replace=True ) ]

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



