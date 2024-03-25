#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Model selection: choosing estimators and their parameters
version: 1.0
keywords: [model selection, estimators, parameters, ...]
description: |
content:
remarks:
todo:
sources:
    - title: Model selection: choosing estimators and their parameters
      link: https://scikit-learn.org/stable/tutorial/statistical_inference/model_selection.html
file:
    usage:
        interactive: True
        terminal: False
    date: 2023-11-09
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@quantup.pl
"""
# %%
import numpy as np
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)

# %%  Score, and cross-validated scores
"""
As we have seen, every estimator exposes a score method that can judge the quality of the fit (or the prediction)
on new data.
Bigger is better.
"""
from sklearn import datasets, svm

X_digits, y_digits = datasets.load_digits(return_X_y=True)

svc = svm.SVC(C=1, kernel='linear')
svc.fit(X_digits[:-100], y_digits[:-100])
svc.score(X_digits[-100:], y_digits[-100:])     # 0.98

# %%
"""
To get a better measure of prediction accuracy (which we can use as a proxy for goodness of fit of the model),
we can successively split the data in folds that we use for training and testing:
"""
X_folds = np.array_split(X_digits, 3)                               # !
y_folds = np.array_split(y_digits, 3)

scores = list()

for k in range(3):
    # We use 'list' to copy, in order to 'pop' later on             # !
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)                               # !
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)

# !  This is called a KFold cross-validation.


# %% Cross-validation generators
"""
Scikit-learn has a collection of classes which can be used to generate lists of train/test indices
for popular cross-validation strategies.

They expose a `.split()` method which accepts the input dataset to be split
and yields the  train/test set indices (!)  for each iteration of the chosen cross-validation strategy.
"""
from sklearn.model_selection import KFold

X = ["a", "a", "a", "b", "b", "c", "c", "c", "c", "c"]

k_fold = KFold(n_splits=5)
type(k_fold)                # sklearn.model_selection._split.KFold  !!! ~= factory of genrators !!!

k_fold.split(X)             # <generator object _BaseKFold.split at 0x7fa27af89460>

for train_indices, test_indices in k_fold.split(X):
     print('Train: %s | test: %s' % (train_indices, test_indices))

# %% !!! BTW: How generators work

kfs = k_fold.split(X)
next(kfs)   # (array([2, 3, 4, 5, 6, 7, 8, 9]), array([0, 1]))
next(kfs)   # (array([0, 1, 4, 5, 6, 7, 8, 9]), array([2, 3]))

[{"train": test, "test": train} for train, test in kfs]
# [{'train': array([4, 5]), 'test': array([0, 1, 2, 3, 6, 7, 8, 9])},
#  {'train': array([6, 7]), 'test': array([0, 1, 2, 3, 4, 5, 8, 9])},
#  {'train': array([8, 9]), 'test': array([0, 1, 2, 3, 4, 5, 6, 7])}]
next(kfs)   # ! StopIteration   -- generator (which is always iterator) is used up
# one must recreate it to restart generating
kfs = k_fold.split(X)
[{"train": test, "test": train} for train, test in kfs]     # full set of splits
next(kfs)   # ! StopIteration ...

# BUT
[{"train": test, "test": train} for train, test in k_fold.split(X)]
# will always return nonempty list (always the same!) as it is called anew inside a list

# see more in 'User Guide/3.1-cross_validation.py'

# %%  The cross-validation can then be performed easily:
[svc.fit(X_digits[train], y_digits[train]).score(X_digits[test], y_digits[test])
 for train, test in k_fold.split(X_digits)]
# [0.9638888888888889, 0.9222222222222223, 0.9637883008356546, 0.9637883008356546, 0.9303621169916435]

# %%
"""
The cross-validation score can be directly calculated using the cross_val_score helper.
Given
- an estimator,
- the cross-validation object and
- the input dataset,
the `cross_val_score()` splits the data repeatedly into a training and a testing set,
trains the estimator using the training set
and computes the scores based on the testing set
for each iteration of cross-validation.

!   By default  the estimator’s score method  is used to compute the individual scores.

Refer the  `.metrics`  module to learn more on the available scoring methods.
"""
from sklearn.model_selection import cross_val_score
cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)
# array([0.96388889, 0.92222222, 0.9637883 , 0.9637883 , 0.93036212])

# %%
"""
`n_jobs=-1` means that the computation will be dispatched on all the CPUs of the computer.

