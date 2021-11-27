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

title: Functional programming
version: 1.0
type: tutorial
keywords: [array, numpy,]
sources:
    - title: Functional programming
      link: https://numpy.org/doc/stable/reference/routines.functional.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: functional.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-16
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import numpy as np

#%%
#%%  numpy.apply_along_axis(func1d, axis, arr, *args, **kwargs)
"""
Apply a function `func1d` to 1-D slices along the given axis.

Execute func1d(a, *args, **kwargs) where func1d operates
on 1-D arrays and a is a 1-D slice of arr along axis.

This is equivalent to (but faster than) the following use of ndindex and s_,
which sets each of ii, jj, and kk to a tuple of indices:
"""
Ni, Nk = a.shape[:axis], a.shape[axis + 1:]
for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        f = func1d(arr[ii + s_[:,] + kk])
        Nj = f.shape
        for jj in ndindex(Nj):
            out[ii + jj + kk] = f[jj]

#! Equivalently, eliminating the inner loop, this can be expressed as:

Ni, Nk = a.shape[:axis], a.shape[axis + 1:]
for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        out[ii + s_[...,] + kk] = func1d(arr[ii + s_[:,] + kk])

#%%
def my_func(a):
    """Average first and last element of a 1-D array"""
    return (a[0] + a[-1]) * 0.5

b = np.array([[1,2,3], [4,5,6], [7,8,9]])
b

#%%
np.apply_along_axis(my_func, 0, b)   # array([4., 5., 6.])

np.apply_over_axes(my_func, b, [0])  #! TypeError: my_func() takes 1 positional argument but 2 were given
#! see below

#%%
np.apply_along_axis(my_func, 1, b)   # array([2., 5., 8.])

#%%
np.apply_along_axis(np.sum, 0, b)   # array([12, 15, 18])
np.apply_along_axis(sum, 0, b)      # array([12, 15, 18])

np.apply_over_axes(np.sum, b, [0])  # array([[12, 15, 18]])
np.apply_over_axes(sum, b, [0])     # array([[12, 15, 18]])

#%%
np.apply_along_axis(tuple, 0, b)   # no changes as array(tuples) -> array(lists)

#%% For a function that returns a 1D array, the number of dimensions in outarr is the same as arr.
b = np.array([[8,1,7], [4,3,9], [5,2,6]])

np.apply_along_axis(sorted, 1, b)
# array([[1, 7, 8],
#        [3, 4, 9],
#        [2, 5, 6]])

#%% For a function that returns a higher dimensional array,
# those dimensions are inserted in place of the axis dimension.

b = np.array([[1,2,3], [4,5,6], [7,8,9]])

np.apply_along_axis(np.diag, -1, b)   # ? -1 ?
np.apply_along_axis(np.diag, 1, b)    # the same but clear
#array([[[1, 0, 0],
#        [0, 2, 0],
#        [0, 0, 3]],
#       [[4, 0, 0],
#        [0, 5, 0],
#        [0, 0, 6]],
#       [[7, 0, 0],
#        [0, 8, 0],
#        [0, 0, 9]]])


#%%
#%%  numpy.apply_over_axes(func, a, axes)[source]
"""
Apply a function repeatedly over multiple axes.

 !!!  `func`  is called as  `res = func(a, axis)`,  !!!
where `axis` is the first element of `axes`.
The result `res` of the function call must have either the same dimensions as `a` or one less dimension.
If `res` has one less dimension than `a`, a dimension is inserted before axis.
The call to func is then repeated for each axis in axes, with `res` as the first argument.

Parameters
    func : function; This function must take two arguments, func(a, axis).
    a : array_like; Input array.
    axes : array_like; Axes over which func is applied; the elements must be integers.
Returns
    apply_over_axis : ndarray
        The output array.
        The number of dimensions is the same as `a`, but the shape can be different.
        This depends on whether `func` changes the shape of its output with respect to its input.
Notes
This function is equivalent to __tuple axis arguments__ to reorderable ufuncs with `keepdims=True`.
Tuple axis arguments to ufuncs have been available since version 1.7.0.
"""
a = np.arange(24).reshape(2,3,4)
a
#array([[[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]],
#       [[12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]]])

