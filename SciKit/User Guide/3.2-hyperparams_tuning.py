#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Tuning the hyper-parameters
version: 1.0
type: sub-module
keywords: [cross validation, ...]
description: |
content:
remarks:
todo:
sources:
    - title: 3.2. Tuning the hyper-parameters of an estimator
      link: https://scikit-learn.org/stable/modules/grid_search.html
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
"""
Hyper-parameters are parameters that are not directly learnt within estimators.
In scikit-learn they are passed as arguments to the constructor of the estimator classes.
Typical examples include C, kernel and gamma for Support Vector Classifier, alpha for Lasso, etc.

It is possible and recommended to search the hyper-parameter space for  _the best cross validation score_.

Any parameter provided when constructing an estimator may be optimized in this manner.
Specifically, to find the names and current values for all parameters for a given estimator, use:
    estimator.get_params()

A search consists of:
1. an estimator (regressor or classifier such as sklearn.svm.SVC());
2. a parameter space;
3. a method for searching or sampling candidates;
4. a cross-validation scheme; and
5. a score function.

Two generic approaches to parameter search are provided in scikit-learn:
1. for given values,  GridSearchCV  exhaustively considers all parameter combinations,
2. while  RandomizedSearchCV  can sample a given number of candidates
   from a parameter space with a specified distribution.

Both these tools have successive halving counterparts  HalvingGridSearchCV  and  HalvingRandomSearchCV,
which can be much faster at finding a good parameter combination.

...
"""

# %% 3.2.1. Exhaustive Grid Search
"""
The grid search provided by  GridSearchCV  exhaustively generates candidates from a grid of parameter values
specified with the `param_grid` parameter, e.g.
"""
param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]
"""
specifies that two grids should be explored: ...

The GridSearchCV instance implements the usual estimator API:
when “fitting” it on a dataset all the possible combinations of parameter values are evaluated
!  and the best combination is retained.

Examples:
    ... (quite a lot - study them!)
"""

# %% 3.2.2. Randomized Parameter Optimization
"""
This has two main benefits over an exhaustive search:
RandomizedSearchCV  implements a randomized search over parameters, ...

1. A budget can be chosen independent of the number of parameters and possible values.
2. Adding parameters that do not influence the performance does not decrease efficiency.

...
Additionally, a computation budget, being the number of sampled candidates or sampling iterations,
is specified using the `n_iter` parameter.

For each parameter, either a distribution over possible values or a list of discrete choices
(which will be sampled uniformly) can be specified:
"""
{'C': scipy.stats.expon(scale=100), 'gamma': scipy.stats.expon(scale=.1),
  'kernel': ['rbf'], 'class_weight':['balanced', None]}
"""
This example uses the  scipy.stats  module, which contains many useful distributions for sampling parameters,
such as expon, gamma, uniform, loguniform or randint.
...
"""

# %%
"""
A continuous log-uniform random variable is the continuous version of a log-spaced parameter.
For example to specify the equivalent of C from above, loguniform(1, 100) can be used instead of [1, 10, 100].

Mirroring the example above in grid search, we can specify a continuous random variable
that is log-uniformly distributed between 1e0 and 1e3:
"""
from sklearn.utils.fixes import loguniform
{'C': loguniform(1e0, 1e3),
 'gamma': loguniform(1e-4, 1e-3),
 'kernel': ['rbf'],
 'class_weight':['balanced', None]}
"""
Examples:
Comparing randomized search and grid search for hyperparameter estimation
compares the usage and efficiency of randomized search and grid search.
"""

# %% 3.2.3. Searching for optimal parameters with successive halving
"""
Scikit-learn also provides the  HalvingGridSearchCV  and  HalvingRandomSearchCV  estimators
that can be used to search a parameter space using successive halving [1] [2].
Successive halving (SH) is like a tournament among candidate parameter combinations.
SH is an iterative selection process where all candidates (the parameter combinations)
are evaluated with a small amount of resources at the first iteration.
Only some of these candidates are selected for the next iteration, which will be allocated more resources.

For parameter tuning, the _resource_  is typically  the number of training samples,
but it can also be an arbitrary numeric parameter such as  n_estimators  in a random forest.

As illustrated in the figure below, only a subset of candidates ‘survive’ until the last iteration.
These are the candidates that have consistently ranked among the top-scoring candidates across all iterations.

Each iteration is allocated an increasing amount of resources per candidate, here the number of samples.
"""

