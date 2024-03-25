#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Cross-validation
version: 1.0
type: sub-module
keywords: [cross validation, ...]
description: |
content:
remarks:
todo:
sources:
    - title: 3.1. Cross-validation: evaluating estimator performance
      link: https://scikit-learn.org/stable/modules/cross_validation.html
file:
    name: 3.1-cross_validation.py
    usage:
        interactive: True
        terminal: False
    date: 2023-10-27
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@quantup.pl
"""
# %%
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
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

X, y = datasets.load_iris(return_X_y=True)
X.shape, y.shape

# %%
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.4, random_state=0)

X_train.shape, y_train.shape
X_test.shape, y_test.shape

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)

# %%
"""
When evaluating different settings (“hyperparameters”) for estimators,
such as the C setting that must be manually set for an SVM,
!   there is still a risk of overfitting on the test set
!   because the parameters can be tweaked until the estimator performs optimally.

!   This way, knowledge about the test set can “leak” into the model
and evaluation metrics no longer report on generalization performance.

To solve this problem, yet another part of the dataset can be held out as a so-called “validation set”:
training proceeds on the  training set,
after which evaluation is done on the  validation set,
and when the experiment seems to be successful, final evaluation can be done on the  test set.

However, by partitioning the available data into three sets,
we drastically reduce the number of samples which can be used for learning the model,
and the results can depend on a particular random choice for the pair of (train, validation) sets.

A solution to this problem is a procedure called cross-validation (CV for short).

A test set should still be held out for final evaluation,
!   but the validation set is no longer needed when doing CV.

In the basic approach, called  k-fold CV,
the training set is split into k smaller sets
(other approaches are described below, but generally follow the same principles).
The following procedure is followed for each of the k “folds”:

1. A model is trained using `k - 1` of the folds as training data.
2. The resulting model is validated on the remaining part of the data
   (i.e., it is used as a test set to compute a performance measure such as accuracy).

The performance measure reported by  k-fold cross-validation  is then
!   the average of the values computed in the loop.
This approach can be computationally expensive, but does not waste too much data
(as is the case when fixing an arbitrary validation set),
which is a major advantage in problems such as inverse inference where the number of samples is very small.
"""
# %% 3.1.1. Computing cross-validated metrics

from sklearn.model_selection import cross_val_score

clf = svm.SVC(kernel='linear', C=1, random_state=42)
type(clf)   # sklearn.svm._classes.SVC
dir(clf)
scores = cross_val_score(clf, X, y, cv=5)
scores      # array([0.96666667, 1.        , 0.96666667, 0.96666667, 1.        ])

# !!!
print("%0.2f accuracy with a standard deviation of %0.2f" % (scores.mean(), scores.std()))
# !!!

# %%
"""
By default, the score computed at each CV iteration is the  score method of the estimator.
It is possible to change this by using the scoring parameter:
"""
# from sklearn import metrics

scores = cross_val_score(clf, X, y, cv=5, scoring='f1_macro')
scores      # array([0.96658312, 1.        , 0.96658312, 0.96658312, 1.        ])

# %%
"""
It is also possible to use other cross validation strategies by passing a  cross validation iterator  instead,
for instance:
"""
from sklearn.model_selection import ShuffleSplit

# n_samples = X.shape[0]
cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)    # cross-validation iterator
cross_val_score(clf, X, y, cv=cv)

# %%  how it works:
cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=0)
[(train, test) for train, test in cv.split(X)]  # cool!

cv = ShuffleSplit(n_splits=2, test_size=0.5, random_state=0)    # cross-validation iterator
cross_val_score(clf, X, y, cv=cv)

[(train, test) for train, test in cv.split(X)]  #

# %%
# Another option is to use an  iterable yielding (train, test) splits  as arrays of indices, for example:
def custom_cv_2folds(X):
    n = X.shape[0]
    i = 1
    while i <= 2:
        idx = np.arange(n * (i - 1) / 2, n * i / 2, dtype=int)
        #! yield idx, idx  # ???  should be rather:
        yield idx,  np.array(list(set(range(n)).difference(idx)))
        i += 1

custom_cv = custom_cv_2folds(X)
cross_val_score(clf, X, y, cv=custom_cv)    # array([0.33333333, 0.30666667])    ??? why so low ???

# %%
custom_cv = custom_cv_2folds(X)
[(train, test) for train, test in custom_cv]

# %% analogously with KFold
from sklearn.model_selection import KFold

kfold = KFold(n_splits=2)
[(train, test) for train, test in kfold.split(X)]

cross_val_score(clf, X, y, cv=kfold)    # array([0.33333333, 0.30666667])

kfold5 = KFold(n_splits=5)
[(train, test) for train, test in kfold5.split(X)]

cross_val_score(clf, X, y, cv=kfold5)    # array([1.        , 1.        , 0.86666667, 1.        , 0.86666667])

# ! Very intriguing

# %%
q = .3
kfoldq = KFold(n_splits=int(1/q))
[(train, test) for train, test in kfoldq.split(X)]
# nonsense

# %%
# %%  Data transformation with held out data
from sklearn import preprocessing

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.4, random_state=0)

scaler = preprocessing.StandardScaler().fit(X_train)

X_train_transformed = scaler.transform(X_train)
clf = svm.SVC(C=1).fit(X_train_transformed, y_train)

X_test_transformed = scaler.transform(X_test)
clf.score(X_test_transformed, y_test)

# %% better with pipeline
from sklearn.pipeline import make_pipeline
clf = make_pipeline(preprocessing.StandardScaler(), svm.SVC(C=1))
clf     # Pipeline(steps=[('standardscaler', StandardScaler()), ('svc', SVC(C=1))])
cross_val_score(clf, X, y, cv=cv)

# %% 3.1.1.1. The cross_validate function and multiple metric evaluation¶
"""
The  cross_validate  function differs from  cross_val_score  in two ways:

