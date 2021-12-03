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
#%% see also
#  numpy.diag_indices(n, ndim=2)
#  numpy.diag_indices_from(arr)
#
#

#%%
#%%   lib.stride_tricks.sliding_window_view(x, window_shape, axis=None, *, subok=False, writeable=False)
"""
Create a sliding window view into the array with the given window shape.

Also known as rolling or moving window,
the window slides across all dimensions of the array
and extracts subsets of the array at all window positions.
New in version 1.20.0.

Parameters
x : array_like
    Array to create the sliding window view from.
window_shape : int or tuple of int
    Size of window over each axis that takes part in the sliding window.
    If axis is not present, must have same length as the number of input array dimensions.
    Single integers i are treated as if they were the tuple (i,).
axis : int or tuple of int, optional
    Axis or axes along which the sliding window is applied.
    By default, the sliding window is applied to all axes
    and `window_shape[i]` will refer to axis `i` of `x`.
    If `axis` is given as a tuple of int, `window_shape[i]` will refer to the axis `axis[i]` of `x`.
    Single integers i are treated as if they were the tuple (i,).
subok : bool, optional
    If True, sub-classes will be passed-through,
    otherwise the returned array will be forced to be a base-class array (default).
writeable : bool, optional
    When true, allow writing to the returned view.
    The default is false, as this should be used with caution:
    the returned view contains the same memory location multiple times,
    so writing to one location will cause others to change.

Returns
view : ndarray
    Sliding window view of the array.
    The sliding window dimensions are inserted at the end,
    and the original dimensions are trimmed as required by the size of the sliding window.
    That is, view.shape = x_shape_trimmed + window_shape,
    where x_shape_trimmed is x.shape with every entry reduced
    by one less than the corresponding window size.

See also
lib.stride_tricks.as_strided
    A lower-level and less safe routine for creating arbitrary views from custom shape and strides.
broadcast_to
    broadcast an array to a given shape.

Notes
For many applications using a sliding window view can be convenient, but potentially very slow.
Often specialized solutions exist, for example:
    scipy.signal.fftconvolve
    filtering functions in scipy.ndimage
    moving window functions provided by bottleneck.
As a rough estimate, a sliding window approach with an input size of N and a window size of W
will scale as O(N*W) where frequently a special algorithm can achieve O(N).
That means that the sliding window variant for a window size of 100
can be a 100 times slower than a more specialized version.

Nevertheless, for small window sizes, when no custom algorithm exists,
or as a prototyping and developing tool, this function can be a good solution.
"""
from np.lib.stride_tricks import sliding_window_view

x = np.arange(6)
x.shape     # (6,)

v = sliding_window_view(x, 3)
v.shape     # (4, 3)
v
#array([[0, 1, 2],
#       [1, 2, 3],
#       [2, 3, 4],
#       [3, 4, 5]])

# This also works in more dimensions, e.g.
i, j = np.ogrid[:3, :4]

x = 10*i + j
x.shape     # (3, 4)
x
#array([[ 0,  1,  2,  3],
#       [10, 11, 12, 13],
#       [20, 21, 22, 23]])

shape = (2,2)
v = sliding_window_view(x, shape)
v.shape     # (2, 3, 2, 2)
v
#array([[[[ 0,  1],
#         [10, 11]],
#        [[ 1,  2],
#         [11, 12]],
#        [[ 2,  3],
#         [12, 13]]],
#       [[[10, 11],
#         [20, 21]],
#        [[11, 12],
#         [21, 22]],
#        [[12, 13],
#         [22, 23]]]])

# The axis can be specified explicitly:
v = sliding_window_view(x, 3, 0)
v.shape     # (1, 4, 3)
v
#array([[[ 0, 10, 20],
#        [ 1, 11, 21],
#        [ 2, 12, 22],
#        [ 3, 13, 23]]])

# The same axis can be used several times. In that case, every use reduces the corresponding original dimension:
v = sliding_window_view(x, (2, 3), (1, 1))
v.shape     # (3, 1, 2, 3)
v
#array([[[[ 0,  1,  2],
#         [ 1,  2,  3]]],
#       [[[10, 11, 12],
#         [11, 12, 13]]],
#       [[[20, 21, 22],
#         [21, 22, 23]]]])

# Combining with stepped slicing (::step), this can be used to take sliding views which skip elements:
x = np.arange(7)
sliding_window_view(x, 5)[:, ::2]
#array([[0, 2, 4],
#       [1, 3, 5],
#       [2, 4, 6]])

# or views which move by multiple elements
x = np.arange(7)
sliding_window_view(x, 3)[::2, :]
#array([[0, 1, 2],
#       [2, 3, 4],
#       [4, 5, 6]])

# A common application of sliding_window_view is the calculation of running statistics.
# The simplest example is the moving average:
x = np.arange(6)
x.shape     # (6,)
v = sliding_window_view(x, 3)
v.shape     # (4, 3)
v
#array([[0, 1, 2],
#       [1, 2, 3],
#       [2, 3, 4],
#       [3, 4, 5]])

moving_average = v.mean(axis=-1)
moving_average  # array([1., 2., 3., 4.])

# Note that a sliding window approach is often not optimal (see Notes).

#%%
#%%  lib.stride_tricks.as_strided(x, shape=None, strides=None, subok=False, writeable=True)
"""
Create a view into the array with the given shape and strides.

   Warning
This function has to be used with extreme care, see notes.

Parameters
xndarray

    Array to create a new.
shapesequence of int, optional

    The shape of the new array. Defaults to x.shape.
stridessequence of int, optional

    The strides of the new array. Defaults to x.strides.
subokbool, optional

    New in version 1.10.

    If True, subclasses are preserved.
writeablebool, optional

    New in version 1.12.

    If set to False, the returned array will always be readonly. Otherwise it will be writable if the original array was. It is advisable to set this to False if possible (see Notes).

Returns
view : ndarray

See also
broadcast_to
    broadcast an array to a given shape.
reshape
    reshape an array.
lib.stride_tricks.sliding_window_view
    userfriendly and safe function for the creation of sliding window views.

Notes
as_strided creates a view into the array given the exact strides and shape.
This means it manipulates the internal data structure of ndarray and, if done incorrectly, the array elements can point to invalid memory and can corrupt results or crash your program. It is advisable to always use the original x.strides when calculating new strides to avoid reliance on a contiguous memory layout.

Furthermore, arrays created with this function often contain self overlapping memory, so that two elements are identical. Vectorized write operations on such arrays will typically be unpredictable. They may even give different results for small, large, or transposed arrays. Since writing to these arrays has to be tested and done with great care, you may want to use writeable=False to avoid accidental write operations.

For these reasons it is advisable to avoid as_strided when possible.
"""



#%%
#%%
