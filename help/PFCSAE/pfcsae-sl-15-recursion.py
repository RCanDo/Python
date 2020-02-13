# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Wed Dec 13 12:57:05 2017

14. Recursion
=============
"""
## •

## recurring (or referencing) to previous (with lower indexes) values in a relevantly defined sequence

#%% factorial, i.e. n!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial(0)
factorial(1)
factorial(10)

[factorial(n) for n in range(10)]

#%% Fibonacci
## f(0) = 1, f(1) = 1, ..., f(n+1) = f(n) + f(n-1)

def fib(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n in [0,1]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

[fib(n) for n in range(20)]

#%%
fib(-1)

#%%