- It allows specifying multiple metrics for evaluation.
- It returns a dict containing fit-times, score-times
  (and optionally training scores, fitted estimators, train-test split indices)
  in addition to the test score.

For single metric evaluation, where the scoring parameter is a string, callable or None, the keys will be:
['test_score', 'fit_time', 'score_time']

And for multiple metric evaluation, the return value is a dict with the following keys:
['test_<scorer1_name>', 'test_<scorer2_name>', 'test_<scorer...>', 'fit_time', 'score_time']
"""

# %%
from sklearn.model_selection import cross_validate

scoring = ['precision_macro', 'recall_macro']
clf = svm.SVC(kernel='linear', C=1, random_state=0)
scores = cross_validate(clf, X, y, scoring=scoring)

scores.keys()
# dict_keys(['fit_time', 'score_time', 'test_precision_macro', 'test_recall_macro'])
scores

pd.DataFrame(scores)

# %%
from sklearn.metrics import make_scorer
from sklearn.metrics import recall_score

scoring = {'prec_macro': 'precision_macro',
           'rec_macro': make_scorer(recall_score, average='macro')
          }
scores = cross_validate(clf, X, y, scoring=scoring,
                        cv=5, return_train_score=True)
# `return_train_score` is set to `False` by default to save computation time

pd.DataFrame(scores)

# %%  3.1.1.2. Obtaining predictions by cross-validation
# https://scikit-learn.org/stable/modules/cross_validation.html#obtaining-predictions-by-cross-validation
"""
The function  `cross_val_predict()`  has a similar interface to `cross_val_score()`,
but returns, for each element in the input,
the prediction that was obtained for that element when it was in the test set.

Only cross-validation strategies that assign all elements to a test set exactly once (!)
can be used (otherwise, an exception is raised).