# %%
...

# %% 3.2.3.6. Analyzing results with the  cv_results_  attribute
"""
The `cv_results_` attribute contains useful information for analyzing the results of a search.
It can be converted to a pandas dataframe with df = pd.DataFrame(est.cv_results_).

The `cv_results_` attribute of  HalvingGridSearchCV  and  HalvingRandomSearchCV
is similar to that of  GridSearchCV  and  RandomizedSearchCV,
with additional information related to the successive halving process.

pd.DataFrame(est.cv_results_)

Each row corresponds to a given parameter combination (a candidate) and a given iteration.
The iteration is given by the `iter` column.
The `n_resources` column tells you how many resources were used.
...
"""

# %% 3.2.4. Tips for parameter search

# %% 3.2.4.1. Specifying an objective metric
"""
By default, parameter search uses the score function of the estimator to evaluate a parameter setting.
These are the  sklearn.metrics.accuracy_score  for classification and
sklearn.metrics.r2_score  for regression.

For some applications, other scoring functions are better suited
! (for example in unbalanced classification, the accuracy score is often uninformative).

An alternative scoring function can be specified via the `scoring` parameter of most parameter search tools.
See 3.3.. The scoring parameter: defining model evaluation rules for more details.
"""

# %% 3.2.4.2. Specifying multiple metrics for evaluation
"""
GridSearchCV  and  RandomizedSearchCV  allow specifying multiple metrics for the scoring parameter.

Multimetric scoring can either be specified as a list of strings of predefined scores names
or a dict mapping the scorer name to the scorer function and/or the predefined scorer name(s).
See 3.3.1.4 Using multiple metric evaluation for more details.

When specifying multiple metrics,
!  the `refit` parameter must be set to the metric (string) for which the `best_params_` will be found
and used to build the `best_estimator_` on the whole dataset.

If the search should not be refit, set `refit=False`.
!  Leaving refit to the default value None will result in an error when using multiple metrics.

See Demonstration of multi-metric evaluation on  cross_val_score  and  GridSearchCV  for an example usage.

HalvingRandomSearchCV  and  HalvingGridSearchCV  do not support multimetric scoring.
"""

# %% 3.2.4.3. Composite estimators and parameter spaces
"""
GridSearchCV  and  RandomizedSearchCV  allow searching over parameters of  composite  or  nested  estimators
such as  Pipeline,  ColumnTransformer,  VotingClassifier  or  CalibratedClassifierCV
using a dedicated <estimator>__<parameter> syntax:
"""
from sklearn.model_selection import GridSearchCV
from sklearn.calibration import CalibratedClassifierCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons

X, y = make_moons()

calibrated_forest = CalibratedClassifierCV(
   estimator=RandomForestClassifier(n_estimators=10))

param_grid = {
   'estimator__max_depth': [2, 4, 6, 8]
}

search = GridSearchCV(calibrated_forest, param_grid, cv=5)
search.fit(X, y)

"""
Here, <estimator> is the parameter name of the nested estimator, in this case estimator.
If the meta-estimator is constructed as a collection of estimators as in pipeline.Pipeline,
then <estimator> refers to the name of the estimator, see Access to nested parameters.
In practice, there can be several levels of nesting:
"""

from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest

pipe = Pipeline([
   ('select', SelectKBest()),
   ('model', calibrated_forest)]
)

param_grid = {
   'select__k': [1, 2],
   'model__estimator__max_depth': [2, 4, 6, 8]}

search = GridSearchCV(pipe, param_grid, cv=5).fit(X, y)

