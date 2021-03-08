#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:35:48 2021

@author: arek
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os

PYWORKS = "E:/ROBOCZY/Python"
#PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/task0/")
print(os.getcwd())

# %%
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 500)
pd.set_option('display.max_seq_items', None)

#%%
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

pd.set_option('display.large_repr', 'truncate')

pd.set_option('display.precision', 3)

#%%

RANDSTATE = 11

data = pd.read_csv("recruitment_task.csv")
data.head()
data.shape    # 150000, 48
data.columns

data.info()
"""
Only first five columns are not 'sparse'
('sparse' in the meaning of having majority of NULLs)
"""

data.count()

#%%
target_var = "group"

"""
It's easy here to set the 'sparsity' threshold
"""
def variables_sparsity(df, threshold=.5):
    sparse_vars = df.apply(lambda col: col.isnull().sum() > df.shape[0] * threshold)
    sparse_vars = sparse_vars.index[sparse_vars].tolist()
    dense_vars = df.columns.difference(sparse_vars).tolist()
    return dense_vars, sparse_vars

dense_vars, sparse_vars = variables_sparsity(data.drop(target_var, axis=1))
print(dense_vars)
print(sparse_vars)

#%%
data.dtypes[dense_vars]
data.dtypes[sparse_vars]

#%%
data[dense_vars].count()

from sklearn.impute import SimpleImputer
data[dense_vars] = SimpleImputer(strategy="constant", fill_value="NA") \
    .fit_transform(data[dense_vars])

for n, c in data.iloc[:,0:3].iteritems():
    print(" {:s} :".format(n))
    print(c.value_counts())

data.memory_usage().sum() / 1e6   ## 57.6 MB

#%%
#%%
sdata = data[sparse_vars]

def no_nulls_in_row_distribution(df):
    df_rsum = df.notna().sum(axis=1)
    return pd.DataFrame(
                { "count": df_rsum.value_counts(),
                  "ratio": df_rsum.value_counts()/df.shape[0]
                }
            )

no_nulls_in_row_distribution(sdata)

#%%
(sdata < 0).sum(axis=0).sum()     # 0
(sdata == 0).sum(axis=0).sum()    # 0
(sdata > 0).sum(axis=0).sum()     # 150622

#%%
"""
## removing cases with two 'factor levels'
data2 = data1.loc[data_fsum==1,:]
data2.notna().sum(axis=1).value_counts()   ## OK
"""

#%%

X0 = data[dense_vars].copy()
X0['factor'] = sdata.apply(lambda r: r.index[r.notna()][0], axis=1)
X0['value'] = sdata.apply(lambda r: r[r.notna()][0], axis=1)
X0.head()

X0.memory_usage().sum() / 1e6   ## 7.2 MB

#%%
y0 = data[target_var]      ## pd.Series
y0.value_counts()

#%%
X1 = pd.concat([X0, y0], axis=1)
print(pd.pivot_table(X1, index="group", columns="f0", aggfunc=len, values="f1"))
pd.pivot_table(X1, index="f0", columns="group", aggfunc=len, values="f1").plot()


print(pd.pivot_table(X1, index="group", columns="f1", aggfunc=len, values="f0"))
pd.pivot_table(X1, index="f1", columns="group", aggfunc=len, values="f0").plot()


print(pd.pivot_table(X1, index="group", columns="factor", aggfunc=len, values="f0"))
pd.pivot_table(X1, index="factor", columns="group", aggfunc=len, values="f0").plot()

#%%
Xg = X0.groupby(y0)
Xg.head()
Xg.f0.value_counts()
Xg.f1.value_counts()
Xg.factor.value_counts()
Xg.boxplot()

#%%
#%% PLOTS
#%%%
plt.hist(y0)

#%%
fig, ax = plt.subplots(3, 1, figsize=(7, 9))
for i, var in enumerate(['f0', 'f1', 'factor']):
    xi = X0[var]
    ax[i].hist([xi[y0=="A"], xi[y0=="B"]], histtype="bar", density=True, label=["A", "B"])  #!
    ax[i].set_title(var)
    ax[i].legend()
fig.tight_layout()

#%%
 plt.bar(data.iloc[:, 1])

#%%
#import plotly.express as px

#%%
from scipy.stats import gaussian_kde

def plots(varname, Max=None, X=X1):
    variable = X[varname]

    if Max is None:
        title = varname
    else:
        title = "{:s} < {:d}".format(varname, Max)
        variable = variable[variable < Max]

    fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)
    ax0.hist(variable, bins=50)
    ax0.set_title("histogram")
    ax1.scatter(variable, range(len(variable)), s=.1)
    ax1.set_title("cloud")
    ax2.boxplot(variable, vert=False)
    ax2.set_title("boxplot")
    density = gaussian_kde(variable)
    xx = np.linspace(min(variable), max(variable), 1000)
    ax3.plot(xx, density(xx))
    ax3.set_title("density")

    fig.suptitle(title)
    fig.tight_layout()
    plt.show()

