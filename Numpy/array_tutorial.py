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
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "array_tutorial.py"
    path: "~/Works/Python/Numpy/"
    date: 2019-11-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
pwd
cd D:/ROBOCZY/Python/Numpy/
cd ~/Works/Python/Numpy/
ls

#%%
import numpy as np

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

arr3d = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],
                  [[1, 2, 3, 4], [9, 10, 11, 12]]])
arr3d

arr3d.data
arr3d.shape
arr3d.dtype    # dtype('int32')
arr3d.strides

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

#%% from text
# This is your data in the text file
# Value1  Value2  Value3
# 0.2536  0.1008  0.3857
# 0.4839  0.4536  0.3561
# 0.1292  0.6875  0.5929
# 0.1781  0.3049  0.8928
# 0.6253  0.3486  0.8791

# Import your data
x, y, z = np.loadtxt('data.txt', skiprows=1, unpack=True,
                     delimiter=None,    # default
                     dtype='float64'   # defult?
                     )
"""
you skip the first row,
and you return the columns as separate arrays with  `unpack=TRUE`.
This means that the values in column Value1 will be put in x, and so on.
"""
x
y
z
#%%
# Your data in the text file
# Value1  Value2  Value3
# 0.4839  0.4536  0.3561
# 0.1292  0.6875  MISSING
# 0.1781  0.3049  0.8928
# MISSING 0.5801  0.2038
# 0.5993  0.4357  0.7410

my_array2 = np.genfromtxt('data2.txt', skip_header=1,
                          missing_values='MISSING', filling_values=-999)
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt

"""
loadtxt(), only works when each row in the text file has the same number of values;
So when you want to handle missing values easily,
you’ll typically find it easier to use genfromtxt().

there is really a lot more things that you can specify in your import,
using genfromtxt(), such as the
- maximum number of rows to read or
- the option to automatically strip white spaces from variables.
"""
#%%
x = np.arange(0.0, 5.0, 1.0)
np.savetxt('test.out', x, delimiter=',')
ls

y = np.loadtxt('test.out')
y
y == x
y is x  # False
np.array_equal(x, y)

"""
save() 	    Save an array to a _binary_ file in NumPy .npy format
savez() 	Save several arrays into an _uncompressed_ .npz archive
savez_compressed() 	Save several arrays into a _compressed_ .npz archive
"""
#%%
arr3d
len(arr3d)
arr3d.dtype  # dtype('int32')
arr3d.ndim
arr3d.size  # nr of elements
arr3d.flags # memory layout
arr3d.itemsize  # one element size in bytes
arr3d.nbytes    # size of arr in bytes

arr3dfloat = arr3d.astype(float)
arr3dfloat.dtype  # dtype('float64')
arr3d.dtype # not changed

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
x+z

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

#%% How To Subset, Slice, And Index Arrays
...
arr3d
arr3d[1,...]
arr3d[1,1,...]
arr3d[1,1,1,...]

x
x % 3 == 0
type(x % 3 == 0)  # numpy.ndarray
x[x % 3 == 0]

#%%
arr2d
arr2d[[1,0,1,0]]
arr2d[[1,0,1,0]][:,[0,1,2,0]]

#%% other manipulations

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

#%% .reshape() and np.reshape()
#%%
newarr
newarr.reshape((4, 3)) # not in-place!!!
newarr
np.reshape(newarr, (4, 3))

#%% .ravel()
x
x.ravel()
arr3d
arr3d.ravel()

#%% np.append()
newarr
np.append(newarr, [1, 2, 4, 7])
np.append(newarr.T, [1, 2, 4, 7])
np.append(newarr, [[1, 2, 4, 7]])
np.append(newarr.T, [[1, 2, 4, 7]])

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

np.row_stack((x, y, z))

#%%
np.hstack((x, y))

np.c_[x, y]
np.c_[x, y, z]

np.column_stack((x, y, z))

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


