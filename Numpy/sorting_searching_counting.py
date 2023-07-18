# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:29:23 2021

@author: staar
"""
#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Counting elements in array
version: 1.0
type: tutorial
keywords: [array, numpy, count]
sources:
    - title: Sorting, searching, and counting
      link: https://numpy.org/doc/stable/reference/routines.sort.html
    - title: How to count the occurrence of certain item in an ndarray?
      link: https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: counting_elements.py
    path: ~/Works/Python/Numpy/
    date: 2021-09-17
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import numpy as np

#%%
#%% How to count the occurrence of certain item in an ndarray?
#   https://stackoverflow.com/questions/28663856/how-to-count-the-occurrence-of-certain-item-in-an-ndarray
#%%
a = np.array([0, 3, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 3, 4])
unique, counts = np.unique(a, return_counts=True)
unique
counts
dict(zip(unique, counts))

#%%
np.count_nonzero(a)         # 8
np.count_nonzero(a == 0)    # 7
np.count_nonzero(a == 1)    # 4

#%%
(a == 0).sum()
(a == 1).sum()

#%%
a.tolist().count(0)
a.tolist().count(1)
"""
This code may be one of the fastest solutions for larger arrays.
Getting the result as a list is a bonus, too.
If 'a' is an n-dimensional array, we can just use:
    np.bincount(np.reshape(a, a.size))

This rounds down non-integers. e.g.
    np.bincount([0, 0.5, 1.1])  # -> array([2, 1])
If you have an array with large integers, you will get a long output, e.g.
    len(np.bincount([1000]))   # 1001.
"""

#%%
from collections import Counter
Counter(a)

#%%
a = np.array([0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1])

np.bincount(a)
# array([8, 4])    # count of zeros is at index 0 : 8
                   # count of ones is at index  1 : 4
b = [0,0, 1,1,1, 2,2,2,2,2, 5]
np.bincount(b)

dict(zip(range(max(b)+1), np.bincount(b)))

#%%
#%%

#%%
#%%  numpy.argwhere(a)
"""
Find the indices of array elements that are non-zero, grouped by element.
`np.argwhere(a)` is almost the same as `np.transpose(np.nonzero(a))`,
but produces a result of the correct shape for a 0D array.

The output of argwhere is not suitable for indexing arrays.
For this purpose use `np.nonzero(a)` instead.
"""

x = np.array([3, 2, 2, 0, 3, 4, 2, 4, 3])
np.argwhere(x==4)
# array([[5],
#        [7]])

x = np.arange(6).reshape(2,3)
x
# array([[0, 1, 2],
#        [3, 4, 5]])

np.argwhere(x>1)
# array([[0, 2],
#        [1, 0],
#        [1, 1],
#        [1, 2]])

for k in np.argwhere(x>1): print(x[tuple(k)])   # this may be useful

#%%
#%%  numpy.nonzero(a)
"""
Return the indices of the elements that are non-zero.

!!!  Returns a tuple of arrays, one for each dimension of a,  !!!
containing the indices of the non-zero elements in that dimension.
The values in a are always tested and returned in row-major, C-style order.

!!!  To group the indices by element, rather than dimension,  !!!
use `argwhere`, which returns a row for each non-zero element.
"""
x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
np.nonzero(x)       # (array([0, 1, 2, 2]), array([0, 1, 0, 1]))
x[np.nonzero(x)]    # array([3, 4, 5, 6])
# so dimension is lost -- but it's obvious !

# notice that for 'fancy indexing' wee need rows passed as column vector:
x[(np.array([0, 1, 2, 2], ndmin=2).T, np.array([0, 1, 0, 1]))]

np.transpose(np.nonzero(x))
# array([[0, 0],
#        [1, 1],
#        [2, 0],
#        [2, 1]])
np.argwhere(x>0)    # the same

x[np.transpose(np.nonzero(x))]   #...???...  but it's just wrong use of it

"""
A common use for `nonzero` is to __find the indices__ of an array, where a condition is True.
"""
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a
a > 3               # array([[False, False, False], [ True,  True,  True], [ True,  True,  True]])

np.nonzero(a > 3)   # (array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))

# Using this result to index a is equivalent to using the mask directly:

a[np.nonzero(a > 3)]    # array([4, 5, 6, 7, 8, 9])
a[a > 3]                #! prefer this spelling

#! nonzero can also be called as a method of the array.
(a > 3).nonzero()       # (array([1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2]))

#%%
#%%  numpy.count_nonzero(a, axis=None, *, keepdims=False)[source]
"""
Counts the number of non-zero values in the array a.
The word “non-zero” is in reference to the Python 2.x built-in method __nonzero__()
(renamed __bool__() in Python 3.x) of Python objects that tests an object’s “truthfulness”.
For example, any number is considered truthful if it is nonzero,
whereas any string is considered truthful if it is not the empty string.
Thus, this function (recursively) counts how many elements in a (and in sub-arrays thereof)
have their __nonzero__() or __bool__() method evaluated to True.

