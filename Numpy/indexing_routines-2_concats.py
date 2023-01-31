#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Indexing routines 2
subtitle: Concatenatins
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
    name: indexing_routines-2_concats.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-21
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
#%%  numpy.r_ = <numpy.lib.index_tricks.RClass object>
"""
Translates slice objects to concatenation along the first axis.

This is a simple way to build up arrays quickly. There are two use cases.
1. If the index expression contains comma separated arrays, then stack them __along their FIRST axis__.
2. If the index expression contains slice notation or scalars then create a 1-D array
   with a range indicated by the slice notation.

If slice notation is used,
the syntax start:stop:step is equivalent to np.arange(start, stop, step) inside of the brackets.
However, if step is an imaginary number (i.e. 100j)
then its integer portion is interpreted as a number-of-points desired
and the start and stop are inclusive.
In other words start:stop:stepj is interpreted as np.linspace(start, stop, step, endpoint=1)
inside of the brackets.
After expansion of slice notation, all comma separated sequences are concatenated together.

Optional character strings placed as the first element of the index expression can be used to change the output.
The strings ‘r’ or ‘c’ result in matrix output.
If the result is 1-D and ‘r’ is specified a 1 x N (row) matrix is produced.
If the result is 1-D and ‘c’ is specified, then a N x 1 (column) matrix is produced.
If the result is 2-D then both provide the same matrix result.

A string integer specifies which axis to stack multiple comma separated arrays along.
A string of two comma-separated integers allows indication of the minimum number of dimensions
to force each entry into as the second integer (the axis to concatenate along is still the first integer).

A string with three comma-separated integers allows
1. specification of the axis to concatenate along,
2. the minimum number of dimensions to force the entries to,
and
3. which axis should contain the start of the arrays which are less than the specified number of dimensions.
In other words the third integer allows you to specify where the 1’s should be placed
in the shape of the arrays that have their shapes upgraded.
By default, they are placed in the front of the shape tuple.
The third argument allows you to specify where the start of the array should be instead.
 Thus, a third argument of ‘0’ would place the 1’s at the end of the array shape.
 Negative integers specify where in the new shape tuple
the last dimension of upgraded arrays should be placed, so the default is ‘-1’.

Parameters
    Not a function, so takes no parameters

Returns
    A concatenated ndarray or matrix.

See also
concatenate
    Join a sequence of arrays along an existing axis.
c_
    Translates slice objects to concatenation along the second axis.
"""

np.r_[np.array([1,2,3]), 0, 0, np.array([4,5,6])]
# array([1, 2, 3, 0, 0, 4, 5, 6])

np.r_[-1:1:6j, [0]*3, 5, 6]
# array([-1. , -0.6, -0.2,  0.2,  0.6,  1. ,  0. ,  0. ,  0. ,  5. ,  6. ])

# String integers specify the axis to concatenate along or the minimum number of dimensions to force entries into.

a = np.array([[0, 1, 2], [3, 4, 5]])

np.r_[a, a]       # concatenate along first axis
np.r_['0', a, a]  # concatenate along first axis
np.r_['1', a, a]  # concatenate along second axis
np.r_['-1', a, a] # concatenate along last axis
#array([[0, 1, 2, 0, 1, 2],
#       [3, 4, 5, 3, 4, 5]])

np.r_[[1,2,3], [4,5,6]]
np.r_['1', [1,2,3], [4,5,6]]   # AxisError: axis 1 is out of bounds for array of dimension 1
np.r_['0,2', [1,2,3], [4,5,6]] # concatenate along first axis, dim>=2
#array([[1, 2, 3],
#       [4, 5, 6]])
#!!! hence it adds dimensinos first !!!
np.r_['1,2', [1,2,3], [4,5,6]] # concatenate along second axis, dim>=2

np.r_['0,2,0', [1,2,3], [4,5,6]]
#array([[1],
#       [2],
#       [3],
#       [4],
#       [5],
#       [6]])
np.r_['0,2,-1', [1,2,3], [4,5,6]]
#array([[1, 2, 3],
#       [4, 5, 6]])
np.r_['0,2,1', [1,2,3], [4,5,6]]
# the same

np.r_['1,2,0', [1,2,3], [4,5,6]]
#array([[1, 4],
#       [2, 5],
#       [3, 6]])
np.r_['1,2,1', [1,2,3], [4,5,6]]
#array([[1, 2, 3, 4, 5, 6]])

a3 = np.expand_dims(a, 2)
a3
np.r_['2,3', a3, a3, a3]


# Using ‘r’ or ‘c’ as a first string argument creates a matrix.

