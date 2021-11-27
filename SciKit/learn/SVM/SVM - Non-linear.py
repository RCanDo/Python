#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Non-linear SVM
version: 1.0
type: example
keywords: [support vector machine, non-linear, scikit]
description: |
    Perform binary classification using non-linear SVC with RBF kernel.
    The target to predict is a XOR of the inputs.
    The color map illustrates the decision function learned by the SVC.
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Non-linear SVM
      link: https://scikit-learn.org/stable/auto_examples/svm/plot_svm_nonlinear.html
    - title: Support Vector Machines Examples
      link: https://scikit-learn.org/stable/auto_examples/#support-vector-machines
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: SVM - Non-linear.py
    path: E:/ROBOCZY/Python/SciKit/learn/SVM/
    date: 2021-10-24
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

#%%
ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/SciKit/learn/SVM//")   #!!! adjust
os.chdir(WD)

#%%
WD = os.getcwd()
print(WD)

#%%
import numpy as np
import pandas as pd

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

# other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500
# the same

pd.options.display.width = 120

#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('dark_background')
# see `plt.style.available` for list of available styles

#%%
#%%
#%%
from sklearn import svm
xx, yy = np.meshgrid(np.linspace(-3, 3, 500),
                     np.linspace(-3, 3, 500))
xx  # the same 'row' repeated == one value in each 'columns'
yy  # one value in each 'row'

#%%
np.random.seed(0)
X = np.random.randn(300, 2)
X
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
Y

#%% fit the model
# define a classifier (clf)
clf = svm.NuSVC(gamma='auto')
vars(clf)
clf.fit(X, Y)

sum(clf.predict(X) == Y)
sum(clf.predict(X) != Y)

#%% plot the decision function for each datapoint
help(np.c_)
points = np.c_[xx.ravel(), yy.ravel()]   # list all points (x-y pairs) ~= (m x 2) matrix

# 'prediction' on each point
Z = clf.decision_function(points)           #!!!
Z                                           #!!! floats
plt.hist(Z, bins=100)
Z.shape    # m= 250k  a lot

# final prediction: True/False
zz = clf.predict(points)
zz
np.unique(zz, return_counts=True)    # (array([False,  True]), array([118388, 131612], dtype=int64))

#%% create an "image"
# i.e. array of the shape of initial meshgrid of values for each point
Z = Z.reshape(xx.shape)
Z.shape   # (500, 500)

#%% plotly
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
           origin='lower', cmap=plt.cm.PuOr_r)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2,
                       linestyles='dashed')
plt.scatter(X[:, 0], X[:, 1], s=30, c=Y,
            cmap=plt.cm.Paired,     # one of "Qualitative" colormaps
            edgecolors='k')
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()

#%% for colormaps types see:
#  https://matplotlib.org/stable/tutorials/colors/colormaps.html
# Qualitative:
#  Pastel1, Pastel2, Paired, Accent, Dark2, Set1, Set2, Set3, tab10, tab20, tab20b, tab20c

#%% OO
fig, ax = plt.subplots()
img = ax.imshow(Z, interpolation="nearest", origin="lower",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),   # makes proper axes range/ticks -- proper image scale!!!
    aspect="auto", cmap=mpl.cm.PuOr_r
    )
    #! without `extent` properly set the scale is in pixels!  x, y in (0, 500) while we should heve the same as xx, yy
contours = ax.contour(xx, yy, Z, levels=[0], linewidths=2, linestyles="dashed")
ax.scatter(X[:, 0], X[:, 1], s=30, c=Y,
    cmap=plt.cm.Set1,
    edgecolors='k')
ax.set_xticks((xx.min(), 0, xx.max()))
ax.set_yticks((yy.min(), 0, yy.max()))
ax.axis([-3, 3, -3, 3])

fig.colorbar(img)

ax.axhline(0, c='gray')
ax.axvline(0, c='gray')

#%%
help(ax.imshow)
