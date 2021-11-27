#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Image tutorial
subtitle:
version: 1.0
type: tutorial
keywords: [image, ]
description: |
remarks:
    - This tutorial will use Matplotlib's imperative-style plotting interface, pyplot.
    - This interface maintains global state, and is very useful for quickly and easily experimenting with various plot settings.
    - The alternative is the object-oriented interface ...
todo:
    - THE SAME USING OO style (not immediate! and not clear how!)
sources:
    - title: Image tutorial
      link: https://matplotlib.org/stable/tutorials/introductory/images.html
    - title:
      link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: tut-03-images.py
    path: E:/ROBOCZY/Python/graphics/matplotlib/
    date: 2021-10-16
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
plt.style.use('dark_background')
# see `plt.style.available` for list of available styles
import matplotlib.image as mpimg

#%%
dir(mpimg)
#  https://matplotlib.org/stable/api/image_api.html   !!!

#%%
img = mpimg.imread('stinkbug.png')
type(img)    # numpy.ndarray
img.shape    # (375, 500, 3)  3 colors
print(img)   # gray

#%%
imgplot = plt.imshow(img)

imgplot      # <matplotlib.image.AxesImage at 0x17b225748e0>
dir(imgplot)
vars(imgplot)
imgplot.cmap
imgplot.cmap.name
vars(imgplot.cmap)

# methods, e.g.
imgplot.format_cursor_data(img)    # don't use
imgplot.get_cursor_data(`event`)  # for interactive use
imgplot.get_extent()    # (-0.5, 499.5, 374.5, -0.5) -- image extent as tuple (left, right, bottom, top).
imgplot.get_window_extent()   # Bbox([[81.6, 52.79], [574.4, 422.39]])  -- Get the axes bounding box in display space...

imgplot.make_image(renderer, magnification=1.0, unsampled=False)  # `renderer` ???

imgplot.set_extent(extent) # Set the image extent.
 # `extent4` - The position and size of the image as tuple (left, right, bottom, top) in data coordinates.
 # This updates ax.dataLim, and, if autoscaling, sets ax.viewLim to tightly fit the image, regardless of dataLim.
 # Autoscaling state is not changed, so following this with ax.autoscale_view() will redo the autoscaling in accord with dataLim.

#!!! there are many more methods which are not listed on the API page... !!!


#%%
lum_img = img[:, :, 0]
plt.imshow(lum_img)      # why green ???

"""
Now, with a luminosity (2D, no color) image,
the default __colormap__ (aka __lookup table, LUT__), is applied.
The default is called `viridis`.
There are plenty of others to choose from.
"""
dir(mpl.cm)     # colormaps

# see .../colors/tut-02-colormaps.py

#%%
plt.imshow(lum_img, cmap="hot")

#%%
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
imgplot.set_cmap('viridis')

#%%
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0))
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='y', ec='r')

#%%
"""
Most often, the "interesting" part of the image is around the peak,
and you can get extra contrast by clipping the regions above and/or below the peak.
In our histogram, it looks like there's not much useful information in the high end
(not many white things in the image).
Let's adjust the upper limit, so that we effectively "zoom in on" part of the histogram.
We do this by passing the `clim` argument to imshow().
You could also do this by calling the set_clim() method of the image plot object,
"""
imgplot = plt.imshow(lum_img)
imgplot = plt.imshow(lum_img, clim=(0.0, 0.7))

#%% You can also specify the `clim` using the returned object

fig = plt.figure(figsize=(12, 4))

ax = fig.add_subplot(1, 3, 1)
ax.set_title('Before')
imgplot = ax.imshow(lum_img)
plt.colorbar(lum_img, ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

ax = fig.add_subplot(1, 3, 2)
ax.set_title('After')
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
plt.colorbar(ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

ax = fig.add_subplot(1, 3, 3)
ax.set_title('After 2')
imgplot = plt.imshow(lum_img)
imgplot.set_clim(0.4, 0.7)
plt.colorbar(ticks=[0.4, 0.5, 0.6, 0.7], orientation='horizontal')


#%% the same with OO style -- bit more complicaed

fig = plt.figure(figsize=(12, 4))

ax = fig.add_subplot(1, 3, 1)
ax.set_title('Before')
imgplot = ax.imshow(lum_img)
#fig.colorbar(imgplot, ax=ax, ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')
             #! `mappable` must be passed for OO style
             # but `ax` is by default the current `ax` so it may be ommited
fig.colorbar(imgplot, ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

# i.e.  `imgplot` is used as `mappable`; see tut on `colorbars`

ax = fig.add_subplot(1, 3, 2)
ax.set_title('After')
imgplot = ax.imshow(lum_img)
imgplot.set_clim(0.0, 0.7)
fig.colorbar(imgplot, ticks=[0.1, 0.3, 0.5, 0.7], orientation='horizontal')

ax = fig.add_subplot(1, 3, 3)
ax.set_title('After 2')
imgplot = ax.imshow(lum_img)
imgplot.set_clim(0.4, 0.7)
fig.colorbar(imgplot, ticks=[0.4, 0.5, 0.6, 0.7], orientation='horizontal')

#%% other colormap
colors = ["r", 'k', "y"]
nodes  = [0, .5, 1]
cmap = mpl.colors.LinearSegmentedColormap.from_list("mycmap", list(zip(nodes, colors)))
#cmap = mpl.colors.ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])  # looks bad

fig, ax = plt.subplots(tight_layout=True)
imgplot = ax.imshow(lum_img, cmap=cmap)
fig.colorbar(imgplot, ticks=[0, .2, .5, .8, 1], orientation='horizontal')

#%% Array Interpolation schemes
"""
Interpolation calculates what the color or value of a pixel "should" be,
according to different mathematical schemes.
One common place that this happens is when you resize an image.
The number of pixels change, but you want the same information.
Since pixels are discrete, there's missing space.
Interpolation is how you fill that space.
This is why your images sometimes come out looking pixelated when you blow them up.
The effect is more pronounced when the difference between the original image
and the expanded image is greater.

Let's take our image and shrink it.
We're effectively discarding pixels, only keeping a select few.
Now when we plot it, that data gets blown up to the size on your screen.
The old pixels aren't there anymore, and the computer has to draw in pixels to fill that space.

We'll use the Pillow library that we used to load the image also to resize the image.
"""
from PIL import Image    #!!! Python Imaging Library

img = Image.open('stinkbug.png')
type(img)   # PIL.PngImagePlugin.PngImageFile
dir(img)

img.thumbnail((64, 64), Image.ANTIALIAS)  # resizes image in-place
imgplot = plt.imshow(img)

#%%
"""
Here we have the default interpolation, bilinear,
since we did not give imshow() any interpolation argument.
Let's try some others. Here's "nearest", which does no interpolation.
"""

imgplot = plt.imshow(img, interpolation="nearest")

# or "bicubic"
imgplot = plt.imshow(img, interpolation="bicubic")
# Bicubic interpolation is often used when blowing up photos
# - people tend to prefer blurry over pixelated.

#%% THE END
#%%