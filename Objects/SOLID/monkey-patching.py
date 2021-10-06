# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 09:26:30 2021

@author: staar

Monkey Patching - ANTI-PATTERN !!!
Almost surely violates  Liskov Substitution Principle (one of SOLID)

https://medium.com/analytics-vidhya/monkey-patching-in-python-dc3b3f52906c
"""

#%%

class MonkeyPatch:

    def __init__(self, num):
        self.num = num

    def addition(self, other):
        return (self.num + other)

obj = MonkeyPatch(10)

obj.addition(20)

#%%
import inspect
dir(inspect)

inspect.getmembers(obj, predicate=inspect.ismethod)

#%%
def subtraction(self, num2):
    return self.num - num2

MonkeyPatch.subtraction = subtraction

#%%
inspect.getmembers(obj, predicate=inspect.ismethod)

#%%
obj.subtraction(1)           # 9  Working as expected

obj_1 = MonkeyPatch(10)      # create some new object
obj_1.subtraction(2)         # 8

#%%
"""
Things to keep in mind

The best thing is not to monkey patch.
You can define child classes for the ones you want to alter.
Still, if monkey patch needed then follow these rules -

    Use if you have a really good reason(like — temporary critical hotfix)

    Write proper documentation describing the reason for monkey patch

    Documentation should contain the information about the removal of the monkey patch and what to watch for.
    Lots of monkey patches are temporary, so they should be easy to remove.

    Try to make monkey patch as transparent as possible also place monkey patch code in separate files

"""
#%%