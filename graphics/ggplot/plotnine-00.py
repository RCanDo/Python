#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Introduction to Plotnine
subtitle:
version: 1.0
type: tutorial
keywords: [plotnine, ggplot]
description: |
remarks:
todo:
sources:
    - title: Introduction to Plotnine (ggplot port in Python)
      link: http://www.mbel.io/2019/08/06/introduction-to-plotnine-ggplot-port-in-python/
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
    date: 2021-03-12
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando as ak
import os

PYWORKS = "E:/ROBOCZY/Python"
#PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/graphics/ggplot/")
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
from plotnine.data import economics, mtcars, mpg
warnings.filterwarnings("ignore")

theme_set(theme_gray()) # default theme
#%matplotlib inline

#%%
mpg.head()

#%%
ggplot(mpg, aes(x='displ', y='hwy')) + geom_point()
ggplot(mpg) + aes(x='displ', y='hwy') + geom_point()

ggplot(mpg) + aes(x='displ', y='hwy', color='cyl') + geom_point()

#%% make 'cyl' categorical
mpg2 = mpg.copy()
mpg2.dtypes

mpg2['cyl'] = mpg2['cyl'].astype('category')
ggplot(mpg2) + aes(x='displ', y='hwy', color='cyl') + geom_point()

#%%
p = ggplot(mpg2)
p += aes(x='displ', y='hwy', color='cyl')  ## better not use += as it's not possible in R
p = p + geom_point()
p

#%%
p = ggplot(mpg2)
p = p + aes(x='cyl', y='displ')
p + geom_point()
p + geom_boxplot()

#%%
mpg2['year'] = mpg['year'].astype('category')
ggplot(mpg2) + aes(x='cyl', y='displ', fill='year') + geom_boxplot()
ggplot(mpg2) + aes(x='cyl', y='displ', color='year') + geom_boxplot()
ggplot(mpg2) + aes(x='cyl', y='displ', fill='year') + geom_point()
ggplot(mpg2) + aes(x='cyl', y='displ', color='year') + geom_point()

#%%
ggplot(mpg2) + aes(x='displ', fill='year') + geom_density()
ggplot(mpg2) + aes(x='displ', fill='year') + geom_density(alpha=.5)

ggplot(mpg2) + aes(x='displ', color='year') + geom_density()
#%%
#%%
economics.head()

ggplot(economics) + aes(x='date', y='pop') + geom_line()

#%%
economics['year'] = pd.DatetimeIndex(economics.date).year.astype('category')

economics['unemployment_rate'] = \
    (economics['unemploy'] / economics['pop']) * 100

ggplot(economics, aes(x='year', y='unemployment_rate')) + \
   geom_boxplot() + \
   theme(axis_text_x = element_text(angle=90, hjust=1))

#%%
# 3. Facets
#%%
mpg.head()
ggplot(mpg) + \
   geom_histogram(aes(x='hwy'), bins=15) + \
   facet_wrap("~ class")

#%%
# Making scales of each plot independent
ggplot(mpg) + \
   geom_histogram(aes(x='hwy'), bins=15) + \
   facet_wrap("~ class",  scales='free_y')      #!!!

#%%
ggplot(mpg, aes(x='displ', y='hwy')) + \
   geom_point() + \
   facet_wrap("~ class")


#%%
"""
facet_grid() is used for plotting 2 categorical variables
whereas facet_wrap() is mostly used for plotting 1 categorical variable,
even though it’s possible to plot 2.

From a stats perspective it’s possible to think of this plot
as how the interaction of `cyl` and `year` affects `displ`
"""

ggplot(mpg, aes(x='displ')) + geom_histogram() + facet_grid('cyl ~ year')

#%%
ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + \
    geom_point()

ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + \
    geom_point() + geom_smooth(method="rlm")

ggplot(mtcars, aes('wt', 'mpg', color='factor(gear)')) + \
    geom_point() + geom_smooth(method="rlm") + facet_wrap('~ gear')

#%%


#%%


#%%
