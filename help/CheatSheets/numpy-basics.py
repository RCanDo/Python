# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: NumPy basics
subtitle:
version: 1.0
type: cheat sheet
keywords: [numpy, array]
description: code chunks
remarks:
todo:
sources:   # there may be more sources
    - title: Python For Data Science Cheat Sheet
      chapter: NumPy basics
      link: D:/bib/...
      authors:
          - link: www.DataCamp.com
      usage: copy & isnpiration for some investigations
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: numpy-basics.py
    path: D:/ROBOCZY/Python/help/CheatSheets/
    date: 2019-10-29
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@tieto.com
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
cd "D:/ROBOCZY/Python/help/CheatSheets/"

#%%
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1.5, 2, 3], [4, 5, 6]])
c = np.array([[[1.5, 2, 3], [4, 5, 6]], [[3, 2, 1], [4, 5, 6]]])
a
b
c

#%%
a.shape
c.shape
c.ndim
c.size
c.dtype
c.dtype.name
c.astype(int)
c

#%%
np.zeros((3, 4))
np.ones((2, 3, 4), dtype=np.int16)

d = np.arange(10, 25, 5)
d

np.linspace(0, 2, 9)

e = np.full((2, 2), 7)
e

f = np.eye(2)
f
np.eye(3, 4)

np.random.random((2, 2))
np.empty((3, 2))          #!!!!! ?????
z = np.empty((3, 2))          #!!!!! ?????
z
np.empty((8, 9))    # WHAT THE HELL IT IS ????

#%%

np.info(np.ndarray)   # ???

#%%
#%% SAVING AND LOADING

#%% BINARY

#%%

np.save('arr1', a)
# ls
del(a)
np.load('arr1.npy')
a
a = np.load('arr1.npy')
a

#%%
np.savez('arrs.npz', a, b, c)
del(a,b,c)
np.load('arrs.npz')
a
b
c
load = np.load('arrs.npz')
load   # ???

for k in load.keys(): print(k)

load['arr_0']
for k in load: print(load[k])

a = load['arr_0']
b = load['arr_1']
c = load['arr_2']

a
b
c

#%%
np.savez('arrs.npz', a=a, b=b, c=c)
del(a,b,c)
# ls

np.load('arrs.npz')
a
load = np.load('arrs.npz')
for k in load: print(k)
load['a']
a = load['a']
b = load['b']
c = load['c']

#%%  TEXT

np.savetxt('array_c.txt', c, delimiter=",")  # ValueError: Expected 1D or 2D array, got 3D array instead
np.savetxt('array_b.txt', b, delimiter=",")

btxt = np.loadtxt('array_b.txt')  # ValueError: could not convert string to float:
btxt = np.genfromtxt('array_b.txt', delimiter=",")
btxt

abctxt = np.loadtxt('abc.txt')   # ValueError: could not convert string to float: 'abcd'

numtxt = np.loadtxt('numeric.txt')  # only numbers in one column! (one number in a row)
numtxt


#%%
#%%
a = np.array([[1,2,3], [4,3,2]])
b = np.array([[-2, 0, 4], [3, 5, -1]])
c

a+b
a+c   # broadcasting

np.add(a, b)
a-b
np.subtract(a, b)

a*b   # elementwise !!!
np.multiply(a, b)

a/b
np.divide(a, b)

np.abs(b)
np.log(b)
np.log(a)
np.cos(a)
np.exp(a)

#%% matrix multiplication
a.T
np.transpose(a)

a.dot(b)
a.dot(b.T)

a @ b.T  #!!

#%% reshaping
a
a.reshape(3, 2)
a.reshape((3, 2))   # dimensionality passed as a tuple

a.reshape(3, 2, 1)
a.reshape(1, 6)
a.reshape(4, 1)   # ValueError: cannot reshape array of size 6 into shape (4,1)

# the same as
np.reshape(a, (3, 2))
np.reshape(a, (1, 6))

# One shape dimension can be -1.
# In this case, the value is inferred from the length of the array and remaining dimensions.

a.reshape(-1, 2)
a.reshape(-1, 2, 1)
a.reshape(3, -1)
a.reshape(6, -1, 1)

#%% adding dimension
a.reshape((1,2,3))
np.reshape(a, (1,2,3))

np.expand_dims(a, axis=0)
a.expand_dims(axis=0)       #! AttributeError: 'numpy.ndarray' object has no attribute 'expand_dims'

a.reshape((1,2,3))
np.array([a])

# but reshape has many more options
a.reshape((2,3,1))

#%% concatenations
a
b
np.concatenate((a, b), axis=0)
# this is not:
np.array([a, b])

np.concatenate((a, b), axis=1)

#%% aggregates
#%%

np.cross(a, b)     # only in R^3 - cross product of two vectors - orthogonal to them; ...
ab0 = np.cross(a[0,:], b[0,:])
ab0
ab1 = np.cross(a[1,:], b[1,:])
ab1

np.array(ab0) @ np.array([a[0,:], b[0,:]]).T
np.array(ab1) @ np.array([a[1,:], b[1,:]]).T

np.reshape(ab0, (1, 3)) @ np.array([a[0,:], b[0,:]]).T
ab0.reshape((1, 3)) @ np.array([a[0,:], b[0,:]]).T


#%%
np.corrcoef(a)
np.corrcoef(b)
np.corrcoef(a, b)
np.corrcoef(a.T, b)   # err
np.corrcoef(a.T, b.T)

a.corrcoef()  # AttributeError: 'numpy.ndarray' object has no attribute 'corrcoef'

np.cov(a)
np.cov(b)
np.cov(a, b)

#%%
a.sum()
a.sum(axis=0)
a.sum(axis=1)
a.sum(1)

a.cumsum()
a.cumsum(0)
a.cumsum(1)

a.min()
a.min(0)
a.min(1)

a.max(1)
a.cumprod()

a.mean()
a.mean(0)

a.median()  # 'numpy.ndarray' object has no attribute 'median'
np.median(a)
np.median(a, axis=1)
np.median(a, 1)

np.std(a)
np.std(a, 1)

#%% VIES AND COPIES
h = a.view()
h

h[0,0]
h[0,0] = 0
h
a  # elemnt of a also changed
del(h)
a

h = a.view()
h
del(a)
h
a = h
a
del(h)
a

#%% deepcopy
ca = np.copy(a)
ca
a[0,0] = 1
a
ca # value of a deepcopy do not change

da = a.copy()
da
a[0,0] = -1
da # value of a deepcopy do not change

#%% sorting
r = np.random.randint(0, 12, (3, 4))
r
r.sort()
r
r.sort(0)
r

r = np.random.randint(0, 12, (3, 4))
r
np.sort(r)
r

#%%
#%% SUBSETTING, SLICING, INDEXING

#%%

r = np.random.randint(0, 12, (3, 4))