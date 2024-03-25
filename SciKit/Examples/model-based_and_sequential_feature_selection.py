"""
============================================
Model-based and sequential feature selection
============================================

This example illustrates and compares two approaches for feature selection:
:class:`~sklearn.feature_selection.SelectFromModel` which is based on feature
importance, and
:class:`~sklearn.feature_selection.SequentialFeatureSelector` which relies
on a greedy approach.

We use the Diabetes dataset, which consists of 10 features collected from 442
diabetes patients.

Authors: `Manoj Kumar <mks542@nyu.edu>`_,
`Maria Telenczuk <https://github.com/maikia>`_, Nicolas Hug.

License: BSD 3 clause

https://scikit-learn.org/stable/auto_examples/feature_selection/plot_select_from_model_diabetes.html#sphx-glr-auto-examples-feature-selection-plot-select-from-model-diabetes-py
plot_select_from_model_diabetes.py

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
# Loading the data
# ----------------
#
# We first load the diabetes dataset which is available from within
# scikit-learn, and print its description:
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)

# %%
# Feature importance from coefficients
# ------------------------------------
#
# To get an idea of the importance of the features, we are going to use the
# :class:`~sklearn.linear_model.RidgeCV` estimator. The features with the
# highest absolute `coef_` value are considered the most important.
# We can observe the coefficients directly without needing to scale them (or
# scale the data) because from the description above, we know that the features
# were already standardized.
# For a more complete example on the interpretations of the coefficients of
# linear models, you may refer to
# https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html#sphx-glr-auto-examples-inspection-plot-linear-model-coefficient-interpretation-py.  # noqa: E501
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import RidgeCV

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=5)).fit(X, y)
ridge.coef_
importance = np.abs(ridge.coef_)
importance
feature_names = np.array(diabetes.feature_names)
plt.bar(height=importance, x=feature_names)
plt.title("Feature importances via coefficients")
plt.show()

# %%
# SelectFromModel
# ---------------
# Selecting features based on  importance  (from model) -- no CV, meta-, threshold
#
# Now we want to select the two features which are the most important according to the coefficients.
# !   The `SelectFromModel` is meant just for that.
# `SelectFromModel` accepts a `threshold` parameter and will select the features whose
# !   importance (defined by the coefficients)
# are above this threshold.
#
# Since we want to select only 2 features, we will set this threshold slightly
# above the coefficient of third most important feature.
from time import time

from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

tic = time()
sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
toc = time()
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
print(f"Done in {toc - tic:.3f}s")

# %%
# SequentialFeatureSelector (SFS)
# -------------------------------
# Selecting features based on CV  score  of model -- CV, meta-, tol
#
# Another way of selecting features is to use
# `SequentialFeatureSelector` (SFS).
# !   SFS is a greedy procedure where, at each iteration,
# we choose the best new feature to add to our selected features based a cross-validation score.
# That is, we start with 0 features and choose the best single feature with the highest score.
# The procedure is repeated until we reach the desired number of selected features.
#
# We can also go in the reverse direction (backward SFS),
# i.e. start with all the features and greedily choose features to remove one by one.
# We illustrate both approaches here.

from sklearn.feature_selection import SequentialFeatureSelector

tic_fwd = time()
sfs_forward = SequentialFeatureSelector(
    ridge, n_features_to_select=2, direction="forward"
).fit(X, y)
toc_fwd = time()
# `ridge` was fitted but meta-estimator  SequentialFeatureSelector  refits it while it is fit;
# !   see  https://scikit-learn.org/stable/glossary.html#term-metaestimators

tic_bwd = time()
sfs_backward = SequentialFeatureSelector(
    ridge, n_features_to_select=2, direction="backward"
).fit(X, y)
toc_bwd = time()

print(
    "Features selected by forward sequential selection: "
    f"{feature_names[sfs_forward.get_support()]}"
)
print(f"Done in {toc_fwd - tic_fwd:.3f}s")
print(
    "Features selected by backward sequential selection: "
    f"{feature_names[sfs_backward.get_support()]}"
)
print(f"Done in {toc_bwd - tic_bwd:.3f}s")

# %%
# Interestingly, forward and backward selection have selected the same set of features.
# In general, this isn't the case and the two methods would lead to different results.
#
# We also note that the features selected by SFS differ from those
# selected by feature importance: SFS selects `bmi` instead of `s1`.
# This does sound reasonable though, since `bmi` corresponds to the third most important
# feature according to the coefficients.
#
# !  It is quite remarkable considering that SFS makes no use of the coefficients at all.
#
# To finish with, we should note that
# `SelectFromModel` is significantly faster than SFS.
# Indeed, `SelectFromModel` only needs to fit a model once,
# !  while SFS needs to cross-validate (???!!!) many different models for each of the iterations.
#
# SFS however works with any model, while
# `SelectFromModel`
# !  requires the underlying# estimator to expose a `coef_` attribute or a `feature_importances_` attribute
# (XGBoost does!)
#
# The forward SFS is faster than the backward SFS because it only
# needs to perform `n_features_to_select = 2` iterations, while the backward
# SFS needs to perform `n_features - n_features_to_select = 8` iterations.

# %%
# Using negative tolerance values
# -------------------------------
#
# `SequentialFeatureSelector`  can be used to remove features present in the dataset
# and return a smaller subset of the original features with `direction="backward"`
# and a negative value of `tol`.
#
# We begin by loading the Breast Cancer dataset, consisting of 30 different features and 569 samples.

from sklearn.datasets import load_breast_cancer

breast_cancer_data = load_breast_cancer()
X, y = breast_cancer_data.data, breast_cancer_data.target
feature_names = np.array(breast_cancer_data.feature_names)
print(breast_cancer_data.DESCR)

# %%
# We will make use of the  `LogisticRegression`
# estimator with  `SequentialFeatureSelector`
# to perform the feature selection.
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

for tol in [-1e-2, -1e-3, -1e-4]:
    start = time()
    feature_selector = SequentialFeatureSelector(
        LogisticRegression(),
        n_features_to_select="auto",
        direction="backward",
        scoring="roc_auc",
        tol=tol,
        n_jobs=2,
    )
    model = make_pipeline(StandardScaler(), feature_selector, LogisticRegression())
    model.fit(X, y)
    end = time()
    print(f"\ntol: {tol}")
    print(f"Features selected: {feature_names[model[1].get_support()]}")
    print(f"ROC AUC score: {roc_auc_score(y, model.predict_proba(X)[:, 1]):.3f}")
    print(f"Done in {end - start:.3f}s")

# %%
# We can see that the number of features selected tend to increase as negative
# values of `tol` approach to zero. The time taken for feature selection also
# decreases as the values of `tol` come closer to zero.