#%%

vname="f2"
plots(vname)
plots(vname, Max=100)

vname="f3"
plots(vname)
plots(vname, Max=1e4)

vname="value"
plots(vname)
plots(vname, Max=3e4)

Xg.boxplot()

## hence we see that data are heavily skewed

#%%

from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer()
X1 = X0.copy()
to_transform_vars = ['f2', 'f3', 'value']
X1[to_transform_vars] = pt.fit_transform(X1[to_transform_vars])
pt.lambdas_

vname="f2"
xi = X1[vname]
plots(xi, vname)

vname="f3"
xi = X1[vname]
plots(xi, vname)

vname="value"
xi = X1[vname]
plots(xi, vname)

X1.groupby(y0).boxplot()

#%%

def pairwise(v1, v2, X=X1):
    x1 = X[v1]
    x2 = X[v2]
    fig, ax = plt.subplots()
    B = ax.scatter(x1[y0=="B"], x2[y0=="B"], s=.1)
    A = ax.scatter(x1[y0=="A"], x2[y0=="A"], s=.1, alpha=.5)
    ax.set_xlabel(v1)
    ax.set_ylabel(v2)
    ax.legend([A, B], ["A", "B"])
    fig.suptitle("{:s} vs {:s}".format(v1, v2))
    fig.tight_layout()

pairwise('f2', 'f3')
pairwise('f2', 'value')
pairwise('f3', 'value')

#%%
##  END PLOTS
#%%


#%%
from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y0)
np.array(np.unique(y, return_counts=True))

type(y)                    ## np.ndarray ... WHY !!!

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X0, y, random_state=RANDSTATE)


#%%

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    [ ("pt", PowerTransformer(), ["f2", "f3", "value"]),
      ("oh", OneHotEncoder(), ["f0", "f1", "factor"])
    ],
    remainder="passthrough"
    )


#%%
    X = pd.get_dummies(X1, columns=['f0', 'f1', 'factor'])
    X.columns
    X.shape       # (150000, 60)

    X.memory_usage().sum() / 1e6   ## 12.15 MB



#%%
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, plot_confusion_matrix

#%%
dtc = DecisionTreeClassifier(random_state=RANDSTATE)

    #cross_val_score(dtc, X_tr, y_tr, cv=10)
    # plot_tree(model_tree) # too large to plot !

dtc.fit(X_tr, y_tr)
accuracy_score(dtc.predict(X_ts), y_ts)
confusion_matrix(dtc.predict(X_ts), y_ts)

#%%
pl_dtc = Pipeline([("transformer", ct), ("model", dtc)])

 pl_dtc.fit(X_tr, y_tr)

 accuracy_score(pl_dtc.predict(X_ts), y_ts)
 confusion_matrix(pl_dtc.predict(X_ts), y_ts)

##
parameters = {'model__criterion':['gini', 'entropy']}
grid = GridSearchCV(pl_dtc, parameters)
grid.fit(X_train, y_train)

grid.cv_results_
grid.best_estimator_
grid.best_params_
grid.best_score_
grid.best_index_

def GridSearchCV_results(grid):
    pd.DataFrame(
        {k: grid.cv_results_[k] for k in \
             ['params', 'mean_test_score', 'std_test_score', 'rank_test_score']}
        ).T
GridSearchCV_results(grid)

from sklearn.metrics import accuracy_score, confusion_matrix
accuracy_score(grid.predict(X_test), y_test)
confusion_matrix(grid.predict(X_test), y_test)

#%%
#%%
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(random_state=RANDSTATE)
rfc.fit(X_tr, y_tr)
accuracy_score(rfc.predict(X_ts), y_ts)
confusion_matrix(rfc.predict(X_ts), y_ts)

plot_confusion_matrix(rfc, X_ts, y_ts)

#%%
from sklearn.svm import LinearSVC

svc = LinearSVC(random_state=RANDSTATE)
svc.fit(X_tr, y_tr)
accuracy_score(svc.predict(X_ts), y_ts)
confusion_matrix(svc.predict(X_ts), y_ts)   ## oops...

#%%
from  sklearn.linear_model import LogisticRegression

lr = LogisticRegression(random_state=RANDSTATE)
lr.fit(X_tr, y_tr)
accuracy_score(lr.predict(X_ts), y_ts)
confusion_matrix(lr.predict(X_ts), y_ts)



#%%
#%%
from sklearn.datasets import load_iris
from sklearn import tree
X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

#%%
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

svc = svm.SVC()
grid = GridSearchCV(svc, parameters)
grid.fit(iris.data, iris.target)

grid.cv_results_
grid.best_estimator_
grid.best_score_
grid.best_index_

from sklearn.metrics import accuracy_score, confusion_matrix
accuracy_score(grid.predict(iris.data), iris.target)
confusion_matrix(grid.predict(iris.data), iris.target)


#%%

#%%



#%%



#%%