Parameters
a : array_like;    The array for which to count non-zeros.
axis : int or tuple, optional;
    Axis or tuple of axes along which to count non-zeros.
    Default is `None`, meaning that non-zeros will be counted along a __flattened__ version of a.
keepdims : bool, optional
    If this is set to True, the axes that are counted are left in the result as dimensions with size one.
    With this option, the result will broadcast correctly against the input array.
    New in version 1.19.0.
Returns
count : int or array of int
    Number of non-zero values in the array along a given axis.
    Otherwise, the total number of non-zero values in the array is returned.
"""
np.count_nonzero(np.eye(4))  # 4

a = np.array([[0, 1, 7, 0], [3, 0, 2, 19]])
np.count_nonzero(a)     # 5

np.count_nonzero(a, axis=0)     # array([1, 1, 2, 1])

np.count_nonzero(a, axis=1)     # array([2, 3])

np.count_nonzero(a, axis=1, keepdims=True)      #! New in version 1.19.0.
# array([[2], [3]])

#%%
#%%  np.searchsorted(a, v, side='left', sorter=None)
"""
Find indices where elements should be inserted to maintain order.
Find the indices into a sorted array `a` such that,
if the corresponding elements in `v` were inserted before the indices, the order of `a` would be preserved.
Assuming that a is sorted:
side        returned index i satisfies
'left'        a[i-1] < v <= a[i]
'right'       a[i-1] <= v < a[i]
"""
np.searchsorted([1,2,3,4,5], 3)    # 2
np.searchsorted([1,2,3,4,5], 3, side='right')   # 3
np.searchsorted([1,2,3,4,5], [-10, 10, 2, 3])   # array([0, 5, 1, 2])

xx = np.random.randn(20)
xx
bins=[-3, -1, 0, 1, 3]
np.searchsorted(bins, xx, side="left")

#%%
#%% np.bincount(x, weights=None, minlength=0)     # statistics
"""
!!! It is NOT counting values falling into each bin. !!!

Count number of occurrences of each value in array of __non-negative ints__.

The number of bins (of size 1) is one larger than the largest value in x.
If minlength is specified, there will be at least this number of bins in the output array
(though it will be longer if necessary, depending on the contents of x).
Each bin gives the number of occurrences of its index value in x.
"""
np.bincount(np.arange(5))   # array([1, 1, 1, 1, 1])
np.bincount(np.array([0, 1, 1, 3, 2, 1, 7]))    # array([1, 3, 1, 1, 0, 0, 0, 1])

x = np.array([0, 1, 1, 3, 2, 1, 7, 23])

np.bincount(x)
#! The input array needs to be of integer dtype, otherwise a TypeError is raised:
np.bincount(np.arange(5, dtype=float))  #! TypeError: Cannot cast array data from dtype('float64') to dtype('int64') according to the rule 'safe'

"""
If weights is specified the input array is weighted by it,
i.e. if a value n is found at position i, out[n] += weight[i] instead of out[n] += 1.

A possible use of bincount is to perform sums over variable-size
chunks of an array, using the weights keyword.
"""
w = np.array([0.3, 0.5, 0.2, 0.7, 1., -0.6]) # weights
x = np.array([0, 1, 1, 2, 2, 2])

np.bincount(x,  weights=w)  # array([ 0.3,  0.7,  1.1])

# hence len(x) == len(w) !!! else
np.bincount(x,  weights=[.1, .2])  #! ValueError: The weights and list don't have the same length.

# ! nonitegers are rounded
np.bincount([0, 0.5, 1.1])  # array([2, 1])

#%%



#%%



#%%