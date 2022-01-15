#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: lowess
subtitle: statsmodels
version: 1.0
type: example
keywords: [lowess, nonparametric, regression]
description: |
    Guide, examples, tutorial, etc...
remarks:
todo:
sources:
    - title: LOWESS Smoother
      link: https://www.statsmodels.org/stable/examples/notebooks/generated/lowess.html?highlight=lowess
      date:
      authors:
          - nick:
            fullname:
            email:
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-xxx.py
    path: ~/Roboczy/Python/StatsModels/
    date: 2022-01-02
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import rcando as ak
import os

PYWORKS = "D:/ROBOCZY/Python"
#PYWORKS = "~/Works/Python"

os.chdir(PYWORKS + "/StatsModels/")
print(os.getcwd())

#%%
import numpy as np
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices

#%%
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)

#%%
"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""

pd.options.display.width = 0  # autodetects the size of your terminal window

pd.set_option('display.max_rows', 500)
pd.options.display.max_rows = 500         # the same
pd.options.display.max_colwidth = 500         # the same

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

pd.set_option('display.max_rows', 500)   #!!!


# %% However, some style checkers like Flake may complain on #%% - there should be space after #

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

pd.set_option('display.precision', 2)


# %%
"""
This notebook introduces the LOWESS smoother in the nonparametric package.
LOWESS performs weighted local linear fits.

We generated some non-linear data and perform a LOWESS fit,
then compute a 95% confidence interval around the LOWESS fit by performing bootstrap resampling.
"""
#%%
import numpy as np
import pylab
import seaborn as sns
import statsmodels.api as sm

#%%
sns.set_style("darkgrid")
pylab.rc("figure", figsize=(16, 8))
pylab.rc("font", size=14)

#%%
# Seed for consistency
np.random.seed(1)

# Generate data looking like cosine
x = np.random.uniform(0, 4 * np.pi, size=200)
y = np.cos(x) + np.random.random(size=len(x))

#%%
# Compute a lowess smoothing of the data
smoothed = sm.nonparametric.lowess(exog=x, endog=y, frac=0.2)
type(smoothed)  # numpy.ndarray
smoothed.shape  # (200, 2)
smoothed

# Plot the fit line
fig, ax = pylab.subplots()

ax.scatter(x, y)
ax.plot(smoothed[:, 0], smoothed[:, 1], c="k")
pylab.autoscale(enable=True, axis="x", tight=True)

#%%
# Compute a lowess smoothing of the data
smoothed = sm.nonparametric.lowess(exog=x, endog=y, xvals=np.linspace(0, 4 * np.pi, 20),  frac=0.2)
type(smoothed)  # numpy.ndarray
smoothed.shape  # (20, )
np.array([np.linspace(0, 4 * np.pi, 20), smoothed])

# Plot the fit line
fig, ax = pylab.subplots()

ax.scatter(x, y)
ax.plot(smoothed[:, 0], smoothed[:, 1], c="k")
pylab.autoscale(enable=True, axis="x", tight=True)

#%%
"""
Confidence interval

Now that we have performed a fit, we may want to know how precise it is.
Bootstrap resampling gives one way of estimating confidence intervals around a LOWESS fit
by recomputing the LOWESS fit for a large number of random resamplings from our data.
"""
# Now create a bootstrap confidence interval around the a LOWESS fit

def lowess_with_confidence_bounds(
        x, y, eval_x, N=200, conf_interval=0.95, lowess_kw=None
        ):
    """
    Perform Lowess regression and determine a confidence interval by bootstrap resampling
    """
    # Lowess smoothing
    smoothed = sm.nonparametric.lowess(exog=x, endog=y, xvals=eval_x, **lowess_kw)

    # Perform bootstrap resamplings of the data
    # and  evaluate the smoothing at a fixed set of points
    smoothed_values = np.empty((N, len(eval_x)))
    for i in range(N):
        sample = np.random.choice(len(x), len(x), replace=True)
        sampled_x = x[sample]
        sampled_y = y[sample]

        smoothed_values[i] = sm.nonparametric.lowess(
            exog=sampled_x, endog=sampled_y, xvals=eval_x, **lowess_kw
        )

    # Get the confidence interval
    sorted_values = np.sort(smoothed_values, axis=0)
    bound = int(N * (1 - conf_interval) / 2)
    bottom = sorted_values[bound - 1]
    top = sorted_values[-bound]

    return smoothed, bottom, top


# Compute the 95% confidence interval
eval_x = np.linspace(0, 4 * np.pi, 31)
smoothed, bottom, top = lowess_with_confidence_bounds(
    x, y, eval_x, lowess_kw={"frac": 0.1}
)

# Plot the confidence interval and fit
fig, ax = pylab.subplots()
ax.scatter(x, y)
ax.plot(eval_x, smoothed, c="k")
ax.fill_between(eval_x, bottom, top, alpha=0.5, color="b")
pylab.autoscale(enable=True, axis="x", tight=True)




#%%



#%%
