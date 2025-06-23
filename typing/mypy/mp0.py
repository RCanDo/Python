#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: numpy.typing.NDArray[A] is an alias for numpy.ndarray[Any, numpy.dtype[A]]
sources:
    - https://stackoverflow.com/questions/66349242/specific-type-annotation-for-numpy-ndarray-using-mypy
file:
    date: 2024-09-19
"""

from typing import Any
import numpy as np


def f(a: np.ndarray[Any, np.dtype[np.floating]]) -> int:
    return len(a)

def g(a: np.typing.NDArray[np.floating]) -> int:
    return len(a)

f(np.array([1]))
f(np.array([1.]))
