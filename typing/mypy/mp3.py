#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:25:54 2024

@author: arek

https://stackoverflow.com/questions/75041623/how-to-check-that-a-string-is-a-string-literal-for-mypy
"""
# %%
from typing import cast, get_args, Literal

T = Literal['a', 'b']

get_args(T)     # tuple
list(get_args(T))
get_args(T)[0]


# %%
# https://docs.python.org/3/library/typing.html#typing.TypeGuard

from typing import TypeGuard

def isT(s: str) -> TypeGuard[T]:
    return s in get_args(T)

isT('a')
isT('c')

# %%
