#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 09:48:46 2022

@author: arek
"""
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%

fig, ax = plt.subplots()

xx = np.arange(9)
yy = np.random.rand(9)
color = np.random.choice(list('rgb'), 9)
size = np.random.randint(2,5, 9) * 10

ax.scatter(xx, yy, color=color, s=size)

# %%
