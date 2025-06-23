#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: returning self
file:
    date: 2024-09-21
"""
# %%
from __future__ import annotations
import numpy as np
# from typing import SupportsFloat as Num
from typing import Sequence, Callable, Optional

Numeric = np.typing.NDArray[np.floating]


class Center():
    def __init__(self) -> None:
        self.is_fit = False

    def fit(self, x: Numeric) -> None:
        self.mean = sum(x) / len(x)
        self.is_fit = True

    def transform(self, y: Numeric) -> Numeric:
        res = y - self.mean
        return res


def get_standardised(center: Center, name: str) -> Callable:

    def standardised(x: Numeric) -> tuple[Numeric, Callable]:
        if not center.is_fit:
            center.fit(x)
        transform = center.transform
        y = transform(x)
        return y, get_standardised(center, name)

    standardised.__name__ = name

    return standardised

# %%
x = np.arange(5)
x

center = Center()
transformation = get_standardised(center, 'std.center')
transformation.__name__

y, transformation = transformation(x)
y
