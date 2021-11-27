#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Numpy Array Tutorial
version: 1.0
type: tutorial
keywords: [array, numpy]
sources:
    - title: Python Numpy Array Tutorial
      chapter:
      link: https://www.datacamp.com/community/tutorials/python-numpy-tutorial
      usage: |
          not only copy
    - title: NumPy quickstart
      link: https://numpy.org/doc/stable/user/quickstart.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: array_tutorial.py
    path: ~/Works/Python/Numpy/
    date: 2019-11-27
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
"""
If an array is too large to be printed,
NumPy automatically skips the central part of the array and only prints the corners:
"""
print(np.arange(10000))
print(np.arange(10000).reshape(100, 100))
"""
To disable this behaviour and force NumPy to print the entire array,
you can change the printing options using set_printoptions.
"""
#!   np.set_printoptions(threshold=sys.maxsize)   # sys module should be imported

#%% help
print(np.lookfor("mean"))
np.info(np.ndarray.dtype)
np.info('mean')

#%%
arr1d = np.array([1, 2, 3, 4, 5])
arr1d
arr1d.data
arr1d.shape
arr1d.dtype
arr1d.strides

arr2d = np.array([[1, 2 ,3, 4], [5, 6, 7, 8]])
arr2d
arr2d.data
arr2d.shape
arr2d.dtype
arr2d.strides
"""
The strides are the number of bytes that should be skipped in memory
to go to the next element.
If your strides are (16,4), you need to proceed 4 bytes to get to the next column
and 16 bytes to locate the next row.
"""

#%% !!!
arr2d[..., np.newaxis]

#%%
arr3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                  [[1, 2, 3, 4], [9, 10, 11, 12]]])
arr3d
len(arr3d)
arr3d.ndim

arr3d.shape
arr3d.dtype    # dtype('int32')

arr3d.size  # nr of elements
arr3d.flags # memory layout
arr3d.itemsize  # one element size in bytes
arr3d.nbytes    # size of arr in bytes
arr3d.strides
arr3d.data

arr3dfloat = arr3d.astype(float)
arr3dfloat.dtype  # dtype('float64')
arr3d.dtype # not changed

#%% NaN in numpy are only float !!!
randarr = np.random.randint(0, 10, (3, 4))
randarr.dtype
randarr[1, 1] = np.nan #! ValueError: cannot convert float NaN to integer

randarr = np.random.randint(0, 10, (3, 4)).astype(float)
randarr.dtype
randarr[1, 1] = np.nan
randarr

# this is somehow resolved in Pandas but still causes problems

# also notice that
randarr = np.random.randint(0, 10, (3, 4), dtype=np.float64) #! TypeError: Unsupported dtype "float64" for randint
# that's why we used .astype() method above
# compare below

#%%
np.ones((2, 3))
np.ones((2, 3)).dtype  # float64 !!!  this is the default (but we've seen above that not always...)
np.ones((2, 3, 4))

np.zeros((2, 3))
np.zeros((2, 3)).dtype # float64
np.zeros((2, 3), dtype=np.int16)

np.random.random((2, 3))
np.random.random((2, 3)).dtype  # float64

np.empty((3, 2))  # these values are very random collections from memory

np.full((2, 3), 2222)

np.arange(-2, 2, .5) # array from -2 to 2 with step .5 (ending 2 EXcluded!)

np.linspace(-2, 2, 9) # array of 9 elements evenly spaced from -2 to 2 (included!!!)

np.eye(3)
np.eye(1)
# the same:
np.identity(3)

#%% complex
c = np.array([[1, 2], [3, 4]], dtype=complex)
c       # array([[1.+0.j, 2.+0.j], [3.+0.j, 4.+0.j]])
c.real  # array([[1., 2.], [3., 4.]])
c.imag  # array([[0., 0.], [0., 0.]])
c.real.dtype    # dtype('float64')   -- but int was used when created  !!!  complex are always floats  !!!

d = 1 + np.array([[1, 2], [3, 4]])*1j
d
d.real
d.imag

#%%
arr = np.array([1,2,3])
arr
np.expand_dims(arr, 0)
np.expand_dims(arr, -1)
np.expand_dims(arr, 1)

arr2d
np.expand_dims(arr2d, 0)
np.expand_dims(arr2d, 1)
np.expand_dims(arr2d, 2)
np.expand_dims(arr2d, -1)

