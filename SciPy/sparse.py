#! python3
# -*- coding: utf-8 -*-
"""
---
title: Sparse matrices
subtitle:
version: 1.0
type: examples
keywords: [sparse matrix, linalg, linear algebra, ]
description: |
    About sparse matrices
sources:
    - title: Sparse matrices
      link: https://docs.scipy.org/doc/scipy/reference/sparse.html
    - link: https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_array.html#scipy.sparse.csr_array
    - title: Using a sparse matrix versus numpy array
      link: https://stackoverflow.com/questions/36969886/using-a-sparse-matrix-versus-numpy-array
file:
    date: 2021-10-21
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import os, sys, json

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('dark_background')
# see `plt.style.available` for list of available styles

#!!! SciPy sub-packages need to be imported separately !!!
from scipy import linalg, stats, sparse

from utils.builtin import *  # flatten, paste
from utils.ak import *  # data_frame
from utils.config.setup import pandas_options
pandas_options()

WD = os.getcwd()
print(WD)

#%%
#%%
"""
Note
----

This package is switching to an _array_ interface, compatible with NumPy arrays, from the older _matrix_ interface.
We recommend that for all new work you use the array objects like
`bsr_array`, `coo_array`, etc. instead of `bsr_matrix`, `coo_matrix`, etc.

When using the array interface, please note that:

- `x * y` no longer performs matrix multiplication, but element-wise multiplication (just like with NumPy arrays).
  To make code work with both arrays and matrices, use `x @ y` for matrix multiplication.

- Operations such as sum, that used to produce dense matrices,
  now produce arrays, whose multiplication behavior differs similarly.

- Sparse arrays currently must be two-dimensional.
  This also means that all slicing operations on these objects must produce two-dimensional results,
  or they will result in an error.
  This will be addressed in a future version.

The construction utilities (`eye`, `kron`, `random`, `diags`, etc.) have not yet been ported,
but their results can be wrapped into arrays:

    A = csr_array(eye(3))

Usage information
-----------------

There are seven available sparse _array_ (former sparse _matrix_) types:

    csc_array (csc_matrix): Compressed Sparse Column format     – efficient multiplication, inversion

    csr_array (csr_matrix): Compressed Sparse Row format        – efficient multiplication, inversion

    bsr_array (bsr_matrix): Block Sparse Row format

    lil_array (lil_matrix): List of Lists format                – efficient construction

    dok_array (dok_matrix): Dictionary of Keys format           – efficient construction

    coo_array (coo_matrix): COOrdinate format (aka IJV, triplet format)     – efficient construction, intuitive

    dia_array (dia_matrix): DIAgonal format

To construct a matrix efficiently, use either `dok_matrix` or `lil_matrix`.

The `lil_matrix` class supports basic slicing and fancy indexing
with a similar syntax to NumPy arrays.

To perform manipulations such as multiplication or inversion,
first convert the matrix to either `CSC` or `CSR` format.

The `lil_matrix` format is row-based, so conversion to `CSR` is efficient,
whereas conversion to `CSC` is less so.

All conversions among the `CSR`, `CSC`, and `COO` formats are efficient, linear-time operations.

As illustrated below, the `COO` format may also be used to efficiently construct matrices.

CSR column indices are not necessarily sorted.
Likewise for CSC row indices.
Use the `.sorted_indices()` and `.sort_indices()` methods
when sorted indices are required (e.g., when passing data to other libraries).

!!! Warning !!!

Despite their similarity to NumPy arrays,
!!!  it is strongly discouraged to use NumPy functions directly on these matrices  !!!
because NumPy may not properly convert them for computations,
leading to unexpected (and incorrect) results.
If you do want to apply a NumPy function to these matrices,
first check if SciPy has its own implementation for the given sparse matrix class,
or convert the sparse matrix to a NumPy array (e.g., using the `.toarray()` method of the class) first
before applying the method.
BUT then all efficiency of sparse matrices vanishes!

"""

# %% csr format – best for multiplication / inversion
from scipy.sparse import csr_matrix, csr_array

A = csr_matrix([[1, 2, 0],
                [0, 0, 3],
                [4, 0, 5]])
A   # <Compressed Sparse Row sparse matrix of dtype 'int64' with 5 stored elements and shape (3, 3)>
print(A)
# <Compressed Sparse Row sparse matrix of dtype 'int64'
# 	with 5 stored elements and shape (3, 3)>
#   Coords	Values
#   (0, 0)	1
#   (0, 1)	2
#   (1, 2)	3
#   (2, 0)	4
#   (2, 2)	5

A = csr_array([[1, 2, 0],
                [0, 0, 3],
                [4, 0, 5]])
A   # <Compressed Sparse Row sparse array of dtype 'int64'with 5 stored elements and shape (3, 3)>
print(A)
# <Compressed Sparse Row sparse array of dtype 'int64'
# 	with 5 stored elements and shape (3, 3)>
#   Coords	Values
#   (0, 0)	1
#   (0, 1)	2
#   (1, 2)	3
#   (2, 0)	4
#   (2, 2)	5

# ! Hence, as for now, _array is basically the same as _matrix. Methods and attrs below are also the same.

A.toarray()
# array([[1, 2, 0],
#        [0, 0, 3],
#        [4, 0, 5]])
A.indices
# array([0, 1, 2, 0, 2], dtype=int32)   # indices of non-zeros along rows (1-dim) – but which for which row ???
A.indptr        # !
# array([0, 2, 3, 5], dtype=int32)
#  it has lenght  num_rows + 1
# i-th element indicates from which element of `A.indices` (inclusive)
# begins indices of non-zero elements in the i-th row :)  very funny!
# the last element is basically always the length of the .indices vector.
A.data
# array([1, 2, 3, 4, 5])

# more on `csr_array` further below

# %%
"""
To do a vector product between a sparse matrix and a vector
simply use the matrix dot method, as described in its docstring:
"""
v = np.array([1, 0, -1])
A.dot(v)
# array([ 1, -3, -1], dtype=int64)

"""
!!! Warning !!!

