# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 09:02:47 2018

@author: akasprzy
"""
#%%
import os

import matplotlib as mpl
import matplotlib.pyplot as plt

root = "E:/ROBOCZY"

#%%
#%%
plt.figure( num=None
         , figsize=None
         , dpi=None
         , facecolor=None
         , edgecolor=None
         , frameon=True
         , FigureClass=<class 'matplotlib.figure.Figure'>
         , clear=False
         , **kwargs
         )
...

plt.close('all')

#%% `pyplot` style
#%% v.0
plt.plot([1,2,3], [3,1,2], 'g',label='line1')
plt.plot([1,2,3], [1,3,2], 'r:',label='line2', )
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

#%% v.2
fig, ax = plt.subplots()  # a figure with a single Axes
ax.plot([1,2,3], [3,1,2])
...

#%% v.3
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
axs
# array([[<AxesSubplot:>, <AxesSubplot:>],
#        [<AxesSubplot:>, <AxesSubplot:>]], dtype=object)
axs[0, 0].plot([1,2,3], [3,1,2])
...

# see below for exact example on OO style

#%%
fig = mpl.figure.Figure()


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
plt.figure(figsize=(2,3), facecolor='black', edgecolor='red')
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

#%%