arr3d
np.expand_dims(arr3d, 0)
np.expand_dims(arr3d, 1)
np.expand_dims(arr3d, 2)
np.expand_dims(arr3d, 3)
np.expand_dims(arr3d, -1)

#%% NumPy broadcasting (recycling rule in R)
x = np.ones((3, 4))
x.shape

y = np.random.random((3, 4))
y.shape

x+y

#%%
z = np.arange(4)
z
z.shape

# broadcasting in action: two dimensions are _compatible_ when one of them is 1:
x + z
x + z.T  # THE SAME !!!  because z is 1-dim so .T is irrelevant
x.T + z  #! ValueError: operands could not be broadcast together with shapes (4,3) (4,)

np.arange(4).reshape(4, -1)
x.T + np.arange(4).reshape(4, -1)

# Noteice though that if the dimensions are not _compatible_, you will get a ValueError.
x + np.ones(3) #! ValueError: operands could not be broadcast together with shapes (3,4) (3,)
x + np.ones(4) # OK
x + np.ones(1) # this works too!
x + np.ones(2) # ValueError: operands could not be broadcast together with shapes (3,4) (2,)

"""
the maximum size along each dimension of x and y is taken to make up
the shape of the new, resulting array.
"""
#%%
x
y = np.random.randint(0, 10, (5, 1, 4))
y
x + y
# IT WORKS!!!
# That is because the dimensions are _compatible_ in all dimensions:
x.shape
y.shape

#%% How Do Array Mathematics Work?

x = np.random.randint(-10, 10, (2, 3))
y = np.random.randint(-2, 2, (2, 3))
x
y

x+y
np.add(x, y)
x-y
np.subtract(x, y)

x*y
np.multiply(x, y)  # elementwise !!!

x/y
np.divide(x, y)    # elementwise !!!
# do not confuse with this attribute
np.division

x % y
np.remainder(x, y)

x // y
np.divmod(x, y)    # == (x // y, x % y)

# for logical operators:
# if array is numeric then 0 is False and anything other is True
np.logical_and(x, y)
np.logical_or(x, y)
np.logical_not(y)

#%% aggregates
x
x.sum()
x.sum(axis=0)
x.sum(axis=1)
x.cumsum()
x.cumsum(axis=0)
x.cumsum(axis=1)
x.min()
x.min(axis=1)
x.max()
x.max(axis=1)
x.mean()
x.mean(axis=1)

x.median()    #! AttributeError: 'numpy.ndarray' object has no attribute 'median'
np.median(x)
np.median(x, axis=1)
np.corrcoef(x)
x.std()
x.std(axis=1)

#%% matrix multiplication
aa = np.array([[1,2], [4, 3], [5,7]])
aa
bb = np.array([[-1, 1, 2], [1, -1, -1]])
bb

aa @ bb
aa.dot(bb)

aa @ bb.T   # ValueError: matmul: ... of course!


#%%
#%% indexing
#%%

def f(x, y):
    return 10 * x + y

b = np.fromfunction(f, (5, 4), dtype=int)               #!!!
b
#array([[ 0,  1,  2,  3],
#       [10, 11, 12, 13],
#       [20, 21, 22, 23],
#       [30, 31, 32, 33],
#       [40, 41, 42, 43]])
b[2, 3]     # 23
b[0:5, 1]  # each row in the second column of b
# array([ 1, 11, 21, 31, 41])
b[:, 1]    # equivalent to the previous example
# array([ 1, 11, 21, 31, 41])
b[1:3, :]  # each column in the second and third row of b
#array([[10, 11, 12, 13],
#       [20, 21, 22, 23]])

#%%
xx = np.random.randint(0, 36, size=[6, 6])
xx

xx[0, 1]
xx[[0, 3], :]
xx[:, [1, 5, 1]]

xx[:4, :]
xx[1:4:, :]
xx[1:5:2, :]
xx[1:5:-2, :]
xx[5::-2, :]
xx[::-2, :]

xx[:,::2]
xx[:,::-2]
xx[:,:2:-1]
xx[:,-2::]

xx[::2, ::2]
xx[::-1, ::-1]
xx[::-2, ::-3]


#%% notice that
# using specific indices via list is allowed only for one dim:

xx[range(3), :]
#! BUT
xx[range(3), range(4)]  #! IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (3,) (4,)
xx[range(3), range(3)]  # OK  -- but this is diagonal not a grid ! see below (fancy indexing)

