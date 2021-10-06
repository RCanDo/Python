#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Customized Colorbars Tutorial
subtitle:
version: 1.0
type: tutorial
keywords: [color]
description: |
    This tutorial shows how to build and customize standalone colorbars,
    i.e. without an attached plot.
remarks:
    - Not so important.
    - ???
todo:
    - problem 1
sources:
    - title: Customized Colorbars Tutorial
      link: https://matplotlib.org/stable/tutorials/colors/colorbar_only.html#sphx-glr-tutorials-colors-colorbar-only-py
    - title:
      link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: E:/ROBOCZY/Python/graphics/matplotlib/colors/
    date: 2021-10-04
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/graphics/matplotlib/")   #!!! adjust
os.chdir(WD)

print(os.getcwd())

#%%
import numpy as np
import pandas as pd

#%%
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
# plt.style.use('dark_background')
# see `plt.style.available` for list of available styles

#%%
#%% Customized Colorbars
"""
A colorbar needs a "mappable" (matplotlib.cm.ScalarMappable) object (typically, an image)
which indicates the colormap and the `norm` to be used.
In order to create a colorbar without an attached image,
one can instead use a `ScalarMappable` with no associated data.

!!! However,
usually one creates `mappable` from data, with the use of appropriate method;
e.g. see next file `tut-02-colormaps.py`  # Creating listed colormaps
where
    mappable = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
"""

#%% Basic continuous colorbar
"""
Here we create a basic continuous colorbar with ticks and labels.

The arguments to the `colorbar` call are the `ScalarMappable`
(constructed using the `norm` and `cmap` arguments),
the axes where the colorbar should be drawn, and the colorbar's orientation.

For more information see the `colorbar` API.
"""
import matplotlib.pyplot as plt
import matplotlib as mpl

fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.cm.cool
norm = mpl.colors.Normalize(vmin=5, vmax=10)

mappable = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

fig.colorbar(mappable,
             cax=ax, orientation='horizontal',
             label='Some Units')

#%%
dir(norm)
dir(mappable)
mappable.cmap           # ListedColormap  - see next file
mappable.cmap.colors    # ...


#%%  Extended colorbar with continuous colorscale
"""
The second example shows how to make a discrete colorbar based on a continuous `cmap`.
With the "extend" keyword argument the appropriate colors are chosen
to fill the colorspace, including the extensions:
"""
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.cm.viridis
bounds = [-1, 2, 5, 7, 12, 15]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='both')

mappable = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)

fig.colorbar(mappable,
             cax=ax, orientation='horizontal',
             label="Discrete intervals with extend='both' keyword")

#%%
vars(norm)
"""
{'clip': False,
 'vmin': -1,
 'vmax': 15,
 'boundaries': array([-1,  2,  5,  7, 12, 15]),
 'N': 6,
 'Ncmap': 256,
 'extend': 'both',
 '_N': 7,
 '_offset': 1}
"""

#%% Discrete intervals colorbar
"""
The third example illustrates the use of a
`ListedColormap` which generates a colormap from a set of listed colors,
`colors.BoundaryNorm` which generates a colormap index based on discrete intervals
and extended ends to show the "over" and "under" value colors.

`over` and `under` are used to display data outside of the normalized [0, 1] range.
Here we pass colors as gray shades as a string encoding a float in the 0-1 range.

If a `ListedColormap` is used, the length of the bounds array must be one greater
than the length of the color list.
The bounds must be monotonically increasing.

This time we pass additional arguments to colorbar.
For the out-of-range values to display on the colorbar
without using the `extend` keyword with `colors.BoundaryNorm`,
we have to use the `extend` keyword argument directly in the `colorbar` call,
and supply an additional boundary on each end of the range.
Here we also use the spacing argument to make the length of each `colorbar` segment
proportional to its corresponding interval.
"""
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.colors.ListedColormap(['red', 'green', 'blue', 'cyan'])
cmap.set_over('0.25')   # shade of gray
cmap.set_under('0.75')  # shade of gray

bounds = [1, 2, 4, 7, 8]       # gray.25 1 'red' 2 'green' 4 'blue' 7 'cyan' 8 gray.75
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

mappable = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)

fig.colorbar( mappable,
    cax=ax,
    boundaries=[0] + bounds + [13],  # Adding values for extensions.
    extend='both',
    ticks=bounds,
    spacing='proportional',
    orientation='horizontal',
    label='Discrete intervals, some other units',
)

#%%
dir(cmap)
cmap.N       # 4
cmap.name    # from_list
cmap.colors  # ['red', 'green', 'blue', 'cyan']
cmap._i_bad     # 6
cmap._i_over    # 5
cmap._i_under   # 4

dir(norm)
norm.boundaries # array([1, 2, 4, 7, 8])
norm.vmin    # 1
norm.vmax    # 8

#%% Colorbar with custom extension lengths
"""
Here we illustrate the use of custom length colorbar extensions,
on a colorbar with discrete intervals.
To make the length of each extension the same as the length of the interior colors, use extendfrac='auto'.
"""
fig, ax = plt.subplots(figsize=(6, 1))
fig.subplots_adjust(bottom=0.5)

cmap = mpl.colors.ListedColormap(['royalblue', 'cyan', 'yellow', 'orange'])
cmap.set_over('red')   # shade of gray
cmap.set_under('blue')  # shade of gray


bounds = [-1.0, -0.5, 0.0, 0.5, 1.0]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

fig.colorbar(
    mpl.cm.ScalarMappable(cmap=cmap, norm=norm),
    cax=ax,
    boundaries=[-10] + bounds + [10],
    extend='both',
    extendfrac='auto',
    ticks=bounds,
    spacing='uniform',
    orientation='horizontal',
    label='Custom extension lengths, some other units',
)

#%%
help(mpl.cm.ScalarMappable)
"""
A mixin class to map scalar data to RGBA.

 The ScalarMappable applies data normalization before returning RGBA colors
 from the given colormap.

 Methods defined here:

 __init__(self, norm=None, cmap=None)
      Parameters
      ----------
      norm : `matplotlib.colors.Normalize` (or subclass thereof)
          The normalizing object which scales data, typically into the
          interval ``[0, 1]``.
          If *None*, *norm* defaults to a *colors.Normalize* object which
          initializes its scaling based on the first data processed.
      cmap : str or `~matplotlib.colors.Colormap`
          The colormap used to map normalized data values to RGBA colors.
"""
#%%