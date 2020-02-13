# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:05:20 2019

@author: staar
"""

def deep_flatten(lst):
    flat = []
    for l in lst:
        if isinstance(l, list):
            flat += deep_flatten(l, k+1)
        else:
            flat.append(l)
    return flat

deep_flatten([1, [2], [[3], 4], 5])
