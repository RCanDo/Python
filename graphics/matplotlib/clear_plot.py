# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:01:24 2019

@author: kasprark
"""

import matplotlib.pyplot as plt


#%%
for i in range(5):
    fig = plt.figure()
    plt.close(fig)

# This returns a list with all figure numbers available
print(plt.get_fignums())  # empty list

#%%

for i in range(5):
    fig = plt.figure()
    fig.clf()   # clears given figure (this is a method of a class)
    plt.clf()   # clears currently active figure (function)
# This returns a list with all figure numbers available
print(plt.get_fignums())

#%%
"""
what is the difference between closing a figure and closing a window. Maybe that will clarify.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1000)
y = np.sin(x)

for i in range(5):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    plt.close(fig)

print(plt.get_fignums())

for i in range(5):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y)
    fig.clf()

print(plt.get_fignums())

#%%