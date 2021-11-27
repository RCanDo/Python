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

title: ufunc - Universal Functions
version: 1.0
type: tutorial
keywords: [ufunc, function, broadcasting, ]
sources:
    - title: Universal functions (ufunc)
      link: https://numpy.org/doc/stable/reference/ufuncs.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: ufunc.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-19
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import numpy as np

#%%
... a lot of ...

#%% Optional keyword arguments
"""

"""

#%%
#%% Attributes
"""
There are some informational attributes that universal functions possess.
None of the attributes can be set.
__doc__             A docstring for each ufunc. The first part of the docstring is dynamically generated from the number of outputs, the name, and the number of inputs. The second part of the docstring is provided at creation time and stored with the ufunc.
__name__            The name of the ufunc.
ufunc.nin           The number of inputs.
ufunc.nout          The number of outputs.
ufunc.nargs         The number of arguments.
ufunc.ntypes        The number of types.
ufunc.types         Returns a list with types grouped input->output.
ufunc.identity      The identity value.
ufunc.signature     Definition of the core elements a generalized ufunc operates on.
"""

#%%
#%%  Optional keyword arguments
"""
All ufuncs take optional keyword arguments.
Most of these represent advanced usage and will not typically be used.

 out

New in version 1.6.
The first output can be provided as either a positional or a keyword parameter.
Keyword ‘out’ arguments are incompatible with positional ones.

New in version 1.10.
The ‘out’ keyword argument is expected to be a tuple with one entry per output
(which can be None for arrays to be allocated by the ufunc).
For ufuncs with a single output, passing a single array (instead of a tuple holding a single array) is also valid.

Passing a single array in the ‘out’ keyword argument to a ufunc with multiple outputs is deprecated,
and will raise a warning in numpy 1.10, and an error in a future release.

If ‘out’ is None (the default), a uninitialized return array is created.
The output array is then filled with the results of the ufunc in the places that the broadcast ‘where’ is True.
If ‘where’ is the scalar True (the default), then this corresponds to the entire output being filled.
Note that outputs not explicitly filled are left with their uninitialized values.

New in version 1.13.
Operations where ufunc input and output operands have memory overlap are defined to be the same
as for equivalent operations where there is no memory overlap.
Operations affected make temporary copies as needed to eliminate data dependency.
As detecting these cases is computationally expensive, a heuristic is used,
which may in rare cases result in needless temporary copies.
For operations where the data dependency is simple enough for the heuristic to analyze,
temporary copies will not be made even if the arrays overlap,
if it can be deduced copies are not necessary.
As an example, np.add(a, b, out=a) will not involve copies.

 where

New in version 1.7.
Accepts a boolean array which is broadcast together with the operands.
Values of True indicate to calculate the ufunc at that position,
values of False indicate to leave the value in the output alone.
This argument cannot be used for generalized ufuncs as those take non-scalar input.

Note that if an uninitialized return array is created, values of False will leave those values uninitialized.

 axes

New in version 1.15.
A list of tuples with indices of axes a generalized ufunc should operate on.
For instance, for a signature of (i,j),(j,k)->(i,k) appropriate for matrix multiplication,
the base elements are two-dimensional matrices and these are taken to be stored in the two last axes of each argument.
The corresponding axes keyword would be [(-2, -1), (-2, -1), (-2, -1)].
For simplicity, for generalized ufuncs that operate on 1-dimensional arrays (vectors),
a single integer is accepted instead of a single-element tuple,
and for generalized ufuncs for which all outputs are scalars, the output tuples can be omitted.

 axis

New in version 1.15.
A single axis over which a generalized ufunc should operate.
This is a short-cut for ufuncs that operate over a single, shared core dimension,
equivalent to passing in axes with entries of (axis,)
for each single-core-dimension argument and () for all others.
For instance, for a signature (i),(i)->(), it is equivalent to passing in axes=[(axis,), (axis,), ()].

 keepdims

New in version 1.15.
If this is set to True, axes which are reduced over will be left in the result as a dimension with size one,
so that the result will broadcast correctly against the inputs.
This option can only be used for generalized ufuncs that operate on inputs
that all have the same number of core dimensions and with outputs that have no core dimensions,
i.e., with signatures like (i),(i)->() or (m,m)->().
If used, the location of the dimensions in the output can be controlled with axes and axis.

 casting

New in version 1.6.
May be ‘no’, ‘equiv’, ‘safe’, ‘same_kind’, or ‘unsafe’. See can_cast for explanations of the parameter values.
Provides a policy for what kind of casting is permitted. For compatibility with previous versions of NumPy, this defaults to ‘unsafe’ for numpy < 1.7. In numpy 1.7 a transition to ‘same_kind’ was begun where ufuncs produce a DeprecationWarning for calls which are allowed under the ‘unsafe’ rules, but not under the ‘same_kind’ rules. From numpy 1.10 and onwards, the default is ‘same_kind’.

 order

New in version 1.6.
Specifies the calculation iteration order/memory layout of the output array. Defaults to ‘K’. ‘C’ means the output should be C-contiguous, ‘F’ means F-contiguous, ‘A’ means F-contiguous if the inputs are F-contiguous and not also not C-contiguous, C-contiguous otherwise, and ‘K’ means to match the element ordering of the inputs as closely as possible.

 dtype

New in version 1.6.
Overrides the DType of the output arrays the same way as the signature. This should ensure a matching precision of the calculation. The exact calculation DTypes chosen may depend on the ufunc and the inputs may be cast to this DType to perform the calculation.

 subok

New in version 1.6.
Defaults to true. If set to false, the output will always be a strict array, not a subtype.

 signature

Either a Dtype, a tuple of DTypes, or a special signature string indicating the input and output types of a ufunc.

This argument allows the user to specify exact DTypes to be used for the calculation. Casting will be used as necessary. The actual DType of the input arrays is not considered unless signature is None for that array.

When all DTypes are fixed, a specific loop is chosen or an error raised if no matching loop exists. If some DTypes are not specified and left None, the behaviour may depend on the ufunc. At this time, a list of available signatures is provided by the types attribute of the ufunc. (This list may be missing DTypes not defined by NumPy.)

The signature only specifies the DType class/type. For example, it can specifiy that the operation should be datetime64 or float64 operation. It does not specify the datetime64 time-unit or the float64 byte-order.

For backwards compatibility this argument can also be provided as sig, although the long form is preferred. Note that this should not be confused with the generalized ufunc signature that is stored in the signature attribute of the of the ufunc object.

 extobj

a list of length 3 specifying the ufunc buffer-size, the error mode integer, and the error call-back function. Normally, these values are looked up in a thread-specific dictionary. Passing them here circumvents that look up and uses the low-level specification provided for the error mode. This may be useful, for example, as an optimization for calculations requiring many ufunc calls on small arrays in a loop.
"""

