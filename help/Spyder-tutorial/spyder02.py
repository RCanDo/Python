# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:35:41 2017

@author: kasprark
"""

from __future__ import division
import sympy

#%%
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

#%%

expr = (x+y)**3
print(expr)
expr.expand()

#%%