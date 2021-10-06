# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:33:11 2021

https://www.toptal.com/python/python-design-patterns
"""
#%% Favor object composition over inheritance
"""
!!! Favor object composition over inheritance. !!!

Now, that’s what I call a Pythonic principle!

I have created fewer classes/subclasses compared to wrapping one class (or more often, several classes)
in another class.

Instead of doing this:
"""
class User(DbObject):
    pass

"""
We can do something like this:
"""
class User:
    _persist_methods = ['get', 'save', 'delete']

    def __init__(self, persister):
        self._persister = persister
            # !!! `persister` is an instance of a "parent" class
            # form which we want to "inherit" some methods mentioned in `_persist_methods`

    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)

"""
The advantages are obvious.
We can restrict what methods of the wrapped class to expose.       !!!
We can inject the persister instance in runtime!                   ???
For example, today it’s a relational database, but tomorrow it could be whatever,
with the interface we need (again those pesky ducks).

Composition is elegant and natural to Python.
"""
#%%