#%%
#   METHODS
#
#%%  ufunc.at(a, indices, b=None, /)
"""
Performs __unbuffered__ __in place__ operation on operand ‘a’ for elements specified by ‘indices’.
For addition ufunc, this method is equivalent to `a[indices] += b`,
except that results are __accumulated__ for elements that are indexed more than once.
For example, `a[[0,0]] += 1` will only increment the first element once __because of buffering__,
whereas `add.at(a, [0,0], 1)` will increment the first element twice.

Parameters
a : array_like;    The array to perform in place operation on.
indices : array_like or tuple
    Array like index object or slice object for indexing into first operand.
    If first operand has multiple dimensions,
    indices can be a tuple of array like index objects or slice objects.
b : array_like
    Second operand for ufuncs requiring two operands.
    Operand must be broadcastable over first operand after indexing or slicing.
"""
# Set items 0 and 1 to their negative values:
a = np.array([1, 2, 3, 4])
a
np.negative.at(a, [0, 1])
a   # array([-1, -2,  3,  4])
# the same as
a[a<0] = -a[a<0]
a

a = np.array([1, 2, 3, 4])
np.negative.at(a, [0, 1, 1])
a   # array([-1,  2,  3,  4])

# Increment items 0 and 1, and increment item 2 twice:
a = np.array([1, 2, 3, 4])
a
np.add.at(a, [0, 1, 2, 2], 1)
a   # array([2, 3, 5, 4])

