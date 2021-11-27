#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: LinearSVC - Linear Support Vector Classification
subtitle:
version: 1.0
type: examples
keywords: [LinearSVC]
description: |
remarks:
todo:
sources:
    - title: LinearSVC - Linear Support Vector Classification.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
    - title: LinearSVR - Linear Support Vector Regression.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html
    - title: SVC - C-Support Vector Classification.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    - title: SVR  - Epsilon-Support Vector Regression.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
    - title: NuSVC - Nu-Support Vector Classification.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html
    - title: NuSVR - Nu Support Vector Regression.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVR.html
    - title: OneClassSVM - Unsupervised Outlier Detection.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.OneClassSVM.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: SVM.py
    path: E:/ROBOCZY/Python/SciKit/learn/SVM/
    date: 2021-10-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
import os, json

ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/SciKit/learn/SVM/")   #!!! adjust
os.chdir(WD)

#%%
WD = os.getcwd()
print(WD)

#%%
"""
Parameters
----------
penalty : {‘l1’, ‘l2’}, default=’l2’
    Specifies the norm used in the penalization.   ??? what math formula ???
    The ‘l2’ penalty is the standard used in SVC.
    The ‘l1’ leads to `coef_ vectors` that are sparse.
loss : {‘hinge’, ‘squared_hinge’}, default=’squared_hinge’
    Specifies the loss function.
    ‘hinge’ is the standard SVM loss (used e.g. by the SVC class)
    while ‘squared_hinge’ is the square of the hinge loss.
    The combination of penalty='l1' and loss='hinge' is not supported.
dual : bool, default=True
    Select the algorithm to either solve the dual or primal optimization problem.
   !!! Prefer `dual=False` when n_samples > n_features.  !!!
tol : float, default=1e-4
    Tolerance for stopping criteria.
C : float, default=1.0
    Regularization parameter. Must be strictly positive.
   !!! The strength of the regularization is inversely proportional to C.  !!!
    large C ~= large penalty - weak regularization -> overfitting  (large variance / small bias)
multi_class : {‘ovr’, ‘crammer_singer’}, default=’ovr’
    Determines the multi-class strategy if y contains more than two classes.
    "ovr" trains n_classes one-vs-rest classifiers,
    while "crammer_singer" optimizes a joint objective over all classes.
    While "crammer_singer" is interesting from a theoretical perspective as it is consistent,
    it is seldom used in practice as it rarely leads to better accuracy
    and is more expensive to compute.
    If "crammer_singer" is chosen, the options `loss`, `penalty` and `dual` will be ignored.
fit_intercept : bool, default=True
    Whether to calculate the intercept for this model.
    If set to `False`, no intercept will be used in calculations
    (i.e. data is expected to be already centered).
intercept_scaling : float, default=1
    When `self.fit_intercept` is True,
    instance vector x becomes [x, self.intercept_scaling],
    i.e. a “synthetic” feature with constant value equals to intercept_scaling
    is appended to the instance vector.
    The intercept becomes `intercept_scaling * synthetic feature` weight
    Note! the synthetic feature weight is subject to L1/L2 regularization
    as all other features.
    To lessen the effect of regularization on synthetic feature weight
    (and therefore on the intercept) `intercept_scaling` has to be increased.
class_weight : dict or ‘balanced’, default=None
    Set the parameter C of class i to class_weight[i]*C for SVC.
    If not given, all classes are supposed to have weight one.
    The “balanced” mode uses the values of y to automatically adjust weights
    inversely proportional to class frequencies in the input data as
    n_samples / (n_classes * np.bincount(y)).
verbose : int, default=0
    Enable verbose output.
    Note that this setting takes advantage of a per-process runtime setting in liblinear
    that, if enabled, may not work properly in a multithreaded context.
random_stateint, RandomState instance or None, default=None
    Controls the pseudo random number generation for shuffling the data
    for the dual coordinate descent (if dual=True).
    When dual=False the underlying implementation of LinearSVC is not random
    and random_state has no effect on the results.
    Pass an int for reproducible output across multiple function calls. See Glossary.
max_iterint, default=1000
    The maximum number of iterations to be run.

Attributes
----------
coef_ : ndarray of shape (1, n_features) if n_classes == 2 else (n_classes, n_features)
    Weights assigned to the features (coefficients in the primal problem).
    coef_ is a readonly property derived from raw_coef_
    that follows the internal memory layout of liblinear.
intercept_ : ndarray of shape (1,) if n_classes == 2 else (n_classes,)
    Constants in decision function.
classes_ : ndarray of shape (n_classes,)
    The unique classes labels.
n_features_in_ : int
    Number of features seen during fit.
feature_names_in_ : ndarray of shape (n_features_in_,)
    Names of features seen during fit. Defined only when X has feature names that are all strings.
n_iter_ : int
    Maximum number of iterations run across all classes.


SVC
---
Implementation of Support Vector Machine classifier using libsvm:
the kernel can be non-linear but its SMO algorithm
does not scale to large number of samples as `LinearSVC` does.
Furthermore SVC multi-class mode is implemented using "one vs one" scheme
while `LinearSVC` uses "one vs the rest".
It is possible to implement "one vs the rest" with SVC
!!!   by using the `OneVsRestClassifier` wrapper.                             !!!

Finally SVC can fit dense data without memory copy if the input is C-contiguous.
Sparse data will still incur memory copy though.

`sklearn.linear_model.SGDClassifier`   <-   use it instead !!!
`SGDClassifier` can optimize the same cost function as `LinearSVC`
by adjusting the penalty and loss parameters.
In addition it requires less memory,
allows incremental (online) learning,
and implements various loss functions and regularization regimes.

Notes
-----
The underlying C implementation uses a random number generator
to select features when fitting the model.
It is thus not uncommon to have slightly different results for the same input data.
If that happens, try with a smaller `tol` parameter.

The underlying implementation, liblinear,
uses a sparse internal representation for the data that will incur a memory copy.

Predict output may not match that of standalone liblinear in certain cases.
See differences from liblinear in the narrative documentation.
"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('dark_background')
# see `plt.style.available` for list of available styles
import matplotlib.image as mpimg

#%%
#%% SVR
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

X, y = make_classification(n_features=4, random_state=0)
X.shape  # 100, 4
y

clf = make_pipeline(StandardScaler(), LinearSVC(random_state=0))
clf.fit(X, y)
# Pipeline(steps=[('standardscaler', StandardScaler()), ('linearsvc', LinearSVC(random_state=0))])
type(clf)    # klearn.pipeline.Pipeline

print(clf.predict([[0, 0, 0, 0]]))    # [1]

vars(clf.named_steps['linearsvc'])

"""
{'dual': True,
 'tol': 0.0001,
 'C': 1.0,
 'multi_class': 'ovr',
 'fit_intercept': True,
 'intercept_scaling': 1,
 'class_weight': None,
 'verbose': 0,
 'random_state': 0,
 'max_iter': 1000,
 'penalty': 'l2',
 'loss': 'squared_hinge',
 'n_features_in_': 4,
 'classes_': array([0, 1]),
 'coef_': array([[0.14144157, 0.52678338, 0.67978523, 0.49307305]]),
 'intercept_': array([0.16935988]),
 'n_iter_': 282}