!!! Warning
Note on inappropriate usage of cross_val_predict
...
"""

# %%
# %%  3.1.2. Cross validation iterators

KFold
StratifiedKFold
GroupKFold
StratifiedGroupKFold

RepeatedKFold
RepeatedStratifiedKFold

ShuffleSplit
StratifiedShuffleSplit
GroupShuffleSplit

LeaveOneOut
LeaveOneGroupOut

LeavePOut
LeavePGroupOut

# %%  3.1.2.1. Cross-validation iterators for i.i.d. data

# %% K-fold
""""""
from sklearn.model_selection import KFold

X = ["a", "b", "c", "d"]
kf = KFold(n_splits=2)

for train, test in kf.split(X):
    print("%s %s" % (train, test))

# %%
# one split
kf = KFold(n_splits=3)

X = np.array([[0., 0.], [1., 1.], [-1., -1.], [2., 2.], [3, 3], [-2, -2]])
y = np.array([0, 1, 1, 0, 1, 1])

[(train, test) for train, test in kf.split(X)]

train, test = next(kf.split(X))
X[train]
X[test]
y[train]
y[test]

# %%
# %%  !!!  digression on generators;
# see `Functional/iterators_vs_generators.py`
kf = KFold(n_splits=3)
kf                      # KFold(n_splits=3, random_state=None, shuffle=False)  ~= a factory of generators
type(kf)                # sklearn.model_selection._split.KFold
kf.split                # <bound method _BaseKFold.split of KFold(n_splits=3, random_state=None, shuffle=False)>
                        # !!! it is _generator function_ !!!

kf_gen = kf.split(X)
kf_gen                  # <generator object _BaseKFold.split at 0x7f5cddd34dd0>
type(kf_gen)            # generator
dir(kf_gen)             # it has  `__iter__` and `__next__` methods
                        # ! thus it is  _iterator_ !
# BTW: Every  generator  is an  iterator.

next(kf_gen)            # (array([2, 3, 4, 5]), array([0, 1]))
next(kf_gen)            # (array([0, 1, 4, 5]), array([2, 3]))
next(kf_gen)            # (array([0, 1, 2, 3]), array([4, 5]))
next(kf_gen)            # ! StopIteration
# but
next(kf.split(X))       # will always return (array([2, 3, 4, 5]), array([0, 1]))
                        # because each time we recreate generator  kf_gen = kf.split(X)

[(train, test) for train, test in kf.split(X)]
[(train, test) for train, test in kf.split(X)]   # always the same set
# BUT
kf_gen = kf.split(X)
[(train, test) for train, test in kf_gen]
[(train, test) for train, test in kf_gen]       # empty beacuse previous call used the generator up

# %% !!!  ONE CANNOT .pkl generators  !!!
kf_gen = kf.split(X)
type(kf_gen)            # generator

import dill as pickle   # `dill` can pickle more then `pickle` and has exactly the same API
pickle.dump([kf_gen], open('kf_gen.pkl', 'bw'))     # ! TypeError: cannot pickle 'generator' object

# iter() doesn't help
pickle.dump([iter(kf_gen)], open('kf_gen.pkl', 'bw'))     # ! TypeError: cannot pickle 'generator' object
type(iter(kf_gen))      # generator

# !!! That's real problem when one wants to .pkl an estimator which uses CV generator

import joblib
joblib.dump([kf_gen], open('kf_gen.pkl', 'bw'))     # ! TypeError: cannot pickle 'generator' object

# %% However one  CAN .pkl  iterator
it = iter(range(9))
type(it)    # range_iterator
dir(it)
pickle.dump([it], open('it.pkl', 'bw'))

# and every CV generator could have been easily written as iterator... (but it's not easy now to turn it into iterator)
# It's also possible to .pkl  "a factory of generators":
pickle.dump([kf], open('kf.pkl', 'bw'))
# however one cannot pass this factory to estimator...

# !!! that's SHAME on scikit !!!

# pickle.dump([ids_per_userid_target_split], open('qq.pkl', 'bw'))


# %%
# %%  !!!  indexing returned by all "splitters" is always numeric
# i.e. only like  .iloc  (when working on pd.DataFrames or pd.Series)

from sklearn.model_selection import KFold

X = pd.DataFrame({'a': [0, 1, 1, 0, 0, 1], 'b': list('bababb')}, index=list('abcdef'))
kf = KFold(n_splits=2)

for train, test in kf.split(X):
    print("%s %s" % (train, test))


# %% Repeated K-Fold
"""
RepeatedKFold repeats K-Fold n times.
It can be used when one requires to run KFold n times, producing different splits in each repetition.

