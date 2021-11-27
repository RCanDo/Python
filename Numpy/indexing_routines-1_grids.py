#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Indexing routines 1
subtitle: Grids
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
    name: indexing_routines-1_grids.py
    path: ~/Works/Python/Numpy/
    date: 2021-11-20
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
#%%  numpy.indices(dimensions, dtype=<class 'int'>, sparse=False)
"""
Return an array representing the indices of a grid.
Compute an array where the subarrays contain index values 0, 1, …
varying only along the corresponding axis.

Parameters
dimensions : sequence of ints;    The shape of the grid.
dtype : dtype, optional;    Data type of the result.
sparse : boolean, optional;    Return a sparse representation of the grid instead of a dense representation.
    Default is False.
    New in version 1.17.

Returns
grid : one ndarray or tuple of ndarrays

If sparse is False:
    Returns one array of grid indices,
        grid.shape = (len(dimensions),) + tuple(dimensions).      (*)
   !!!  BECAUSE for each dimension the array with the same given shape (`dimensions`) is created   !!!
        with values varying along respective dimension and constant across all other dimensions
        (this values are respective indices -- position along given dimension).
If sparse is True:
    Returns a tuple of arrays,
    with grid[i].shape = (1, ..., 1, dimensions[i], 1, ..., 1) with dimensions[i] in the ith place

See also
mgrid,
ogrid,
meshgrid

Notes
The output shape in the dense case is obtained by prepending the number of dimensions
in front of the tuple of dimensions, as in (*);
i.e. if dimensions is a tuple (r0, ..., rN-1) of length N, the output shape is (N, r0, ..., rN-1).
The subarrays grid[k] contains the N-D array of indices along the k-th axis. Explicitly:
    grid[k, i0, i1, ..., iN-1] = ik
"""
grid = np.indices((2, 3))
grid
grid.shape  # (2, 2, 3)

grid[0]        # row indices
#array([[0, 0, 0],
#       [1, 1, 1]])

grid[1]        # column indices
#array([[0, 1, 2],
#       [0, 1, 2]])

# The indices can be used as an index into an array.
x = np.arange(20).reshape(5, 4)
x

row, col = np.indices((2, 3))
row
col

x[row, col]
#array([[0, 1, 2],
#       [4, 5, 6]])

# Note that it would be more straightforward in the above example
# to extract the required elements directly with x[:2, :3].
#
# If sparse is set to True, the grid will be returned in a sparse representation.

i, j = np.indices((2, 3), sparse=True)
i.shape   # (2, 1)
j.shape   # (1, 3)

i         # row indices
# array([[0],
#        [1]])

j         # column indices
# array([[0, 1, 2]])

#%%
#%% np.ix_[]
"""
Construct an __open mesh__ from multiple sequences.
This function takes N 1-D sequences and returns N outputs with N dimensions each,
such that the shape is 1 in all but one dimension
and the dimension with the non-unit shape value cycles through all N dimensions.

Using `ix_` one can quickly construct index arrays that will index the cross product.
`a[np.ix_([1,3],[2,5])]` returns the array `[[a[1,2] a[1,5]], [a[3,2] a[3,5]]]`.

Parameters
args : 1-D sequences
    Each sequence should be of integer or boolean type.
    Boolean sequences will be interpreted as boolean masks for the corresponding dimension
    (equivalent to passing in np.nonzero(boolean_sequence)).
Returns
out : tuple of ndarrays
    N arrays with N dimensions each, with N the number of input sequences.
    Together these arrays form an open mesh.
See also
    ogrid, mgrid, meshgrid
"""
a = np.arange(15).reshape(3, 5)
a

a[np.ix_([0, 2], [1, 4])]
# array([[ 1,  4],
#        [11, 14]])
a[[[0], [2]], [1, 4]]   # the same  -->  01_fancy_indexing.py

ixgrid = np.ix_([0, 2], [1, 4])
ixgrid
# (array([[0],
#         [2]]),
#  array([[1, 4]]))