# Sum over axes 0 and 2. The result has same number of dimensions as the original array:
np.apply_over_axes(np.sum, a, [0,2])
array([[[ 60],
        [ 92],
        [124]]])

# Tuple axis arguments to ufuncs are equivalent:
np.sum(a, axis=(0,2), keepdims=True)
#array([[[ 60],
#        [ 92],
#        [124]]])

a = np.arange(120).reshape(2,3,4,5)
a
np.apply_over_axes(np.sum, a, [0,2])
np.sum(a, axis=(0,2), keepdims=True)


#%%
#%%  numpy.piecewise(x, condlist, funclist, *args, **kw)
"""
Evaluate a piecewise-defined function.

Given a set of conditions and corresponding functions,
evaluate each function on the input data wherever its condition is true.

Parameters
    x : ndarray or scalar; The input domain.

    condlist : list of bool arrays or bool scalars;
        Each boolean array corresponds to a function in `funclist`.
        Wherever `condlist[i]` is True, `funclist[i](x)` is used as the output value.
        Each boolean array in condlist selects a piece of x,
        and should therefore be of the same shape as x.
        The length of `condlist` must correspond to that of `funclist`.
        If one extra function is given, i.e. if `len(funclist) == len(condlist) + 1`,
        then that extra function is the default value,
        used wherever all conditions are false.

    funclist : list of callables, f(x,*args,**kw), or scalars;
        Each function is evaluated over x wherever its corresponding condition is True.
       !!!  It should take a 1d array as input and give an 1d array or a scalar value as output.  !!!
        If, instead of a callable, a scalar is provided then a constant function
        (lambda x: scalar) is assumed.

    args : tuple, optional
        Any further arguments given to piecewise are passed to the functions upon execution,
        i.e., if called piecewise(..., ..., 1, 'a'), then each function is called as f(x, 1, 'a').

    kw : dict, optional
        Keyword arguments used in calling piecewise are passed to the functions upon execution,
        i.e., if called piecewise(..., ..., alpha=1), then each function is called as f(x, alpha=1).

Returns
    out : ndarray
       !!!  The output is the same shape and type as `x`  !!!
        and is found by calling the functions in `funclist` on the appropriate portions of `x`,
        as defined by the boolean arrays in `condlist`.
        Portions not covered by any condition have a default value of 0.

See also:  choose, select (Indexing routines),  where (Sorting, searching, and counting)

Notes
This is similar to `choose` or `select`,
except that functions are evaluated on elements of `x` that satisfy the corresponding condition from `condlist`.
"""

x = np.linspace(-2.5, 2.5, 6)
x
np.piecewise(x, [x < 0, x >= 0], [-1, 1])       # array([-1., -1., -1.,  1.,  1.,  1.])

# Define the absolute value, which is -x for x <0 and x for x >= 0.

np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])   # array([2.5,  1.5,  0.5,  0.5,  1.5,  2.5])

# Apply the same function to a scalar value.
y = -2
np.piecewise(y, [y < 0, y >= 0], [lambda x: -x, lambda x: x])   # array(2)

#%%
xx = np.arange(100)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
#!!! NO !!!
np.piecewise(xx, [xx < 30, (30 <= xx) & (xx < 70), (70 <= xx) & (xx < 100)],
                 [lambda x: ax.plot(x, 2*x),
                  lambda x: ax.plot(x, 60),
                  lambda x: ax.plot(x, 60 - 2*(x-70)),
                 ])
#! TypeError: int() argument must be a string, a bytes-like object or a number, not 'Line2D'

#%% plot once !!!
plt.close('all')
fig, ax = plt.subplots()
yy = np.piecewise(xx, [xx < 30, (30 <= xx) & (xx < 70), (70 <= xx) & (xx < 100)],
                      [lambda x: 2*x,
                       lambda x: 60,
                       lambda x: 60 - 2*(x-70)])
ax.plot(xx, yy)

