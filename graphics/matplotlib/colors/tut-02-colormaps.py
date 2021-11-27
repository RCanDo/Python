#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Creating Colormaps in Matplotlib
subtitle:
version: 1.0
type: tutorial
keywords: [colormap]
description: |
remarks:
    - !!! see the end of file for most convenient solution !!!
      `cmap = LinearSegmentedColormap.from_list("mycmap", list(zip(nodes, colors)))`
todo:
    - problem 1
sources:
    - title: Creating Colormaps in Matplotlib
      link: https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html#creating-colormaps-in-matplotlib
    - title: Colormap Refernece
      link: https://matplotlib.org/stable/gallery/color/colormap_reference.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: tut-02-colormaps.py
    path: E:/ROBOCZY/Python/graphics/matplotlib/colors/
    date: 2021-10-05
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import os, json

ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/graphics/matplotlib/")   #!!! adjust
os.chdir(WD)

#%%
WD = os.getcwd()
print(WD)

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
"""
Matplotlib has a number of built-in `colormaps` accessible via `matplotlib.cm.get_cmap()`.

There are also external libraries like `palettable` that have many extra colormaps.

However, we often want to create or manipulate colormaps in Matplotlib.
This can be done using the class
    `ListedColormap` or
    `LinearSegmentedColormap`.
"""
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
"""
!!! Seen from the outside, both colormap classes map values between 0 and 1 to a bunch of colors. !!!

There are, however, slight differences, some of which are shown in the following.
"""
#%%  Getting colormaps and accessing their values
"""
First, getting a named colormap, most of which are listed in
'Choosing Colormaps in Matplotlib',
may be done using `matplotlib.cm.get_cmap()`, which returns a `colormap` object.

The second argument `N` gives the size of the list of colors used to define the colormap,
"""
viridis = mpl.cm.get_cmap('viridis', 8)
viridis
    # matplotlib.colors.ListedColormap
"""
!!! The object viridis is a __callable__,
that when passed a float between 0 and 1 returns an RGBA value from the colormap:
"""
viridis(.56, .6) #  (0.122312, 0.633153, 0.530398, .6)
# second argument is `alpha` (see help on __call__(self, X, alpha, bytes) )
help(viridis)
# the same as
help(ListedColormap)
"""
Colormap object generated from a list of colors.

This may be most useful when indexing directly into a colormap,
but it can also be used to generate special colormaps for ordinary
mapping.

Parameters
----------
colors : list, array
    List of Matplotlib color specifications, or an equivalent Nx3 or Nx4
    floating point array (*N* rgb or rgba values).
name : str, optional
    String to identify the colormap.
N : int, optional
    Number of entries in the map. The default is *None*, in which case
    there is one colormap entry for each element in the list of colors.
    If ::
        N < len(colors)
    the list will be truncated at *N*. If ::
        N > len(colors)
    the list will be extended by repetition.
"""
#%%
help(mpl.cm.viridis)  # see __call__ description
help(viridis)         #   "
"""
__call__(...)
Parameters
    X : float or int, ndarray or scalar
        The data value(s) to convert to RGBA.
        For floats, X should be in the interval ``[0.0, 1.0]`` to
        return the RGBA values ``X*100`` percent along the Colormap line.
        For integers, X should be in the interval ``[0, Colormap.N)`` to
        return RGBA values *indexed* from the Colormap with index ``X``.
    alpha : float, None
        Alpha must be a scalar between 0 and 1, or None.
    bytes : bool
        If False (default), the returned RGBA values will be floats in the
        interval ``[0, 1]`` otherwise they will be uint8s in the interval
        ``[0, 255]``.

    Returns
    -------
    Tuple of RGBA values if X is scalar, otherwise an array of
    RGBA values with a shape of ``X.shape + (4, )``.
"""

#%% notice that each colormap may be called directly

