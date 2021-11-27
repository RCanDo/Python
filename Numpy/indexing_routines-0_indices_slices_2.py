#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Indexing routines 0
subtitle: Indices, slices 2
version: 1.0
type: help
keywords: [array, numpy]
sources:
    - title: Indexing routines
      link: https://numpy.org/doc/stable/reference/routines.indexing.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: indexing_routines-0_indices_slices_2.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-26
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%%
pwd
cd E:/ROBOCZY/Python/Numpy/
cd ~/Works/Python/Numpy/
ls

#%%
import numpy as np


#%%
#%%   numpy.mask_indices(n, mask_func, k=0)
"""
Return the indices to access (n, n) arrays, given a masking function.

Assume mask_func() is a function that,
for a square array a of size (n, n) with a possible offset argument k,
when called as mask_func(a, k) returns a new array with zeros in certain locations
(functions like triu or tril do precisely this).
Then this function returns the indices where the non-zero values would be located.

Parameters
n : int
    The returned indices will be valid to access arrays of shape (n, n).
mask_func : callable
    A function whose call signature is similar to that of triu, tril. That is, mask_func(x, k) returns a boolean array, shaped like x. k is an optional argument to the function.
k : scalar
    An optional argument which is passed through to mask_func. Functions like triu, tril take a second argument that is interpreted as an offset.

Returns
indices : tuple of arrays.
    The n arrays of indices corresponding to the locations where
    `mask_func(np.ones((n, n)), k)` is True.


Notes
New in version 1.4.0.
"""
# These are the indices that would allow you to access the upper triangular part of any 3x3 array:
iu = np.mask_indices(3, np.triu)
iu
arr = np.arange(1,10).reshape(3,3)
arr
np.triu(arr)
arr[iu]

# An offset can be passed also to the masking function.
# This gets us the indices starting on the first diagonal right of the main one:

iu1 = np.mask_indices(3, np.triu, 1)
iu1
arr[iu1]   # array([2, 3, 6])

iu_1 = np.mask_indices(3, np.triu, -1)
iu_1
arr[iu_1]

#%%
def mask(arr, *args):
    res = arr.copy()
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if (i+j) % 2 == 0:
                res[i, j] = 0
    return res

iu3 = np.mask_indices(3, mask)
iu3
arr[iu3]
arr

#%% See also:
np.triu()
np.tril()
np.triu_indices()
np.triu_indices_from()
np.tril_indices()
np.tril_indices_from()

#%%
#%%   numpy.ravel_multi_index(multi_index, dims, mode='raise', order='C')
"""
Converts a tuple of index arrays into an array of flat indices, applying boundary modes to the multi-index.

Parameters

multi_index : tuple of array_like
    A tuple of integer arrays, one array for each dimension.
dims : tuple of ints
    The shape of array into which the indices from multi_index apply.
mode{‘raise’, ‘wrap’, ‘clip’}, optional
    Specifies how out-of-bounds indices are handled.
    Can specify either one mode or a tuple of modes, one mode per index.
        ‘raise’ – raise an error (default)
        ‘wrap’ – wrap around
        ‘clip’ – clip to the range
    In ‘clip’ mode, a negative index which would normally wrap will clip to 0 instead.
order{‘C’, ‘F’}, optional
    Determines whether the multi-index should be viewed as indexing
    in row-major (C-style) or column-major (Fortran-style) order.

Returns
raveled_indices : ndarray
    An array of indices into the flattened version of an array of dimensions dims.

See also
unravel_index   -- reverse operation

Notes
New in version 1.6.0.
"""
ref = np.arange(42).reshape(7, 6)
ref

rows = [0, 1, 3]
cols = [5, 1, 0]
np.ravel_multi_index((rows, cols), (7,6))
# array([ 5,  7, 18], dtype=int64)

arr = np.array([[3,6,6],[4,5,1]])
np.ravel_multi_index(arr, (7,6))
# array([22, 41, 37])   ## OK

np.ravel_multi_index(arr, (7,6), order='F')
array([31, 41, 13])

np.ravel_multi_index(arr, (4,6), mode='clip')
# array([22, 23, 19])

