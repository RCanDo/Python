#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: tempfile .md to .pdf example
type: tutorial
keywords: [temporary, file, diectory, markdown, pdf]
description: |
    Create temporary .md, transform into temp .pdf and then comy to final directory.
    Own example.
todo:
remarks:
sources:
    - title: tempfile — Temporary File System Objects
      link: https://pymotw.com/3/tempfile/index.html
      description: |
file:
    date: 2023-07-16
    authors:
        - email: akasp@int.pl
"""
# %%
import os
import tempfile
import pathlib

import numpy as np
import pandas as pd

# %%
df = pd.DataFrame(
    {"a": np.random.randint(0, 3, size=99),
     "b": np.random.sample(size=99),
     })
df
fig = df.plot()
type(fig)           # ! matplotlib.axes._axes.Axes
type(fig.figure)    # matplotlib.figure.Figure
fig.figure.savefig("qq.png")

# %%
with tempfile.NamedTemporaryFile() as f:
    print(f.name)
    fig.figure.savefig(f)
    os.listdir("/tmp")

os.listdir("/tmp")

# %%
with tempfile.TemporaryDirectory() as d:
    p = pathlib.Path(d)
    f0 = p / "fig0.png"
    fig.figure.savefig(f0)




# %%