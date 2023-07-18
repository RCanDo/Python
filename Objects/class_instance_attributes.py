#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 12:31:21 2023

@author: arek
"""
# %%
class A():
    a = 1
    b = 2
    def __init__(self, a):
        self.a = a
        self.c = 3 * self.a
        self.d = 3 * A.a
        self.e = 3 * self.b     # takes A.b instead

a = A(-1)


# %%
A.a     # 1
a.a     # -1

A.b     # 2
a.b     # 2    there is no  self.b !!!

a.c     # -3
A.c     # AttributeError: type object 'A' has no attribute 'c'

a.d     # 3
a.e     # 6


# %%
from collections import defaultdict
dd = defaultdict(lambda: False)
dd['a']=2
dd['b']=3
dd[None]
dd[None]=1
