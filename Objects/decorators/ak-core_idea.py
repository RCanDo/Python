# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:09:05 2021

@author: staar
"""
#%%
"""
Decorator is every function which modifies another function, i.e.
 - takes function f as argument
 - returns another function g which takes the same set of arguments as f
"""

#%% here is an absurd example which shows the technical core of a decorator

def obfuscator(f):

    def g(*args, **kwargs):

        result = f(*args, **kwargs)

        print("we're really don't bother about the result of f = {}".format(result))
        # we could completely ignore the result of `f`,
        # the core problem is to process the same set of arguments as `f` !

        lst = [*args]
        dic = {**kwargs}

        return lst, dic  # we always return the same

    return g

# Of course: this is only technical side of the problem.
# We use decorators to neatly modify result of f so we cannot ignore neither its result nor arguments.
#%%
import math

@obfuscator
def fun(x):
    return math.acos(x)

#%%
fun(1)
fun(44)     # ValueError: math domain error -- this indicates that some try ... except could be used.
fun(.333)
#%% obviously, decorator may be used a traditional way as ordinary functions

obfus_fun = obfuscator(math.log)
obfus_fun(8, 2)     # ([8, 2], {})

#%%
def super_fun(p, q, r, s):
    return p+q, r+s

obfus_super_fun = obfuscator(super_fun)
obfus_super_fun(1, 2, r=3, s=4)      # ([1, 2], {'r': 3, 's': 4})

#%%