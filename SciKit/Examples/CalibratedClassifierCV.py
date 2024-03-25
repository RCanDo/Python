#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: sklearn.calibration.CalibratedClassifierCV
version: 1.0
keywords: [preprocessing, variables, ...]
description: |
content:
remarks:
todo:
sources:
    - title: sklearn.calibration.CalibratedClassifierCV
      link: https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html
file:
    usage:
        interactive: True
        terminal: False
    date: 2023-11-18
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@quantup.pl
"""
# %%
from pprint import pprint
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
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.calibration import CalibratedClassifierCV

# %%
X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
X
# pd.DataFrame(X)

model = GaussianNB()

# %% fitting with calibration
modelc = CalibratedClassifierCV(
    estimator=model,
    method='sigmoid', # default. The method to use for calibration.
    # Can be ‘sigmoid’ which corresponds to Platt’s method (i.e. a logistic regression model)
    # or ‘isotonic’ which is a non-parametric approach.
    # It is not advised to use isotonic calibration with too few calibration samples (<<1000) since it tends to overfit.
    cv=3,   # or cv generator, "prefit" when `model` already fit (no cv then -- uses all data at once);
    n_jobs=1, # default; -1 = using all processors (sensible only for big tasks; for small tasks may actually take more time)
    ensemble=True,  # default -- valid only if NOT `cv="prefit"`
    # ! base_estimator -- depricated
)
modelc.fit(X, y)

modelc.predict_proba(X[:3, :])
# array([[0.11009913, 0.88990087],
#        [0.07226373, 0.92773627],
#        [0.92831861, 0.07168139]])

modelc  # CalibratedClassifierCV(cv=3, estimator=GaussianNB())
modelc.estimator.predict_proba(X[:3, :])
# ! NotFittedError: This GaussianNB instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.

dir(modelc)
modelc.base_estimator       # 'depricated'
modelc.calibrated_classifiers_
# [<sklearn.calibration._CalibratedClassifier at 0x7fbcbac7c4f0>,
#  <sklearn.calibration._CalibratedClassifier at 0x7fbcbac7e230>,
#  <sklearn.calibration._CalibratedClassifier at 0x7fbcbac7dc60>]
dir(modelc.calibrated_classifiers_[0])
# ..., 'calibrators', 'classes', 'estimator', 'method', 'predict_proba']
modelc.calibrated_classifiers_[0].estimator     # GaussianNB()
modelc.calibrated_classifiers_[0].calibrators   # [_SigmoidCalibration()]
modelc.calibrated_classifiers_[0].predict_proba(X[:3, :])
# array([[0.12630691, 0.87369309],
#        [0.12022896, 0.87977104],
#        [0.88154379, 0.11845621]])         prediction for 1st fold after calibration
modelc.calibrated_classifiers_[0].estimator.predict_proba(X[:3, :])
# array([[1.42005356e-02, 9.85799464e-01],
#        [1.30906229e-04, 9.99869094e-01],
#        [9.99997707e-01, 2.29309358e-06]]) prediction for 1st fold before calibration
modelc.calibrated_classifiers_[1].estimator.predict_proba(X[:3, :])
# array([[6.50821471e-02, 9.34917853e-01],
#        [3.98759417e-03, 9.96012406e-01],
#        [9.99837611e-01, 1.62388620e-04]])     "
# ...

# %% continue
dir(modelc)
modelc.classes_     # array([0, 1])
modelc.cv           # 3
modelc.ensemble     # True
modelc.estimator    # GaussianNB()
modelc.estimator.predict_proba(X[:3, :])
# ! NotFittedError: This GaussianNB instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.
modelc.get_metadata_routing()
# {'$self_request':
#    {'fit': {'sample_weight': None}, 'score': {'sample_weight': None}},
#     'estimator': {'mapping': [{'callee': 'fit', 'caller': 'fit'}],
#                   'router': {'fit': {'sample_weight': None},
#                              'partial_fit': {'classes': None, 'sample_weight': None},
#                              'score': {'sample_weight': None}
#                              }
#                  },
#     'splitter': {'mapping': [{'callee': 'split', 'caller': 'fit'}],
#                  'router': {}
#                 }
# }
modelc.get_params()
# {'base_estimator': 'deprecated',
#  'cv': 3,
#  'ensemble': True,
#  'estimator__priors': None,
#  'estimator__var_smoothing': 1e-09,
#  'estimator': GaussianNB(),
#  'method': 'sigmoid',
#  'n_jobs': -1}
modelc.method   # 'sigmoid'
modelc.n_features_in_   # 2
modelc.n_jobs           # -1
modelc.predict          # <bound method CalibratedClassifierCV.predict of CalibratedClassifierCV(cv=3, estimator=GaussianNB(), n_jobs=-1)>
modelc.predict_proba    # <bound method CalibratedClassifierCV.predict_proba of CalibratedClassifierCV(cv=3, estimator=GaussianNB(), n_jobs=-1)>
modelc.score            # <bound method ClassifierMixin.score of CalibratedClassifierCV(cv=3, estimator=GaussianNB(), n_jobs=-1)>
modelc.set_fit_request  # <function sklearn.utils._metadata_requests.RequestMethod.__get__.<locals>.func(self: sklearn.calibration.CalibratedClassifierCV, *, sample_weight: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.calibration.CalibratedClassifierCV>
modelc.set_params       # <bound method BaseEstimator.set_params of CalibratedClassifierCV(cv=3, estimator=GaussianNB(), n_jobs=-1)>
modelc.set_score_request    # <function sklearn.utils._metadata_requests.RequestMethod.__get__.<locals>.func(self: sklearn.calibration.CalibratedClassifierCV, *, sample_weight: Union[bool, NoneType, str] = '$UNCHANGED$') -> sklearn.calibration.CalibratedClassifierCV>

# %% calibrating model already fit -- `cv='prefit'`
"""
If “prefit” is passed, it is assumed that estimator has been fitted already and all data is used for calibration.
"""
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)
X_train, X_calib, y_train, y_calib = train_test_split(X, y, random_state=42)
model = GaussianNB()
model.fit(X_train, y_train)

# %% calibration on separate _calib data
calib = CalibratedClassifierCV(model, cv="prefit")
calib.fit(X_calib, y_calib)

model.predict_proba([[-0.5, 0.5]])     # array([[0.91931748, 0.08068252]])  # ! original estimator = non-calibrated
calib.predict_proba([[-0.5, 0.5]])     # array([[0.93677315, 0.06322685]])  # !!! OK  calibrated
calib.estimator.predict_proba([[-0.5, 0.5]])     # array([[0.91931748, 0.08068252]]) # ! original

calib.calibrated_classifiers_
# [<sklearn.calibration._CalibratedClassifier at 0x7fbcbac7ddb0>]
# `cv="prefit"` hence there's only one 'fold'

calib.calibrated_classifiers_[0].estimator.predict_proba([[-0.5, 0.5]])
# array([[0.91931748, 0.08068252]])         # ! original
calib.calibrated_classifiers_[0].predict_proba([[-0.5, 0.5]])
# array([[0.93677315, 0.06322685]])         # !!! OK  calibrated


# %% calibaration on original data
calib = CalibratedClassifierCV(model, cv="prefit")
calib.fit(X_train, y_train)

model.predict_proba([[-0.5, 0.5]])           # array([[0.91931748, 0.08068252]])  # ! original estimator = non-calibrated
calib.predict_proba([[-0.5, 0.5]])     # array([[0.93821812, 0.06178188]])  # !!! OK
calib.estimator.predict_proba([[-0.5, 0.5]])     # array([[0.91931748, 0.08068252]]) # ! original

calib.calibrated_classifiers_[0].estimator.predict_proba([[-0.5, 0.5]])
# array([[0.91931748, 0.08068252]])         # ! original
calib.calibrated_classifiers_[0].predict_proba([[-0.5, 0.5]])
# array([[0.93677315, 0.06322685]])         # !!! OK  calibrated
modelc.calibrated_classifiers_[0].calibrators   # [_SigmoidCalibration()]

# %%
# %% How it works with Pipelines ?



# %%