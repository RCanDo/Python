# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Wed Dec 13 15:57:13 2017

18. Numpy
=========
"""
## •

'''
`numpy`
* is an interface to high performance linear algebra libraries (ATLAS, LAPACK, BLAS)
* provides
    - the array object
    - fast mathematical operations over arrays
    - linear algebra, Fourier transforms, Random Number generation
* Numpy is NOT part of the Python standard library.
'''

#%%
'''
A. Arrays (vectors)
-------------------

* An array is a sequence of objects
* all objects in one array are of the same type
* you create arrays via lists or tuples

'''

import numpy as np

a = np.array([1, 4, 10])
a

type(a)

a.shape
type(a.shape)
np.shape(a)

a**2

np.sqrt(a)

a>3
type(a>3)

(a>3).shape

#%%

B = np.array([[0, 1.5], [10, 12]])
print(B)

B.size
B.shape

#%% you may use tuples instead of lists
A = np.array([(1,2), (3,4), (5,6)])
A

A = np.array(((1,2), (3,4), (5,6)))
A

A = np.array(([1,2], [3,4], [5,6]))
A

#%% shape

a.shape
B.shape

B.shape = (4,)
B
print(B)
B.shape = (2,2)
B                   ## rowwise !!! NOT columnwise like in R

#%% size = nr of elements
a.size
B.size

a.nbytes
B.nbytes

len(a)
A
len(A)
len(B)

#%%
'''
* All elements in an array must be of the same type
* For existing array, the type is the `dtype` attribute
'''

a.dtype
B.dtype

a2 = np.array([1, 4, 10], np.float)
a2
a2.dtype
a2.size


#%%

np.zeros((3,3))
np.zeros((3,6))
np.zeros((3,))

np.zeros(3)   ## WORKS!!!
 np.zeros(3,3)   ## TypeError: data type not understood

np.ones((3,))
np.ones((3,3))

np.ones(3)
 np.ones(3,3)    ## TypeError: data type not understood

b = np.ones((3,6))
b
len(b)
len(b[1])
b.shape

a3 = np.array(range(0, 10, 2))
a3
a3[1]
a3[-1]

len(a3)
a3.shape  ## dimensionality
a3.size   ## nr of elements
a3.nbytes ## size of bytes
a3.dtype  ## numpy type of elements

#%% array indexing

c = np.arange(12)  ## single 'r' !!! 'a range'
c
c.shape = (3, 4)
c

c[0, 0]
c[1, 2]

c[2, -1]
c[-1, -1]

#%% slicing
##  start:end:step

d = np.arange(10)
d

d[]   ## SyntaxError: invalid syntax
d[:]
d[::]

d[0:5]
d[2:5]
d[:4]
d[5:]
d[::2]
d[1:7:2]
d[1:8:2]

d[::-1]
d[0:5:-1]   ## !!! empty!!! strange
d[5:0]      ## !!! empty!!!
d[5:0:-1]   ## !!! from 5 to 1 !!! lack of 0
## hence to get all elements of array backward form given element you must omit second arg
d[5::-1]

reversed(d[:5])
print(reversed(d[:5]))   ## ???


d[::-2]
d[8::-2]

#%%
e = np.arange(20)
e.shape = (5,4)
e

e[1:4]
e[1:4,1:2]
e[1:4,1:3]

e[::-1,::-1]

e[:-1]   ## OK!!!

e[1,]
e[,1]    ## SyntaxError: invalid syntax
e[:,1]   ## OK!!!
e[1,:]

#%%
type(e.shape)

np.zeros(e.shape)
np.ones(e.shape)

np.transpose(e)
e.T

np.diag(e)
e.diagonal()
e.diagonal(1)
e.diagonal(-1)
e.diagonal(0,1,0)

np.diag(np.diag(e))

np.diag((1,2,3,4,5))
np.diag([1,2,3,4,5])
np.diag(range(3))


np.diag(3)     ## ValueError: Input must be 1- or 2-d.
np.diag((3))   ## ValueError: Input must be 1- or 2-d.
np.diag((3,))
np.diag([3])
np.shape(np.diag([3]))

np.diagflat([[1,2],[3,4]])
np.diagflat([[1,2],[3,4],[5,6]])