ixgrid[0].shape, ixgrid[1].shape
# ((2, 1), (1, 2))

np.ogrid[[0, 2], [1, 4]]   #! AttributeError: 'list' object has no attribute 'step'
#! see description of `numpy.ogrid` below


a[ixgrid]
# array([[ 1,  4],
#        [11, 14]])

ixgrid = np.ix_([True, True], [2, 4])
# (array([[0],
#         [1]]), array([[2, 4]]))

a[ixgrid]
# array([[2, 4],
#        [7, 9]])

ixgrid = np.ix_([True, True], [False, False, True, False, True])
# (array([[0],
#         [1]]), array([[2, 4]]))

a[ixgrid]
# array([[2, 4],
#        [7, 9]])
a[[[True], [True], [False]], [False, False, True, False, True]]   #! IndexError: too many indices for array ???

#%%
a[np.ix_(range(2), range(4))]
# array([[0, 1, 2, 3],    [5, 6, 7, 8]])
# the same as simpler
a[:2, :4]   # OK

# however
a[range(2), range(4)]   #! IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (2,) (4,)
# -->  01.fancy_indexing.py

#%% other usage
rows = np.array([2, 3, 4, 5])
cols = np.array([8, 5, 4])
pags = np.array([5, 4, 6, 8, 3])
rx, cx, px = np.ix_(rows, cols, pags)

rx
#array([[[2]],
#       [[3]],
#       [[4]],
#       [[5]]])
np.expand_dims(np.expand_dims(rows, 1), 1)

cx
#array([[[8],
#        [5],
#        [4]]])
np.expand_dims(np.expand_dims(cols, 1), 0)
np.expand_dims(np.expand_dims(cols, 0), 2)     # not commutable !!!

px
#array([[[5, 4, 6, 8, 3]]])
np.expand_dims(np.expand_dims(pags, 0), 0)
np.expand_dims(np.expand_dims(pags, 0), 1)

rx.shape, cx.shape, px.shape    # ((4, 1, 1), (1, 3, 1), (1, 1, 5))
result = rx + cx * px
result   # all possible values for each possible combination of args
#array([[[42, 34, 50, 66, 26],
#        [27, 22, 32, 42, 17],
#        [22, 18, 26, 34, 14]],
#
#       [[43, 35, 51, 67, 27],
#        [28, 23, 33, 43, 18],
#        [23, 19, 27, 35, 15]],
#
#       [[44, 36, 52, 68, 28],
#        [29, 24, 34, 44, 19],
#        [24, 20, 28, 36, 16]],
#
#       [[45, 37, 53, 69, 29],
#        [30, 25, 35, 45, 20],
#        [25, 21, 29, 37, 17]]])
result[3, 2, 4]     # 17
rows[3] + cols[2] * pags[4]  # 17

#%%
def ufunc_reduce(ufunc, *vectors):
    """ see  02_ufunc.py
    The advantage of this version of reduce compared to the normal `ufunc.reduce`
    is that it makes use of the broadcasting rules in order to avoid creating an argument array
    the size of the output times the number of vectors.
    """
    vs = np.ix_(*vectors)
    r = ufunc.identity  # each `ufunc` has this attr -- neutral element of given operation
    for v in vs:
        r = ufunc(r, v)
    return r

ufunc_reduce(np.add, rows, cols, pags)

#%%
#%%  numpy.ogrid = <numpy.lib.index_tricks.OGridClass object>
help(np.ogrid)
dir(np.ogrid)
"""
nd_grid instance which returns an open multi-dimensional “meshgrid”.
An instance of `numpy.lib.index_tricks.nd_grid` which returns
???  an __open (i.e. not fleshed out) mesh-grid__ when indexed,     ???
so that only one dimension of each returned array is greater than 1.
The dimension and number of the output arrays are equal to the number of indexing dimensions.

!!!  If the __step length__ is NOT a __complex number__, then the stop is NOT inclusive.   !!!

However, if the step length is a complex number (e.g. 5j),
then the __integer part__ of its magnitude is interpreted
as specifying __the number of points__ to create between the start and stop values,
where the stop value is inclusive.

Returns
mesh-grid    list of ndarrays with only one dimension not equal to 1

See also
np.lib.index_tricks.nd_grid
    class of ogrid and mgrid objects
mgrid
    like ogrid but returns __dense (or fleshed out) mesh grids__
r_
    array concatenator
"""

