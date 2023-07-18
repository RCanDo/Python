#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:30:08 2023

https://docs.python.org/3/library/collections.abc.html
"""

from collections.abc import Sequence

# %%
class A(Sequence):
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = A(3, 5)     # TypeError: Can't instantiate abstract class A with abstract methods __getitem__, __len__


# %%