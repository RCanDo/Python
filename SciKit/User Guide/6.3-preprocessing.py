#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Preprocessing data
version: 1.0
keywords: [preprocessing, variables, ...]
description: |
content:
remarks:
todo:
sources:
    - title: 6.3. Preprocessing data
      link: https://scikit-learn.org/stable/modules/preprocessing.html
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

# %%
"""
The sklearn.preprocessing package provides several common utility functions and transformer classes
to change raw feature vectors into a representation that is more suitable for the  downstream estimators.

In general, many learning algorithms such as linear models benefit from standardization of the data set
(see Importance of Feature Scaling).
If some outliers are present in the set,
robust scalers or other transformers can be more appropriate.

The behaviors of the different scalers, transformers, and normalizers on a dataset
containing marginal outliers is highlighted in  Compare the effect of different scalers on data with outliers.
"""

# %% 6.3.1. Standardization, or mean removal and variance scaling
"""
Standardization of datasets is a common requirement for many machine learning estimators implemented in scikit-learn;
they might behave badly if the individual features do not more or less look like standard normally distributed data:
    Gaussian with zero mean and unit variance.

In practice we often ignore the shape of the distribution and just transform the data to center it
by removing the mean value of each feature, then scale it by dividing non-constant features by their standard deviation.

For instance, many elements used in the objective function of a learning algorithm
(such as the RBF kernel of Support Vector Machines or the l1 and l2 regularizers of linear models)
may assume that all features are centered around zero or have variance in the same order.
If a feature has a variance that is orders of magnitude larger than others,
it might dominate the objective function and make the estimator unable to learn from other features correctly as expected.

The preprocessing module provides the  StandardScaler  utility class,
which is a quick and easy way to perform the following operation on an array-like dataset:
"""
from sklearn import preprocessing
X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])
scaler = preprocessing.StandardScaler().fit(X_train)
scaler

scaler.mean_

scaler.scale_

X_scaled = scaler.transform(X_train)
X_scaled

# %%
...


# %% 6.3.4. Encoding categorical features
"""
Often features are not given as continuous values but categorical. For example a person could have features ["male", "female"], ["from Europe", "from US", "from Asia"], ["uses Firefox", "uses Chrome", "uses Safari", "uses Internet Explorer"]. Such features can be efficiently coded as integers, for instance ["male", "from US", "uses Internet Explorer"] could be expressed as [0, 1, 3] while ["female", "from Asia", "uses Chrome"] would be [1, 2, 1].

To convert categorical features to such integer codes, we can use the OrdinalEncoder. This estimator transforms each categorical feature to one new feature of integers (0 to n_categories - 1):
"""
...

# %% 6.3.4.2. Target Encoder
"""
The TargetEncoder uses the target mean conditioned on the categorical feature for encoding unordered categories,
i.e. nominal categories [PAR] [MIC].
This encoding scheme is useful with categorical features with high cardinality,
where one-hot encoding would inflate the feature space making it more expensive for a downstream model to process.
A classical example of high cardinality categories are location based such as zip code or region.
For the binary classification target, the target encoding is given by:
    S_i = l_i (n_i_Y / n_i) + (1 - l_i) (n_Y / n)  ==  l_i E(Y|i) + (1 - l_i) EY
where S_i is the encoding for category i,
n_i_Y is the number of observations with Y = 1 and category i,
n_i is the number of observations with category i,
n_Y is the number of all observations with Y = 1,
n is the number of all observations,
and l_i is a shrinkage factor for category i
    l_i = n_i / (m + n_i)
where is a smoothing factor, which is controlled with the smooth parameter in TargetEncoder.
Large smoothing factors will put more weight on the global mean.
When smooth="auto", the smoothing factor is computed as an empirical Bayes estimate:
    m = s_i^2 / s^2
where s_i^2 is the variance of y with category i and s^2 is the global variance of y.

For continuous targets, the formulation is similar to binary classification:
    S_i = l_i E(Y|i) + (1 - l_i) EY.

!!!   `.fit_transform()` internally relies on a  _cross fitting_  scheme
to prevent target information from leaking into the train-time representation,
especially for non-informative high-cardinality categorical variables,
and help prevent the downstream model from overfitting spurious correlations.
???

!!!   Note that as a result, `.fit(X, y).transform(X)` does not equal `.fit_transform(X, y)`.
In `.fit_transform`, the training data is split into k folds (determined by the `cv` parameter)
and each fold is encoded using the encodings learnt using the other k-1 folds.
The following diagram shows the  cross fitting  scheme in `.fit_transform` with the default cv=5:

| fold 1 | train  | train  | train  | train  |                  | fold 1 |
| train  | fold 2 | train  | train  | train  |                  | fold 2 |
| train  | train  | fold 3 | train  | train  |   -- combine ->  | fold 3 |
| train  | train  | train  | fold 4 | train  |       folds      | fold 4 |
| train  | train  | train  | train  | fold 5 |                  | fold 5 |

`.fit_transform` also learns a ‘full data’ encoding using the whole training set.
This is never used in `.fit_transform` but is saved to the attribute `encodings_`,
for use when `.transform` is called.
Note that the encodings learned for each fold during the cross fitting scheme are not saved to an attribute.

!!!   The `.fit` method does not use any  cross fitting  schemes and learns one encoding on the entire training set,
which is used to encode categories in transform.
!   This encoding is _the same_ as the ‘full data’ encoding learned in `.fit_transform`.

Note
TargetEncoder  considers missing values, such as np.nan or None,
as another category and encodes them like any other category.
Categories that are not seen during fit are encoded with the target mean, i.e. `.target_mean_`.

Examples:
    Comparing Target Encoder with Other Encoders    !
    Target Encoder’s Internal Cross fitting         !

References
[MIC] Micci-Barreca, Daniele.
“A preprocessing scheme for high-cardinality categorical attributes in classification and prediction problems”
SIGKDD Explor. Newsl. 3, 1 (July 2001), 27–32.
[PAR] Pargent, F., Pfisterer, F., Thomas, J. et al.
“Regularized target encoding outperforms traditional methods in supervised machine learning with high cardinality features”
Comput Stat 37, 2671–2692 (2022)
"""