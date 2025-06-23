#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: typing.SupportsFloat as type-hint for generic numerics
sources:
    - https://stackoverflow.com/questions/60616802/how-to-type-hint-a-generic-numeric-type-in-python
file:
    date: 2024-09-21
"""

from decimal import Decimal
from fractions import Fraction
from typing import SupportsFloat as Numeric

import numpy as np


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