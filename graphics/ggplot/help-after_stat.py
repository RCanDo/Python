"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: plotnine.mapping.after_stat
subtitle:
version: 1.0
type: example
keywords: [plotnine, ggplot]
description: |
remarks:
todo:
sources:
    - title: plotnine.mapping.after_stat
      link: https://plotnine.readthedocs.io/en/stable/generated/plotnine.mapping.after_stat.html#plotnine.mapping.after_stat
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
    date: 2021-4-25
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

#%%
plotnine.mapping.after_stat(x: str)

#%%
df = pd.DataFrame({
    'var1': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
})

(ggplot(df, aes('var1'))
 + geom_bar()
)

#%%
(ggplot(df, aes('var1'))
 + geom_bar(aes(y=after_stat('prop'))) # default is after_stat('count')
)

#%%
(ggplot(df) + aes('var1', y=after_stat('prop'))
 + geom_bar() # default is after_stat('count')
)
# the same

#%%
ggplot(df, aes('var1')) \
 + geom_bar(aes(y=after_stat('count / np.sum(count)'))) \
 + labs(y='prop')


#%% ???
(ggplot(df, aes('var1'))
 + geom_bar(aes(fill='var1'))
)

#%%
"""
By default `geom_bar` uses `stat_count` to compute a frequency table with the x aesthetic
as the key column.
As a result, any mapping to a continuous variable (other than the x aesthetic) is lost;
e.g. if you have a classroom and you compute a frequency table of the gender,
you lose any other information like height of students.

For example, below fill='var1' has no effect,
but the `var1` variable has not been lost it has been turned into x aesthetic.
"""
(ggplot(df, aes('var1')) + geom_bar(aes(fill='var1')))

(ggplot(df, aes('var1')) + geom_bar())

#%%
"""We use `after_stat` to map `fill` to the x aesthetic after it has been computed.
"""

(ggplot(df, aes('var1'))
 + geom_bar(aes(fill=after_stat('x')))
 + labs(fill='var1')
)

(ggplot(df) + aes('var1', fill=after_stat('x')) + geom_bar()
 + labs(fill='var1')
)

#%%