2-fold K-Fold repeated 2 times:
"""
from sklearn.model_selection import RepeatedKFold

rkf = RepeatedKFold(n_splits=2, n_repeats=2, random_state=12883823)

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
for train, test in rkf.split(X):
    print("%s %s" % (train, test))
# [2 3] [0 1]
# [0 1] [2 3]
# [0 2] [1 3]
# [1 3] [0 2]

# !  Note that K-Fold is not affected by classes or groups.

# %% Leave One Out (LOO)
from sklearn.model_selection import LeaveOneOut

loo = LeaveOneOut()

X = [1, 2, 3, 4]
for train, test in loo.split(X):
    print("%s %s" % (train, test))

# %% Leave P Out (LPO)
"""
For samples, this produces `math.comb(n, p)` train-test pairs.
Unlike LeaveOneOut and KFold, the test sets will overlap for p > 1.
"""
from sklearn.model_selection import LeavePOut

lpo = LeavePOut(p=2)

X = np.ones(4)
for train, test in lpo.split(X):
    print("%s %s" % (train, test))

# %%  ShuffleSplit
# Random permutations cross-validation a.k.a. Shuffle & Split
""""""
from sklearn.model_selection import ShuffleSplit

ss = ShuffleSplit(n_splits=5, test_size=0.25, random_state=0)

X = np.arange(10)
for train, test in ss.split(X):
    print("%s %s" % (train, test))

# !  Note that ShuffleSplit is not affected by classes or groups.

# %%
ss.test_size
ss.test_size = .5
for train, test in ss.split(X):
    print("%s %s" % (train, test))

ss.n_splits = 1
for train, test in ss.split(X):
    print("%s %s" % (train, test))

idx_train, idx_test = next(ss.split(X))
idx_train
idx_test

# %% 3.1.2.2. Cross-validation iterators with stratification based on class labels

# %% Stratified k-fold
"""
StratifiedKFold is a variation of k-fold which returns stratified folds:
each set contains approximately  the same percentage of samples of each  target class  as the complete set.
"""
from sklearn.model_selection import StratifiedKFold, KFold
import numpy as np
X, y = np.ones((50, 1)), np.hstack(([0] * 45, [1] * 5))

skf = StratifiedKFold(n_splits=3)

for train, test in skf.split(X, y):
    print('train -  {}   |   test -  {}'.format(
        np.bincount(y[train]), np.bincount(y[test])))

kf = KFold(n_splits=3)

for train, test in kf.split(X, y):
    print('train -  {}   |   test -  {}'.format(
        np.bincount(y[train]), np.bincount(y[test])))

"""
RepeatedStratifiedKFold
can be used to repeat Stratified K-Fold n times with different randomization in each repetition.
"""
# %% Stratified Shuffle Split
"""
StratifiedShuffleSplit
is a variation of ShuffleSplit, which returns stratified splits,
i.e which creates splits by preserving the same percentage for each target class as in the complete set.
"""

# %% 3.1.2.3. Cross-validation iterators for grouped data¶

# %% Group k-fold¶
"""
GroupKFold is a variation of k-fold which ensures that
!!! the same group is NOT represented in both testing and training sets.

For example if the data is obtained from different subjects with several samples per-subject
and if the model is flexible enough to learn from highly person specific features
it could fail to generalize to new subjects.

GroupKFold makes it possible to detect this kind of overfitting situations.

Imagine you have three subjects, each with an associated number from 1 to 3:
"""
from sklearn.model_selection import GroupKFold

X = [0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 8.8, 9, 10]
y = ["a", "b", "b", "b", "c", "c", "c", "d", "d", "d"]
groups = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]

gkf = GroupKFold(n_splits=3)

for train, test in gkf.split(X, y, groups=groups):
    print("%s %s" % (train, test))

# %% StratifiedGroupKFold
"""
StratifiedGroupKFold is a cross-validation scheme that combines both StratifiedKFold and GroupKFold.

The idea is to try to preserve the distribution of classes in each split
while keeping each group within a single split.

That might be useful when you have an unbalanced dataset so that using just GroupKFold might produce skewed splits.
"""
from sklearn.model_selection import StratifiedGroupKFold

X = list(range(18))
y = [1] * 6 + [0] * 12
groups = [1, 2, 3, 3, 4, 4, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 6]

sgkf = StratifiedGroupKFold(n_splits=3)

for train, test in sgkf.split(X, y, groups=groups):
    print("%s %s" % (train, test))

"""
Implementation notes:

With the current implementation full shuffle is not possible in most scenarios.
When shuffle=True, the following happens:

1. All groups are shuffled.
2. ! Groups are sorted by standard deviation of classes using stable sort.
3. Sorted groups are iterated over and assigned to folds.

That means that only groups with the same standard deviation of class distribution will be shuffled,
which might be useful when each group has only a single class.

The algorithm greedily assigns each group to one of n_splits test sets,
choosing the test set that minimises the variance in class distribution across test sets.

Group assignment proceeds from groups with highest to lowest variance in class frequency,
i.e. large groups peaked on one or few classes are assigned first.

This split is suboptimal in a sense that it might produce imbalanced splits
even if perfect stratification is possible.
If you have relatively close distribution of classes in each group, using GroupKFold is better.

"""

# %% Leave One Group Out
"""
LeaveOneGroupOut is a cross-validation scheme where
each split holds out samples belonging to one specific group.
Group information is provided via an array that encodes the group of each sample.