# Add items 0 and 1 in first array to second array, and store results in first array:
a = np.array([1, 2, 3, 4])
b = np.array([1, 2])
np.add.at(a, [0, 1], b)
a   # array([2, 4, 3, 4])


#%%
#%%  ufunc.reduce(array, axis=0, dtype=None, out=None, keepdims=False, initial=<no value>, where=True)
"""
Reduces array’s dimension by one, by applying ufunc along one axis.
For a one-dimensional array, reduce produces results equivalent to:
"""
r = op.identity     # op = ufunc
for i in range(len(A)):
  r = op(r, A[i])
return r
"""
For example, add.reduce() is equivalent to sum().
"""
nn = np.arange(12).reshape((3, 4))
nn
#
np.add.reduce(nn)   # array([12, 15, 18, 21])
np.add.reduce(nn, axis=None)   # 66
sum(nn)             # array([12, 15, 18, 21])
np.sum(nn)          # 66
np.sum(nn, axis=0)  # array([12, 15, 18, 21])
np.sum.reduce(nn, axis=0)  #! AttributeError: 'function' object has no attribute 'reduce' -- it's not `ufunc`
np.apply_along_axis(np.sum, 0, nn)

np.add.reduce(nn, axis=1)   # array([ 6, 22, 38])
np.apply_along_axis(np.sum, 1, nn)
np.apply_along_axis(sum, 1, nn)
sum(nn, axis=1)   #! TypeError: sum() takes no keyword arguments
np.sum(nn, axis=1)          # array([ 6, 22, 38])

"""
Parameters
array : array_like;    The array to act on.
axis : None or int or tuple of ints, optional;
    Axis or axes along which a reduction is performed.
    The default (axis = 0) is perform a reduction over the first dimension of the input array.
    axis may be negative, in which case it counts from the last to the first axis.
    If this is None, a reduction is performed over all the axes.
    If this is a tuple of ints, a reduction is performed on multiple axes,
    instead of a single axis or all the axes as before.
   !!!  For operations which are either not commutative or not associative,  !!!
    doing a reduction over multiple axes is not well-defined.
    The ufuncs do not currently raise an exception in this case, but will likely do so in the future.
dtype : data-type code, optional;
    The type used to represent the __intermediate results__.
    Defaults to the data-type of the output array if this is provided,
    or the data-type of the input array if no output array is provided.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result is stored.
    If not provided or None, a freshly-allocated array is returned.
   !!!  For consistency with ufunc.__call__, if given as a keyword,  !!!
    this may be wrapped in a 1-element tuple.
keepdims: bool, optional
    If this is set to True, the axes which are reduced are left in the result
    as dimensions with size one.
    With this option, the result will broadcast correctly against the original array.
    New in version 1.7.0.
initial : scalar, optional
    The value with which to start the reduction.
    If the ufunc has no `identity` or the dtype is object, this defaults to None
    - otherwise it defaults to `ufunc.identity`.
   !!!  If None is given, the first element of the reduction is used,  !!!
    and an error is thrown if the reduction is empty.
where : array_like of bool, optional
    A boolean array which is broadcasted to match the dimensions of array,
    and selects elements to include in the reduction.
   !!!  Note that for ufuncs like minimum that do not have an identity defined,  !!!
    one has to pass in also initial.
Returns
r : ndarray;    The reduced array. If out was supplied, r is a reference to it.
"""
np.multiply.reduce([2,3,5])   # 30

# A multi-dimensional array example:
X = np.arange(8).reshape((2,2,2))
X
#array([[[0, 1],
#        [2, 3]],
#       [[4, 5],
#        [6, 7]]])
np.add.reduce(X, 0)   # axis=0 is default
#array([[ 4,  6],
#       [ 8, 10]])
np.add.reduce(X)      # the same

np.add.reduce(X, 1)
#array([[ 2,  4],
#       [10, 12]])

np.minimum.reduce(X, 0)
#array([[0, 1],
#       [2, 3]])
np.minimum.reduce(X, 1)
#array([[0, 1],
#       [4, 5]])

np.add.reduce(X, 2)
#array([[ 1,  5],
#       [ 9, 13]])