#%%
#%% numpy.vectorize
"""
class numpy.vectorize(pyfunc, otypes=None, doc=None, excluded=None, cache=False, signature=None)[source]

Generalized function class
--------------------------
Define a vectorized function
which takes a nested sequence of objects or numpy arrays as inputs
and returns a single numpy array or a tuple of numpy arrays.
The vectorized function evaluates pyfunc over successive tuples of the input arrays
 !!!  like the python map function, except it uses the broadcasting rules of numpy.  !!!

The data type of the output of vectorized is determined
by calling the function with the first element of the input.
This can be avoided by specifying the otypes argument.

Parameters
    pyfunc : callable; A python function or method.
    otypes : str or list of dtypes, optional; The output data type.
        It must be specified as either a string of typecode characters or a list of data type specifiers.
        There should be one data type specifier for each output.
    doc : str, optional
        The docstring for the function.
        If None, the docstring will be the pyfunc.__doc__.
    excluded : set, optional;
        Set of strings or integers representing the positional or keyword arguments
        for which the function will not be vectorized.
        These will be passed directly to pyfunc unmodified.
        New in version 1.7.0.
    cache : bool, optional
        If True, then cache the first function call that determines the number of outputs
        if otypes is not provided.
        New in version 1.7.0.
    signature : string, optional
        Generalized universal function signature,
        e.g., (m,n),(n)->(m) for vectorized matrix-vector multiplication.
        If provided, pyfunc will be called with (and expected to return) arrays
        with shapes given by the size of corresponding core dimensions.
        By default, pyfunc is assumed to take scalars as input and output.
        New in version 1.12.0.

Returns
    vectorized : callable;   Vectorized function.

Methods
__call__(*args, **kwargs)
Return arrays with the results of `pyfunc` broadcast (vectorized) over args and kwargs not in `excluded`.

See also:  frompyfunc (Takes an arbitrary Python function and returns a ufunc),

Notes
 !!!  The `vectorize` function is provided primarily for convenience, not for performance.  !!!
The implementation is essentially a for loop.
If otypes is not specified,
then a call to the function with the first argument will be used
to determine the number of outputs.
The results of this call will be cached if cache is True to prevent calling the function twice.
However, to implement the cache, the original function must be wrapped
which will slow down subsequent calls, so only do this if your function is expensive.

The new keyword argument interface and `excluded` argument support further degrades performance.
"""
#%%
def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    if a > b:
        return a - b
    else:
        return a + b
#%%
vfunc = np.vectorize(myfunc)

vfunc([1, 2, 3, 4], 2)   # array([3, 4, 1, 2])

list(map(lambda x: myfunc(x, 2), [1, 2, 3, 4]))  # [3, 4, 1, 2]
# or
from functools import partial
list(map(partial(myfunc, b=2), [1, 2, 3, 4]))    # [3, 4, 1, 2]
#!!! but!:
list(map(partial(myfunc, 2), [1, 2, 3, 4]))      # [1, 4, 5, 6]   as


# The docstring is taken from the input function to vectorize unless it is specified:
vfunc.__doc__   # 'Return a-b if a>b, otherwise return a+b'

vfunc = np.vectorize(myfunc, doc='Vectorized `myfunc`')
vfunc.__doc__   # 'Vectorized `myfunc`'

# The output type is determined by evaluating the first element of the input, unless it is specified:
out = vfunc([1, 2, 3, 4], 2)
type(out[0])    # <class 'numpy.int64'>

vfunc = np.vectorize(myfunc, otypes=[float])
out = vfunc([1, 2, 3, 4], 2)
type(out[0])    # <class 'numpy.float64'>

#%%
#!!!  The `excluded` argument can be used to __prevent vectorizing over certain arguments__.
# This can be useful for array-like arguments of a fixed length
# such as the coefficients for a polynomial as in polyval:

def mypolyval(p, x):
    _p = list(p)
    res = _p.pop(0)
    while _p:
        res = res*x + _p.pop(0)
    return res

#%%
vpolyval = np.vectorize(mypolyval, excluded=['p'])

vpolyval(p=[1, 2, 3], x=[0, 1])     # array([3, 6])

#%%
# Positional arguments may also be excluded by specifying their position:
vpolyval.excluded.add(0)
vpolyval([1, 2, 3], x=[0, 1])       # array([3, 6])