# %% 3.2.4.4. Model selection: development and evaluation
"""
Model selection by evaluating various parameter settings can be seen
as a way to use the labeled data to “train” the parameters of the grid.

When evaluating the resulting model it is important to do it on held-out samples
that were not seen during the grid search process:
it is recommended to split the data into a development set (to be fed to the GridSearchCV instance)
and an evaluation set to compute performance metrics.

This can be done by using the  train_test_split  utility function,
!!!  which is only wrapper around   ShuffleSplit  !!!
and thus only allows for stratified splitting (using the class labels) and cannot account for groups
see 3.1
"""

# %% 3.2.4.5. Parallelism
"""
The parameter search tools evaluate each parameter combination on each data fold independently.
Computations can be run in parallel by using the keyword  `n_jobs=-1`.

See function signature for more details, and also the Glossary entry for `n_jobs`.
"""
# %% 3.2.4.6. Robustness to failure
"""
Some parameter settings may result in a failure to fit one or more folds of the data.
By default, this will cause the entire search to fail, even if some parameter settings could be fully evaluated.

Setting  `error_score=0` (or `=np.nan`) will make the procedure robust to such failure,
issuing a warning and setting the score for that fold to 0 (or nan), but completing the search.
"""

# %% 3.2.5. Alternatives to brute force parameter search

# %% 3.2.5.1. Model specific cross-validation
"""
Some models can fit data for a range of values of some parameter almost as efficiently
as fitting the estimator for a single value of the parameter.

This feature can be leveraged to perform a more efficient cross-validation used for model selection of this parameter.

The most common parameter amenable to this strategy is the parameter encoding the strength of the regularizer.

In this case we say that we _ compute the regularization path of the estimator _.

Here is the list of such models:

linear_model.ElasticNetCV(*[, l1_ratio, ...])   Elastic Net model with iterative fitting along a regularization path.
linear_model.LarsCV(*[, fit_intercept, ...])    Cross-validated Least Angle Regression model.
linear_model.LassoCV(*[, eps, n_alphas, ...])   Lasso linear model with iterative fitting along a regularization path.
linear_model.LassoLarsCV(*[, fit_intercept, ...])   Cross-validated Lasso, using the LARS algorithm.
linear_model.LogisticRegressionCV(*[, Cs, ...])	    Logistic Regression CV (aka logit, MaxEnt) classifier.
linear_model.MultiTaskElasticNetCV(*[, ...])    Multi-task L1/L2 ElasticNet with built-in cross-validation.
linear_model.MultiTaskLassoCV(*[, eps, ...])    Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer.
linear_model.OrthogonalMatchingPursuitCV(*)     Cross-validated Orthogonal Matching Pursuit model (OMP).
linear_model.RidgeCV([alphas, ...])             Ridge regression with built-in cross-validation.
linear_model.RidgeClassifierCV([alphas, ...])   Ridge classifier with built-in cross-validation.
"""

# %% 3.2.5.2. Information Criterion
"""
Some models can offer an  information-theoretic  closed-form formula of the optimal estimate
of the  regularization parameter  by computing a single  regularization path
(instead of several when using cross-validation).

Here is the list of models benefiting from the Akaike Information Criterion (AIC)
or the Bayesian Information Criterion (BIC) for automated model selection:

linear_model.LassoLarsIC([criterion, ...])  Lasso model fit with Lars using BIC or AIC for model selection.
"""

# %% 3.2.5.3. Out of Bag Estimates
"""
When using ensemble methods base upon  bagging,
!   i.e. generating new training sets using sampling with replacement,
part of the training set remains unused.
For each classifier in the ensemble, a different part of the training set is left out.

This left out portion can be used to estimate the  generalization error
without having to rely on a separate validation set.
This estimate comes “for free” as no additional data is needed and can be used for model selection.

This is currently implemented in the following classes:

ensemble.RandomForestClassifier([...])  A random forest classifier.
ensemble.RandomForestRegressor([...])   A random forest regressor.
ensemble.ExtraTreesClassifier([...])    An extra-trees classifier.
ensemble.ExtraTreesRegressor([n_estimators, ...])   An extra-trees regressor.
ensemble.GradientBoostingClassifier(*[, ...])       Gradient Boosting for classification.
ensemble.GradientBoostingRegressor(*[, ...])        Gradient Boosting for regression.
"""

# %%