As of NumPy 1.7, `np.dot` is not aware of sparse matrices,
therefore using it will result on unexpected results or errors.
The corresponding dense array should be obtained first instead:
"""
np.dot(A, v)
# array([<Compressed Sparse Row sparse array of dtype 'int64'
#        	with 5 stored elements and shape (3, 3)>           ,
#        <Compressed Sparse Row sparse array of dtype 'int64'
#        	with 5 stored elements and shape (3, 3)>           ,
#        <Compressed Sparse Row sparse array of dtype 'int64'
#        	with 5 stored elements and shape (3, 3)>           ], dtype=object)
# ! better not !

np.dot(A.toarray(), v)      # ok
# array([ 1, -3, -1], dtype=int64)
"""
but then all the performance advantages would be lost.
The `CSR` format is specially suitable for fast matrix vector products.
"""
A @ v   # !
# array([ 1, -3, -1])

#%% Example 1
# Construct a 1000x1000 `lil_array` and add some values to it:

from scipy.sparse import lil_array
from scipy.sparse.linalg import spsolve  #!!!
# submodule: https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html#module-scipy.sparse.linalg

from numpy.linalg import solve, norm
from numpy.random import rand

A = lil_array((1000, 1000))
A[0, :100] = rand(100)
A[1, 100:200] = A[0, :100]  # ! NotImplementedError: We have not yet implemented 1D sparse slices;
                             # please index using explicit indices, e.g. `x[:, [0]]`
A[1, list(range(100, 200))] # ! NotImplementedError: We have not yet implemented 1D sparse slices;

A.setdiag(rand(1000))

# Now convert it to `CSR` format and solve `A x = b` for x:
A = A.tocsr()
A.data
A.indices
A.indptr        # array([   0,  100,  101, ..., 1097, 1098, 1099], dtype=int32)    ok
b = rand(1000)
x = spsolve(A, b)

# Convert it to a dense matrix and solve, and check that the result is the same:
x_ = solve(A.toarray(), b)

# Now we can compute norm of the error with:
err = norm(x-x_)
err   # np.float64(5.684341886080802e-14)

#%% Example 2
# Construct a matrix in COO format:
from scipy.sparse import coo_array, find

I = np.array([0,3,1,0])   # row
J = np.array([0,3,1,2])   # column
V = np.array([4,5,7,9])   # value
A = coo_array((V, (I, J)), shape=(4,4))
A   # <COOrdinate sparse array of dtype 'int64' with 4 stored elements and shape (4, 4)>
find(A) # (array([0, 1, 0, 3]), array([0, 1, 2, 3]), array([4, 7, 9, 5], dtype=int32))
# Notice that the indices do not need to be sorted.

#!!! Duplicate (i,j) entries are summed when converting to CSR or CSC.
I = np.array([0,0,1,3,1,0,0])
J = np.array([0,2,1,3,1,0,0])
V = np.array([1,1,1,1,1,1,1])
B = coo_array((V, (I, J)), shape=(4,4)).tocsr()
B   # <Compressed Sparse Row sparse array of dtype 'int64'	with 4 stored elements and shape (4, 4)>
B.toarray()
# array([[3, 0, 1, 0],
#       [0, 2, 0, 0],
#       [0, 0, 0, 0],
#       [0, 0, 0, 1]])
# This is useful for constructing finite-element stiffness and mass matrices.

# %%
# %%  csr_array  examples
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_array.html#scipy.sparse.csr_array

import numpy as np
from scipy.sparse import csr_array

csr_array((3, 4), dtype=np.int8).toarray()
# array([[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]], dtype=int8)

row = np.array([0, 0, 1, 2, 2, 2])
col = np.array([0, 2, 2, 0, 1, 2])
data = np.array([1, 2, 3, 4, 5, 6])
csr_array((data, (row, col)), shape=(3, 3)).toarray()
# array([[1, 0, 2],
#        [0, 0, 3],
#        [4, 5, 6]])

data = np.array([1, 2, 3, 4, 5, 6])
indices = np.array([0, 2, 2, 0, 1, 2])
indptr = np.array([0, 2, 3, 6])         # !
#  it has lenght  num_rows + 1;
# i-th element indicates from which element of `A.indices` (inclusive)
# begins indices of non-zero elements in the i-th row :)  very funny!
# the last element is basically always the length of the .indices vector.
csr_array((data, indices, indptr), shape=(3, 3)).toarray()
# array([[1, 0, 2],
#        [0, 0, 3],
#        [4, 5, 6]])

# Duplicate entries are summed together:
row = np.array([0, 1, 2, 0])
col = np.array([0, 1, 1, 0])
data = np.array([1, 2, 4, 8])
csr_array((data, (row, col)), shape=(3, 3)).toarray()
# array([[9, 0, 0],
#        [0, 2, 0],
#        [0, 4, 0]])

# As an example of how to construct a CSR array incrementally, the following snippet builds a term-document array from texts:

docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
indptr = [0]
indices = []
data = []
vocabulary = {}

for d in docs:
    for term in d:
        index = vocabulary.setdefault(term, len(vocabulary))
        indices.append(index)
        data.append(1)
    indptr.append(len(indices))

csr_array((data, indices, indptr), dtype=int).toarray()
# array([[2, 1, 0, 0],
#        [0, 1, 1, 1]])

#%%


#%%