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

#%%
help(np.random.random_sample)
# Return random floats in the half-open interval [0.0, 1.0).
np.random.random_sample()
np.random.sample()             # just alias !
np.random.sample(5)
np.random.sample((5,))
np.random.sample((5,3))

# from interval [3, 5)
(5 - 3)*np.random.sample((5,3)) + 3
# or
#%% .uniform(low=0.0, high=1.0, size=None) ~  U(a, b)
np.random.uniform(size=20)
np.random.uniform(1, 10, size=20)

#%%! another alias !
np.random.rand(5)
np.random.rand(5, 3)
# but little different
np.random.sample(5,3)         #! ERROR

#%%%
#%%
# random samples from a normal (Gaussian) distribution.
np.random.normal(loc=0.0, scale=1.0, size=None)
np.random.normal(10, 5, size=10)         # scale == sigma (dispersion) == sqrt(variance)
np.random.normal(10, 5, size=(10, 5))
help(np.random.normal)
"""
Parameters
----------
loc : float or array_like of floats
    Mean ("centre") of the distribution.
scale : float or array_like of floats
    Standard deviation (spread or "width") of the distribution. Must be
    non-negative.
size : int or tuple of ints, optional
    Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
    ``m * n * k`` samples are drawn.  If size is ``None`` (default),
    a single value is returned if ``loc`` and ``scale`` are both scalars.
    Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.
"""
np.random.normal(10, 5, size=(10, 5)).mean()    # 9.955969763582148
np.random.normal(10, 5, size=(10, 5)).var()     # 19.934248561926882

# sample (or samples) from the "standard_normal" distribution  N(0, 1)
np.random.randn(10)
np.random.randn(8, 4)
help(np.random.randn)
# Return a sample (or samples) from the "standard normal" distribution. ...

#%%  integers
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
x_sub, y_sub = zip(*np.random.sample(list(zip([1, 2, 3], [-1, -2, -3])), 2))   #! TypeError: random_sample() takes at most 1 positional argument (2 given)

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

np.random.choice(['Head',"Tail"])

np.random.choice(list('abc'), 10, replace=True)
np.random.choice(['s1', 's2', 's3'], 10, replace=True)


#%%
#%% for Pandas Series / DataFrames
import pandas as pd

## simplest and best
ss = pd.Series(list('abcdefghijk'))
ss
ss.sample()    ## returns! NOT inplace
ss

ss.sample(frac=1)  ## == permutation / shuffling
# notice though that index follows values
# when plotting cloud agains index we'd like to reindex to 0, 1, ...
ss.sample(frac=1, ignore_index=True)   # reindexed !


# for DataFrames:
df = pd.DataFrame({'a' : ss, 'b': range(11)})
df
df.sample()  # returns! NOT inplace
df.sample(frac=1)
df # not changed
df.sample(frac=1, ignore_index=True) # reindexed

#%%
## Other method from NumPy
ss = pd.Series(np.arange(9))
ss
np.random.shuffle(ss)
ss  # reindexed !!!

ss = pd.Series(np.arange(9))
ss
idx = ss.index.to_list()
idx
np.random.shuffle(idx)     # inplace !!!
idx
ss[idx]   #

## doesn't work for DataFrames
np.random.shuffle(df)  #! KeyError: 2


## maybe better .choice()
np.random.choice(ss, len(ss))    # returns list

# so again via index but may be in one line (because it's not inplace)
ss = pd.Series(np.arange(9))
ss
ss[np.random.choice(ss.index.to_list(), len(ss), replace=False)]

# the same as .permutation()
ss = ss[np.random.permutation(ss.index.to_list())]
ss



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
