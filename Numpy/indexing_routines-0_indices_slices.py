#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Indexing routines 0
subtitle: Indices, slices
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
    name: indexing_routines-0_indices_slices.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-25
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
#%%   numpy.s_ = <numpy.lib.index_tricks.IndexExpression object>
#%    np.lib.index_tricks.index_exp = <numpy.lib.index_tricks.IndexExpression object>
"""
A nicer way to build up index tuples for arrays.

Use one of the two predefined instances `index_exp` or `s_` rather than directly using `IndexExpression`.

For any index combination, including slicing and axis insertion,
    a[indices]   is the same as
    a[np.index_exp[indices]]   for any array a.
However,
    np.index_exp[indices]
can be used anywhere in Python code and returns a tuple of slice objects
that can be used in the construction of complex index expressions.

Parameters
maketuple : bool;    If True, always returns a tuple.

See also
index_exp
    Predefined instance that always returns a tuple: index_exp = IndexExpression(maketuple=True).
s_
    Predefined instance without tuple conversion: s_ = IndexExpression(maketuple=False).

Notes
You can do all this with slice() plus a few special objects,
but there’s a lot to remember and this version is simpler because it uses the standard array indexing syntax.
"""
sl = np.s_[2::2]
sl                  #  slice(2, None, 2)
ie = np.index_exp[2::2]
ie                  # (slice(2, None, 2),)

np.array([0, 1, 2, 3, 4])[sl]   # array([2, 4])
np.array([0, 1, 2, 3, 4])[ie]   #  "

#%%
np.lib.index_tricks.index_exp       # numpy.lib.index_tricks.IndexExpression
np.lib.index_tricks.s_              # numpy.lib.index_tricks.IndexExpression

np.lib.index_tricks.index_exp.maketuple     # True
np.lib.index_tricks.s_.maketuple            # False


#%%
#%%  class numpy.ndindex(*shape)
"""
An N-dimensional iterator object to index arrays.
Given the shape of an array,
an `ndindex` instance iterates over the N-dimensional index of the array.
At each iteration a tuple of indices is returned, the last dimension is iterated over first.

Parameters
shape : ints, or a single tuple of ints
    The size of each dimension of the array can be passed as individual parameters
    or as the elements of a tuple.

See also
ndenumerate(), flatiter()  in  indexing_routines-3_iteration.py  (big topic!)

Methods
ndincr()    Increment the multi-dimensional index by one.  -- do not use !!!
"""
np.ndindex(3)     # numpy.ndindex

list(np.ndindex(3))     # [(0,), (1,), (2,)]

# dimensions as individual arguments
list(np.ndindex(3, 2, 1))
# [(0, 0, 0), (0, 1, 0),  (1, 0, 0), (1, 1, 0),  (2, 0, 0), (2, 1, 0)]

# same dimensions - but in a tuple (3, 2, 1)
list(np.ndindex((3, 2, 1)))
# [(0, 0, 0), (0, 1, 0),  (1, 0, 0), (1, 1, 0),  (2, 0, 0), (2, 1, 0)]

arr = np.arange(np.prod([3, 4, 5])).reshape(3, 4, 5)
arr
[arr[idx] for idx in np.ndindex(3, 4, 5)]     # all elements
# BUT:
[arr[idx] for idx in np.ndindex(3, 2, 1)]     # !!!

#??? sth more useful ???


#%%
#%%   numpy.compress(condition, a, axis=None, out=None)[source]
"""
Return selected slices of an array along given axis.                        !!!  just like standard indexing !!!
When working along a given axis, a slice along that axis is returned in output
for each index where condition evaluates to True.
When working on a 1-D array, compress is equivalent to extract.

Parameters
condition : 1-D array of bools
    Array that selects which entries to return.
    If len(condition) is less than the size of a along the given axis,
    then output is truncated to the length of the condition array.          !!! maybe this is bit different then standard indexing
a : array_like
    Array from which to extract a part.
axis : int, optional
    Axis along which to take slices.
   !!!  If None (default), work on the __flattened__ array.    !!!
out : ndarray, optional
    Output array. Its type is preserved and it must be of the right shape to hold the output.

Returns
compressed_array : ndarray
    A copy of `a` without the slices along axis for which condition is false.

See also
take, choose, diag, diagonal, select
ndarray.compress()    Equivalent method in ndarray
extract               Equivalent method when working on 1-D arrays
"""
a = np.array([[1, 2], [3, 4], [5, 6]])
a