np.r_['r',[1,2,3], [4,5,6]]
# matrix([[1, 2, 3, 4, 5, 6]])
np.r_['c',[1,2,3], [4,5,6]]
#matrix([[1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6]])

#%%
#%%  numpy.c_ = <numpy.lib.index_tricks.CClass object>
"""
Translates slice objects to concatenation along the second axis.
This is short-hand for
    np.r_['-1,2,0', index expression]
which is useful because of its common occurrence.

In particular, arrays will be stacked along their last axis
after being upgraded to at least 2-D with 1’s post-pended to the shape
(column vectors made out of 1-D arrays).

See also
column_stack
    Stack 1-D arrays as columns into a 2-D array.
r_
    For more detailed documentation.
"""
np.c_[np.array([1,2,3]), np.array([4,5,6])]
#array([[1, 4],
#       [2, 5],
#       [3, 6]])
np.r_['-1,2,0', np.array([1,2,3]), np.array([4,5,6])]
np.r_['1,2,0', np.array([1,2,3]), np.array([4,5,6])]
np.r_['0,2,0', np.array([1,2,3]), np.array([4,5,6])]
#array([[1],
#       [2],
#       [3],
#       [4],
#       [5],
#       [6]])

np.c_[np.array([[1,2,3]]), 0, 0, np.array([[4,5,6]])]
#array([[1, 2, 3, 0, 0, 4, 5, 6]])

np.expand_dims(np.array([1,2,3]), 0)
np.expand_dims(np.array([1,2,3]), -1)
np.expand_dims(np.array([1,2,3]), 1)

#%%
#%%  numpy.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, casting="same_kind")
"""
Join a sequence of arrays along an existing axis.

Parameters
a1, a2, … : sequence of array_like
    The arrays must have the same shape, except in the dimension corresponding to axis (the first, by default).
axis : int, optional;   Default is 0.
    The axis along which the arrays will be joined.
    If axis is None, arrays are flattened before use.
out : ndarray, optional
    If provided, the destination to place the result.
    The shape must be correct, matching that of what concatenate would have returned
    if no out argument were specified.
dtype : str or dtype
    If provided, the destination array will have this dtype.
   !!! Cannot be provided together with `out`.
    New in version 1.20.0.
casting {‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’}, optional
    Controls what kind of data casting may occur. Defaults to ‘same_kind’.
    New in version 1.20.0.

Returns
res : ndarray
    The concatenated array.

See also
ma.concatenate  Concatenate function that preserves input masks.
array_split     Split an array into multiple sub-arrays of equal or near-equal size.
split           Split an array into a list of multiple sub-arrays of equal size.
hsplit          Split array into multiple sub-arrays horizontally (column wise).
vsplit          Split array into multiple sub-arrays vertically (row wise).
dsplit          Split array into multiple sub-arrays along the 3rd axis (depth).
stack           Stack a sequence of arrays along a new axis.
block           Assemble arrays from blocks.
hstack          Stack arrays in sequence horizontally (column wise).
vstack          Stack arrays in sequence vertically (row wise).
dstack          Stack arrays in sequence depth wise (along third dimension).
column_stack    Stack 1-D arrays as columns into a 2-D array.

Notes
When one or more of the arrays to be concatenated is a MaskedArray,
this function will return a MaskedArray object instead of an ndarray,
!!!  but the input masks are not preserved.  !!!
In cases where a MaskedArray is expected as input,
use the `ma.concatenate` function from the masked array module instead.
"""
a = np.array([[1, 2], [3, 4]])
a
b = np.array([[5, 6]])
b

np.concatenate((a, b), axis=0)
#array([[1, 2],
#       [3, 4],
#       [5, 6]])

np.concatenate((a, b.T), axis=1)
#array([[1, 2, 5],
#       [3, 4, 6]])

np.concatenate((a, b), axis=None)
# array([1, 2, 3, 4, 5, 6])

# This function will not preserve masking of MaskedArray inputs.
a = np.ma.arange(3)
a
a[1] = np.ma.masked
a
#masked_array(data=[0, --, 2],
#             mask=[False,  True, False],
#       fill_value=999999)

# BTW:
np.ma.masked   # masked
type(np.ma.masked)   # numpy.ma.core.MaskedConstant
dir(np.ma.masked)
# see  https://numpy.org/doc/stable/user/tutorial-ma.html

b = np.arange(2, 5)
b
array([2, 3, 4])

np.concatenate([a, b])
#masked_array(data=[0, 1, 2, 2, 3, 4],
#             mask=False,
#       fill_value=999999)

np.ma.concatenate([a, b])
#masked_array(data=[0, --, 2, 2, 3, 4],
#             mask=[False,  True, False, False, False, False],
#       fill_value=999999)

#%%



#%%



#%%



#%%



#%%