mpl.cm.viridis(.56, .6)   # (0.120081, 0.622161, 0.534946, .6)
help(mpl.cm.viridis)
dir(mpl.cm.viridis)
"""
Second argument is `alpha`.
How to pass `N`?
Notice that `mpl.cm.viridis` is an instance of `ListedColormap`
and `N` may be passed only on the initialisation of new instance (it's arg of __init__).

mpl.cm.get_cmap() is a way to call initialiser which
recreates given colormap with additional parameters like `N`
(probably from a template instance `mpl.cm.<colormap>`).
"""
mpl.cm.viridis.colors  #
len(mpl.cm.viridis.colors) # 256 colors
mpl.cm.viridis.N           # 256
viridis.colors    # only 8 colors
viridis.N         # 8

dir(viridis)
viridis.monochrome   # False
viridis.name         # 'viridis'

#%%
"""
Of course, one may call
"""
new_cmap = ListedColormap(colors, name='from_list', N=None)
# see the head of
help(ListedColormap)
"""
From this we see that such a direct call is not very useful;
especially `N` makes not much sense;

!!! It's really better to use
    `mpl.cm.get_cmap()`
    to load predefined colormaps
    limited to N different colors (evenly spaced across whole original colormap).

All the colormaps:
"""
dir(mpl.cm)
help(mpl.cm)
"""
colormap refernece
https://matplotlib.org/stable/gallery/color/colormap_reference.html
"""

#%%
"""
`ListedColormap`s store their color values in a .colors attribute.
The list of colors that comprise the colormap can be directly accessed using the colors property,
or it can be accessed indirectly by calling `viridis` with an array of values
matching the length of the colormap.
Note that the returned list is in the form of an RGBA Nx4 array,
where N is the length of the colormap.
"""
viridis.colors
mpl.cm.viridis(range(8))    # array of first 8 colors in original `viridis` colormap
viridis(range(8))           # array of first 8 colors in re-instantiated `viridis` colormap
viridis(7)
viridis(10)                 # if N > viridis.N  then it returns the last color on the list

# for floats
viridis(0.)                 # the first color on the list
viridis(1.)                 # the last
viridis(.56)
viridis(.33)                # the color which index on the list is closest to  x*(8-1)
viridis([.1, .33, .56, .99])   # array of colors

"""
The colormap is a lookup table, so "oversampling" the colormap returns nearest-neighbor
interpolation (note the repeated colors in the list below)
"""

#%%
#%% Creating listed colormaps
"""
Creating a colormap is essentially the inverse operation of the above
where we supply a list or array of color specifications to ListedColormap to make a new colormap.

Before continuing with the tutorial, let us define a helper function
that takes one or more colormaps as input,
creates some random data and applies the colormap(s) to an image plot of that dataset.
"""

def plot_examples(colormaps):
    """
    Helper function to plot data with associated colormap.
    """

    np.random.seed(19680801)
    data = np.random.randn(30, 30)

    n = len(colormaps)

    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            constrained_layout=True,
                            squeeze=False
                           )

    for [ax, cmap] in zip(axs.flat, colormaps):
        mappable = ax.pcolormesh(data, cmap=cmap,
            rasterized=True, vmin=-4, vmax=4)  #!!! .pcolormesh()
        fig.colorbar(mappable, ax=ax)

    plt.show()

    return fig, axs, mappable


#%%
"""
In the simplest case we might type in a list of color names to create a colormap from those.
"""
cmap = ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])
fig, axs, mappable = plot_examples([cmap])

#%%
help(axs.flat[-1].pcolormesh)    # returns  `matplotlib.collections.QuadMesh`
help(fig.colorbar)               # !!!
    # notice that first arg is expected to be `matplotlib.cm.ScalarMappable`
    # but is still works with other classes, e.g.
mappable                         # matplotlib.collections.QuadMesh  --

# so a bit confusing...

#%%

#%%
"""
In fact, that list may contain any valid matplotlib color specification.
Particularly useful for creating custom colormaps are Nx4 numpy arrays.
Because with the variety of numpy operations that we can do on a such an array,
carpentry of new colormaps from existing colormaps become quite straight forward.

For example, suppose we want to make the first 25 entries of a 256-length
"viridis" colormap pink for some reason:
"""
viridis = mpl.cm.get_cmap('viridis', 256)
viridis.colors
newcolors = viridis(np.linspace(0, 1, 256))
newcolors     # only array (not the whole object)