np.compress([0, 1], a, axis=0)      # array([[3, 4]])
a[1, :]                             # "

np.compress([False, True, True], a, axis=0)
#array([[3, 4],
#       [5, 6]])
a[[False, True, True], :]   # "

np.compress([False, True], a, axis=1)
#array([[2],
#       [4],
#       [6]])
a[:, [False, True]]     # "

# Working on the flattened array does not return slices along an axis but selects elements.
np.compress([False, True], a)
# array([2])

#???  what's the point if it all is the same as standard indexing (with very little difference) ???


#%%
#%%  numpy.choose(a, choices, out=None, mode='raise')[source]
"""
Construct an array from an index array and a list of arrays to choose from.
First of all, if confused or uncertain, definitely look at the Examples - in its full generality,
this function is less simple than it might seem from the following code description
(below ndi = numpy.lib.index_tricks):

    np.choose(a,c) == np.array([c[a[I]][I] for I in ndi.ndindex(a.shape)]).

But this omits some subtleties. Here is a fully general summary:

Given an “index” array (a) of integers and a sequence of n arrays (choices),
a and each choice array are first broadcast, as necessary, to arrays of a common shape;
calling these Ba and Bchoices[i], i = 0,…,n-1
we have that, necessarily, `Ba.shape == Bchoices[i].shape` for each i.
Then, a new array with shape `Ba.shape` is created as follows:
    if mode='raise' (the default), then, first of all, each element of a (and thus Ba) must be in the range [0, n-1];
        now, suppose that i (in that range) is the value at the (j0, j1, ..., jm) position in Ba
        - then the value at the same position in the new array is the value in Bchoices[i] at that same position;
    if mode='wrap', values in a (and thus Ba) may be any (signed) integer;
        modular arithmetic is used to map integers outside the range [0, n-1] back into that range; and then the new array is constructed as above;
    if mode='clip', values in a (and thus Ba) may be any (signed) integer;
        negative integers are mapped to 0; values greater than n-1 are mapped to n-1; and then the new array is constructed as above.

Parameters
a : int array
    This array must contain integers in [0, n-1], where n is the number of choices,
    unless `mode=wrap` or `mode=clip`, in which cases any integers are permissible.
choices : sequence of arrays
    Choice arrays.
    `a` and all of the choices must be broadcastable to the same shape.
    If `choices` is itself an array (not recommended),
    then its outermost dimension (i.e., the one corresponding to choices.shape[0])
    is taken as defining the “sequence”.
out : array, optional
    If provided, the result will be inserted into this array.
    It should be of the appropriate shape and dtype.
    Note that out is always buffered if mode='raise'; use other modes for better performance.
mode {‘raise’ (default), ‘wrap’, ‘clip’}, optional
    Specifies how indices outside [0, n-1] will be treated:
        ‘raise’ : an exception is raised
        ‘wrap’ : value becomes value mod n
        ‘clip’ : values < 0 are mapped to 0, values > n-1 are mapped to n-1

Returns
merged_array : array
    The merged result.

Raises
ValueError: shape mismatch
    If a and each choice array are not all broadcastable to the same shape.

See also
ndarray.choose()            equivalent method
numpy.take_along_axis()     Preferable if choices is an array      ??? !!!  see below in this file

Notes
To reduce the chance of misinterpretation, even though the following “abuse” is nominally supported,
`choices` should neither be, nor be thought of as a single array,
i.e., the outermost sequence-like container should be either a list or a tuple.
"""
choices = [[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]]
np.choose([2, 3, 1, 0], choices)
    # the first element of the result will be the first element of the
    # third (2+1) "array" in choices, namely, 20; the second element
    # will be the second element of the fourth (3+1) choice array, i.e.,
    # 31, etc.
