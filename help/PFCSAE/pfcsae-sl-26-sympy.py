# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Wed Dec 27 14:19:12 2017

26. Sympy
=========
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/PFCSAE
ls

import importlib ## may come in handy

import sympy

import pylab as pl
import scipy as sp
## importlib.reload(sp)
import numpy as np

#%%
'''
1. Symbolic Python - basics
---------------------------
'''

import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')

x+x
t = (x+y)**2
t
print(t)

sympy.expand(t)
sympy.pprint(t)
sympy.printing.latex(t)

t.subs(x, 3)
t.subs(x, 3).subs(y, 1)

n = t.subs(x,3).subs(y, sympy.pi)
n
n.evalf()    ## EVALuate to Float

p = sympy.pi
p
eval(p)  ## TypeError: eval() arg 1 must be a string, bytes or code object
p.evalf()
p.evalf(47)

#%%
## infinity

sympy.limit(1/x, x, 50)   ## \lim_{x\to 50} 1/x

sympy.limit(1/x, x, sympy.oo)   ## oo is infinity

sympy.limit(sympy.sin(x)/x, x, 0)

sympy.limit(sympy.sin(x)**2/x, x, 0)

sympy.limit(sympy.sin(x)/x**2, x, 0)

#%%
## integration

a, b = sympy.symbols('a, b')
a
b

sympy.integrate(2*x, (x, a, b))

sympy.integrate(2*x, (x, .1, b))

sympy.integrate(2*x, (x, .1, 2))

#%%
## Taylor series

tseries = sympy.series(sympy.sin(x), x, 0)
tseries

sympy.pprint(tseries)

tseries = sympy.series(sympy.sin(x), x, 0, n=10)
tseries
sympy.pprint(tseries)

#%%
## solving equations

x = sympy.Symbol('x')
x

(x+2)*(x-3)
r = (x+2)*(x-3)
r
sympy.expand(r)
sympy.solve(r, x)  ## solve r=0

r0 = sympy.expand(r)
r0
sympy.expand(r0)   ## no more expansion

sympy.pprint(r0)

sympy.solve(r0, x)

sympy.plot(r0)
sympy.plot(r0,(x,-5,5))

#%%
'''
In the Jupyter Notebook, run sympy.init_printing() to set up (LATEX-style) rendered output

'''

