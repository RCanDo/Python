# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 08:26:10 2021

@author: staar
"""
#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Making Plots With plotnine
subtitle:
version: 1.0
type: tutorial
keywords: [plotnine, ggplot]
description: |
remarks:
todo:
sources:
    - title: Making Plots With plotnine
      site: Data Analysis and Visualization in Python for Ecologists
      link: https://datacarpentry.org/python-ecology-lesson/07-visualization-ggplot-python/index.html
      date: 2019-08-06
      authors:
          - nick:
            fullname:
            email:
      usage: |

file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: ~/graphics/ggplot/
    date: 2021-03-15
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando.ak as ak
import os

#ROOT = "E:/"
ROOT = "/home/arek"
#PYWORKS = os.path.join(ROOT, "ROBOCZY/Python")
PYWORKS = os.path.join(ROOT, "Works/Python")
##
DATA = os.path.join(ROOT, "Data/eco")           ## adjust !!!
WD = os.path.join(PYWORKS, "graphics/ggplot/")  ## adjust !!!

os.chdir(WD)
print(os.getcwd())

#%% Block delimiters allows to run separated blocks of code by one key-stroke
# e.g. Shift+Enter in Spyder

"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""
import numpy as np
import pandas as pd
import warnings

#%%
#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

#%% other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500         # the same

#%%
from plotnine import *     ## not pythonic but using alias e.g. `pn.` all the time is really cumbersome !!!

#from plotnine.data import economics, mtcars, mpg
warnings.filterwarnings("ignore")

theme_set(theme_gray()) # default theme
#%matplotlib inline

#%%

surveys0 = pd.read_csv(os.path.join(DATA, 'surveys.csv'))
surveys0.head()
surveys0.shape   # (35549, 9)
surveys0.count()

surveys0 = surveys0.dropna()
surveys0.shape   # (30676, 9)
surveys0.count()

#%%
p0 = ggplot(data=surveys0)
p0
# empty figure

#%%
"""Define aesthetics (`aes`),
by selecting variables used in the plot and mapping
them to a presentation such as plotting `size`, `shape`, `color`, etc.
You can interpret this as:
    which of the variables will influence the plotted objects/geometries
"""
p0 = ggplot(data=surveys0,
    mapping=aes(x="weight", y="hindfoot_length"))
p0
"""
The most important aes() _mappings_ are:
    `x`, `y`, `alpha`, `color`, `colour`, `fill`,
    `linetype`, `shape`, `size` and `stroke`
"""

#%%
"""Still no specific data is plotted, as we have to define
 what kind of geometry will be used for the plot.
The most straightforward is probably using  `points`.
Points is one of the  `geoms`  options,
the graphical representation of the data in the plot.
Others are `lines`, `bars`,…
To add a `geom` to the plot use + operator:
"""
p0 = p0 + geom_point()
p0

#%%
surveys0.plot_id.value_counts()
p1 = ggplot(data=surveys0, mapping=aes(x="plot_id"))
p1 = p1 + geom_bar()
p1

#%%
"""
- Anything you put in the ggplot() function can be seen by any geom layers
  that you add (i.e., these are universal plot settings).
  This includes the x and y axis you set up in aes().
- You can also specify aesthetics for a given geom independently
  of the aesthetics defined globally in the ggplot() function.
"""

#%%
# Building your plots iteratively
#%%
"""
Building plots with plotnine is typically an iterative process.
We start by defining
1. the dataset we’ll use,  `data=`
2. lay the axes,  aes(...)
3. and choose a geom.  geom_*(...)
Hence, the data, aes and geom_* are the elementary elements of any graph:
"""
p0 = ggplot(data=surveys0,
    mapping=aes(x="weight", y="hindfoot_length"))
#%%
p0 + geom_point()
p0 + geom_point(alpha=.1)
p0 + geom_point(alpha=.1, size=.5, color="red")

#%% color accordint to "species_id"
p0 + geom_point(alpha=.1, size=.5, color="species_id")   #! ERROR !

p2 = p0 + aes(color="species_id") + geom_point(alpha=.1, size=.5)
p2  # OK

#%%
p2 = p2 + xlab("Weight (g)")
p2

p2 = p2 + scale_x_log10()
p2

p2 = p2 + theme_bw()
p2

p2 = p2 + theme(text=element_text(size=16))
p2

#%%
p1 = p1 + aes(color="sex")
p1
p1 = p1 + scale_color_manual(["blue", "green"])
p1

#%%
#%%
p3 = ggplot(data=surveys0, mapping=aes(x='species_id', y='weight'))
p3 + geom_boxplot()

#%%
p3 + geom_boxplot(alpha=0.) + geom_jitter(alpha=.2)  ## not so good
p3 + geom_jitter(alpha=.2) + geom_boxplot(alpha=0.)  ## better! order matters !!!

#%%
p3 + geom_violin()
p3 + geom_violin() + scale_y_log10()

#%%
p3 + aes(color="factor(plot_id)") + geom_boxplot()
## ooops!  not sensible... separate boxplot series for each 'plot_id'

#%%
p3 + aes(color="factor(plot_id)") + \
     geom_jitter(alpha=0.3) + \
     geom_violin(alpha=0.5, color="0.9") + \
     scale_y_log10()

#%%
p3 + aes(color="factor(plot_id)") + \
     geom_jitter(alpha=0.3) + \
     geom_violin(alpha=0.5, color="0.2") + \
     scale_y_log10()

#%%
p3 + aes(color="factor(plot_id)") + \
     geom_jitter(alpha=0.3) + \
     geom_violin(alpha=0, color="0.2") + \
     scale_y_log10()

#%%
## Plotting time series data
#%%


#%%


#%%


#%%


#%%