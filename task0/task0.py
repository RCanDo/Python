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

#PYWORKS = "E:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/task0/")
print(os.getcwd())

# %%
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 500)
pd.set_option('display.max_seq_items', None)

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
data[dense_vars] = SimpleImputer(strategy="constant", fill_value="NA").fit_transform(data[dense_vars])

for n, c in data.iloc[:,0:3].iteritems(): print(" {:s} :".format(n)); print(c.value_counts())

data.memory_usage().sum() / 1e6   ## 57.6 MB



#%%
#%%
sdata = data[sparse_vars]
sdata_fsum = sdata.notna().sum(axis=1)
sdata_fsum.value_counts()
sdata_fsum.value_counts()/sdata.shape[0]

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
y0 = data[target_var]
y0.value_counts()

from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y0)
np.array(np.unique(y, return_counts=True))


#%%
#%% plots
plt.hist(y0)

x0 = X0.iloc[:, 0]
plt.hist(x0)

plt.hist([x0[group=="A"], x0[group=="B"]], histtype="bar")

 plt.bar(data.iloc[:, 1])

#%%
gdata = data.groupby('group')
gdc1 = gdata.f1.value_counts()
gdc1[("A")]
gdc1[("B")]

plt.hist([gdc1[("A")], gdc1[("B")]], histtype='bar')

#%%
#import plotly.express as px

#%%
x2 = data.iloc[:, 2]
plt.hist(x2[x2.notna()])

#%%
from scipy.stats import gaussian_kde

def plots(variable):
    print(len(variable))
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
    fig.tight_layout()
    plt.show()


x2 = X0.f2
plots(x2)
plots(x2[x2<100])

x3 = X0.f3
plots(x3)
plots(x3[x3<1e4])

val = X0.value
plots(val)
plots(val[val<3e4])

from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer()
X1 = X0.copy()
to_transform_vars = ['f2', 'f3', 'value']
X1[to_transform_vars] = pt.fit_transform(X1[to_transform_vars])
pt.lambdas_

x2 = X1.f2
plots(x2)

x3 = X1.f3
plots(x3)

val = X1.value
plots(val)

## END PLOTS
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
from sklearn.model_selection import train_test_split

X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, random_state=RANDSTATE)

#%%
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, plot_confusion_matrix

#%%
dtc = DecisionTreeClassifier(random_state=RANDSTATE)
cross_val_score(dtc, X_tr, y_tr, cv=10)

# plot_tree(model_tree) # too large to plot !

dtc.fit(X_tr, y_tr)
accuracy_score(dtc.predict(X_ts), y_ts)
confusion_matrix(dtc.predict(X_ts), y_ts)

#%%
pl = Pipeline([("transformer", ct), ("model", dtc)])

pl.fit(X_tr, y_tr)

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

