#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Creation routines 0
subtitle:
version: 1.0
type: help
keywords: [array, numpy]
sources:
    - title: Array creation routines
      link: https://numpy.org/doc/stable/reference/routines.array-creation.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: creation_routines-0.py
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
"""
Extract a diagonal or construct a diagonal array.
See the more detailed documentation for `numpy.diagonal`
if you use this function to extract a diagonal
and wish to write to the resulting array;
whether it returns a copy or a view depends on what version of numpy you are using.

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

#%%
#%%   numpy.diagonal(a, offset=0, axis1=0, axis2=1)[source]
#     https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html
"""
    Return specified diagonals.

    If a is 2-D, returns the diagonal of a with the given offset, i.e., the collection of elements of the form a[i, i+offset]. If a has more than two dimensions, then the axes specified by axis1 and axis2 are used to determine the 2-D sub-array whose diagonal is returned. The shape of the resulting array can be determined by removing axis1 and axis2 and appending an index to the right equal to the size of the resulting diagonals.

    In versions of NumPy prior to 1.7, this function always returned a new, independent array containing a copy of the values in the diagonal.

    In NumPy 1.7 and 1.8, it continues to return a copy of the diagonal, but depending on this fact is deprecated. Writing to the resulting array continues to work as it used to, but a FutureWarning is issued.

    Starting in NumPy 1.9 it returns a read-only view on the original array. Attempting to write to the resulting array will produce an error.

    In some future release, it will return a read/write view and writing to the returned array will alter your original array. The returned array will have the same type as the input array.

    If you don’t write to the array returned by this function, then you can just ignore all of the above.

    If you depend on the current behavior, then we suggest copying the returned array explicitly, i.e., use np.diagonal(a).copy() instead of just np.diagonal(a). This will work with both past and future versions of NumPy.

Parameters

    aarray_like

        Array from which the diagonals are taken.
    offsetint, optional

        Offset of the diagonal from the main diagonal. Can be positive or negative. Defaults to main diagonal (0).
    axis1int, optional

        Axis to be used as the first axis of the 2-D sub-arrays from which the diagonals should be taken. Defaults to first axis (0).
    axis2int, optional

        Axis to be used as the second axis of the 2-D sub-arrays from which the diagonals should be taken. Defaults to second axis (1).

Returns

    array_of_diagonalsndarray

        If a is 2-D, then a 1-D array containing the diagonal and of the same type as a is returned unless a is a matrix, in which case a 1-D array rather than a (2-D) matrix is returned in order to maintain backward compatibility.

        If a.ndim > 2, then the dimensions specified by axis1 and axis2 are removed, and a new axis inserted at the end corresponding to the diagonal.

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
array([[0, 1],
       [2, 3]])

a.diagonal()
array([0, 3])

a.diagonal(1)
array([1])

A 3-D example:

a = np.arange(8).reshape(2,2,2); a
array([[[0, 1],
        [2, 3]],
       [[4, 5],
        [6, 7]]])

a.diagonal(0,  # Main diagonals of two arrays created by skipping

           0,  # across the outer(left)-most axis last and

           1)  # the "middle" (row) axis first.
array([[0, 6],
       [1, 7]])

The sub-arrays whose main diagonals we just obtained; note that each corresponds to fixing the right-most (column) axis, and that the diagonals are “packed” in rows.

a[:,:,0]  # main diagonal is [0 6]
array([[0, 2],
       [4, 6]])

a[:,:,1]  # main diagonal is [1 7]
array([[1, 3],
       [5, 7]])

The anti-diagonal can be obtained by reversing the order of elements using either numpy.flipud or numpy.fliplr.

a = np.arange(9).reshape(3, 3)

a
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

np.fliplr(a).diagonal()  # Horizontal flip
array([2, 4, 6])

np.flipud(a).diagonal()  # Vertical flip
array([6, 4, 2])

Note that the order in which the diagonal is retrieved varies depending on the flip function.

#%%
#%%



#%%
#%%
