# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 18:19:56 2021

@author: staar
"""
#%%
def something(x=[]):
        x.append(1)
        print (x)

something() # [1]
something() # [1, 1]
something() # [1, 1, 1]

#%%
def something(x = None):
    if x is None:
        x = []
    x.append(1)
    print (x)

something()  # [1]
something()  # [1]

#%%