#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Manipulations 0
subtitle: Substituting
version: 1.0
type: help
keywords: [substituting, indexing, array, numpy]
remarks:
    - Includes number of Indexing Routines: palce, put, put_along_axis, putmask
sources:
    - title: Array manipulation routines
      link: https://numpy.org/doc/stable/reference/routines.array-manipulation.html
    - title: Indexing routines
      link: https://numpy.org/doc/stable/reference/routines.indexing.html
      remarks: |
          ....
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: manipulations-0_susbstituting.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-30
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
#%%  numpy.place(arr, mask, vals)                !!! inplace !!!
#    https://numpy.org/doc/stable/reference/generated/numpy.place.html
"""
Change elements of an array based on conditional and input values.

Similar to
    np.copyto(arr, vals, where=mask),
the difference is that
- `place` uses the first N elements of `vals`, where N is the number of True values in `mask`,
while
- `copyto` uses the elements where `mask` is True.

Note that `extract()` does the exact opposite of place.

Parameters
arr : ndarray
    Array to put data into.
mask : array_like
    Boolean mask array. Must have the same size as `arr`.   !!!
vals : 1-D sequence
    Values to put into `arr`.
    Only the first N elements are used, where N is the number of True values in `mask`.
    If `vals` is smaller than N, it will be repeated, and if elements of `arr` are to be masked,
    this sequence must be non-empty.

See also
copyto, put, take, extract
"""
arr = np.arange(6).reshape(2, 3)
arr
np.place(arr, arr>2, [10, 20])      #!!! inplace
arr
#array([[ 0,  1,  2],
#       [10, 20, 10]])

# also
arr = np.arange(6).reshape(2, 3)
arr
np.putmask(arr, (arr>2), [10, 20])      #!!! the same
arr

# while
np.copyto(arr, [10, 20], where=arr>2)  # ValueError: could not broadcast input array from shape (2) into shape (2,3)

np.place(arr, arr>1, [10, 20, 30])
arr
#array([[ 0,  1, 10],
#       [20, 30, 10]])

np.copyto(arr, [10, 20, 30], where=arr>1)
arr
#array([[ 0,  1, 30],
#       [10, 20, 30]])

#%%  https://numpy.org/doc/stable/reference/generated/numpy.extract.html#numpy.extract
np.extract(arr>1, arr)

#%% place via standard indexing

arr[arr>2] = [10, 20]   #! ValueError: NumPy boolean array indexing assignment cannot assign 2 input values to the 3 output values where the mask is true
arr[arr>2] = [10, 20, 30]   # ok
arr
#array([[ 0,  1,  2],
#       [10, 20, 30]])

# no bradcasting (recycling) possible this way (?)
arr[arr>1] = [10, 20, 30]   #! ValueError: NumPy boolean array indexing assignment cannot assign 3 input values to the 4 output values where the mask is true
arr

#%%
#%%  numpy.copyto(dst, src, casting='same_kind', where=True)    !!! inplace !!!
#    https://numpy.org/doc/stable/reference/generated/numpy.copyto.html#numpy.copyto
"""
Copies values from one array to another, broadcasting as necessary.
Raises a TypeError if the casting rule is violated,
and if `where` is provided, it selects which elements to copy.
New in version 1.7.0.

Parameters
dst : ndarray;    The array into which values are copied.
src : array_like;    The array from which values are copied.
casting{‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’}, optional
    Controls what kind of data casting may occur when copying.
        ‘no’ means the data types should not be cast at all.
        ‘equiv’ means only byte-order changes are allowed.
        ‘safe’ means only casts which can preserve values are allowed.
        ‘same_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.
        ‘unsafe’ means any data conversions may be done.
where : array_like of bool, optional
    A boolean array which is broadcasted to match the dimensions of `dst`,
    and selects elements to copy from `src` to `dst` wherever it contains the value True.
"""
# basic usage: dst.shape == src.shape

dst0 = np.arange(12).reshape(3, 4)
dst0
src = 10 * dst0
src

dst = dst0.copy()
np.copyto(dst, src, where=(dst%3==0))
dst

# while via place()
dst = dst0.copy()
np.place(dst, dst%3==0, src)
dst

#%%
dst = np.arange(12).reshape(3, 4)
src0 = src[:,0]
np.copyto(dst, src0, where=(dst%3==0))  #! ValueError: could not broadcast input array from shape (3) into shape (3,4)
np.copyto(dst, [0, 40, 80], where=(dst%3==0))  #!  "
# BUT
np.copyto(dst, src[0, :], where=(dst%3==0))  # ok
dst
#!!! so it works for rows but not for columns... !!!
# see broadcasting rules

#%%
arr = np.arange(6).reshape(2, 3)
arr
np.copyto(arr, [10, 20], where=arr>2)  # ValueError: could not broadcast input array from shape (2) into shape (2,3)
# while
np.place(arr, arr>2, [10, 20])
arr
#array([[ 0,  1,  2],
#       [10, 20, 10]])

np.copyto(arr, [10, 20, 30], where=arr>2)
arr
#array([[ 0,  1,  2],
#       [10, 20, 30]])
np.copyto(arr, [10, 20, 30], where=arr>1)   # ok
arr
#array([[ 0,  1, 30],
#       [10, 20, 30]])

#??? what's the rule ???