"""

#%%
fig, axs = plt.subplots(1, 4, figsize=(18, 6), sharey=True)
for i in range(4):
    j = (i+1) % 4
    axs[i].set_title(f'X_{i} ~ X_{j}')
    sc = axs[i].scatter(X[:, i], X[:, j], c=y, s=1, cmap='spring')
    axs[i].legend(*sc.legend_elements())  # see  https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html


#%%
#%%  Examples AK

import numpy as np

#%%  1. trivial - just two points on 2d plane

A, y_a = [0, 0], 0
B, y_b = [1, 1], 1

X = np.array([A, B])
y = np.array([y_a, y_b])

mod01 = LinearSVC()
mod01.fit(X, y)
vars(mod01)
dir(mod01)


#%%
def line0(x, a=None, b=None, d=None):
    """ `d` instead of `c` as `c` stands for `color` in `.plot()`
        ax + by + d = 0
        y = -(a/b)x - (d/b)
    """
    a = 1 if a is None else a
    b = 1 if b is None else b
    d = 0 if d is None else d
    if b == 0:
        y = None
    else:
        y = -(a/b) * x - (d/b)
    return y


def line(xx, a=None, b=None, d=None):
    def line1(x):
        return line0(x, a, b, d)
    yy = list(map(line1, xx))
    return yy


def plot_model(model, X, y):
    fig, axs = plt.subplots()
    axs.scatter(X[:, 0], X[:, 1], c=y, cmap='cool')

    a, b = model.coef_[0]
    d = model.intercept_[0]

    xx = [X[:, 0].min(), X[:, 0].max()]
    axs.plot(xx, line(xx, a=a, b=b, d=d), c='y')


#%%
plot_model(mod01, X, y)

#%%  2. 3 points
C, y_c = [1, .5], 1

X = np.array([A, B, C])
y = np.array([y_a, y_b, y_c])

mod02 = LinearSVC()
mod02.fit(X, y)
vars(mod02)

plot_model(mod02, X, y)

#%%  3. 4 points
D, y_d = [.5, .5], 0

X = np.array([A, B, C, D])
y = np.array([y_a, y_b, y_c, y_d])

mod03 = LinearSVC()
mod03.fit(X, y)
vars(mod03)

plot_model(mod03, X, y)
mod03.predict(X)        # array([0, 1, 1, 0])

#%%
mod04 = LinearSVC(loss="hinge")
mod04.fit(X, y)
vars(mod04)

plot_model(mod04, X, y)
mod04.predict(X)        # array([0, 1, 1, 1])   !!!  WTF  !!!

#%%


#%%


#%%


#%%


#%%


#%%