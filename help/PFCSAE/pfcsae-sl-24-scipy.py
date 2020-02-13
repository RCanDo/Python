# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec 21 15:07:38 2017

24. SciPy
=========
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/PFCSAE
ls

import importlib as il

import numpy as np
import scipy as sp
## import scipy.interpolate as spi
import pylab as pl

#%%
help(sp)
'''
stats --- Statistical Functions
sparse --- Sparse matrix
lib --- Python wrappers to external libraries
linalg --- Linear algebra routines
signal --- Signal Processing Tools
misc --- Various utilities that don't have another home.
interpolate --- Interpolation Tools
optimize --- Optimization Tools
cluster --- Vector Quantization / Kmeans
fftpack --- Discrete Fourier Transform
io --- Data input and output
integrate --- Integration routines
lib.lapack --- Wrappers to LAPACK library
special --- Special Functions
lib.blas --- Wrappers to BLAS library
'''

#%%
'''
1. Interpolation of data
------------------------
'''

#%%
def create_data(a=0, b=1, n=7):
    """Given an integer n, returns n data points x and values y as a numpy.array."""
    xmax = 5.
    x = np.linspace(0, xmax, n)  #!#!
    y = -x**2
    # add some noise
    y += 1.5 * np.random.normal(size=len(x))
    return x, y

#%% e.g.

xx, yy = create_data()

pl.plot(xx, yy, 'o', label='date')

min(xx)
max(xx)
sum(xx)

pl.mean(xx)
pl.median(xx)
pl.var(xx)

#%%
## main program

xx, yy = create_data(0,5,11)
pl.plot(xx, yy, 'o', label='data points')

#%%
## use finer and regular mesh for plot
a, b = min(xx), max(xx)
h = b-a
n = 1000

xfine = np.linspace( a, b, 1000)
type(xfine)
xfine.shape
xfine.size
xfine.nbytes
## xfine

#%%
## interpolate with piecewise constant function (p=0)
y0 = sp.interpolate.interp1d(xx, yy, kind='nearest', fill_value='extrapolate')

type(y0)    ## scipy.interpolate.interpolate.interp1d
    ## not an array, it's function or sth like that...
y0.axis
y0.x
y0.y

pl.plot(xfine, y0(xfine), label='nearest')

#%%
y1 = sp.interpolate.interp1d(xx, yy, kind='linear', fill_value='extrapolate')

pl.plot(xfine, y1(xfine), label='linear')

#%%
y2 = sp.interpolate.interp1d(xx, yy, kind='cubic', fill_value='extrapolate')

pl.plot(xfine, y2(xfine), label='cubic')

#%%

pl.legend()
pl.xlabel('x')
pl.savefig('interpolate.pdf')
pl.show()

#%%
'''
2. Curve fitting
----------------
'''
import scipy.optimize as spo  ## not needed if scipy already imported although you must use the whole name

#%%
## you may use the same x as above, or create new with the same function

xx, yy = create_date(0, 5, 12)
pl.plot(xx, yy, 'o', label='data points')

#%%
## MODEL must be defined first

def model(x,  a, b, c):
    return a*x**2 + b*x + c

model

#%%

p, pcov = sp.optimize.curve_fit(model, xx, yy)
p
pcov

a, b, c = p
a
b
c
a, b, c

pl.plot(xfine, model(xfine, a, b, c), label='curve_fit')

pl.xlabel('x')
pl.ylabel('y')
pl.legend()
pl.show()



#%%
'''
3. Integration
--------------
'''

import scipy.integrate as spg

#%%
## some function to be integrated

def fun(x):
    return np.exp(np.cos(-2*x*np.pi)) + 3.2

xx = np.linspace(-2, 2, num=100)

pl.plot(xx, fun(xx), label='fun')

#%% quad integration from -2 to 2

res, err = sp.integrate.quad(fun, -2, 2)
print("The numerical result is {:f} (+-{:g})".format(res, err))


res, err = sp.integrate. {...nothing fits here...}  (fun, -2, 2)
print("The numerical result is {:f} (+-{:g})".format(res, err))

#%%
'''
4. Optimisation (Minimisation)
------------------------------

Optimisation typically described as:
given a function f(x), find xm so that f(xm) is the (local) minimum of f.
To maximise f(x), create a second function g(x) = -f(x) and minimise g(x).
Optimisation algorithms need to be given a starting point (initial guess x0 as close as possible to xm).
Minimum position x obtained may be local (not global) minimum
'''

def fun(x):
    return sp.cos(x) - 3*sp.exp(-(x-.2)**2)

xx = sp.arange(-10, 10, .1)
pl.plot(xx, fun(xx), label='$\cos(x)-3e^{-(x-0.2)^2}$')
pl.xlabel('x')
pl.grid()
pl.axis([-5, 5, -2.2, .5])
pl.legend(loc='lower left')

#%%
## find minima of fun(x) from 1.0 and 2.0

## init = 1.
min1 = sp.optimize.fmin(fun, 1.)
min1
print("Start search at x=1., minimum is", min1)
pl.plot(1., fun(1.), 'or', label='init1')
pl.plot(min1, fun(min1), 'vr', label='min1')

#%%
## init = 2.
min2 = sp.optimize.fmin(fun, 2.)
min2
print("Start search at x=2., minimum is", min2)
pl.plot(2., fun(2.), 'og', label='init2')
pl.plot(min2, fun(min2), 'vg', label='min2')

#%%
pl.legend(loc='lower left')
pl.show()