Each training set is thus constituted by all the samples except the ones related to a specific group.
This is the same as LeavePGroupsOut with n_groups=1
and the same as GroupKFold with n_splits equal to the number of unique labels passed to the groups parameter.

For example, in the cases of multiple experiments,
LeaveOneGroupOut can be used to create a cross-validation based on the different experiments:
we create a training set using the samples of all the experiments except one:
"""
from sklearn.model_selection import LeaveOneGroupOut

X = [1, 5, 10, 50, 60, 70, 80]
y = [0, 1, 1, 2, 2, 2, 2]
groups = [1, 1, 2, 2, 3, 3, 3]

logo = LeaveOneGroupOut()

for train, test in logo.split(X, y, groups=groups):
    print("%s %s" % (train, test))

# %% Leave P Groups Out
"""
LeavePGroupsOut is similar as LeaveOneGroupOut,
but removes samples related to P groups for each training/test set.
All possible combinations of P groups are left out, meaning test sets will overlap for P > 1.
"""
from sklearn.model_selection import LeavePGroupsOut

X = np.arange(6)
y = [1, 1, 1, 2, 2, 2]
groups = [1, 1, 2, 2, 3, 3]

lpgo = LeavePGroupsOut(n_groups=2)

for train, test in lpgo.split(X, y, groups=groups):
    print("%s %s" % (train, test))

# %% Group Shuffle Split
"""
The GroupShuffleSplit iterator
behaves as a combination of ShuffleSplit and LeavePGroupsOut,
and generates a sequence of randomized partitions in which a subset of groups are held out for each split.

Each train/test split is performed independently
meaning there is no guaranteed relationship between successive test sets.
"""
from sklearn.model_selection import GroupShuffleSplit

X = [0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 0.001]
y = ["a", "b", "b", "b", "c", "c", "c", "a"]
groups = [1, 1, 2, 2, 3, 3, 4, 4]

gss = GroupShuffleSplit(n_splits=4, test_size=0.5, random_state=0)

for train, test in gss.split(X, y, groups=groups):
    print("%s %s" % (train, test))

# %% 3.1.2.4. Predefined Fold-Splits / Validation-Sets

"""
For some datasets, a pre-defined split of the data into training- and validation fold
or into several cross-validation folds already exists.

Using  PredefinedSplit  it is possible to use these folds e.g. when searching for hyperparameters.

For example, when using a validation set,
set the test_fold to 0 for all samples that are part of the validation set, and to -1 for all other samples.
"""

# %% 3.1.2.5. Using cross-validation iterators to split train and test¶

"""
The above group cross-validation functions
may also be useful for splitting a dataset into training and testing subsets.

!!!  Note that the convenience function  train_test_split  is a wrapper around  ShuffleSplit  !!!
and thus only allows for stratified splitting (using the class labels) and cannot account for groups.

To perform the train and test split, use the indices for the train and test subsets yielded by the generator output
by the  .split()  method of the cross-validation splitter.
"""
import numpy as np
from sklearn.model_selection import GroupShuffleSplit

X = np.array([0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 0.001])
y = np.array(["a", "b", "b", "b", "c", "c", "c", "a"])
groups = np.array([1, 1, 2, 2, 3, 3, 4, 4])

gss = GroupShuffleSplit(random_state=7)     # ~= generators' factory
GroupShuffleSplit(random_state=7).split     # _generator function_
gss_gen = GroupShuffleSplit(random_state=7).split(X, y, groups)     # generator

train, test = next(gss_gen)

X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]

X_train.shape, X_test.shape

np.unique(groups[train]), np.unique(groups[test])

# %%
X = pd.DataFrame(
    {
         "x": [0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 0.001],
         "g": [1, 1, 2, 2, 3, 3, 4, 4],
         "y": ["a", "b", "b", "b", "c", "c", "c", "a"]
    }
)
X

y = X.pop("y")
y

gss = GroupShuffleSplit(random_state=7)     # ~= generators' factory
GroupShuffleSplit(random_state=7).split     # _generator function_
gss_gen = GroupShuffleSplit(random_state=7).split(X, y, X['g'])     # generator

train, test = next(gss_gen)

X.iloc[train, :]
X.iloc[test, :]
y[train]
y[test]

np.unique(groups[train]), np.unique(groups[test])


# %% 3.1.2.6. Cross validation of time series data¶

# %%


# %%

# %%

# %%