# You can use the initial keyword argument to initialize the reduction with a different value,
# and where to select specific elements to include:
np.add.reduce([10], initial=5)    # 15

np.add.reduce(np.ones((2, 2, 2)), axis=(0, 2), initial=10)  # array([14., 14.])

a = np.array([10., np.nan, 10])
np.add.reduce(a, where=~np.isnan(a))    #!!! 20.0             !!!

# Allows reductions of empty arrays where they would normally fail, i.e. for ufuncs without an identity.
np.minimum.reduce([], initial=np.inf)   # inf

np.minimum.reduce([[9., 11.], [13., 14.]])   # array([ 9., 11.])
np.minimum.reduce([[9., 11.], [13., 14.]], keepdims=True)   # array([[ 9., 11.]])
np.minimum.reduce([[9., 11.], [13., 14.]], initial=10., keepdims=True)   # array([[ 9., 10.]])
np.minimum.reduce([[9., 11.], [13., 14.]], where=[True, False])   #! ValueError: reduction operation 'minimum' does not have an identity, so to use a where mask one has to specify 'initial'
np.minimum.reduce([[9., 11.], [13., 14.]], initial=10., where=[True, False])   # array([ 9., 10.])
np.minimum.reduce([[9., 11.], [13., 14.]], initial=10., where=[False, True])   # array([ 10., 10.])
np.minimum.reduce([])  #! ValueError: zero-size array to reduction operation minimum which has no identity

#%%
#%%   ufunc.reduceat(array, indices, axis=0, dtype=None, out=None)
"""
Performs a (local) reduce with specified slices over a single axis.
"""
for i in range(len(indices)):
    reduceat(...) computes ufunc.reduce(array[indices[i]:indices[i+1]]),
"""
which becomes the i-th generalized “row” parallel to axis in the final result
(i.e., in a 2-D array, for example, if axis = 0,
it becomes the i-th row, but if axis = 1, it becomes the i-th column).
There are three exceptions to this:
1. when i = len(indices) - 1 (so for the last index), indices[i+1] = array.shape[axis].
2. if indices[i] >= indices[i + 1], the i-th generalized “row” is simply array[indices[i]].
3. if indices[i] >= len(array) or indices[i] < 0, an error is raised.
The shape of the output depends on the size of indices,
and may be larger than array (this happens if len(indices) > array.shape[axis]).

Parameters
array : array_like;    The array to act on.
indices : array_like;    Paired indices, comma separated (not colon), specifying slices to reduce.
axis : int, optional;    The axis along which to apply the reduceat.
dtype : data-type code, optional
    The type used to represent the intermediate results.
    Defaults to the data type of the output array if this is provided,
    or the data type of the input array if no output array is provided.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result is stored.
    If not provided or None, a freshly-allocated array is returned.
    For consistency with ufunc.__call__, if given as a keyword, this may be wrapped in a 1-element tuple.

Returns
r : ndarray;    The reduced values. If out was supplied, r is a reference to out.

Notes
If array is 1-D, the function ufunc.accumulate(array)
is the same as ufunc.reduceat(array, indices)[::2] where indices is range(len(array) - 1)
with a zero placed in every other element:
    indices = zeros(2 * len(array) - 1),
    indices[1::2] = range(1, len(array)).
Don’t be fooled by this attribute’s name:
reduceat(array) is not necessarily smaller than array.
"""

np.add.reduceat(np.arange(8),[0,4, 1,5, 2,6, 3,7])
array([ 6,  4, 10,  5, 14,  6, 18,  7], dtype=int32)

# To take the running sum of four successive values:
np.add.reduceat(np.arange(8),[0,4, 1,5, 2,6, 3,7])[::2]
# array([ 6, 10, 14, 18])

# A 2-D example:
x = np.arange(16).reshape(4,4)
x
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11],
#       [12, 13, 14, 15]])

# reduce such that the result has the following five rows:
# [row1 + row2 + row3]
# [row4]
# [row2]
# [row3]
# [row1 + row2 + row3 + row4]
np.add.reduceat(x, [0, 3, 1, 2, 0])
#array([[12, 15, 18, 21],
#       [12, 13, 14, 15],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11],
#       [24, 28, 32, 36]], dtype=int32)

