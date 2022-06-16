#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: 3D plots in matplotlib
subtitle:
version: 1.0
type: tutorial
keywords: [3d plot, matplotlib, pyplot]
description: |
    About 3d plots in matplotlib
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: The mplot3d Toolkit
      link: https://matplotlib.org/stable/gallery/index.html#d-plotting
      usage: |
          Collated from separate examples.
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: E:/ROBOCZY/Python/graphics/matplotlib
    date: 2021-04-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%

%reset

pwd
cd c:/PROJECTS/Python/tuts/Tutorial/mplot3d
ls

import importlib ## may come in handy

# importlib.reload(fibo)

#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

#%%
'''
Getting started
===============
'''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#%%
'''
Line plots
----------
'''

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')   # depricated
"""
Calling gca() with keyword arguments was deprecated in Matplotlib 3.4.
Starting two minor releases later, gca() will take no keyword arguments.
The gca() function should only be used to get the current axes,
or if no axes exist, create new axes with default keyword arguments.
To create a new axes with non-default arguments, use plt.axes() or plt.subplot().
HENCE, the former is better:
"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#%%
# Prepare arrays x, y, z
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()


#%%
'''
3D scatterplot
--------------

Demonstration of a basic scatterplot in 3D.
'''

# Fixing random state for reproducibility
np.random.seed(19680801)

def randrange(n, vmin, vmax):
    '''
    array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

#%%
'''

'''
