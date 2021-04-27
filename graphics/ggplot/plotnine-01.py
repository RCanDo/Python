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

ROOT = "E:/"
#ROOT = "/home/arek"
PYWORKS = os.path.join(ROOT, "ROBOCZY/Python")
#PYWORKS = os.path.join(ROOT, "Works/Python")
##
DATA = os.path.join(ROOT, "Data/eco")           ## adjust !!!
WD = os.path.join(PYWORKS, "graphics/ggplot/")  ## adjust !!!

os.chdir(WD)
print(os.getcwd())

#%%
import numpy as np
import pandas as pd
import warnings

#%%
"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""
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
1. the dataset we’ll use:  ggplot(data=...)
2. lay the axes:           + aes(x=..., y=...)
3. and choose a geom:      + geom_*(...)
Hence, the data, aes and geom_* are the elementary elements of any graph:
"""
p0 = ggplot(data=surveys0) \
    + aes(x="weight", y="hindfoot_length")
#%%
p0 + geom_point()
p0 + geom_point(alpha=.1)
p0 + geom_point(alpha=.1, size=.5, color="red")

#%% color accordint to "species_id"
p0 + geom_point(alpha=.1, size=.5, color="species_id")   #! ERROR !

p2 = p0 + aes(color="species_id") + geom_point(alpha=.1, size=.5)
p2  # OK
p2 + theme(subplots_adjust={'right': 0.75})  # hmm..

p2.save("hindfoot_length_vs_weight.png", width=12, height=10, dpi=300)

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
p1 + aes(color="sex")      # ugly
p1 = p1 + aes(fill="sex")  # nice !
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
## but not always... or maybe sth changed within library

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
ggplot(surveys0) + aes(x="species_id") + geom_bar() + facet_grid("~plot_id")

#%%
## Plotting time series data
#%%
surveys0.head()
yearly_counts = surveys0.groupby(['year', 'species_id'])['species_id'].count()
yearly_counts
yearly_counts = yearly_counts.reset_index(name='counts')   #!!!
yearly_counts

#%%
p4 = ggplot(data=yearly_counts) + aes(x="year", y="counts") \
    + geom_line()
p4

#%%
p4 + aes(color="species_id")
p4 + aes(color="species_id") + scale_y_log10()

#%%
## Faceting
#%%
p5 = ggplot(data=surveys0) + \
    aes(x="weight", y="hindfoot_length") + \
    geom_point(alpha=.9)
#%%
p5 + aes(color="species_id")

p5 + facet_wrap("sex")

p5 + facet_wrap("sex") + aes(color="species_id")
p5 + facet_wrap("species_id") + aes(color="sex")

p5 + facet_grid("sex ~ species_id")  # no good

#%% try sth different
p6 = ggplot(data=surveys0[surveys0["year"].isin([2000, 2001])]) + \
    aes(x="weight", y="hindfoot_length") + \
    geom_point(alpha=.5)
p6 + aes(color="species_id") + facet_grid("year ~ sex")

#%%
yearly_weight = surveys0.groupby(['year', 'species_id'])
yearly_weight = yearly_weight['weight'].mean().reset_index()

p7 = ggplot(data=yearly_weight, mapping=aes(x='year', y='weight')) + \
    geom_line() + \
    facet_wrap("species_id")
p7

#%%
yearly_weight = surveys0.groupby(['year', 'species_id', 'sex'])
yearly_weight = yearly_weight['weight'].mean().reset_index()

p8 = ggplot(data=yearly_weight,
        mapping=aes(x='year',
                       y='weight',
                       color='species_id')) \
    + geom_line() \
    + facet_wrap("sex")
p8

#%%
p81 = ggplot(data=yearly_weight) \
     + aes(x="year", y="weight", color="sex") \
     + geom_line() \
     + facet_wrap("species_id")
p81

#%%
## Further customization
#%%
p9 = ggplot(data=surveys0,
           mapping=aes(x='factor(year)'))
p9 = p9 + geom_bar()
p9

#%%
my_custom_theme = theme(
    axis_text_x = element_text(color="grey", size=10, angle=50, hjust=.5),
    axis_text_y = element_text(color="grey", size=10))

p9 = p9 + my_custom_theme
p9

#%% saving the plot

p9.save("some_bars.png", width=10, height=10, dpi=300)


#%%


#%%


#%%


#%%


#%%