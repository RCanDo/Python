# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:30:52 2019

@author: kasprark
"""
#%%
def fun(**kwargs):
    print(list(kwargs.keys()))
    print(kwargs.values())
    
#%%
fun(a='b', c=3)
fun(dict(a='b', c=3))


#%%