np.ogrid[-1:1:5j]  # array([-1. , -0.5,  0. ,  0.5,  1. ])
np.ogrid[-1:1:.5]  # array([-1. , -0.5,  0. ,  0.5])
np.ogrid[-1:1:.5j]  # array([])
np.ogrid[-1:1:5]  # array([-1])
np.ogrid[-10:10:5]  # array([-10,  -5,   0,   5])

#!!! see descriptio above !!!
# step = 5.3j -- 5 points inclusive the endpoint; .3 ignored
# step = 5.3   -- step of length 5.3, the endpoint excluded
#  awefull...

np.ogrid[0:5,0:5]
#[array([[0],
#        [1],
#        [2],
#        [3],
#        [4]]), array([[0, 1, 2, 3, 4]])]
#! NO ENDPOINTS

np.ogrid[0:1:.2,0:2:.5]
#[array([[0. ],
#        [0.2],
#        [0.4],
#        [0.6],
#        [0.8]]),
# array([[0. , 0.5, 1. , 1.5]])]
#! NO ENDPOINTS


#%% !!! np.ogird with imaginary step is NOT good for array indexing  !!!
#  as it returns floats   while   real step returns int (if it's int).
#  just another mess...

a = np.arange(15).reshape(3, 5)
a
a[np.ogrid[0:2:2j, 0:4:3j]]   #! IndexError: arrays used as indices must be of integer (or boolean) type
ixgrid = np.ix_(np.ogrid[0:2:2j, 0:4:3j])
ixgrid
a[ixgrid]  #! IndexError: arrays used as indices must be of integer (or boolean) type

#!!!  hence one cannot use it as indices generator  !!!

# however:
a[np.ogrid[0:3:2, 0:5:2]]     # OK although FutureWarning:
a[tuple(np.ogrid[0:3:2, 0:5:2])]     # OK

# BUT it's really nonsense in view of:
a[0:3:2, 0:5:2]     # :)

#%%
#%%  numpy.mgrid = <numpy.lib.index_tricks.MGridClass object>
"""
nd_grid instance which returns a __dense multi-dimensional “meshgrid”__.
An instance of numpy.lib.index_tricks.nd_grid which returns
!!!  a __dense (or fleshed out) mesh-grid__ when indexed,
     so that each returned argument has __the same shape__.    !!!
The dimensions and number of the output arrays are equal to the number of indexing dimensions.

!!!  If the __step length__ is NOT a __complex number__, then the stop is NOT inclusive.   !!!

However, if the step length is a complex number (e.g. 5j),
then the integer part of its magnitude is interpreted
as specifying the number of points to create between the start and stop values,
where the stop value is inclusive.

Returns
mesh-grid  ndarray (one!) with meshgrid-like subarrays (matrices) __all of the same dimensions__
           !!! see np.meshgrid for comparison !!!

See also
numpy.lib.index_tricks.nd_grid
    class of ogrid and mgrid objects
ogrid
    like mgrid but returns __open (not fleshed out) mesh grids__
r_
    array concatenator
"""
np.mgrid[0:5, 0:5]          # returns ONE array
#array([[[0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1],
#        [2, 2, 2, 2, 2],
#        [3, 3, 3, 3, 3],
#        [4, 4, 4, 4, 4]],
#       [[0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4]]])
# when using as indices each element is the index for the 1st dim only:

xx = np.random.randint(0, 36, size=[6, 6])
xx
xx[np.mgrid[0:5,0:5]]    #!!!  ooooops  !!!

#!!! hence it's rather not for indexing !!!

