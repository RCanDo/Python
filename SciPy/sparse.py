#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Sparse matrices
subtitle:
version: 1.0
type: examples
keywords: []
description: |
    About sparse matrices
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Sparse matrices
      link: https://docs.scipy.org/doc/scipy/reference/sparse.html
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: sparse.py
    path: E:/ROBOCZY/Python/SciPy/
    date: 2021-10-21
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

#%%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

#%%
ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/SciPy/")   #!!! adjust
os.chdir(WD)

#%%
WD = os.getcwd()
print(WD)

#%% Block delimiters allows to run separated blocks of code by one key-stroke
# e.g. Shift+Enter in Spyder

import numpy as np
import pandas as pd

"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""
#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

# %% other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500
# the same

#%%
pd.options.display.width = 120

#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('dark_background')
# see `plt.style.available` for list of available styles

#!!! SciPy sub-packages need to be imported separately !!!
from scipy import linalg, stats, sparse

#%%
#%%
"""
There are seven available sparse matrix types:

    csc_matrix: Compressed Sparse Column format

    csr_matrix: Compressed Sparse Row format

    bsr_matrix: Block Sparse Row format

    lil_matrix: List of Lists format       !

    dok_matrix: Dictionary of Keys format  !

    coo_matrix: COOrdinate format (aka IJV, triplet format)

    dia_matrix: DIAgonal format

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
#%%
"""
Matrix vector product

To do a vector product between a sparse matrix and a vector
simply use the matrix dot method, as described in its docstring:
"""
from scipy.sparse import csr_matrix

A = csr_matrix([[1, 2, 0], [0, 0, 3], [4, 0, 5]])

v = np.array([1, 0, -1])

A.dot(v)
# array([ 1, -3, -1], dtype=int64)

"""
!!! Warning !!!

As of NumPy 1.7, `np.dot` is not aware of sparse matrices,
therefore using it will result on unexpected results or errors.
The corresponding dense array should be obtained first instead:
"""
np.dot(A.toarray(), v)
#array([ 1, -3, -1], dtype=int64)
"""
but then all the performance advantages would be lost.
The `CSR` format is specially suitable for fast matrix vector products.
"""

#%% Example 1
# Construct a 1000x1000 `lil_matrix` and add some values to it:

from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve  #!!!
# submodule: https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html#module-scipy.sparse.linalg

from numpy.linalg import solve, norm
from numpy.random import rand

A = lil_matrix((1000, 1000))
A[0, :100] = rand(100)
A[1, 100:200] = A[0, :100]
A.setdiag(rand(1000))

# Now convert it to `CSR` format and solve `A x = b` for x:
A = A.tocsr()
b = rand(1000)
x = spsolve(A, b)

# Convert it to a dense matrix and solve, and check that the result is the same:
x_ = solve(A.toarray(), b)

# Now we can compute norm of the error with:
err = norm(x-x_)
err   # 3.06111178766429e-13

#%% Example 2
# Construct a matrix in COO format:

I = np.array([0,3,1,0])   # row
J = np.array([0,3,1,2])   # column
V = np.array([4,5,7,9])   # value
A = sparse.coo_matrix((V, (I, J)), shape=(4,4))
A
sparse.find(A) # (array([0, 1, 0, 3]), array([0, 1, 2, 3]), array([4, 7, 9, 5], dtype=int32))
# Notice that the indices do not need to be sorted.


#!!! Duplicate (i,j) entries are summed when converting to CSR or CSC.
I = np.array([0,0,1,3,1,0,0])
J = np.array([0,2,1,3,1,0,0])
V = np.array([1,1,1,1,1,1,1])
B = sparse.coo_matrix((V, (I, J)), shape=(4,4)).tocsr()
B
B.toarray()
# This is useful for constructing finite-element stiffness and mass matrices.

#%% Further details
"""
"""


#%%


#%%