# array([20, 31, 12,  3])

np.choose([2, 4, 1, 0], choices, mode='clip') # 4 goes to 3 (4-1)
# array([20, 31, 12,  3])

np.choose([2, 4, 1, 0], choices, mode='wrap') # 4 goes to (4 mod 4)
array([20,  1, 12,  3])

# A couple examples illustrating how choose broadcasts:
a = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
choices = [-10, 10]

np.choose(a, choices)
#array([[ 10, -10,  10],
#       [-10,  10, -10],
#       [ 10, -10,  10]])

# With thanks to Anne Archibald
a = np.array([0, 1]).reshape((2,1,1))
a
c1 = np.array([1, 2, 3]).reshape((1,3,1))
c1
c2 = np.array([-1, -2, -3, -4, -5]).reshape((1,1,5))
c2

np.choose(a, (c1, c2)) # result is 2x3x5, res[0,:,:]=c1, res[1,:,:]=c2
#array([[[ 1,  1,  1,  1,  1],
#        [ 2,  2,  2,  2,  2],
#        [ 3,  3,  3,  3,  3]],
#       [[-1, -2, -3, -4, -5],
#        [-1, -2, -3, -4, -5],
#        [-1, -2, -3, -4, -5]]])

#!!!  hence it may used as another way for creating grids  !!!

#%%
#%%   numpy.select(condlist, choicelist, default=0)[source]
"""
Return an array drawn from elements in choicelist, depending on conditions.

Parameters
condlist : list of __bool__ ndarrays        !!! for choose() we need int -- that's the difference
    The list of conditions which determine from which array in `choicelist` the output elements are taken.
    When multiple conditions are satisfied, the first one encountered in `condlist` is used.
choicelist : list of ndarrays
    The list of arrays from which the output elements are taken.
   !!!  It has to be of the same length as `condlist`.   !!!
default : scalar, optional
    The element inserted in output when all conditions evaluate to False.

Returns
output : ndarray
    The output at position m is the m-th element of the array in `choicelist`
    where the m-th element of the corresponding array in `condlist` is True.

See also
choose
where    Return elements from one of two arrays depending on condition.
take, compress, diag, diagonal

"""
x = np.arange(10)
x
condlist = [x<3, x>5]
condlist
choicelist = [x, x**2]
choicelist
np.select(condlist, choicelist)     # array([ 0,  1,  2,  0,  0,  0, 36, 49, 64, 81])
np.select(condlist, choicelist, default=None)     # array([ 0,  1,  2, None, None, None, 36, 49, 64, 81])

# works also with lists
np.select([[True,  True,  True, False, False, False, False, False, False, False],
           [False, False, False, False, False, False,  True,  True,  True, True]],
          choicelist)
np.select([[True,  True,  True, False, False, False, False, False, False, False],
           [False, False, False, False, False, False,  True,  True,  True, True]],
          [list(range(10)), [x**2 for x in range(10)]])
# but `condlist` should be logical values
np.select([[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]],  choicelist)
    #! __main__:3: DeprecationWarning: select condlists containing integer ndarrays is deprecated
    # and will be removed in the future. Use `.astype(bool)` to convert to bools.
np.select([np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0], dtype=bool),
           np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1], dtype=bool)],
           choicelist) # ok

# the same result as
np.choose( [0, 0, 0, 2, 2, 2, 1, 1, 1, 1], [x, x**2, np.zeros_like(x)])
np.choose( [0, 0, 0, 2, 2, 2, 1, 1, 1, 1], [x, x**2, [None]*len(x)])




