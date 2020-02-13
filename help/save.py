# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:15:41 2019

@author: kasprark
"""

#%%

import pickle

obj1 = {'a', 'b', 'c'}
obj2 = list(range(5))
fun1 = lambda x, y: x**y
obj3 = map(fun1, [2, 3], [5, 4])

with open('pickle_example.pobj', 'wb') as p:
    pickle.dump()
   
    ...
    
#%%    
#%%
import shelve

cd D:/ROBOCZY/Python/help
pwd

dir(shelve)
globals()
dir()

#%%
shelf = shelve.open('shelve1.data', 'n')

for k in ['obj1', 'obj2']:   
    # cannot save 'fun1' and 'obj3': Can't pickle <function <lambda> at 0x0000026C91D90730>: attribute lookup <lambda> on __main__ failed
    shelf[k] = globals()[k]
shelf.close()

#%%
# 

shelf = shelve.open('shelve1.data')

for k in shelf:
    globals()[k] = shelf[k]
shelf.close()

#%%

obj1
obj2

#%%


