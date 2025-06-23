#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:36:50 2024

@author: arek
"""
# %%
import numpy as np
import pandas as pd

# %%
from decimal import Decimal
from fractions import Fraction
from typing import SupportsFloat as Numeric

isinstance(1, Numeric)
isinstance(1., Numeric)
isinstance(np.uintc(55), Numeric)
isinstance(Fraction(-3, 2), Numeric)
isinstance(Decimal("-3.14"), Numeric)
isinstance(np.array([1, 2, 3]), Numeric)
isinstance(complex(2, 3), Numeric)          # False

def f(x: Numeric) -> None:
    pass

# Accepted by mypy/Pyright:
f(123)
f(np.uintc(55))
f(Fraction(-3, 2))
f(Decimal("-3.14"))
f(np.array([1, 2, 3]))  # Should an array be numeric?

# Results in type errors:
f(complex(2, 3))
f("asdf")

# %%

NUMS = ["float", "float64", "int", "int64", "int32", "int16",
        "int8", "uint64", "uint32", "uint16", "uint8"]

ss = pd.Series(np.random.sample(9))
ss.dtype
ss.dtype in NUMS

# %%
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import PowerTransformer

isinstance(PowerTransformer, BaseEstimator)
issubclass(PowerTransformer, BaseEstimator)
isinstance(PowerTransformer, TransformerMixin)
issubclass(PowerTransformer, TransformerMixin)

# %%
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

list(plt.colormaps)

# custom colormap
default_cycler = [
    (0.0, '#17becf'),  # tab:cyan  (~teal)
    (0.1, '#2ca02c'),  # tab:green
    (0.2, '#7f7f7f'),  # tab:grey  (medium dark)
    (0.35, '#ff7f0e'),  # tab:orange
    (0.5, '#bcbd22'),  # tab:olive (green-yellow-grey)
    (0.65, '#d62728'),  # tab:red
    (0.75, '#9467bd'),  # tab:purple (violet)
    # '#8c564b',  # tab:brown   # too dark
    (0.85, '#e377c2'),  # tab:pink
    (1.0, '#1f77b4'), ]  # tab:blue

mpl.colormaps.register(LinearSegmentedColormap.from_list("ak01", default_cycler), name="ak01", force=True)

plt.colormaps['ak01'](np.linspace(0.1, 0.9, 9))     # np.ndarray([[R, G, B, alpha], ...])

# %%