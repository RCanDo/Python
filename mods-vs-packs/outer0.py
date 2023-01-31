#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 10:41:02 2022

@author: arek
"""
from pack0 import mod_a

print("# ----- outer0 body ----- #")
mod_a.fun_a()
print(__package__, " outer0 ")
print(__name__, " outer0 ")

if __name__=="__main__":
    print("# ----- outer0 main ----- #")
    print(__package__, " outer0 ")
    print(__name__, " outer0 ")