#%%
#%%   numpy.put(a, ind, v, mode='raise')         !!! inplace !!!
"""
Replaces specified elements of an array with given values.
!!!  The indexing works on the __flattened__ target array.  !!!
`put` is roughly equivalent to:
    a.flat[ind] = v

Parameters
a : ndarray;    Target array.
ind : array_like;    Target indices, interpreted as integers.
v : array_like
    Values to place in `a` at target indices. If `v` is shorter than `ind` it will be repeated as necessary.
mode{‘raise’, ‘wrap’, ‘clip’}, optional
    Specifies how out-of-bounds indices will behave.
        ‘raise’ – raise an error (default)
        ‘wrap’ – wrap around
        ‘clip’ – clip to the range
    ‘clip’ mode means that all indices that are too large are replaced by the index
    that addresses the last element  XXX(? along that axis ?).
    Note that this disables indexing with negative numbers.
    In ‘raise’ mode, if an exception occurs the target array may still be modified.

See also
putmask, place, put_along_axis
    Put elements by matching the array and the index arrays
"""

a = np.arange(5)
a
np.put(a, [0, 2], [-44, -55])       #!!! inplace
a   # array([-44,   1, -55,   3,   4])

a = np.arange(5)
np.put(a, 22, -5, mode='clip')
a   # array([ 0,  1,  2,  3, -5])

a = np.arange(5)
np.put(a, 22, -5, mode='wrap')
a   # array([ 0,  1, -5,  3,  4])

a = np.arange(12).reshape(3, 4)
np.put(a, [1, 3, 7, 14], [-1, -3, -7, -14], mode="wrap")
a

a = np.arange(12).reshape(3, 4)
np.put(a, [1, 3, 7, 13], [-1, -3, -7, -13], mode="wrap")    # !
a

#%% standard indexing
a = np.arange(12).reshape(3, 4)
# works only via .flat
a[[1, 3, 7, 11]] = [-1, -3, -7, -11]        #!  IndexError: index 3 is out of bounds for axis 0 with size 3
a.flat[[1, 3, 7, 11]] = [-1, -3, -7, -11]   # ok
a
# no wrapping/clipping possible
a.flat[[1, 3, 7, 13]] = [-1, -3, -7, -13]   #! IndexError: index 13 is out of bounds for size 12


#%%
#%%   numpy.put_along_axis(arr, indices, values, axis)     !!! inplace !!!
"""
Put `values` into the destination array by matching 1d index and data slices.
This iterates over matching 1d slices oriented along the specified axis
in the index and data arrays, and uses the former to place values into the latter.
These slices can be different lengths.

!!!  The indexing works on the __flattened__ target array.  !!!

Functions returning an index along an axis,
like `argsort` and `argpartition`, produce suitable indices for this function.
New in version 1.15.0.

Parameters
arr : ndarray (Ni…, M, Nk…)
    Destination array.
indices : ndarray (Ni…, J, Nk…)
    Indices to change along each 1d slice of `arr`.
    This must match the dimension of `arr`,
    but dimensions in Ni and Nj may be 1 to broadcast against `arr`.
values : array_like (Ni…, J, Nk…)
    values to insert at those `indices`.
    Its shape and dimension are broadcast to match that of `indices`.
axis : int
    The axis to take 1d slices along.
   !!! If axis is None, the destination array is treated
    as if a __flattened__ 1d view had been created of it.           !!!

See also
take_along_axis
    Take values from the input array by matching 1d index and data slices

Notes
This is equivalent to (but faster than) the following use of `ndindex` and `s_`,
which sets each of i and k to a tuple of indices:
"""
Ni, M, Nk = a.shape[:axis], a.shape[axis], a.shape[axis+1:]
J = indices.shape[axis]  # Need not equal M

for i in ndindex(Ni):
    for k in ndindex(Nk):
        a_1d       = a      [i + s_[:,] + k]
        indices_1d = indices[i + s_[:,] + k]
        values_1d  = values [i + s_[:,] + k]
        for j in range(J):
            a_1d[indices_1d[j]] = values_1d[j]
"""
Equivalently, eliminating the inner loop, the last two lines would be:

a_1d[indices_1d] = values_1d
"""
a = np.array([[10, 30, 20], [60, 40, 50]])
a
ai = np.expand_dims(np.argmax(a, axis=1), axis=1)
ai      # array([[1], [0]])

np.put_along_axis(a, ai, 99, axis=1)
a
#array([[10, 99, 20],
#       [99, 40, 50]])

#%%
#%%   numpy.putmask(a, mask, values)             !!! inplace !!!
"""
Changes elements of an array based on conditional and input values.
Sets `a.flat[n] = values[n]` for each n where `mask.flat[n]==True`.
If `values` is not the same size as `a` and `mask` then it will repeat.
This gives behavior different from `a[mask] = values`.

!!!  The indexing works on the __flattened__ target array.  !!!

Parameters
and : array;    Target array.
mask : array_like;    Boolean mask array. It has to be the same shape as `a`.
values : array_like;
    Values to put into `a` where `mask` is True. If `values` is smaller than `a` it will be repeated.

See also
place, put, take, copyto
"""
x = np.arange(6).reshape(2, 3)
np.putmask(x, x>2, x**2)
x
#array([[ 0,  1,  2],
#       [ 9, 16, 25]])

x = np.arange(6).reshape(2, 3)
np.putmask(x, (x>2).ravel(), x**2)
x

# If `values` is smaller than `a` it is repeated:
x = np.arange(5)
np.putmask(x, x>1, [-33, -44])

x
# array([  0,   1, -33, -44, -33])

#%%
#%%