pink = np.array([248/256, 24/256, 148/256, 1])   # pink color
newcolors[:25, :] = pink
newcmp = ListedColormap(newcolors)
newcmp
    # `matplotlib.colors.ListedColormap`

plot_examples([viridis, newcmp])

#%%
"""
We can easily reduce the dynamic range of a colormap;
here we choose the middle 0.5 of the colormap.
However, we need to interpolate from a larger colormap,
otherwise the new colormap will have repeated values.
"""
viridis_big = mpl.cm.get_cmap('viridis', 512)
viridis_big.colors.shape      # 512,4   notice repeated values
    # original `viridis` colormap has only 256 colors

newcmp = ListedColormap(viridis_big(np.linspace(0.25, 0.75, 256)))
plot_examples([viridis, newcmp])

#%% and we can easily concatenate two colormaps:

top = mpl.cm.get_cmap('Oranges_r', 128)
bottom = mpl.cm.get_cmap('Blues', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))

newcmp = ListedColormap(newcolors, name='OrangeBlue')
plot_examples([viridis, newcmp])

#%%
"""
Of course we need not start from a named colormap,
we just need to create the Nx4 array to pass to ListedColormap.
Here we create a colormap that goes
from brown (RGB: 90, 40, 40)
  to white (RGB: 255, 255, 255).
"""
N = 256
vals = np.ones((N, 4))
vals[:, 0] = np.linspace(90/256, 1, N)
vals[:, 1] = np.linspace(40/256, 1, N)
vals[:, 2] = np.linspace(40/256, 1, N)

newcmp = ListedColormap(vals)

plot_examples([viridis, newcmp])

#%% some different colors
N = 256
vals = np.ones((N, 4))
vals[:, 0] = np.linspace(1, 0, N)   # red
vals[:, 1] = np.linspace(0, 1, N)   # green
vals[:, 2] = np.zeros(N)            # blue

newcmp = ListedColormap(vals)

plot_examples([viridis, newcmp])

#%%


#%%
#%% LinearSegmentedColormap
"""
`LinearSegmentedColormap`s do not have a `.colors` attribute.
However, one may still call the colormap with an integer array,
or with a float array between 0 and 1.
"""
mpl.cm.copper
    # matplotlib.colors.LinearSegmentedColormap
dir(mpl.cm.copper)

copper = mpl.cm.get_cmap('copper', 8)
copper
    # matplotlib.colors.LinearSegmentedColormap

dir(copper)     # no .colors  attr.

copper(range(8))            # still returns array of 8 colors
copper(np.linspace(0, 1, 8))

#%%
#%% Creating linear segmented colormaps
#!!! see the end of file for most convenient solution !!!
"""
`LinearSegmentedColormap` class specifies colormaps
using anchor points between which RGB(A) values are interpolated.

The format to specify these colormaps allows discontinuities at the anchor points.
Each anchor point is specified as a row in a matrix
of the form [x[i] yleft[i] yright[i]],
where x[i] is the anchor,
and yleft[i] and yright[i] are the values of the color on either side of the anchor point.

If there are no discontinuities, then yleft[i]=yright[i]:
"""
#%%
help(LinearSegmentedColormap)
"""
Colormap objects based on lookup tables using linear segments.

The lookup table is generated using linear interpolation for each
primary color, with the 0-1 domain divided into any number of
segments.

Method resolution order:
    LinearSegmentedColormap
    Colormap
    builtins.object

 __init__(self, name, segmentdata, N=256, gamma=1.0)
Create color map from linear mapping segments

segmentdata argument is a dictionary with a
    red, green and blue  entries.
Each entry should be a list of
    *x*, *y0*, *y1*
tuples, forming rows in a table.
Entries for alpha are optional.

Example: suppose you want red to increase from 0 to 1 over
the bottom half, green to do the same over the middle half,
and blue over the top half.  Then you would use::

    cdict = {'red':   [(0.0,  0.0, 0.0),
                       (0.5,  1.0, 1.0),
                       (1.0,  1.0, 1.0)],

             'green': [(0.0,  0.0, 0.0),
                       (0.25, 0.0, 0.0),
                       (0.75, 1.0, 1.0),
                       (1.0,  1.0, 1.0)],

             'blue':  [(0.0,  0.0, 0.0),
                       (0.5,  0.0, 0.0),
                       (1.0,  1.0, 1.0)]}

Each row in the table for a given color is a sequence of
    *x*, *y0*, *y1* tuples.
In each sequence, *x* must increase
monotonically from 0 to 1.  For any input value *z* falling
between *x[i]* and *x[i+1]*, the output value of a given color
will be linearly interpolated between *y1[i]* and *y0[i+1]*::

    row i:   x  y0  y1
                   /
                  /
    row i+1: x  y0  y1

Hence y0 in the first row and y1 in the last row are never used.
"""

