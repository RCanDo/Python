#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:32:12 2022
https://carlostgameiro.medium.com/fast-pairwise-combinations-in-numpy-c29b977c33e2
https://numpy.org/doc/stable/reference/generated/numpy.triu_indices.html
"""
#%%
import itertools
import numpy as np

def numpy_combinations(x):

    idx = np.stack(np.triu_indices(len(x), k=1), axis=-1)

    return x[idx]

def itertools_combinations(x):

    idx = np.stack(list(itertools.combinations(x, r=2)))

    return x[idx]

#%%
%time a = numpy_combinations(np.arange(1000))
# CPU times: user 5.99 ms, sys: 314 µs, total: 6.3 ms
# Wall time: 5.73 ms

%time b = itertools_combinations(np.arange(1000))
# CPU times: user 541 ms, sys: 25.6 ms, total: 567 ms
# Wall time: 565 ms

(a == b).all()
# True

#%%
