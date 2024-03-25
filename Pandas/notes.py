#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:10:52 2023

@author: arek
"""
# %%
import numpy as np
import pandas as pd
from utils.config import pandas_options
pandas_options()

# %% .groupby()
# %%
N = 99
df = pd.DataFrame(
    {
     'a': np.random.randint(0, 4, N),
     'b': np.random.randn(N),
     'c': np.random.choice(list('abcdef'), N),
     'd': np.random.choice(list('pqr'), N),
     'e': np.random.choice(range(6), N),
    },
    index = np.random.choice(range(N), N, replace=False)
)

# %%
df
df.reset_index()
df
df.groupby(['c', 'd']).max()

df.groupby(['c']).max().reset_index()
df.groupby(['c'], as_index=False).max()     # "

df.groupby(['c'], as_index=False).max().reset_index()   # no!

df.groupby(['c'], group_keys=False).max()
df.groupby(['c'], group_keys=True).max()    # the same  ???

df.reset_index().groupby(['c']).max()
df.reset_index().groupby(['c']).max().reset_index()


# %% multiindex
# %%
dfm = pd.concat({'p': df, 'q': df.reset_index()}, axis=1)

# all the same:
dfm['p', 'a'][:10]
dfm['p']['a'][:10]
dfm[('p', 'a')][:10]
dfm.p['a'][:10]
dfm.p.a[:10]

# %%
# %%
df.b.quantile(np.linspace(.1, .9, 9))
pd.qcut(df.b, np.linspace(.1, .9, 9)).value_counts()
pd.qcut(df.b, 10).value_counts()

qidx, quantiles = pd.qcut(df.b, 10, labels=range(10), retbins=True)
qidx
quantiles

for k, q in enumerate(quantiles):
    print(k, q)
    print(len(df.b[qidx==k]))


# %%
qidx, quantiles = pd.qcut(df.e, 10, labels=range(10), retbins=True)
# ! ValueError: Bin edges must be unique: array([0.1 , 0.1 , 0.1 , 0.2 , 0.3 , 0.3 , 0.36, 0.4 , 0.4 , 0.5 , 0.6 ]).
# You can drop duplicate edges by setting the 'duplicates' kwarg

Q = min(10, len(df.e.unique())-1)
qidx, quantiles = pd.qcut(df.e, Q, labels=range(Q-1), retbins=True, duplicates="drop")

qidx, quantiles = pd.qcut(df.e, Q, labels=range(Q), retbins=True, duplicates="drop")

#
qidx, quantiles = pd.qcut(df.e, Q, retbins=True, duplicates="drop")
qidx = pd.qcut(df.e, Q, duplicates="drop")
qidx.unique()
sorted(qidx.unique())
[q.mid for q in sorted(qidx.unique())]

for q in sorted(qidx.unique()):
    print(q)
    print(q.mid)
    print(len(df[qidx == q].e))
    print(np.mean(df[qidx == q].e))

dir(qidx[0])
qidx[0].mid