#%%
#%%   numpy.take(a, indices, axis=None, out=None, mode='raise')
"""
      ndarray.take()      equivalent method

Take elements from an array along an axis.

When axis is not None, this function does the same thing as “fancy” indexing (indexing arrays using arrays);
however, it can be easier to use if you need elements along a given axis.
A call such as
    np.take(arr, indices, axis=3)
is equivalent to
    arr[:,:,:,indices,...]                      #!!!

Explained without fancy indexing, this is equivalent to the following use of `ndindex()`,
which sets each of i, j, and k to a tuple of indices:

Ni, Nk = a.shape[:axis], a.shape[axis+1:]
Nj = indices.shape
for i in ndindex(Ni):
    for j in ndindex(Nj):
        for k in ndindex(Nk):
            out[i + j + k] = a[i + (indices[j],) + k]

Parameters

a : array_like (Ni…, M, Nk…)
    The source array.
indices : array_like (Nj…)
    The indices of the values to extract.
    New in version 1.8.0.
    Also allow scalars for indices.
axis : int, optional
    The axis over which to select values. By default, the flattened input array is used.
out : ndarray, optional (Ni…, Nj…, Nk…)
    If provided, the result will be placed in this array.
    It should be of the appropriate shape and dtype.
    Note that out is always buffered if mode=’raise’;
    use other modes for better performance.
mode {‘raise’, ‘wrap’, ‘clip’}, optional
    Specifies how out-of-bounds indices will behave.
        ‘raise’ – raise an error (default)
        ‘wrap’ – wrap around
        ‘clip’ – clip to the range
    ‘clip’ mode means that all indices that are too large are replaced by the index
    that addresses the last element along that axis.
    Note that this disables indexing with negative numbers.

Returns
out : ndarray (Ni…, Nj…, Nk…)
    The returned array has the same type as a.

See also
compress()          Take elements using a boolean mask
ndarray.take()      equivalent method
take_along_axis()   Take elements by matching the array and the index arrays

Notes
By eliminating the inner loop in the description above,
and using s_ to build simple slice objects,
take can be expressed in terms of applying fancy indexing to each 1-d slice:

Ni, Nk = a.shape[:axis], a.shape[axis+1:]
for ii in ndindex(Ni):
    for kk in ndindex(Nj):
        out[ii + s_[...,] + kk] = a[ii + s_[:,] + kk][indices]

For this reason, it is equivalent to (but faster than) the following use of apply_along_axis:

out = np.apply_along_axis(lambda a_1d: a_1d[indices], axis, a)
"""
a = [4, 3, 5, 7, 6, 8]
indices = [0, 1, 4]

np.take(a, indices)     # array([4, 3, 6])

# In this example if a is an ndarray, “fancy” indexing can be used.
a = np.array(a)
a
a[indices]  # array([4, 3, 6])

# If indices is not one dimensional, the output also has these dimensions.
np.take(a, [[0, 1], [2, 3]])
#array([[4, 3],
#       [5, 7]])

#%%
axes = [3, 4, 3, 5, 2]
arr = np.arange(np.prod(axes)).reshape(axes)
arr.shape

arr0 = np.take(arr, [0], axis=2)
arr0.shape      # (3, 4, 1, 5, 2)
arr0

arr00 = np.take(arr, 0, axis=2)
arr00.shape      # (3, 4, 5, 2)             #!!!  one dim less  !!!  given slice with dim stripped off
arr00

arr2 = np.take(arr, [0, 2], axis=2)
arr2.shape      # (3, 4, 2, 5, 2)
arr2

#%%  without axis the input array is flattened (raveled)
np.ravel(arr)
np.take(arr, 0)     # 0
np.take(arr, 1)     # 1
np.take(arr, [0])       # array([0])
np.take(arr, [0, 1])    # array([0, 1])
np.take(arr, range(9))  # array([0, 1, 2, 3, 4, 5, 6, 7, 8])
np.take(arr, range(9, 99, 7))  # array([ 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93])
np.take(np.ravel(arr), range(9, 99, 7))  # the same