xx[[0, 3], :]
xx[:, [1, 5, 1]]

#!!! BUT:
xx[[0, 3], [1, 5, 1]]   #! IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes (2,) (3,)
xx[(0, 3), (1, 5, 1)]   #!  "

#!!!  -->  01_fancy_indexing.py  for more on this.   !!!

xx[(0, 3, 1), (1, 5, 1)]  # ok; but again: it's not a grid!

# this is how to get this:
xx[[[0], [3]], [1, 5, 1]]        #!!!
# or
xx[np.ix_([0, 3], [1, 5, 1])]    #!!!  ok
# or
xx[np.meshgrid([0, 3], [1, 5, 1])].T
# while
xx[np.meshgrid([0, 3], [1, 5, 1])]     # :(
np.meshgrid([0, 3], [1, 5, 1])

xx[np.ix_(range(3), range(4))]

#%% boolean indexing
a = np.arange(12).reshape(3, 4)
a
b1 = np.array([False, True, True])         # first dim selection
b2 = np.array([True, False, True, False])  # second dim selection
a[b1, :]                                   # selecting rows
#array([[ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])
a[b1]                                      # same thing
#array([[ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])
a[:, b2]                                   # selecting columns
#array([[ 0,  2],
#       [ 4,  6],
#       [ 8, 10]])

a[b1, b2]                                  # a weird thing to do
# array([ 4, 10])           #!!! ??? HOW ???     This is neither (norma) grid-like indexing nor fancy indexing...

#%%
#%% slice, resize, reshape, transpose, ravel

#%% Slice, Subset, And Index Arrays
"""
The dots (...) represent as many colons as needed to produce a complete indexing tuple.
E.g. if x is 5 dimensional:
    x[1, 2, ...] is equivalent to x[1, 2, :, :, :],
    x[..., 3] to x[:, :, :, :, 3] and
    x[4, ..., 5, :] to x[4, :, :, 5, :].
"""

arr3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                  [[-1, -2, -3, -4], [9, 10, 11, 12]]])
arr3d
arr3d.shape   # (2, 2, 4)

...         # Ellipsis
arr3d
arr3d[1,...]
arr3d[1, :, :]  # the same
arr3d[1,:]      # "
arr3d[1]        # "

arr3d[1,1,...]
arr3d[1,1,:]
arr3d[1,1]

arr3d[1,1,1,...]   # array(10)
arr3d[1,1,1]       # 10


arr3d
arr3d % 3 == 0
type(arr3d % 3 == 0)  # numpy.ndarray
arr3d[arr3d % 3 == 0]

#%%
# Iterating over multidimensional arrays is done with respect to the first axis:
for row in arr3d: print(row)
#[[1 2 3 4]
# [5 6 7 8]]        # 1st row
#[[-1 -2 -3 -4]
# [ 9 10 11 12]]    # 2nd row

#!!!  arr.flat
# However, if one wants to perform an operation on each element in the array,
#!!!  one can use the `flat` attribute which is an iterator over all the elements of the array:   !!!
for element in arr3d.flat: print(element)    # 1 2 3 4 5 6 ... 11 12
# or (as list):
[e for e in arr3d.flat]
# [1, 2, 3, 4, 5, 6, 7, 8, -1, -2, -3, -4, 9, 10, 11, 12]

#%%
arr2d
arr2d[[1,0,1,0]]
arr2d[[1,0,1,0]][:,[0,1,2,0]]  # only 1 dim

#%% other manipulations
x = np.random.randint(-10, 10, (2, 3))
x
x.T
np.transpose(x)

#%% .resize()  and np.resize()

x.resize((6, 4)) #! ValueError: cannot resize an array that references or is referenced
# by another array in this way.
# Use the np.resize function or refcheck=False

np.resize(x, (6, 4))  # it works row-wise and recycles (broadcasts)

newarr = np.random.randint(0, 10, (3, 4))
newarr
newarr.resize((4, 6))
newarr.resize((4, 6), refcheck=False)   # in-place!!!
newarr  ## fills with zoros -- so it's not like  np.resize(x, (..))  !!!

newarr = np.random.randint(0, 10, (3, 4))
newarr
np.resize(newarr, (4, 6))

#%%
#%% .reshape() and np.reshape()

newarr
newarr.reshape((4, 3)) # not in-place!!!
newarr
np.reshape(newarr, (4, 3))