np.meshgrid[0:5,0:5]    #! TypeError: 'function' object is not subscriptable
np.meshgrid(range(5), range(5))  # returns 2 arrays
#[array([[0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4],
#        [0, 1, 2, 3, 4]]),
# array([[0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1],
#        [2, 2, 2, 2, 2],
#        [3, 3, 3, 3, 3],
#        [4, 4, 4, 4, 4]])]
# here indices are interpreted as needed for array indexing
xx[np.meshgrid(range(5),range(5))]    # ok !!!


np.mgrid[-1:1:5j]
# array([-1. , -0.5,  0. ,  0.5,  1. ])   # floats !!! 5 elements; endpoint included
np.mgrid[-5:5:2]            # int; 5 elements; endpoint NOT included

#%%
#%%   numpy.meshgrid(*xi, copy=True, sparse=False, indexing='xy')[source]
"""
Return __coordinate matrices__ (grid of indices) from coordinate vectors.

Make N-D coordinate arrays
for vectorized evaluations of N-D scalar/vector fields over N-D grids,
given one-dimensional coordinate arrays x1, x2,…, xn.

 Changed in version 1.9: 1-D and 0-D cases are allowed.

Parameters
x1, x2,…, xn : array_like
    1-D arrays representing the coordinates of a grid.
indexing{‘xy’, ‘ij’}, optional
    Cartesian (‘xy’, default) or matrix (‘ij’) indexing of output. See Notes for more details.
     New in version 1.7.0.
sparse : bool, optional
    If True a sparse grid is returned in order to conserve memory. Default is False.
     New in version 1.7.0.
copy : bool, optional
    If False, a view into the original arrays are returned in order to conserve memory.
    Default is True.
    Please note that sparse=False, copy=False will likely return non-contiguous arrays.
    Furthermore, more than one element of a broadcast array may refer to a single memory location.
    If you need to write to the arrays, make copies first.
     New in version 1.7.0.

Returns
X1, X2,…, XN : ndarray
    For vectors x1, x2,…, ‘xn’ with lengths Ni=len(xi), return
    (N1, N2, N3,...Nn) shaped arrays if indexing=’ij’ or
    (N2, N1, N3,...Nn) shaped arrays if indexing=’xy’
    with the elements of xi repeated to fill the matrix
    along the first dimension for x1, the second for x2 and so on.

See also
mgrid
    Construct a multi-dimensional “meshgrid” using indexing notation.
ogrid
    Construct an open multi-dimensional “meshgrid” using indexing notation.

Notes
This function supports both indexing conventions through the indexing keyword argument.
Giving the string ‘ij’ returns a meshgrid with matrix indexing,
while ‘xy’ returns a meshgrid with Cartesian indexing.
In the 2-D case with inputs of length M and N,
the outputs are of shape (N, M) for ‘xy’ indexing and (M, N) for ‘ij’ indexing.
In the 3-D case with inputs of length M, N and P, outputs are of shape (N, M, P)
for ‘xy’ indexing and (M, N, P) for ‘ij’ indexing.
The difference is illustrated by the following code snippet:

xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')
for i in range(nx):
    for j in range(ny):
        # treat xv[i,j], yv[i,j]

xv, yv = np.meshgrid(x, y, sparse=False, indexing='xy')
for i in range(nx):
    for j in range(ny):
        # treat xv[j,i], yv[j,i]

In the 1-D and 0-D case, the indexing and sparse keywords have no effect.

"""
nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
xv
#array([[0. , 0.5, 1. ],
#       [0. , 0.5, 1. ]])
yv
#array([[0.,  0.,  0.],
#       [1.,  1.,  1.]])

xv, yv = np.meshgrid(x, y, sparse=True)  # make sparse output arrays
xv
# array([[0. ,  0.5,  1. ]])
yv
#array([[0.],
#       [1.]])

#%% meshgrid is very useful to evaluate functions on a grid.

import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x, y, z)
plt.axis('scaled')
plt.show()

#%%
#%%


#%%