Alternatively, the  `scoring`  argument can be provided to specify an  alternative scoring method.
"""
cross_val_score(svc, X_digits, y_digits, cv=k_fold,
                scoring='precision_macro')
# array([0.96578289, 0.92708922, 0.96681476, 0.96362897, 0.93192644])

# %%  Cross-validation generators
"""
KFold (n_splits, shuffle, random_state)
    Splits it into K folds, trains on K-1 and then tests on the left-out.
StratifiedKFold (n_splits, shuffle, random_state)
    Same as K-Fold but preserves the class distribution within each fold.
GroupKFold (n_splits)
    Ensures that the same group is not in both testing and training sets.


ShuffleSplit (n_splits, test_size, train_size, random_state)
    Generates train/test indices based on random permutation.
StratifiedShuffleSplit
    Same as shuffle split but preserves the class distribution within each iteration.
GroupShuffleSplit
    Ensures that the same group is not in both testing and training sets.

LeaveOneGroupOut ()
    Takes a group array to group observations.
LeavePGroupsOut  (n_groups)
    Leave P groups out.
LeaveOneOut ()
    Leave one observation out.

LeavePOut (p)
    Leave P observations out.
PredefinedSplit
    Generates train/test indices based on predefined splits.
"""
# %% Exercise
"""
On the digits dataset, plot the cross-validation score of a SVC estimator with a linear kernel
as a function of parameter C (use a logarithmic grid of points, from 1 to 10).
"""
from sklearn import datasets, svm
from sklearn.model_selection import cross_val_score

X, y = datasets.load_digits(return_X_y=True)

svc = svm.SVC(kernel="linear")
C_s = np.logspace(-10, 0, 10)

scores = list()
for C in C_s:
    svc.set_params(C=C)
    cv_scores = cross_val_score(svc, X, y, cv=k_fold)
    scores.append([cv_scores.min(), cv_scores.mean(), cv_scores.max()])

scores

import matplotlib.pyplot as plt
for k in range(3):
    plt.plot(C_s, [s[k] for s in scores])
plt.xscale('log')

# %% Grid-search and cross-validated estimators

# %% Grid-search
"""
scikit-learn provides an object that, given data,
computes the score during the fit of an estimator
on a parameter grid
and chooses the parameters to maximize the cross-validation score.

This object takes an estimator during the construction and exposes an estimator API:
"""
from sklearn.model_selection import GridSearchCV, cross_val_score

svc     # estimator
Cs = np.logspace(-6, -1, 10)    # parameter grid

clf = GridSearchCV(estimator=svc, param_grid=dict(C=Cs), # , cv=None  default means 5-fold CV
                   n_jobs=-1,
                   refit=True,      # refits the model on the whole data with the best params  `clf.best_params_`
                   )
clf.fit(X_digits[:1000], y_digits[:1000])

dir(clf)

clf.best_score_             # 0.95
clf.best_params_            # {'C': 0.0021544346900318843}
clf.best_estimator_         # SVC(C=0.0021544346900318843, kernel='linear')
clf.best_estimator_.C       # 0.002154...

# !!! Prediction performance on test set is not as good as on train set
clf.score(X_digits[1000:], y_digits[1000:])     # 0.9460...


# %% !!! Nested cross-validation

cross_val_score(clf, X_digits, y_digits)
# array([0.938..., 0.963..., 0.944...])

"""
Two cross-validation loops are performed in parallel:   ?!?! what exactly it means ???
- one by the GridSearchCV estimator to set gamma
- and the other one by cross_val_score to measure the prediction performance of the estimator.
The resulting scores are unbiased estimates of the prediction score on new data.

Warning
You cannot nest objects with parallel computing (n_jobs different than 1).
"""

# %% Cross-validated estimators
"""
Cross-validation to set a parameter can be done more efficiently on an algorithm-by-algorithm basis
i.e. CV adopted to specific algorithm features.

This is why, for certain estimators, scikit-learn exposes Cross-validation:
evaluating estimator performance estimators that set their parameter automatically by cross-validation:
"""
from sklearn import linear_model, datasets

lasso = linear_model.LassoCV()
X_diabetes, y_diabetes = datasets.load_diabetes(return_X_y=True)
lasso.fit(X_diabetes, y_diabetes)
# The estimator chose automatically its lambda:
lasso.alpha_

# %% Exercise
"""
On the diabetes dataset, find the optimal regularization parameter alpha.

Bonus: How much can you trust the selection of alpha?
"""
import numpy as np

from sklearn import datasets
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]

...
# %%