# the same as
list(map(lambda x: mypolyval([1, 2, 3], x), [0, 1]))

from functools import partial
list(map(partial(mypolyval, [1, 2, 3]), [0, 1]))   # [3, 6]
#!!! but!:
list(map(partial(mypolyval, p=[1, 2, 3]), [0, 1]))   #! TypeError: mypolyval() got multiple values for argument 'p'


#%%
"""
The signature argument allows for vectorizing functions that act on non-scalar arrays of fixed length.
For example, you can use it for a vectorized calculation of Pearson correlation coefficient and its p-value:
"""
from scipy.stats import pearsonr
help(pearsonr)  # pearsonr(x, y)
"""
Parameters
    x : (N,) array_like        Input array.
    y : (N,) array_like        Input array.
Returns
    r : float        Pearson's correlation coefficient.
    p-value : float  Two-tailed p-value.
"""
x = [0, 1, 2, 3]
y = [1, 2, 3, 4]
z = [4, 3, 2, 1]

pearsonr(x, y)  # ( 1.0, 0.0)
pearsonr(x, z)  # (-1.0, 0.0)

vpearsonr = np.vectorize(scipy.stats.pearsonr, signature='(n),(n)->(),()')
vpearsonr([x], [y, z])  # (array([ 1., -1.]), array([ 0.,  0.]))

# not exactly the same:
np.array(list(map(pearsonr, [x, x], [y, z])))
# array([[ 1.,  0.], [-1.,  0.]])

#%% Vectorized convolution
#%%
help(np.convolve)
"""  Discrete, linear convolution of `a` and `v`:
   (a * v)[n] = \sum_{m = -\infty}^{\infty} a[m] v[n - m]
a : (N,) array_like;        First one-dimensional input array.
v : (M,) array_like;        Second one-dimensional input array.
mode : {'full', 'valid', 'same'},   optional
"""
# Note how the convolution operator flips the second array before "sliding" the two across one another:
np.convolve([1, 2, 3], [0, 1, 0.5])     # array([0. , 1. , 2.5, 4. , 1.5])

# Only return the middle values of the convolution.
# Contains boundary effects, where zeros are taken into account:
np.convolve([1,2,3],[0,1,0.5], 'same')  # array([1. ,  2.5,  4. ])

# The two arrays are of the same length, so there is only one position where they completely overlap:
np.convolve([1,2,3],[0,1,0.5], 'valid') # array([2.5])

#%% vectorized version
convolve = np.vectorize(np.convolve, signature='(n),(m)->(k)')
convolve(np.eye(4), [1, 2, 1])
#array([[1., 2., 1., 0., 0., 0.],
#       [0., 1., 2., 1., 0., 0.],
#       [0., 0., 1., 2., 1., 0.],
#       [0., 0., 0., 1., 2., 1.]])

# the same as:
np.tile([1, 2, 1], (4, 1))
np.array(list(map(np.convolve, np.eye(4), np.tile([1, 2, 1], (4, 1)))))


#%%
#%%  numpy.frompyfunc(func, nin, nout, *[, identity])
"""
Takes an arbitrary Python function and returns a NumPy `ufunc`.
Can be used, for example, to add broadcasting to a built-in Python function (see Examples section).
Parameters
func : Python function object; An arbitrary Python function.
nin : int;  The number of input arguments.
nout : int;  The number of objects returned by func.
identity : object, optional;
    The value to use for the identity attribute of the resulting object.
    If specified, this is equivalent to setting the underlying C identity field to PyUFunc_IdentityValue.
    If omitted, the identity is set to PyUFunc_None.
    Note that this is _not_ equivalent to setting the identity to None,
    which implies the operation is reorderable.
Returns
outufunc : Returns a NumPy universal function (ufunc) object.
"""
oct_array = np.frompyfunc(oct, 1, 1)

oct_array(np.array((10, 30, 100)))      # array(['0o12', '0o36', '0o144'], dtype=object)

# for comparison
np.array((oct(10), oct(30), oct(100)))  # array(['0o12', '0o36', '0o144'], dtype='<U5')

#%%
