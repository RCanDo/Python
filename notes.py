#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 09:24:49 2023

@author: arek
"""
# %%
class A():
    qq=1

    def run(xxx, ryq=2):
        print(xxx.qq)
        return xxx.qq + ryq

# %%
a = A()
a
a.run()
a.run(3)

# %%
b = A(11)
b

# %%
import luigi

class A(luigi.Task):
    qq=luigi.Parameter()
    bb=luigi.BoolParameter()

    def run(xxx, ryq=2):
        print(xxx.qq)
        return xxx.qq + ryq

# %%
a = A(11)
a
a.qq
a.bb

# %%