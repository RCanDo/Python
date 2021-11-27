#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Lifecycle of a Plot
subtitle:
version: 1.0
type: tutorial
keywords: [axes, object-oriented API]
description: |
remarks:
    -
todo:
    - problem 1
sources:
    - title: The Lifecycle of a Plot
      link: https://matplotlib.org/stable/tutorials/colors/colormapnorms.html
    - title:
      link:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: tut-02-plot_lifecycle.py
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
# plt.style.use('dark_background')
# see `plt.style.available` for list of available styles

#%%
#%% The Lifecycle of a Plot
"""
This tutorial aims to show the beginning, middle, and end of a single visualization using Matplotlib.
We'll begin with some raw data and end by saving a figure of a customized visualization.
Along the way we try to highlight some neat features and best-practices using Matplotlib.

    Note
    This tutorial is based on this excellent blog post by Chris Moffitt.
    It was transformed into this tutorial by Chris Holdgraf.

A note on the Object-Oriented API vs. Pyplot

Matplotlib has two interfaces.
The first is an object-oriented (OO) interface.
In this case, we utilize an instance of axes.Axes in order
to render visualizations on an instance of figure.Figure.

The second is based on MATLAB and uses a state-based interface.
This is encapsulated in the pyplot module.
See the pyplot tutorials for a more in-depth look at the pyplot interface.

Most of the terms are straightforward but the main thing to remember is that:

    1. The Figure is the final image that may contain 1 or more Axes.

    2. The Axes represent an individual plot
       (don't confuse this with the word "axis", which refers to the x/y axis of a plot).

We call methods that do the plotting directly from the Axes,
which gives us much more flexibility and power in customizing our plot.

    Note
    In general, try to use the object-oriented interface over the pyplot interface.

"""
#%%
#%% DATA: sales information for a number of companies.

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)

#%% Getting started
"""
This data is naturally visualized as a barplot, with one bar per group.
To do this with the object-oriented approach,
we first generate an instance of figure.Figure and axes.Axes.
The Figure is like a canvas,
and the Axes is a part of that canvas on which we will make a particular visualization.

Note
Figures can have multiple axes on them.
For information on how to do this, see the Tight Layout tutorial.
"""
fig, ax = plt.subplots()

# Now that we have an Axes instance, we can plot on top of it.
ax.barh(group_names, group_data)

#%% Controlling the style
# To see a list of styles, we can use style.
print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

#%% You can activate a style:

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.barh(group_names, group_data)

#%% let's rotate the labels on the x-axis so that they show up more clearly.
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

#%%