# reduce such that result has the following two columns:
# [col1 * col2 * col3, col4]

np.multiply.reduceat(x, [0, 3], 1)
#array([[   0,    3],
#       [ 120,    7],
#       [ 720,   11],
#       [2184,   15]], dtype=int32)

#%%
#%%  ufunc.accumulate(array, axis=0, dtype=None, out=None)
"""
Accumulate the result of applying the operator to all elements.
For a one-dimensional array, accumulate produces results equivalent to:
"""
r = np.empty(len(A))
t = op.identity        # op = the ufunc being applied to A's  elements
for i in range(len(A)):
    t = op(t, A[i])
    r[i] = t
return r
"""
For example, add.accumulate() is equivalent to np.cumsum().
For a multi-dimensional array,
accumulate is applied along only one axis (axis zero by default; see Examples below)
so repeated use is necessary if one wants to accumulate over multiple axes.

Parameters
array : array_like;    The array to act on.
axis : int, optional
    The axis along which to apply the accumulation; default is zero.
dtype : data-type code, optional
    The data-type used to represent the intermediate results.
    Defaults to the data-type of the output array if such is provided,
    or the the data-type of the input array if no output array is provided.
out : ndarray, None, or tuple of ndarray and None, optional
    A location into which the result is stored.
    If not provided or None, a freshly-allocated array is returned.
    For consistency with ufunc.__call__, if given as a keyword, this may be wrapped in a 1-element tuple.

Returns
rndarray
    The accumulated values. If out was supplied, r is a reference to out.
"""
# 1-D array examples:
np.add.accumulate([2, 3, 5])    # array([ 2,  5, 10])
np.multiply.accumulate([2, 3, 5])   # array([ 2,  6, 30])

# 2-D array examples:
I = np.eye(2)

# Accumulate along axis 0 (rows), down columns:
np.add.accumulate(I, 0)  # axis=0 is  default
#array([[1.,  0.],
#       [1.,  1.]])

# Accumulate along axis 1 (columns), through rows:
np.add.accumulate(I, 1)
#array([[1.,  1.],
#       [0.,  1.]])

np.add.accumulate(np.add.accumulate(I, 1))
#array([[1., 1.],
#       [1., 2.]])

#%%
#%%  ufunc.outer(A, B, /, **kwargs)
"""
Apply the ufunc op to all pairs (a, b) with a in A and b in B.

Let M = A.ndim, N = B.ndim.
Then the result, C, of op.outer(A, B) is an array of dimension M + N such that:
For A and B one-dimensional, this is equivalent to:
"""
r = empty(len(A),len(B))
for i in range(len(A)):
    for j in range(len(B)):
        r[i,j] = op(A[i], B[j])  # op = ufunc in question
"""
Parameters
A : array_like:    First array
B : array_like;    Second array
kwargs : any
    Arguments to pass on to the ufunc.
    Typically dtype or out.
    See ufunc for a comprehensive overview of all available arguments.

Returns
r : ndarray;    Output array

See also
numpy.outer
    A less powerful version of np.multiply.outer that ravels all inputs to 1D. This exists primarily for compatibility with old code.
tensordot
    np.tensordot(a, b, axes=((), ())) and np.multiply.outer(a, b) behave same for all dimensions of a and b.
"""
np.multiply.outer([1, 2, 3], [4, 5, 6])
#array([[ 4,  5,  6],
#       [ 8, 10, 12],
#       [12, 15, 18]])

# A multi-dimensional example:
A = np.array([[1, 2, 3], [4, 5, 6]])
A.shape     # (2, 3)
B = np.array([[1, 2, 3, 4]])
B.shape     # (1, 4)
C = np.multiply.outer(A, B)
C.shape     # (2, 3, 1, 4)
C
array([[[[ 1,  2,  3,  4]],
        [[ 2,  4,  6,  8]],
        [[ 3,  6,  9, 12]]],
       [[[ 4,  8, 12, 16]],
        [[ 5, 10, 15, 20]],
        [[ 6, 12, 18, 24]]]])

#%%
#%%