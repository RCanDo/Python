# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Tue Dec 19 14:29:50 2017

23. Numpy usage examples
========================
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/PFCSAE
ls

#%% math, numpy, pylab
##

import time as t
import math as m
import numpy as np
#import matplotlib as mpl
import pylab as pl

import importlib as il

#%% np.linspace
#!#!#! GREAT COMMAND
np.linspace(-2,2,20)    ## from -2 to 2, 20 numbers together
                        ## it's array
xs = np.linspace(-5,5,100)
xs
type(xs)
len(xs)
np.shape(xs)

xs.shape
xs.size
xs.nbytes
xs.dtype
repr(xs)

#%% m.exp  on  'vectors'

m.exp(1)
m.exp(range(3))  ## TypeError: must be real number, not range

np.exp(1)
np.exp(range(3)) ## OK

map(m.exp, 1)    ## TypeError: 'int' object is not iterable
ys = map(m.exp, [1])
ys
type(ys)
list(ys)

ys = list(map(m.exp, [0, 1, 2, 3]))
ys

ys = list(map(m.exp, range(4)))
ys


#%% m.exp on arrays

ys = m.exp(xs)  ## TypeError: only length-1 arrays can be converted to Python scalars
                ## you cannot work matrix-wise using math library ...
type(xs)
list(xs)
## must use loop()
ys = list(map(m.exp, xs))
ys
plt = pl.plot(xs,ys)
plt        ## ???
print(plt) ## ...
del(plt)

pl.plot(xs, ys)
pl.xlabel('x')
pl.ylabel('exp(x)')
## pl.show()  ## ???

#%% np.exp

ys = np.exp(xs)    ## understands arrays i.e. works array-wise

pl.plot(xs, ys)

#%%
## more on numpy types

np.sqrt(4.) ## apply numpy-sqrt to scalar
    ## 2.0 # looks like float
type(np.sqrt(4.)) ## but is numpy-float
    ## <class numpy.float64>
float(np.sqrt(4.)) ## but can convert to float
    ## 2.0
a = np.sqrt(4.) ## what shape is the numpy-float?
a.shape
()
type(a) # just to remind us

## So numpy-scalars (i.e. arrays with shape ()) can be converted to float.
## In fact, this happens implicitly:
m.sqrt(np.sqrt(81))
    ## 3.0

## Conversion to float fails if array has more than one element
a = np.array([10., 20., 30.])
a           ## array([ 10., 20., 30.])
print(a)    ## [ 10. 20. 30.]
type(a)     ## <class numpy.ndarray>
a.shape     ## (3,)
float(a)
    ## Traceback (most recent call last): File "<stdin>", line 1, in <module>
    ## TypeError: only length-1 arrays can be converted to Python scalars
m.sqrt(a)
    ## Traceback (most recent call last): File "<stdin>", line 1, in <module>
    ## TypeError: only length-1 arrays can be converted to Python scalars

## However, if the array contains only one number, then the conversion is possible:
b = np.array(4.0)
type(b)     ## <class numpy.ndarray>
b.shape     ## ()
b           ## array(4.0)
float(b)    ## 4.0
m.exp(b)

m.sqrt(b)    ## 2.0
## Note: an array with shape (1,) can also be converted to a float:
c = np.array([3])
c.shape     ## (1,)
float(c)    ## 3.0
m.exp(c)

## This allows us to write functions f(x) that can take an input argument x
## which can either be a numpy.array or a scalar.

#%%
'''
Bigger example
--------------
Comparing efficiency of m.exp and np.exp via some more complicated function, namly:
    Mexican hat wavelet = Ricker wavelet, the second Hermite function (wavelet)
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet

The code for the below is in the module file numpy_math_compare.py
'''

import numpy_math_compare as nmc

il.reload(nmc)

nmc.

### parameters
a = -5; b = 5  ## limits
N = 1e4        ## nr of points

xs = np.linspace(a, b, N)
xs
type(xs)
xs.shape


#%% nmc.mexhat_m

pl.plot(xs, list(map(nmc.mexhat_m, xs)))
pl.plot(xs, nmc.mexhat_m(xs))   ## TypeError: only length-1 arrays can be converted to Python scalars

#%% nmc.mexhat_np

pl.plot(xs, list(map(nmc.mexhat_np, xs)))
pl.plot(xs, nmc.mexhat_np(xs))   ## OK, using np. no need for using loop/map

#%% nmc.time_this

nmc.time_this(lambda: nmc.mexhat_np(xs))
nmc.time_this(lambda: list(map(nmc.mexhat_m,xs)))

## nmc.time_this(lambda x: nmc.mexhat_np(x))

#%% nmc.compare

nmc.compare( lambda: nmc.mexhat_np(xs), lambda: list(map( nmc.mexhat_m, xs ) ) )

#%%
##






