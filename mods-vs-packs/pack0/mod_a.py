#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 10:38:04 2022

@author: arek
"""
def fun_a():
    print("mod_a - fun_a")
    print(__package__, " mod_a - fun_a ")
    print(__name__, " mod_a - fun_a ")

if __name__=="__main__":
    print(__package__, " mod_a ")
    print(__name__, " mod_a ")
