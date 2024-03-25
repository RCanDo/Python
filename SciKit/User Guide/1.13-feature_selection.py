#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Feature selection
version: 1.0
keywords: [feature selection, ...]
description: |
content:
remarks:
todo:
sources:
    - title: 1.13. Feature selection
      link: https://scikit-learn.org/stable/modules/feature_selection.html#rfe
file:
    name: 3.1-cross_validation.py
    usage:
        interactive: True
        terminal: False
    date: 2023-11-07
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

# %% 1.13.1. Removing features with low variance

from sklearn.feature_selection import VarianceThreshold

X = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]])
X
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)

# %% 1.13.2. Univariate feature selection
"""
Univariate feature selection works by selecting the best features
!   based on  univariate statistical tests.

It can be seen as a preprocessing step to an estimator.

Scikit-learn exposes feature selection routines as objects that implement the `.transform()` method:

1. SelectKBest  removes all but the `k` _ highest scoring _ features
2. SelectPercentile  removes all but a user-specified  _ highest scoring _ percentage of features
3. using common univariate statistical tests for each feature:
    - false positive rate  SelectFpr,
    - false discovery rate  SelectFdr,
    - or family wise error  SelectFwe.
    - GenericUnivariateSelect  allows to perform univariate feature selection with a configurable strategy.
      This allows to select the best univariate selection strategy with hyper-parameter search estimator.

For instance, we can use a F-test to retrieve the two best features for a dataset as follows:
"""
# %% SelectKBest(score_func=... , k=...) -- no CV, no model, only 2 params
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

X, y = load_iris(return_X_y=True)
X.shape

f_classif(X, y)
# (array([ 119.26450218,   49.16004009, 1180.16118225,  960.0071468 ]),             F-statistic for each feature.
#  array([1.66966919e-31, 4.49201713e-17, 2.85677661e-91, 4.16944584e-85]))         P-values associated with the F-statistic.

skb = SelectKBest(score_func=f_classif, k=2)
skb.fit(X, y)

dir(skb)
skb.get_params()
# {'k': 2,
#  'score_func': <function sklearn.feature_selection._univariate_selection.f_classif(X, y)>}
skb.get_feature_names_out()     # array(['x2', 'x3'], dtype=object)
skb.get_support()               # array([False, False,  True,  True])
skb.k               # 2
skb.n_features_in_  # 4
skb.pvalues_        # array([1.66966919e-31, 4.49201713e-17, 2.85677661e-91, 4.16944584e-85])
skb.score_func      # <function sklearn.feature_selection._univariate_selection.f_classif(X, y)>
skb.scores_         # array([ 119.26450218,   49.16004009, 1180.16118225,  960.0071468 ])      F-stat
skb.set_output()    # SelectKBest(k=2)  see help on this
skb.set_params()    # SelectKBest(k=2)

X_new = skb.transform(X)
X_new.shape         # (150, 2)
type(X_new)         # numpy.ndarray

skb.set_output(transform="pandas")    # SelectKBest(k=2)
X_new = skb.transform(X)
type(X_new)         # pd.DataFrame
X_new

skb.set_output(transform="default")
X_new = skb.transform(X)
type(X_new)         # numpy.ndarray

# %%
"""
These objects take as input a _scoring function_ that returns
1. univariate scores (statistics, e.g. F-stat),
2. p-values,
or only scores for  SelectKBest  and  SelectPercentile.

possible _scoring functions_ are:
1. For regression:  r_regression,  f_regression,  mutual_info_regression.
2. For classification:  chi2,  f_classif,  mutual_info_classif.

The methods based on  F-test  estimate the degree of linear dependency between two random variables.
On the other hand,  mutual information  methods can capture any kind of statistical dependency,
but being nonparametric, they require more samples for accurate estimation.
Note that the  chi^2 test  should only be applied to non-negative features, such as frequencies.

# Feature selection with sparse data
If you use sparse data (i.e. data represented as sparse matrices), chi2, mutual_info_regression, mutual_info_classif
will deal with the data without making it dense.

Warning
Beware not to use a regression scoring function with a classification problem, you will get useless results.

Examples:
    Univariate Feature Selection
    Comparison of F-test and mutual information
"""

# %% 1.13.3. Recursive feature elimination, RFE  -- no CV, meta-, importances
"""
Given an external estimator that assigns _ weights to features _
(e.g., the coefficients of a linear model),
the goal of  recursive feature elimination  RFE  is to select features
by recursively considering smaller and smaller sets of features.

First, the estimator is trained on the initial set of features and the importance of each feature
is obtained either through any specific attribute (such as `coef_`, `feature_importances_`) or callable.

Then, the least important features are pruned from current set of features.
That procedure is recursively repeated on the pruned set
until the desired number of features to select is eventually reached.

RFECV performs RFE in a cross-validation loop to find the optimal number of features.

Examples:

1. Recursive feature elimination:
    A recursive feature elimination example showing the relevance of pixels in a digit classification task.

2. Recursive feature elimination with cross-validation:
    A recursive feature elimination example with automatic tuning of the number of features
    selected with cross-validation.
"""