np.ravel_multi_index(arr, (4,4), mode=('clip','wrap'))
# array([12, 13, 13])

np.ravel_multi_index((3,1,4,1), (6,7,8,9))
# 1621

#%%
#%%   numpy.unravel_index(indices, shape, order='C')
"""
Converts a flat index or array of flat indices into a tuple of coordinate arrays.

Parameters
indices : array_like
    An integer array whose elements are indices
    into the flattened version of an array of dimensions `shape`.
    Before version 1.6.0, this function accepted just one index value.
shape : tuple of ints
    The shape of the array to use for unraveling indices.
    Changed in version 1.16.0: Renamed from dims to shape.
order{‘C’, ‘F’}, optional
    Determines whether the indices should be viewed as indexing
    in row-major (C-style) or column-major (Fortran-style) order.
    New in version 1.6.0.

Returns
unraveled_coords : tuple of ndarray
    Each array in the tuple has the same shape as the `indices` array.

See also
ravel_multi_index
"""
np.unravel_index([22, 41, 37], (7, 6))       # (array([3, 6, 6]), array([4, 5, 1]))
ref[np.unravel_index([22, 41, 37], (7, 6))]  # array([22, 41, 37])
np.ravel_multi_index(([3, 6, 6], [4, 5, 1]), (7, 6))        # array([22, 41, 37], dtype=int64)

np.unravel_index([31, 41, 13], (7, 6), order='F')           # (array([3, 6, 6]), array([4, 5, 1]))
ref2 = np.arange(42).reshape(6, 7).T
ref2
ref2[np.unravel_index([31, 41, 13], (7, 6), order='F')]     # array([31, 41, 13])
np.ravel_multi_index(([3, 6, 6], [4, 5, 1]), (7, 6), order='F')     # array([31, 41, 13], dtype=int64)

np.unravel_index(1621, (6,7,8,9))
# (3, 1, 4, 1)

#%%
#%%   numpy.diag_indices(n, ndim=2)
"""
Return the indices to access the main diagonal of an array.

This returns a tuple of indices that can be used to access the main diagonal
of an array `a` with `a.ndim >= 2` dimensions and shape (n, n, …, n).
For `a.ndim = 2` this is the usual diagonal,
for `a.ndim > 2` this is the set of indices to access `a[i, i, ..., i] for i = [0..n-1]`.

Parameters
nint
    The size, along each dimension, of the arrays for which the returned indices can be used.
ndimint, optional
    The number of dimensions.

See also
diag_indices_from

Notes
New in version 1.4.0.
"""
# Create a set of indices to access the diagonal of a (4, 4) array:

di = np.diag_indices(4)
di      # (array([0, 1, 2, 3]), array([0, 1, 2, 3]))

a = np.arange(16).reshape(4, 4)
a
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11],
#       [12, 13, 14, 15]])

a[di] = 100
a
#array([[100,   1,   2,   3],
#       [  4, 100,   6,   7],
#       [  8,   9, 100,  11],
#       [ 12,  13,  14, 100]])

# Now, we create indices to manipulate a 3-D array:
d3 = np.diag_indices(2, 3)
d3      # (array([0, 1]), array([0, 1]), array([0, 1]))

# And use it to set the diagonal of an array of zeros to 1:
a = np.zeros((2, 2, 2), dtype=int)
a[d3] = 1
a
#array([[[1, 0],
#        [0, 0]],
#       [[0, 0],
#        [0, 1]]])

#%%  numpy.diag_indices_from(arr)
"""
Return the indices to access the main diagonal of an n-dimensional array.
See diag_indices for full details.
Parameters
    arrarray, at least 2-D
"""
np.diag_indices_from(ref)   #! ValueError: All dimensions of input must be of equal length
#??? why?

np.diag_indices_from(np.arange(16).reshape(4,4))    # (array([0, 1, 2, 3]), array([0, 1, 2, 3]))
np.diag_indices_from(np.zeros((4, 4)))              # (array([0, 1, 2, 3]), array([0, 1, 2, 3]))
np.diag_indices_from(np.zeros((4,3)))               #! ValueError: All dimensions of input must be of equal length

#??? What use of it ???




#%%
#%%
