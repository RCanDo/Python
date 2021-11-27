#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: LinearSVR - Linear Support Vector Regression
subtitle:
version: 1.0
type: examples
keywords: [LinearSVR]
description: |
remarks:
todo:
sources:
    - title: LinearSVR - Linear Support Vector Regression.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVR.html
    - title: LinearSVC - Linear Support Vector Classification.
      link: https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html
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
    date: 2021-10-26
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
#%% LinearSVR
"""
Parameters
----------
epsilon : float, default=0.0
    Epsilon parameter in the epsilon-insensitive loss function.
    Note that the value of this parameter depends on the scale of the target variable y.
   !!! If unsure, set epsilon=0.  !!!
tol : float, default=1e-4
    Tolerance for stopping criteria.
C : float, default=1.0
    Regularization parameter.  Must be strictly positive.
   !!! The strength of the regularization is inversely proportional to C.  !!!
    large C ~= large penalty - weak regularization -> overfitting  (large variance / small bias)
loss : {‘epsilon_insensitive’, ‘squared_epsilon_insensitive’}, default=’epsilon_insensitive’
    Specifies the loss function.
    The `epsilon-insensitive` loss (standard SVR) is the  L1  loss,
    while the `squared epsilon-insensitive` loss (‘squared_epsilon_insensitive’) is the  L2  loss.
fit_intercept : bool, default=`True`
    Whether to calculate the intercept for this model.
    If set to `False`, no intercept will be used in calculations (i.e. data is expected to be already centered).
intercept_scaling : float, default=1.0
    When `self.fit_intercept = True`, instance vector x becomes
    [x, self.intercept_scaling],
    i.e. a “synthetic” feature with constant value equals to `intercept_scaling`
    is appended to the instance vector.
    The intercept becomes `intercept_scaling * synthetic feature` weight
    Note! the synthetic feature weight is subject to   l1/l2 regularization   as all other features.
    To lessen the effect of regularization on synthetic feature weight
    (and therefore on the intercept) `intercept_scaling` has to be increased.
dual : bool, default=True
    Select the algorithm to either solve the `dual` or `primal` optimization problem.
   !!! Prefer dual=False when `n_samples > n_features`.  !!!
verbose : int, default=0
    Enable verbose output.
    Note that this setting takes advantage of a per-process runtime setting in `liblinear` that,
    if enabled, may not work properly in a __multithreaded__ context.
random_state : int, RandomState instance or None, default=None
    Controls the pseudo random number generation for shuffling the data. Pass an int for reproducible output across multiple function calls. See Glossary.
max_iter : int, default=1000
    The maximum number of iterations to be run.

Attributes
----------
coef_ : ndarray of shape (n_features) if n_classes == 2 else (n_classes, n_features)
    Weights assigned to the features (coefficients in the primal problem).
    coef_ is a readonly property derived from raw_coef_ that follows the internal memory layout of liblinear.
intercept_ : ndarray of shape (1) if n_classes == 2 else (n_classes)
    Constants in decision function.
n_features_in_ : int
    Number of features seen during fit.
    New in version 0.24.
feature_names_in_ : ndarray of shape (n_features_in_,)
    Names of features seen during fit. Defined only when X has feature names that are all strings.
    New in version 1.0.
n_iter_ : int
    Maximum number of iterations run across all classes.


"""
#%%
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('dark_background')
# see `plt.style.available` for list of available styles
import matplotlib.image as mpimg

#%%
#%% SVR


#%%
#%% LinearSVR

from sklearn.svm import LinearSVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_regression

X, y = make_regression(n_features=4, random_state=0)
X.shape   # 100, 4
y

regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, tol=1e-5))
regr
# Pipeline(steps=[('standardscaler', StandardScaler()), ('linearsvr', LinearSVR(random_state=0, tol=1e-05))])

regr.fit(X, y)

regr.named_steps['linearsvr'].coef_

regr.named_steps['linearsvr'].intercept_

regr.predict([[0, 0, 0, 0]])

#%% plot ???
X, y0 = make_regression(n_features=1, random_state=0)
x = X[:, 0]
y = y0 + np.random.randn(100) * 50

fig, ax = plt.subplots()
ax.scatter(x, y)

regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, tol=1e-5))
regr
# Pipeline(steps=[('standardscaler', StandardScaler()), ('linearsvr', LinearSVR(random_state=0, tol=1e-05))])

regr.fit(X, y)

regr.named_steps['linearsvr'].coef_

regr.named_steps['linearsvr'].intercept_

x_new = np.array([[-3], [3]])  # for linear regr. it's enough to have 2 values

ax.plot(x_new, regr.predict(x_new), label="C=1")

#%%
regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0))
regr
regr.fit(X, y)
ax.plot(x_new, regr.predict(x_new), "r:", label="tol=1e-4 (default)")
#
#%%
regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, C=10, tol=1e-5))
regr
regr.fit(X, y)
ax.plot(x_new, regr.predict(x_new), label="C=10")

#%%
regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, C=10))
regr
regr.fit(X, y)
ax.plot(x_new, regr.predict(x_new), "g:", label="C=10; tol. default")

#%%
regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, C=100, tol=1e-5))
regr
regr.fit(X, y)
ax.plot(x_new, regr.predict(x_new), label="C=100")

#%%
regr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, C=.1, tol=1e-5))
regr
regr.fit(X, y)
ax.plot(x_new, regr.predict(x_new), label="C=.1")

ax.legend(loc="upper left")
#%%
"""
tol has no visible effect.
But `C` is crucial !!!
"""

vars(regr.named_steps['linearsvr'])

"""
{'tol': 1e-05,
 'C': 0.1,
 'epsilon': 0.0,
 'fit_intercept': True,
 'intercept_scaling': 1.0,
 'verbose': 0,
 'random_state': 0,
 'max_iter': 1000,
 'dual': True,
 'loss': 'epsilon_insensitive',
 'n_features_in_': 1,
 'coef_': array([3.89225992]),
 'intercept_': array([-6.9388939e-17]),
 'n_iter_': 4}
"""
#%%


#%%


#%%


#%%
#%%