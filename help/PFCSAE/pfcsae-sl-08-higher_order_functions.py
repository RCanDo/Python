# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Tue Dec 12 13:52:36 2017

8. Higher Order Functions
=========================
"""

%reset
dir()

import math as m

#%%
def print_fun_tab(xx,f):
    for x in xx:
        print("{}({:7.2f}) = {:7.2f} ".format(f.__name__, x, f(x)))

xx = range(-3,3)
print_fun_tab(xx,m.sin)

#%%
def square(x):
    return x**2

print_fun_tab(xx,square)

#%%


