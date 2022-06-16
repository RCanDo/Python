#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Matplotlib essence
subtitle:
version: 1.0
type: cheat-sheet
keywords: [plot, axes, axis, artist, line, subplot, point]
description: |
    How to begin with matplot lib - the essence.
remarks:
todo:
sources:
    - title: Tutorials
      link: https://matplotlib.org/stable/tutorials/index.html
    - title: API (Python Module Index)
      link: https://matplotlib.org/stable/py-modindex.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: E:/ROBOCZY/Python/graphics/matplotlib/
    date: 2021-10-04
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
#%%
import os, sys, json

#%%
ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/graphics/matplotlib/")   #!!! adjust
os.chdir(WD)

#%%
WD = os.getcwd()
print(WD)

#%%
import matplotlib as mpl
import matplotlib.pyplot as plt

#%%
#%%
plt.figure( num=None  #!!!  number or label for a figure;
         , figsize=None, Width, height in inches
         , dpi=None, float, default: :rc:`figure.dpi`
         , facecolor=None
         , edgecolor=None
         , frameon=True, If False, suppress drawing the figure frame.
         , FigureClass=<class 'matplotlib.figure.Figure'>
         , clear=False, If True and the figure already exists, then it is cleared.
         , tight_layout : bool or dict, default: :rc:`figure.autolayout`
            If ``False`` use *subplotpars*. If ``True`` adjust subplot
            parameters using `.tight_layout` with default padding.
            When providing a dict containing the keys ``pad``, ``w_pad``,
            ``h_pad``, and ``rect``, the default `.tight_layout` paddings will be overridden.      !!!
         , constrained_layout : bool, default: :rc:`figure.constrained_layout.use`
            If ``True`` use constrained layout to adjust positioning of plot elements.
            Like ``tight_layout``, but designed to be more flexible.
            See `/tutorials/intermediate/constrainedlayout_guide` for examples.
            (Note: does not work with `add_subplot` or  `~.pyplot.subplot2grid`.)
         , **kwargs
         )
...

plt.close('all')

#%% `pyplot` style
#%% v.0
plt.plot([1,2,3], [3,1,2], 'g',  label='line1')
plt.plot([1,2,3], [1,3,2], 'r:', label='line2', )
plt.legend()

plt.xlabel('X')
plt.ylabel('Y')

plt.title('lines')
plt.suptitle("Plot")

# i.e. everything via `plt....`


#%% Object Oriented (OO) style
#%% v.1
fig = plt.figure()  # an empty figure with no Axes
#!  fig.plot([1,2,3],[3,1,2])       #! AttributeError: 'Figure' object has no attribute 'plot'

ax = fig.add_subplot()
ax.plot([1,2,3], [3,1,2])
...

#%% v.2 --
fig, ax = plt.subplots()       # a figure with a single Axes
ax.plot([1,2,3], [3,1,2])
...

#%% v.2a
fig, axs = plt.subplots(2, 3)  # a figure with a 2x3 grid of Axes (rows x columns) -- opposite to figsize (width x height)
axs
# array([[<AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>],
#        [<AxesSubplot:>, <AxesSubplot:>, <AxesSubplot:>]], dtype=object)
axs[0, 0].plot([1,2,3], [3,1,2])
...

# see below for exact example on OO style

#%%
fig = mpl.figure.Figure()
...

#%% style and params
#%%
mpl.rcParams
mpl.get_configdir()

plt.style.available

#%%
plt.style.use('dark_background')

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3], [3,1,2])

#%%
plt.figure(figsize=(2,3), facecolor='gray', edgecolor='red')
plt.plot([1,2,3], [3,1,2])


#%% OO style again
#%% ad v.1
#
plt.style.use( os.path.join(root + '/Python/graphics/matplotlib/black.mplstyle') )

fig = plt.figure()

ax = fig.add_subplot(111)

ax.plot([1,2,3], [3,1,2], label='line 1')
ax.plot([1,2,3], [2,1,3], 'r--', label='line 2')
ax.plot([1,2,3], [2,3,1], 'g:', label='line 3')
ax.legend()

ax.locator_params()

ax.grid()

