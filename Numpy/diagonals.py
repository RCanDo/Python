#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Diagonals
subtitle:
version: 1.0
type: help
keywords: [diagonals, array, numpy]
sources:
    - title:
      link: https://numpy.org/doc/stable/reference/generated/numpy.diag.html
    - title:
      link: https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html
    - title:
      link: https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html
    - title:
      link: https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html
    - title:
      link: https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html

file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: diagonals.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-27
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
#%%   numpy.diag(v, k=0)
#     https://numpy.org/doc/stable/reference/generated/numpy.diag.html
"""
Extract a diagonal or construct a diagonal array.
See the more detailed documentation for `numpy.diagonal`
if you use this function to extract a diagonal
and wish to write to the resulting array;
!!!  whether it returns a copy or a view depends on what version of numpy you are using.  !!!

Parameters
v : array_like
    If v is a 2-D array, return a copy of its k-th diagonal.
    If v is a 1-D array, return a 2-D array with v on the k-th diagonal.
k : int, optional
    Diagonal in question. The default is 0.
    Use  k>0  for diagonals  above  the main diagonal,
    and  k<0  for diagonals  below  the main diagonal.

Returns
out : ndarray
    The extracted diagonal or constructed diagonal array.

See also
diagonal    Return specified diagonals.
diagflat    Create a 2-D array with the flattened input as a diagonal.
trace    Sum along diagonals.
triu    Upper triangle of an array.
tril    Lower triangle of an array.
"""

x = np.arange(9).reshape((3,3))
x
#array([[0, 1, 2],
#       [3, 4, 5],
#       [6, 7, 8]])
np.diag(x)          # array([0, 4, 8])
np.diag(x, k=1)     # array([1, 5])
np.diag(x, k=-1)    # array([3, 7])
np.diag(np.diag(x))
#array([[0, 0, 0],
#       [0, 4, 0],
#       [0, 0, 8]])

xd = np.diag(x, k=-1)
xd
xd[0] = 0  #! ValueError: assignment destination is read-only


#%%
#%%   numpy.diagonal(a, offset=0, axis1=0, axis2=1)
#     https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html
"""
    Return specified diagonals.
    If a is 2-D, returns the diagonal of `a` with the given offset, i.e.,
    the collection of elements of the form a[i, i+offset].

    If a has more than two dimensions, then the axes specified by axis1 and axis2 are used
    to determine the 2-D sub-array whose diagonal is returned.
    The shape of the resulting array can be determined by removing axis1 and axis2
    and appending an index to the right equal to the size of the resulting diagonals.

    In versions of NumPy prior to 1.7, this function always returned a new,
    independent array containing a copy of the values in the diagonal.
    In NumPy 1.7 and 1.8, it continues to return a copy of the diagonal,
    but depending on this fact is deprecated.
    Writing to the resulting array continues to work as it used to, but a FutureWarning is issued.
    Starting in NumPy 1.9 it returns a read-only view on the original array.
   !!!  Attempting to write to the resulting array will produce an error.     !!!
    In some future release, it will return a read/write view and writing to the returned array
    will alter your original array.
    The returned array will have the same type as the input array.

    If you don’t write to the array returned by this function, then you can just ignore all of the above.

    If you depend on the current behavior, then we suggest copying the returned array explicitly,
    i.e., use np.diagonal(a).copy() instead of just np.diagonal(a).
    This will work with both past and future versions of NumPy.

Parameters
a : array_like;    Array from which the diagonals are taken.
offset : int, optional
    Offset of the diagonal from the main diagonal.
    Can be positive or negative. Defaults to main diagonal (0).
axis1 : int, optional
    Axis to be used as the first axis of the 2-D sub-arrays from which the diagonals should be taken.
    Defaults to first axis (0).
axis2 : int, optional
    Axis to be used as the second axis of the 2-D sub-arrays from which the diagonals should be taken.
    Defaults to second axis (1).

Returns
array_of_diagonals : ndarray
    If a is 2-D, then a 1-D array containing the diagonal and of the same type as `a`
    is returned unless `a` is a matrix,
    in which case a 1-D array rather than a (2-D) matrix is returned in order to maintain backward compatibility.
    If a.ndim > 2, then the dimensions specified by axis1 and axis2 are removed,
    and a new axis inserted at the end corresponding to the diagonal.

Raises
ValueError
    If the dimension of a is less than 2.

See also

diag

    MATLAB work-a-like for 1-D and 2-D arrays.
diagflat

    Create diagonal arrays.
trace

    Sum along diagonals.

"""
a = np.arange(4).reshape(2,2)
a
#array([[0, 1],
#       [2, 3]])
a.diagonal()    # array([0, 3])
a.diagonal(1)   # array([1])

ad = a.diagonal()
ad[0] = 0   #! ValueError: assignment destination is read-only

ad = np.diagonal(a)
ad[0] = 0   #! ValueError: assignment destination is read-only

