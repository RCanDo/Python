#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Using ggplot in Python: Visualizing Data With plotnine
subtitle:
version: 1.0
type: tutorial
keywords: [plotnine, ggplot]
description: |
remarks:
todo:
sources:
    - title: Using ggplot in Python: Visualizing Data With plotnine
      site:
      link: https://realpython.com/ggplot-python/
      date: 2020-10-12
      authors:
          - nick:
            fullname: Miguel Garcia
            email:
      usage: |

file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: ~/graphics/ggplot/
    date: 2021-03-21
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
from plotnine.data import economics, mpg, huron

huron.head()
economics.head()

#%%
...

#%%
ggplot(huron) + aes(x="level") + stat_bin(bins=10) + geom_bar()
    ## divides the level range into 10 equally sized bins

ggplot(huron) + aes(x="level") + geom_histogram(bins=10)  ## the same

ggplot(huron) + stat_bin(aes(x="level", y=after_stat('count'), bins=10)) + geom_bar()
## ???

#%%
(ggplot(huron)
 + aes(x="factor(decade)", y="level")
 + geom_boxplot()
)

#%%
(ggplot(economics)
 + aes(x="date", y="pop")
 + scale_x_timedelta(name="Years since 1970")
 + labs(title="Population Evolution", y="Population")     # !!!
 + geom_line()
)
#%%
(ggplot(economics)
 + aes(x="date", y="pop")
 + scale_x_datetime()#name="Years since 1970")
 + labs(title="Population Evolution", y="Population")     # !!!
 + geom_line()
)
#%%
"""!!! make factor from date !!!
"""
import datetime as dt
dir(economics.date)
economics.date.apply(lambda x: dt.datetime.strftime(x, "%Y"))
economics.date.apply(lambda x: x.year)

#%%
ggplot(mpg) + aes(x="class") + geom_bar()
ggplot(mpg) + aes(x="class", y=after_stat('prop')) + geom_bar()  # nonsense !

ggplot(mpg) + aes(x="class") \
 + geom_bar(aes(y=after_stat('count / np.sum(count)'))) \
 + labs(y='prop')

ggplot(mpg) + aes(x="class") + geom_histogram()  # ooops... nonsense !

ggplot(mpg) + aes(x="class") + geom_bar() + coord_flip()

#%% facet_grid()
p = (
    ggplot(mpg)
    + aes(x="displ", y="hwy")
    + labs(
        x="Engine Size",
        y="Miles per Gallon",
        title="Miles per Gallon for Each Year and Vehicle Class",
    )
    + geom_point()
    + facet_grid(facets="year ~ class")
)
p

#%% Themes
p + theme_dark()
p + theme_xkcd()


#%% the same data displayed different way

(
    ggplot(mpg)
    + aes(x="cyl", y="hwy", color="class")
    + labs(
        x="Engine Cylinders",
        y="Miles per Gallon",
        color="Vehicle Class",
        title="Miles per Gallon for Engine Cylinders and Vehicle Classes",
    )
    + geom_point()
)

#%% to file
myPlot = ggplot(economics) + aes(x="date", y="pop") + geom_line()
myPlot.save("myplot.png", dpi=600)

#%%


#%%


#%%


#%%


#%%


#%%