ax.set_xlabel("X") #, fontsize = 7)
ax.set_ylabel("Y")

ax.set_title("some plots")

fig.suptitle("Plots", color='cyan', weight='bold')

#%%
#plt.tight_layout()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=.5)                ## fraction of fontsize
#plt.subplots_adjust(left=0.03, right=0.97, top=0.97, bottom=0.03)   ## fraction of a figure

#%%
#%% division of figure into arbitrary axes

fig = plt.figure(figsize=[7, 7], facecolor='gray')

# ( x_left, y_bottom, length_horizontal, length_vertical )

ax_bl = fig.add_axes([0, 0, .35, .65])      # b-l
ax_bl.set_facecolor('silver')
ax_bl.text(x=.5, y=.5, s="[0, 0, .35, .65]")

ax_br = fig.add_axes([.4, 0, .6, .35])    # b-r
ax_br.set_facecolor('ivory')
ax_br.text(x=.5, y=.5, s="[.4, 0, .6, .35]")

ax_tl = fig.add_axes([0, .7, .65, .35])     # t-l
ax_tl.set_facecolor('beige')
ax_tl.text(x=.5, y=.5, s="[0, .7, .65, .35]")

ax_tr = fig.add_axes([.7, .4, .3, .6])    # t-r
ax_tr.set_facecolor('lavender')
ax_tr.text(x=.5, y=.5, s="[.7, .4, .3, .6]")

ax_c  = fig.add_axes([.4, .4, .25, .25])   # center
ax_c.set_facecolor('tan')
ax_c.text(x=.5, y=.5, s="[.4, .4, .25, .25]")

#%%
#%% close / clear

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
#%%  colors
# colormaps
dir(mpl.cm)

# color data
dir(mpl._color_data)
mpl._color_data.BASE_COLORS
mpl._color_data.TABLEAU_COLORS
mpl._color_data.CSS4_COLORS
mpl._color_data.XKCD_COLORS

# or
plt.colormaps()

#%%
dir(mpl.figure)
help(mpl.figure.Figure)
fig = mpl.figure.Figure()
dir(fig)
vars(fig)

#%%
#%%  multiple figures
""" help(plt.sublots)
num : integer or string, optional, default: None
     A `.pyplot.figure` keyword that sets the figure number or label.
"""

f1 = plt.figure(1)
ax = f1.add_subplot()
ax.plot([1,2,3], [3,1,2])

f2, axs = plt.subplots(1, 2, figsize=(10, 5), num='qq') #!!! num = .. providing number or label for the _figure_
axs[0].scatter([1, 2, 3], [-1, 1, 0])
axs[1].plot([1, 2, 3], [-1, 1, 0])

plt.gcf()   # <Figure size 1000x500 with 4 Axes>     # get current figure
i = plt.gcf()   # get current figure
i   # <Figure size 1000x500 with 4 Axes>

plt.get_fignums()       # [1, 2]
plt.get_figlabels()     # ['', 'qq']

# changing current figure:
plt.figure(1)    # now the first is active
plt.gcf()   # <Figure size 640x480 with 1 Axes>
plt.plot([0, 1, 2], [1, 2, 0])

axs[0].plot([0, 3], [0, 0], c='gray')
plt.gcf()   # <Figure size 640x480 with 1 Axes>   still Fig 1 is 'current'

plt.figure('qq')    # now 'qq' first is active
plt.plot([0, 2], [0, 0], '*:r')
axs[0].plot([0, 2], [1, 1], marker='*', linestyle=':', color='g', linewidth=3)
plt.plot([0, 2], [-1, -1], '*:b')
plt.plot([0, 2], [-1, -1], '*:k')   # always last axis ???

plt.close("all")

#%%
#%% other examples

#%%  scale & grid
N = 10
y = np.zeros(N)
plt.semilogx(np.geomspace(1, 1000, N, endpoint=True), y + 1, 'o')
plt.semilogx(np.geomspace(1, 1000, N, endpoint=False), y + 2, 'o')
plt.axis([0.5, 2000, 0, 3])
plt.grid(True, color='0.7', linestyle='-', which='both', axis='both')

#%%
