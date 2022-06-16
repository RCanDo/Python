#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 10:19:29 2022

@author: arek
"""

from dataclasses import dataclass, field, fields, dafault_factory

#%%

@dataclass
class MyClass:
    a: int
    b = None

    def fun(self,
            a = self.a):
        pass


class MyClass:

    def __init__(self):
        a: int
        b = None

    def fun(self,
            a = self.a):
        pass
