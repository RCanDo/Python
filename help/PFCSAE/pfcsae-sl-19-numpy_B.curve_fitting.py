# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Fri Dec 15 09:34:53 2017

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

%reset
dir()

cd c:/PROJECTS/Python/tuts/PFCSAE

import numpy as np
from numpy import array

#%%
'''
B. Other tools
--------------
'''

#%%
'''
### Linear algebra
'''

mm = array([[1, 2, 4], [2, 1, 0], [-1, 0, 1]])
mm

import numpy.random
A = np.random.rand(3,3)
A

help(np.random)
np.random?
np.random.randint?

#%%  matrix multiplication

np.dot(mm,A)

np.dot(A,mm)

x = np.random.randint(3,size=3)
x  ## array !!
x = np.random.randint(-3,3,size=3)
x  ## array !!

b = np.dot(mm,x)
b
np.shape(b)   ## (3,)

 np.dot(x,mm)

xx = np.random.randint(-3,3,size=(2,3))
xx

np.dot(xx,mm)   ## OK!!

np.dot(mm,xx)   ## ValueError: shapes (3,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)



#%% linear equations

import numpy.linalg as la  ## not necessary, you may use  numpy.linalg...

la.solve(mm,b)  ## OK! result is floating

la.solve(b,mm)  ## LinAlgError: 1-dimensional array given. Array must be at least two-dimensional



#%% other algebra tools


help(np.linalg)

np.linalg.norm(mm)
np.linalg.inv(mm)
np.linalg.inv(mm)

np.linalg.det(mm)

#%% eigenvalues & eigenvectors
np.linalg.eig(mm)

mm
eigval, eigvec = np.linalg.eig(mm)

eigval
 np.shape(eigval)
eigvec
 np.shape(eigvec)
 eigvec[0,]
 eigvec[:,0]

np.dot(eigvec[0,],mm) / eigval[0]

np.dot( np.dot(np.transpose(eigvec),np.diag(eigval)),eigvec )
np.dot( np.dot(np.transpose(eigvec),np.diag(eigval)),eigvec ) - mm
np.dot( np.dot(eigvec,np.diag(eigval)), np.transpose(eigvec) )

## nothing works!!!
## ???



#%%
np.linalg.eigvals(mm)

#%%
np.linalg.qr(mm)
np.linalg.qr(mm)[0]
np.linalg.qr(mm)[0]**2

#%%
'''
### Curve Fitting

* We typically fit lower order polynomials or other functions (which are the model that we expect the data to follow)
  through a number of points (often measurements).
* We typically have many more points than degrees of freedom, and would employ techniques such as
  _least squared fitting_.
* The function `numpy.polyfit` provides this functionality for polynomials.
* The function `scipy.optimize.curve_fit` provides curve fitting for generic functions (not restricted to polynomials).
'''


#%%
'''
### Other comments

* numpy provides fast array operations (comparable to Matlab’s matrices)
* fast if number of elements is large: for an array with one element, numpy.sqrt will be slower than math.sqrt
* speed-ups of up to factor 50 to 300 are possible using numpy instead of lists
* Consult Numpy documentation if used outside this course.
* Matlab users may want to read
  [Numpy for Matlab Users](https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html)
'''

#%%
'''
### Plotting arrays (vectors)
'''

import pylab as pl
import numpy as np

t = np.arange(0, 10 * np.pi, .01)
t
len(t)
t.shape
np.shape(t)

y = np.cos(t)
y.shape

pl.plot(t, y)
pl.xlabel('t')
pl.ylabel('y(t)')
pl.show()

import matplotlib

%matplotlib inline
pl.plot(t,y)

%matplotlib qt5
pl.plot(t,y)
matplotlib.show()  ## AttributeError: module 'matplotlib' has no attribute 'show'

%matplotlib notebook  ## cannot...
pl.plot(t,y)

#%%
'''
### Matplotlib / Pylab

* Matplotlib tries to make easy things easy and hard things possible
* Matplotlib is a 2D plotting library which produces publication quality figures (increasingly also 3d)
* Matplotlib can be fully scripted but interactive interface is available

### Matplotlib in IPython QTConsole and Notebook

Within the IPython console (for example in Spyder) and the Jupyter Notebook, use

* `%matplotlib inline` to see plots inside the console window, and
* `%matplotlib qt` to create pop-up windows with the plot when the `matplotlib.show()` command is used.
  We can manipulate the view interactively in that window.
* Within the notebook, you can use `%matplotlib notebook` which embeds an interactive window in the note book.

### Pylab

Pylab is a Matlab-like (state-driven) plotting interface (and comes with `matplotlib`).
* Convenient for ’simple’ plots
* Check examples in lecture note text book and
* Make use of help(pylab.plot) to remind you of line styles, symbols etc.
* Check gallery at  http://matplotlib.org/gallery.html#pylab_examples

### Matplotlib.pyplot

Matplotlib.pyplot is an object oriented plotting interface.
* Very fine grained control over plots
* Check gallery at Matplotlib gallery
* Try Matplotlib notebook (on module’s home page) as an introduction and useful reference.

'''

#%%



