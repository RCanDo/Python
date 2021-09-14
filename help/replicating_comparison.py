#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 20:02:58 2020

@author: arek
"""

import numpy as np
import functools as ft
import operator as op

#%%
def rep_0(p, n):
    return [p]*n

def rep_lc(p, n):
    return [p for k in range(n)]

def rep_loop_app(p, n):
    l = []
    for k in range(n):
        l.append(p)
    return l
    
def rep_loop_plus(p, n):
    l = []
    for k in range(n):
        l += [p]
    return l

def rep_recur_app(p, n):
    if n>1:
        l = rep_recur_app(p, n-1)
        l.append(p)
    else:
        l = [p]
    return l
    
def rep_recur_plus(p, n):
    if n>1:
        l = rep_recur_plus(p, n-1)
        l += [p]
    else:
        l = [p]
    return l
    
def rep_ft(p, n):
    return ft.reduce(lambda l, v: l + [l[-1]], [p]*(n - 1), [p])

def rep_ft_2(p, n):
    # without lambda and list created externally
    def f(l, v):
        return l + [l[-1]]
    ll = [p]*(n - 1)
    return ft.reduce(f, ll, [p])

#%%
# the simplest the fastest:
%timeit [1]*1000                    # 2.48 µs ± 67.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# we loose ~0.1 µs o calling a fuction:
%timeit rep_0(1, 1000)              # 2.57 µs ± 70.7 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

# 10 times slower on list comprehension:
%timeit rep_lc(1, 1000)             # 26.2 µs ± 114 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# loops are another ~2.5 times slower:
%timeit rep_loop_app(1, 1000)       # 75.3 µs ± 850 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
%timeit rep_loop_plus(1, 1000)      # 83.6 µs ± 2.37 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# recurrence 10 times slower the lc
%timeit rep_recur_app(1, 1000)      # 275 µs ± 2.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit rep_recur_plus(1, 1000)     # 264 µs ± 1.51 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

# functools is a disaster... 10 times slower then recurrence!
%timeit rep_ft(1, 1000)             # 2.39 ms ± 77.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
%timeit rep_ft_2(1, 1000)           # 2.41 ms ± 13.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

#%%
#%%
# n=1000
# n=10000

p=.9; n=10000
%timeit for k in range(n): p**k     # 113 µs ± 1.01 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
                                    # 1.45 ms ± 8.67 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
%timeit [p**k for k in range(n)]    # 129 µs ± 824 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
                                    # 1.53 ms ± 2.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
ll = [None]*n
%timeit for k in range(n): ll[k] = p**k   # 162 µs ± 2.46 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
                                    # 1.93 ms ± 46.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
ll = [1] + [None]*(n-1)
%timeit for k in range(1, n): ll[k] = ll[k-1]*p   # 143 µs ± 5.1 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

#%%
ll = [1] + [None]*(n-1)

def powseq(p):
    lk=1
    for k in range(1, n): 
        lk = lk*p
        ll[k] = lk

%timeit powseq(p)     # 99.3 µs ± 2.12 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
                      # 1.04 ms ± 36.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

#%%
#%%
ll = [p]*(n-1)

def powseq_ft(p):
    def multi(q, p):
        return q*p
    ft.reduce(multi, ll, 1)
    
%timeit powseq_ft(p)  # 77.4 µs ± 1.38 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
                      # 766 µs ± 8.61 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

#%%
ll = [p]*(n-1)

def powseq_ft_op(p):
    ft.reduce(op.mul, ll, 1)
    
%timeit powseq_ft_op(p)  # 40 µs ± 731 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
                         # 407 µs ± 6.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

#%%
#%%