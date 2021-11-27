#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Indexing routines 3
subtitle: Iteration
version: 1.0
type: help
keywords: [iteration, array, numpy]
sources:
    - title: numpy.nditer
      link: https://numpy.org/doc/stable/reference/generated/numpy.nditer.html
    - title: Indexing routines
      link: https://numpy.org/doc/stable/reference/routines.indexing.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: indexing_routines-3_iteration.py
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
#%%   class numpy.flatiter[source]
"""
Flat iterator object to iterate over arrays.
A flatiter iterator is returned by `x.flat` for any array x.
It allows iterating over the array as if it were a 1-D array,
either in a for-loop or by calling its next method.

Iteration is done in row-major, C-style order (the last index varying the fastest).
The iterator can also be indexed using basic slicing or advanced indexing.

See also
ndarray.flat
    Return a flat iterator over an array.
ndarray.flatten
    Returns a flattened copy of an array.

Notes
A flatiter iterator can not be constructed directly from Python code by calling the flatiter constructor.

Attributes
base      A reference to the array that is iterated over.
coords    An N-dimensional tuple of current coordinates.
index     Current flat index into the array.

Methods
copy()    Get a copy of the iterator as a 1-D array.
"""
x = np.arange(6).reshape(2, 3)
x
fl = x.flat
type(fl)   # numpy.flatiter

[item for item in fl]   #  [0, 1, 2, 3, 4, 5]
[item for item in fl]   #  []     --  must be recreated !!!

fl = x.flat
fl[2:4]     # array([2, 3])   does not use-up index, i.e.
fl.index    # 0
[item for item in fl]   # [0, 1, 2, 3, 4, 5]

fl = x.flat
{fl.coords: [fl.index, item] for item in fl}
# {(0, 1): [1, 0],
#  (0, 2): [2, 1],
#  (1, 0): [3, 2],
#  (1, 1): [4, 3],
#  (1, 2): [5, 4],
#  (2, 0): [6, 5]}
#! notice that it begun with {(0, 1): [1, 0]  and ends with  (2, 0): [6, 5]
fl.index    # 6  -- iterator used up

#%%
#%%  class numpy.ndenumerate(arr)[source]
"""
Multidimensional index iterator.
Return an iterator yielding pairs of array coordinates and values.

Parameters
arr : ndarray
    Input array.

See also
ndindex, flatiter
"""
a = np.array([[1, 2], [3, 4]])

for index, x in np.ndenumerate(a):  print(index, x)
#(0, 0) 1
#(0, 1) 2
#(1, 0) 3
#(1, 1) 4
{index: x for index, x in np.ndenumerate(a)}    # {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}
#???   How to make array from this dict   ???

#%%
#%%   numpy.nested_iters()
"""
Create `nditers` for use in nested loops
Create a tuple of `nditer` objects which iterate in nested loops over different axes of the `op` argument.
The first iterator is used in the outermost loop,
the last in the innermost loop.
Advancing one will change the subsequent iterators to point at its new element.

Parameters
op : ndarray or sequence of array_like
    The array(s) to iterate over.
axes : list of list of int
    Each item is used as an “op_axes” argument to an nditer
flags, op_flags, op_dtypes, order, casting, buffersize (optional)
    See nditer parameters of the same name

Returns
iters : tuple of `nditer`
    An `nditer` for each item in axes, outermost first

See also
nditer()
"""
# Basic usage.
a = np.arange(12).reshape(2, 3, 2)
a
i, j = np.nested_iters(a, [[1], [0, 2]], flags=["multi_index"])

for x in i:
     print(i.multi_index)
     for y in j:
         print('', j.multi_index, y)
#(0,)
# (0, 0) 0
# (0, 1) 1
# (1, 0) 6
# (1, 1) 7
#(1,)
# (0, 0) 2
# (0, 1) 3
# (1, 0) 8
# (1, 1) 9
#(2,)
# (0, 0) 4
# (0, 1) 5
# (1, 0) 10
# (1, 1) 11
# Note how y is the “flattened” version of [a[:, 0, :], a[:, 1, 0], a[:, 2, :]]
# since we specified the first iter’s axes as [1]

...

