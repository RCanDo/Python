#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Indexing routines 3
subtitle: Iteration - tut
version: 1.0
type: tutorial
keywords: [iteration, array, numpy]
sources:
    - title: Iterating Over Arrays
      link: https://numpy.org/doc/stable/reference/arrays.nditer.html#arrays-nditer
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
    name: indexing_routines-3_iteration_tut.py
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
#%% title: Iterating Over Arrays
#   link: https://numpy.org/doc/stable/reference/arrays.nditer.html#arrays-nditer
#%%
"""
Note
Arrays support the iterator protocol and can be iterated over like Python lists.
See the Indexing, Slicing and Iterating section in the Quickstart guide for basic usage and examples.
The remainder of this document presents the `nditer object and covers more advanced usage.

The iterator object nditer, introduced in NumPy 1.6, provides many flexible ways to visit all the elements of one or more arrays in a systematic fashion. This page introduces some basic ways to use the object for computations on arrays in Python, then concludes with how one can accelerate the inner loop in Cython. Since the Python exposure of nditer is a relatively straightforward mapping of the C array iterator API, these ideas will also provide help working with array iteration from C or C++.
Single Array Iteration

The most basic task that can be done with the nditer is to visit every element of an array. Each element is provided one by one using the standard Python iterator interface.
"""
a = np.arange(6).reshape(2,3)

for x in np.nditer(a):

    print(x, end=' ')


0 1 2 3 4 5

An important thing to be aware of for this iteration is that the order is chosen to match the memory layout of the array instead of using a standard C or Fortran ordering. This is done for access efficiency, reflecting the idea that by default one simply wants to visit each element without concern for a particular ordering. We can see this by iterating over the transpose of our previous array, compared to taking a copy of that transpose in C order.

Example

a = np.arange(6).reshape(2,3)

for x in np.nditer(a.T):

    print(x, end=' ')


0 1 2 3 4 5

for x in np.nditer(a.T.copy(order='C')):

    print(x, end=' ')


0 3 1 4 2 5

The elements of both a and a.T get traversed in the same order, namely the order they are stored in memory, whereas the elements of a.T.copy(order=’C’) get visited in a different order because they have been put into a different memory layout.
Controlling Iteration Order¶