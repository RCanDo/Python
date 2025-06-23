#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:55:00 2025

https://stackoverflow.com/questions/66783109/matplotlibs-legend-how-to-order-entries-by-row-first-rather-than-by-column

@author: arek
"""
# %%
from matplotlib.pyplot import subplots, show

f, ax = subplots(figsize=(6, 2), constrained_layout=True)
for i in range(1, 10):
    ax.plot((0,1),(0,1), label=str(i))
ax.legend(ncol=4, loc=3)
show()


# %%
reorder = lambda l, nc: sum((l[i::nc] for i in range(nc)), [])

f, ax = subplots(figsize=(6, 2), constrained_layout=True)
for i in range(1, 10):
    ax.plot((0,1),(0,1), label=str(i))
h, l = ax.get_legend_handles_labels()
ax.legend(reorder(h, 4), reorder(l, 4), ncol=4, loc=4)
show()


# %%
reorder(list(range(11)), 4)