#%%
#%%  class numpy.nditer(op, flags=None, op_flags=None, op_dtypes=None, order='K',
#                       casting='safe', op_axes=None, itershape=None, buffersize=0)
"""
Efficient multi-dimensional iterator object to iterate over arrays.
To get started using this object, see the introductory guide to array iteration. (above)

Parameters

opndarray or sequence of array_like

    The array(s) to iterate over.
flagssequence of str, optional

    Flags to control the behavior of the iterator.

        buffered enables buffering when required.

        c_index causes a C-order index to be tracked.

        f_index causes a Fortran-order index to be tracked.

        multi_index causes a multi-index, or a tuple of indices with one per iteration dimension, to be tracked.

        common_dtype causes all the operands to be converted to a common data type, with copying or buffering as necessary.

        copy_if_overlap causes the iterator to determine if read operands have overlap with write operands, and make temporary copies as necessary to avoid overlap. False positives (needless copying) are possible in some cases.

        delay_bufalloc delays allocation of the buffers until a reset() call is made. Allows allocate operands to be initialized before their values are copied into the buffers.

        external_loop causes the values given to be one-dimensional arrays with multiple values instead of zero-dimensional arrays.

        grow_inner allows the value array sizes to be made larger than the buffer size when both buffered and external_loop is used.

        ranged allows the iterator to be restricted to a sub-range of the iterindex values.

        refs_ok enables iteration of reference types, such as object arrays.

        reduce_ok enables iteration of readwrite operands which are broadcasted, also known as reduction operands.

        zerosize_ok allows itersize to be zero.

op_flagslist of list of str, optional

    This is a list of flags for each operand. At minimum, one of readonly, readwrite, or writeonly must be specified.

        readonly indicates the operand will only be read from.

        readwrite indicates the operand will be read from and written to.

        writeonly indicates the operand will only be written to.

        no_broadcast prevents the operand from being broadcasted.

        contig forces the operand data to be contiguous.

        aligned forces the operand data to be aligned.

        nbo forces the operand data to be in native byte order.

        copy allows a temporary read-only copy if required.

        updateifcopy allows a temporary read-write copy if required.

        allocate causes the array to be allocated if it is None in the op parameter.

        no_subtype prevents an allocate operand from using a subtype.

        arraymask indicates that this operand is the mask to use for selecting elements when writing to operands with the ‘writemasked’ flag set. The iterator does not enforce this, but when writing from a buffer back to the array, it only copies those elements indicated by this mask.

        writemasked indicates that only elements where the chosen arraymask operand is True will be written to.

        overlap_assume_elementwise can be used to mark operands that are accessed only in the iterator order, to allow less conservative copying when copy_if_overlap is present.

op_dtypesdtype or tuple of dtype(s), optional

    The required data type(s) of the operands. If copying or buffering is enabled, the data will be converted to/from their original types.
order{‘C’, ‘F’, ‘A’, ‘K’}, optional

    Controls the iteration order. ‘C’ means C order, ‘F’ means Fortran order, ‘A’ means ‘F’ order if all the arrays are Fortran contiguous, ‘C’ order otherwise, and ‘K’ means as close to the order the array elements appear in memory as possible. This also affects the element memory order of allocate operands, as they are allocated to be compatible with iteration order. Default is ‘K’.
casting{‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’}, optional

    Controls what kind of data casting may occur when making a copy or buffering. Setting this to ‘unsafe’ is not recommended, as it can adversely affect accumulations.

        ‘no’ means the data types should not be cast at all.

        ‘equiv’ means only byte-order changes are allowed.

        ‘safe’ means only casts which can preserve values are allowed.

        ‘same_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.

        ‘unsafe’ means any data conversions may be done.

op_axeslist of list of ints, optional

    If provided, is a list of ints or None for each operands. The list of axes for an operand is a mapping from the dimensions of the iterator to the dimensions of the operand. A value of -1 can be placed for entries, causing that dimension to be treated as newaxis.
itershapetuple of ints, optional

    The desired shape of the iterator. This allows allocate operands with a dimension mapped by op_axes not corresponding to a dimension of a different operand to get a value not equal to 1 for that dimension.
buffersizeint, optional

    When buffering is enabled, controls the size of the temporary buffers. Set to 0 for the default value.

Notes

nditer supersedes flatiter. The iterator implementation behind nditer is also exposed by the NumPy C API.

The Python exposure supplies two iteration interfaces, one which follows the Python iterator protocol, and another which mirrors the C-style do-while pattern. The native Python approach is better in most cases, but if you need the coordinates or index of an iterator, use the C-style pattern.

Examples

Here is how we might write an iter_add function, using the Python iterator protocol:

def iter_add_py(x, y, out=None):

addop = np.add

it = np.nditer([x, y, out], [],

            [['readonly'], ['readonly'], ['writeonly','allocate']])

with it:

    for (a, b, c) in it:

        addop(a, b, out=c)

return it.operands[2]

Here is the same function, but following the C-style pattern:

def iter_add(x, y, out=None):

   addop = np.add

   it = np.nditer([x, y, out], [],

           [['readonly'], ['readonly'], ['writeonly','allocate']])

   with it:

   while not it.finished:

       addop(it[0], it[1], out=it[2])

       it.iternext()

   return it.operands[2]

Here is an example outer product function:

def outer_it(x, y, out=None):

mulop = np.multiply

it = np.nditer([x, y, out], ['external_loop'],

        [['readonly'], ['readonly'], ['writeonly', 'allocate']],

        op_axes=[list(range(x.ndim)) + [-1] * y.ndim,

                 [-1] * x.ndim + list(range(y.ndim)),

                 None])

with it:

    for (a, b, c) in it:

        mulop(a, b, out=c)

    return it.operands[2]

a = np.arange(2)+1

b = np.arange(3)+1

outer_it(a,b)
array([[1, 2, 3],
   [2, 4, 6]])

Here is an example function which operates like a “lambda” ufunc:

def luf(lamdaexpr, *args, **kwargs):

   '''luf(lambdaexpr, op1, ..., opn, out=None, order='K', casting='safe', buffersize=0)'''

   nargs = len(args)

   op = (kwargs.get('out',None),) + args

   it = np.nditer(op, ['buffered','external_loop'],

       [['writeonly','allocate','no_broadcast']] +

                       [['readonly','nbo','aligned']]*nargs,

       order=kwargs.get('order','K'),

       casting=kwargs.get('casting','safe'),

       buffersize=kwargs.get('buffersize',0))

   while not it.finished:

   it[0] = lamdaexpr(*it[1:])

   it.iternext()

   return it.operands[0]

a = np.arange(5)

b = np.ones(5)

luf(lambda i,j:i*i + j/2, a, b)
array([  0.5,   1.5,   4.5,   9.5,  16.5])

If operand flags “writeonly” or “readwrite” are used the operands may be views into the original data with the WRITEBACKIFCOPY flag. In this case nditer must be used as a context manager or the nditer.close method must be called before using the result. The temporary data will be written back to the original data when the __exit__ function is called but not before:

a = np.arange(6, dtype='i4')[::-2]

with np.nditer(a, [],

   [['writeonly', 'updateifcopy']],

   casting='unsafe',

   op_dtypes=[np.dtype('f4')]) as i:

   x = i.operands[0]

   x[:] = [-1, -2, -3]

   # a still unchanged here

a, x
(array([-1, -2, -3], dtype=int32), array([-1., -2., -3.], dtype=float32))

It is important to note that once the iterator is exited, dangling references (like x in the example) may or may not share data with the original data a. If writeback semantics were active, i.e. if x.base.flags.writebackifcopy is True, then exiting the iterator will sever the connection between x and a, writing to x will no longer write to a. If writeback semantics are not active, then x.data will still point at some part of a.data, and writing to one will affect the other.

Context management and the close method appeared in version 1.15.0.


Attributes
dtypes : tuple of dtype(s)
    The data types of the values provided in value. This may be different from the operand data types if buffering is enabled. Valid only before the iterator is closed.
finished : bool
    Whether the iteration over the operands is finished or not.
has_delayed_bufalloc : bool
    If True, the iterator was created with the delay_bufalloc flag, and no reset() function was called on it yet.
has_index : bool
    If True, the iterator was created with either the c_index or the f_index flag, and the property index can be used to retrieve it.
has_multi_index : bool
    If True, the iterator was created with the multi_index flag, and the property multi_index can be used to retrieve it.
index
    When the c_index or f_index flag was used, this property provides access to the index. Raises a ValueError if accessed and has_index is False.
iterationneedsapi : bool
    Whether iteration requires access to the Python API, for example if one of the operands is an object array.
iterindex : int
    An index which matches the order of iteration.
itersize : int
    Size of the iterator.
itviews
    Structured view(s) of operands in memory, matching the reordered and optimized iterator access pattern. Valid only before the iterator is closed.
multi_index
    When the multi_index flag was used, this property provides access to the index. Raises a ValueError if accessed accessed and has_multi_index is False.
ndim : int
    The dimensions of the iterator.
nop : int
    The number of iterator operands.
operands : tuple of operand(s)
    operands[Slice]
shape : tuple of ints
    Shape tuple, the shape of the iterator.
value
    Value of operands at current iteration. Normally, this is a tuple of array scalars, but if the flag external_loop is used, it is a tuple of one dimensional arrays.


Methods
close()
Resolve all writeback semantics in writeable operands.

copy()
Get a copy of the iterator in its current state.

debug_print()
Print the current state of the nditer instance and debug info to stdout.

enable_external_loop()
When the “external_loop” was not used during construction, but is desired, this modifies the iterator to behave as if the flag was specified.

iternext()
Check whether iterations are left, and perform a single internal iteration without returning the result.

remove_axis(i)
Removes axis i from the iterator.

remove_multi_index()
When the “multi_index” flag was specified, this removes it, allowing the internal iteration structure to be optimized further.

reset()
Reset the iterator to its initial state.
"""