# %% 1.13.4. Feature selection using SelectFromModel
"""
SelectFromModel  is a  meta-transformer  (i.e. takes some model as one of arguments)
that can be used alongside any estimator (model) that assigns importance to each feature
through a specific attribute (such as `coef_`, `feature_importances_`)
or via an  importance_getter  callable after fitting.

The features are considered unimportant and removed if the corresponding importance of the feature values
are below the provided threshold parameter.

!   Apart from specifying the threshold numerically, there are built-in heuristics
for finding a threshold using a string argument.
Available heuristics are “mean”, “median” and float multiples of these like “0.1*mean”.
In combination with the threshold criteria, one can use the `max_features` parameter
to set a limit on the number of features to select.

For examples on how it is to be used refer to the sections below.

Examples
    Model-based and sequential feature selection        !!!
"""

# %% 1.13.4.1. L1-based feature selection
"""
Linear models penalized with the L1 norm have sparse solutions:
many of their estimated coefficients are zero.

When the goal is to reduce the dimensionality of the data to use with another classifier,
they can be used along with  SelectFromModel  to select the non-zero coefficients.

In particular, "sparse estimators" useful for this purpose are the  Lasso  for regression,
and of  LogisticRegression  and  LinearSVC  for classification:
"""
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel

X, y = load_iris(return_X_y=True)
X.shape     # 150, 4

lsvc = LinearSVC(C=0.01, penalty="l1", dual=False)
lsvc.fit(X, y)

model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X)

X_new.shape     # (150, 3)

# %%
# or with "raw" model (not fit yet)

model = SelectFromModel(LinearSVC(C=0.01, penalty="l1", dual=False), prefit=False)
model.fit(X, y)
X_new = model.transform(X)

X_new.shape     # (150, 3)

"""
With SVMs and logistic-regression, the parameter C controls the sparsity:
!   the smaller C the fewer features selected.

With Lasso, the higher the alpha parameter, the fewer features selected.

Examples:
    Lasso on dense and sparse data.
"""

# %% 1.13.4.2. Tree-based feature selection
"""
Tree-based estimators (see the sklearn.tree module and forest of trees in the sklearn.ensemble module)
can be used to compute  impurity-based  feature importances,
which in turn can be used to discard irrelevant features
(when coupled with the  SelectFromModel  meta-transformer):
"""
from sklearn.datasets import load_iris
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel

X, y = load_iris(return_X_y=True)
X.shape     # 150, 4

clf = ExtraTreesClassifier(n_estimators=50)
clf = clf.fit(X, y)
clf.feature_importances_    # array([0.09766541, 0.05775378, 0.43750253, 0.40707828])

model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
X_new.shape     # 150, 2

"""
Examples:
1. Feature importances with a forest of trees:
   example on synthetic data showing the recovery of the actually meaningful features.      !!!
2. Pixel importances with a parallel forest of trees: example on face recognition data.
"""
# %% 1.13.5. Sequential Feature Selection  (SFS) -- uses CV
"""
Sequential Feature Selection [sfs] (SFS) is available in the  SequentialFeatureSelector  transformer.

SFS can be either forward or backward.

Forward-SFS is a greedy procedure that iteratively finds the best new feature to add to the set of selected features.
Concretely, we initially start with zero features and find the one feature that maximizes a cross-validated score
when an estimator is trained on this single feature.
Once that first feature is selected, we repeat the procedure by adding a new feature to the set of selected features.
The procedure stops when the desired number of selected features is reached,
as determined by the `n_features_to_select` parameter.

Backward-SFS follows the same idea but works in the opposite direction:
instead of starting with no features and greedily adding features,
we start with all the features and greedily remove features from the set.
???  What a difference to RFE  ???  see below

The `direction` parameter controls whether forward or backward SFS is used.

Details
In general, forward and backward selection do not yield equivalent results.
Also, one may be much faster than the other depending on the requested number of selected features:
if we have 10 features and ask for 7 selected features,
forward selection would need to perform 7 iterations while backward selection would only need to perform 3.

!!!   SFS differs from  RFE  and  SelectFromModel  !!!
in that it does not require the underlying model to expose a `coef_` or `feature_importances_` attribute.
It may however be slower considering that more models need to be evaluated, compared to the other approaches.
For example in backward selection, the iteration going from `m` features to `m - 1` features
using k-fold cross-validation requires fitting `m * k` models,
while  RFE  would require only a single fit,
and  SelectFromModel  always just does a single fit and requires no iterations.

Reference
[sfs]
Ferri et al, Comparative study of techniques for large-scale feature selection.


Examples
    Model-based and sequential feature selection        !!!
"""

# %% 1.13.6. Feature selection as part of a pipeline
"""
Feature selection is usually used as a pre-processing step before doing the actual learning.

The recommended way to do this in scikit-learn is to use a Pipeline:
"""
clf = Pipeline([
  ('feature_selection', SelectFromModel(LinearSVC(dual="auto", penalty="l1"))),
  ('classification', RandomForestClassifier())
])
clf.fit(X, y)
"""
In this snippet we make use of a LinearSVC coupled with SelectFromModel to evaluate feature importances
and select the most relevant features.
Then, a  RandomForestClassifier  is trained on the transformed output,
i.e. using only relevant features.
You can perform similar operations with the other feature selection methods and also classifiers
that provide a way to evaluate feature importances of course.

See the Pipeline examples for more details.
"""

# %%
