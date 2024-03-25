#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---

title: skopt - BayesSearchCV
version: 1.0
keywords: [skopt, optimisation, cross validation, bayes optimisation, ...]
description: |
content:
remarks:
todo:
sources:
    - title: Scikit-learn hyperparameter search wrapper
      link: https://scikit-optimize.github.io/stable/auto_examples/sklearn-gridsearchcv-replacement.html
file:
    usage:
        interactive: True
        terminal: False
    date: 2023-11-15
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

# %%
"""
Introduction

Search for parameters of machine learning models that result in best cross-validation performance is necessary
in almost all practical cases to get a model with best generalization estimate.

A standard approach in scikit-learn in search for optimal modelling hyperparameters
is using sklearn.model_selection.GridSearchCV class,
which takes a set of values for every parameter to try, and simply enumerates all combinations of parameter values.

The complexity of such search grows exponentially with the addition of new parameters.
A more scalable approach is using sklearn.model_selection.RandomizedSearchCV,
which however does not take advantage of the structure of a search space.

Scikit-optimize provides a drop-in replacement for sklearn.model_selection.GridSearchCV,
which utilizes Bayesian Optimization where a predictive model referred to as  “surrogate”
is used to model the search space and utilized to arrive at good parameter values combination as soon as possible.

Note: for a manual hyperparameter optimization example, see “Hyperparameter Optimization” notebook.
"""

# %%
from skopt import BayesSearchCV
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X, y = load_digits(n_class=10, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=.25, random_state=0)

# log-uniform: understand as search over p = exp(x) by varying x
model = SVC()
opt = BayesSearchCV(
    model,
    {
        'C': (1e-6, 1e+6, 'log-uniform'),
        'gamma': (1e-6, 1e+1, 'log-uniform'),
        'degree': (1, 8),  # integer valued parameter
        'kernel': ['linear', 'poly', 'rbf'],  # categorical parameter
    },
    n_iter=32,
    cv=3,
)

opt.fit(X_train, y_train)

print("val. score: %s" % opt.best_score_)
print("test score: %s" % opt.score(X_test, y_test))

# %%
type(opt)   # skopt.searchcv.BayesSearchCV
dir(opt)
opt.best_estimator_     # SVC(C=55739.27047244013, degree=4, gamma=1.1368692565024818, kernel='poly')
# Estimator that was chosen by the search,
# i.e. estimator which gave highest score (or smallest loss if specified) on the left out data.
# ! Not available if refit=False. (default is True)
opt.best_estimator_.feature_importances_    # AttributeError: 'SVC' object has no attribute 'feature_importances_'
opt.best_estimator_.predict(X_train[:1, :]) # array([2])
opt.best_params_
# OrderedDict([('C', 55739.27047244013),
#              ('degree', 4),
#              ('gamma', 1.1368692565024818),
#              ('kernel', 'poly')])

opt.predict(X_train[:1, :]) # array([2])

# %% !!!
# %% with CV generator

from sklearn.model_selection import KFold

# n_samples = X.shape[0]
cv = KFold(n_splits=5)

model = SVC()
opt = BayesSearchCV(
    model,
    {
        'C': (1e-6, 1e+6, 'log-uniform'),
        'gamma': (1e-6, 1e+1, 'log-uniform'),
        'degree': (1, 8),  # integer valued parameter
        'kernel': ['linear', 'poly', 'rbf'],  # categorical parameter
    },
    n_iter=32,
    cv=cv.split(X_train, y_train)
)
opt.fit(X_train, y_train)

# %%
"""  !!!
As generators are in general NON-pickable objects
!!!  one cannot pickle  skopt.searchcv.BayesSearchCV  with  CV generator as its component
"""
import dill as pickle
pickle.dump([opt], open('opt.pkl', 'bw'))   # ! TypeError: cannot pickle 'generator' object

"""
However it's in general possible to pickle any sklearn estimator (model)
-- it only cannot contain any generators;
e.g. one can pickle the best model found via  BayesSearchCV  (but not the whole BayesSearchCV)
"""
best = opt.best_estimator_
type(best)
dir(best)
best.get_params()

pickle.dump([best], open('best.pkl', 'bw'))     # OK !

# %% ...
from xgboost import XGBClassifier

model = XGBClassifier()
model.fit(X_train, y_train)
dir(model)
model.feature_importances_
model.feature_names_in_

# %%
# %%


# %%
# %%
# %%