# A 3-D example:
a = np.arange(8).reshape(2,2,2); a
#array([[[0, 1],
#        [2, 3]],
#       [[4, 5],
#        [6, 7]]])

a.diagonal(0,  # Main diagonals of two arrays created by skipping
           0,  # across the outer(left)-most axis last and
           1)  # the "middle" (row) axis first.
#array([[0, 6],
#       [1, 7]])

# The sub-arrays whose main diagonals we just obtained;
# note that each corresponds to fixing the right-most (column) axis,
# and that the diagonals are “packed” in rows.

a[:,:,0]  # main diagonal is [0 6]          !!!
#array([[0, 2],
#       [4, 6]])

a[:,:,1]  # main diagonal is [1 7]
array([[1, 3],
       [5, 7]])

# The anti-diagonal can be obtained by reversing the order of elements using either numpy.flipud or numpy.fliplr.

a = np.arange(9).reshape(3, 3)
a
#array([[0, 1, 2],
#       [3, 4, 5],
#       [6, 7, 8]])

np.fliplr(a).diagonal()  # Horizontal flip
# array([2, 4, 6])

np.flipud(a).diagonal()  # Vertical flip
# array([6, 4, 2])

# Note that the order in which the diagonal is retrieved varies depending on the flip function.

#%%
#%%   numpy.fill_diagonal(a, val, wrap=False)              !!!  inplace  !!!
#     https://numpy.org/doc/stable/reference/generated/numpy.fill_diagonal.html
"""
Fill the main diagonal of the given array of any dimensionality.
For an array a with a.ndim >= 2, the diagonal is the list of locations with indices a[i, ..., i] all identical.
This function modifies the input array __in-place__, it does not return a value.

Parameters
a : array, at least 2-D.
    Array whose diagonal is to be filled, it gets modified  __in-place__.
val : scalar or array_like
    Value(s) to write on the diagonal.
    If `val` is scalar, the value is written along the diagonal.
    If array-like, the __flattened__ `val` is written along the diagonal,
    repeating if necessary to fill all diagonal entries.
wrap : bool
    For tall matrices in NumPy version up to 1.6.2,
    the diagonal “wrapped” after N columns.
    You can have this behavior with this option. This affects only tall matrices.

See also
diag_indices, diag_indices_from

Notes
New in version 1.4.0.
This functionality can be obtained via diag_indices,
but internally this version uses a much faster implementation
!!!  that never constructs the indices and uses simple slicing.  !!!                                ???
"""
a = np.zeros((3, 3), int)
np.fill_diagonal(a, 5)
a
#array([[5, 0, 0],
#       [0, 5, 0],
#       [0, 0, 5]])

# The same function can operate on a 4-D array:
a = np.zeros((3, 3, 3, 3), int)
np.fill_diagonal(a, 4)
a
# We only show a few blocks for clarity:
a[0, 0]
#array([[4, 0, 0],
#       [0, 0, 0],
#       [0, 0, 0]])
a[1, 1]
#array([[0, 0, 0],
#       [0, 4, 0],
#       [0, 0, 0]])
a[2, 2]
#array([[0, 0, 0],
#       [0, 0, 0],
#       [0, 0, 4]])

# The wrap option affects only tall matrices:
# tall matrices no wrap
a = np.zeros((5, 3), int)
np.fill_diagonal(a, 4)
a
#array([[4, 0, 0],
#       [0, 4, 0],
#       [0, 0, 4],
#       [0, 0, 0],
#       [0, 0, 0]])

# tall matrices wrap
a = np.zeros((5, 3), int)
np.fill_diagonal(a, 4, wrap=True)
a
#array([[4, 0, 0],
#       [0, 4, 0],
#       [0, 0, 4],
#       [0, 0, 0],
#       [4, 0, 0]])

# wide matrices
a = np.zeros((3, 5), int)
np.fill_diagonal(a, 4, wrap=True)
a
#array([[4, 0, 0, 0, 0],
#       [0, 4, 0, 0, 0],
#       [0, 0, 4, 0, 0]])

# The anti-diagonal can be filled by reversing the order of elements using either numpy.flipud or numpy.fliplr.
a = np.zeros((3, 3), int);
np.fill_diagonal(np.fliplr(a), [1,2,3])  # Horizontal flip
a
#array([[0, 0, 1],
#       [0, 2, 0],
#       [3, 0, 0]])

np.fill_diagonal(np.flipud(a), [1,2,3])  # Vertical flip
a
#array([[0, 0, 3],
#       [0, 2, 0],
#       [1, 0, 0]])

#Note that the order in which the diagonal is filled varies depending on the flip function.


#%%
#%%   numpy.diag_indices(n, ndim=2)
#     https://numpy.org/doc/stable/reference/generated/numpy.diag_indices.html
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
#    https://numpy.org/doc/stable/reference/generated/numpy.diag_indices_from.html
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