#%%
#%%  numpy.take_along_axis(arr, indices, axis)
"""
Take values from the input array by matching 1d index and data slices.
This iterates over matching 1d slices oriented along the specified axis
in the index and data arrays, and uses the former to look up values in the latter.
These slices can be different lengths.

Functions returning an index along an axis, like argsort and argpartition,
produce suitable indices for this function.
New in version 1.15.0.

Parameters

arr : ndarray (Ni…, M, Nk…)

    Source array
indices : ndarray (Ni…, J, Nk…)
    Indices to take along each 1d slice of arr. This must match the dimension of arr, but dimensions Ni and Nj only need to broadcast against arr.
axis : int
    The axis to take 1d slices along. If axis is None, the input array is treated as if it had first been flattened to 1d, for consistency with sort and argsort.

Returns
out : ndarray (Ni…, J, Nk…)
    The indexed result.

See also
take
    Take along an axis, using the same indices for every 1d slice
put_along_axis
    Put values into the destination array by matching 1d index and data slices

Notes
This is equivalent to (but faster than) the following use of ndindex and s_,
which sets each of i and k to a tuple of indices:

Ni, M, Nk = a.shape[:axis], a.shape[axis], a.shape[axis+1:]
J = indices.shape[axis]  # Need not equal M
out = np.empty(Ni + (J,) + Nk)

for i in ndindex(Ni):
    for k in ndindex(Nk):
        a_1d       = a      [i + s_[:,] + k]
        indices_1d = indices[i + s_[:,] + k]
        out_1d     = out    [i + s_[:,] + k]
        for j in range(J):
            out_1d[j] = a_1d[indices_1d[j]]

Equivalently, eliminating the inner loop, the last two lines would be:
out_1d[:] = a_1d[indices_1d]
"""
# For this sample array
a = np.array([[10, 30, 20], [60, 40, 50]])
a

# We can sort either by using sort directly, or `argsort` and this function
np.sort(a, axis=1)
#array([[10, 20, 30],
#       [40, 50, 60]])

ai = np.argsort(a, axis=1); ai
#array([[0, 2, 1],
#       [1, 2, 0]])

np.take_along_axis(a, ai, axis=1)
#array([[10, 20, 30],
#       [40, 50, 60]])

# The same works for max and min, if you expand the dimensions:
np.expand_dims(np.array([0, 1]), axis=0)    # array([[0, 1]])
np.expand_dims(np.array([0, 1]), axis=1)    # array([[0], [1]])
np.expand_dims(np.array([[0, 1], [2, 3]]), axis=0)  # array([  [[0,  1], [2,   3]]  ])
np.expand_dims(np.array([[0, 1], [2, 3]]), axis=1)  # array([ [[0,   1]], [[2,   3]] ])
np.expand_dims(np.array([[0, 1], [2, 3]]), axis=2)  # array([[ [0], [1] ],  [ [2], [3] ]])

np.max(a, axis=1)
np.expand_dims(np.max(a, axis=1), axis=1)
#array([[30],
#       [60]])

np.argmax(a, axis=1)
ai = np.expand_dims(np.argmax(a, axis=1), axis=1)
ai
#array([[1],
#       [0]])
np.take_along_axis(a, ai, axis=1)
#array([[30],
#       [60]])
np.take_along_axis(a, np.argmax(a, axis=1), axis=1)     #! ValueError: `indices` and `arr` must have the same number of dimensions


# If we want to get the max and min at the same time, we can stack the indices first
ai_min = np.expand_dims(np.argmin(a, axis=1), axis=1)
ai_max = np.expand_dims(np.argmax(a, axis=1), axis=1)
ai = np.concatenate([ai_min, ai_max], axis=1)
ai
#array([[0, 1],
#       [1, 0]])

np.take_along_axis(a, ai, axis=1)
#array([[10, 30],
#       [40, 60]])

#%%
#%%



#%%
#%%
#   STRANGE THINGS...