#%% .ravel()
x
x.ravel()
arr3d
arr3d.ravel()


#%%
#%%

#%% np.append()
newarr = np.array(range())
newarr
np.append(newarr, [1, 2, 4, 7])         # array([8, 1, 2, 1,  1, 1, 0, 4,  4, 4, 8, 2,   1, 2, 4, 7])
np.append(newarr.T, [1, 2, 4, 7])       # array([8, 1, 4,  1, 1, 4,  2, 0, 8,  1, 4, 2,  1, 2, 4, 7])
np.append(newarr, [[1, 2, 4, 7]])       # array([8, 1, 2, 1,  1, 1, 0, 4,  4, 4, 8, 2,   1, 2, 4, 7])
np.append(newarr.T, [[1, 2, 4, 7]])     # array([8, 1, 4,  1, 1, 4,  2, 0, 8,  1, 4, 2,  1, 2, 4, 7])

np.append(newarr, [[1, 2, 4, 7]], axis=0)
np.append(newarr.T, [[1, 2, 4, 7]], axis=0)  #! ValueError: all the input array dimensions except for the concatenation axis must match exactly
np.append(newarr.T, [[1, 2, 4, 7]], axis=1)  #! ValueError: all the input array dimensions except for the concatenation axis must match exactly

np.append(newarr, [[1], [2], [4]], axis=1)
np.append(newarr.T, [[1], [2], [4], [7]], axis=1)
np.append(newarr.T, np.array([[1, 2, 4, 7]]).T, axis=1)
np.append(newarr.T, np.transpose([[1, 2, 4, 7]]), axis=1)

# hence sizes in proper directions (on proper axis) must agree

#%% np.insert(), np.delete()
arr1d
np.insert(arr1d, 0, 3)    # at index 0 insert 3
np.insert(arr1d, 3, 0)    # at index 3 insert 0

np.delete(arr1d, [0])
np.delete(arr1d, [0, 3])

# notice that arr1d is untuched

#%%
#%% How To Join And Split Arrays

x = np.random.randint(0, 10, (2, 3))
x
y = np.random.randint(-10, 0, (2, 3))
y

np.concatenate((x, y))   # notice double parenthesis

z = np.random.randint(-5, 5, (2, 3))
z
np.concatenate((x, y, z))
np.concatenate((x, y, z), axis=1)

#%%
np.vstack((x, y))

np.r_[x, y]
np.r_[x, y, z]

np.vstack((x, y, z))        # the same
np.row_stack((x, y, z))

#%%
np.hstack((x, y))

np.c_[x, y]
np.c_[x, y, z]

np.hstack((x, y, z))
np.column_stack((x, y, z))   # the same

#%%
z = np.random.randint(0, 20, (4, 5))
z

#%% np.vsplit() == np.split( , axis=0)  -- row-wise

# split at given index
np.vsplit(z, [2])
np.vsplit(z, [1])
# tha same as
np.split(z, [2], axis=0)
np.split(z, [1], axis=0)

# split into even parts
np.vsplit(z, 1)
np.vsplit(z, 2)
np.vsplit(z, 3) #! ValueError: array split does not result in an equal division
np.vsplit(z, 4)

np.split(z, 2, axis=0)

#%% np.hsplit() == np.split( , axis=1) -- column-wise

np.hsplit(z, [1])
np.hsplit(z, [2])
np.split(z, [2], axis=1)

np.hsplit(z, 1)
np.hsplit(z, 2)  #! ValueError: array split does not result in an equal division
np.hsplit(z, 5)


#%%
#%%  How To Visualize NumPy Arrays

#%% np.histogram()

arr3d
np.histogram(arr3d)
np.histogram(arr3d, bins=range(13))

#%%
import matplotlib.pyplot as plt

plt.hist(arr3d.ravel(), bins=range(13))
plt.show()

#%% np.meshgrid()

points = np.arange(-5, 5, .1)

xx, yy = np.meshgrid(points, points)
xx.shape
xx
yy

z = np.sqrt(xx**2 + yy**2)
z

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()

plt.imshow(z)
plt.colorbar()

#%%
arr = np.random.randint(-10, 10, (10, 10))
arr
plt.imshow(arr, cmap=plt.cm.gray)
# notice that values are normalised to fit into cm.gray (shades of gray)
plt.imshow(arr)
plt.colorbar()

#%%