#%%

cdict = {'red':   [[0.0,  0.0, 0.0],
                   [0.5,  1.0, 1.0],
                   [1.0,  1.0, 1.0]],
         'green': [[0.0,  0.0, 0.0],
                   [0.25, 0.0, 0.0],
                   [0.75, 1.0, 1.0],
                   [1.0,  1.0, 1.0]],
         'blue':  [[0.0,  0.0, 0.0],
                   [0.5,  0.0, 0.0],
                   [1.0,  1.0, 1.0]]}


def plot_linearmap(cdict):
    newcmp = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)
    rgba = newcmp(np.linspace(0, 1, 256))
    fig, ax = plt.subplots(figsize=(4, 3), constrained_layout=True)
    col = ['r', 'g', 'b']
    for xx in [0.25, 0.5, 0.75]:
        ax.axvline(xx, color='0.7', linestyle='--')
    for i in range(3):
        ax.plot(np.arange(256)/256, rgba[:, i], color=col[i])
    ax.set_xlabel('index')
    ax.set_ylabel('RGB')
    plt.show()

    return fig, ax, newcmp

plot_linearmap(cdict)

plot_examples([mpl.cm.viridis, LinearSegmentedColormap('qq', segmentdata=cdict, N=256)])

#%%
"""
In order to make a discontinuity at an anchor point,
the third column is different than the second.
The matrix for each of "red", "green", "blue", and optionally "alpha" is set up as:
cdict['red'] = [...
                [x[i]      yleft[i]     yright[i]],
                [x[i+1]    yleft[i+1]   yright[i+1]],
               ...]

and for values passed to the colormap between x[i] and x[i+1],
the interpolation is between yright[i] and yleft[i+1].

In the example below there is a discontinuity in red at 0.5.
The interpolation between 0 and 0.5 goes from 0.3 to 1,
and between 0.5 and 1 it goes from 0.9 to 1.
Note that red[0, 1], and red[2, 2] are both superfluous to the interpolation
because red[0, 1] is the value to the left of 0, and red[2, 2] is the value to the right of 1.0.
"""

cdict['red'] = [[0.0,  0.0, 0.3],
                [0.5,  1.0, 0.9],
                [1.0,  1.0, 1.0]]
plot_linearmap(cdict)

plot_examples([mpl.cm.viridis, LinearSegmentedColormap('qq', segmentdata=cdict, N=256)])

#%% Directly creating a segmented colormap from a list
"""
The above described is a very versatile approach,
but admittedly a bit cumbersome to implement.
For some basic cases, the use of
    `LinearSegmentedColormap.from_list()`  may be easier.
This creates a segmented colormap with equal spacings from a supplied list of colors.
"""
colors = ["darkorange", "gold", "lawngreen", "lightseagreen"]
cmap1 = LinearSegmentedColormap.from_list("mycmap", colors)   # colors evenly distributed

"""
If desired, the nodes of the colormap can be given as numbers between 0 and 1.
E.g. one could have the reddish part take more space in the colormap.
"""
nodes = [0.0, 0.4, 0.8, 1.0]    # 'centers' of colors between [0, 1]
                                # -- this is mapped to [vmin, vmax] by some `mappable` like `.pcolormesh()` (see above in `plot_examples()` definition)
                                #! data mapping points must start with x=0 and end with x=1
list(zip(nodes, colors))
cmap2 = LinearSegmentedColormap.from_list("mycmap", list(zip(nodes, colors)))

plot_examples([cmap1, cmap2])

#%%
#%%
