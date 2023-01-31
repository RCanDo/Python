#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:13:53 2020

@author: arek
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
plt.plot(range(10), np.random.randint(-10, 10, 10))

plt.axhspan(-1, 2)
plt.axhspan(-1, 2, color='green')
plt.axhspan(-1, 2, .2, .4, color='r')

plt.axvspan(6, 9, color='y')
plt.axvspan(6, 9, .1, .3, color='m')

plt.axhline(0, color='k')
plt.axhline(1, .2, .5, color='k')

plt.axvline(2, color='k')
plt.axvline(4, .1, .9, color='k')

plt.axvline(3, color='b')

#%%
fig, ax = plt.subplots()
help(ax.vlines)

#%%



#%%
