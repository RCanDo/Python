#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:28:14 2024

@author: arek
"""
# %%
import pandas as pd

data = pd.DataFrame({'a': list('abc'), 'n': [2,4,6]})

for i, (j, v) in enumerate(zip([1,2], ['a', 'n'])):
    print(i)
    print(j)
    print(data.iloc[:, i])
    print(data[v])

# %%
variable = pd.Series(list ('abcbabcbdbdbcbdbabcbcdba'), name='abcd', dtype='category')
covariate = pd.Series(list('pqrprpqprprrqprqqprrqprr'), name='pqr')

labels = variable.cat.categories.to_list()

df0 = pd.concat([variable, covariate], axis=1)
df0g = df0.groupby([variable.name, covariate.name])
data: pd.DataFrame = df0g.agg(len).unstack(fill_value=0)     # !!!
data_cum = data.cumsum(axis=1)

# %%
import matplotlib as mpl
import matplotlib.pyplot as plt

x=pd.Series([1,2,3])
y=pd.Series([5,2,7])

plt.scatter(x, y, alpha=[.7, .6, .9])

# %%
fig, ax = plt.subplots(1,1)
ax.scatter(x, y, alpha=pd.Series([.7, .6, .9]))
ax.plot(y, x, color=mpl.colors.to_rgba((.5,.7,.3), .5), marker="*")

# %%