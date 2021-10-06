#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Python Decorators
subtitle: Decorators with parameters
version: 1.0
type: tutorial
keywords: [decorators]
description: |
remarks:
todo:
sources:
    - title:
      chapter:
      link: https://stackoverflow.com/questions/5929107/decorators-with-parameters
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "decorators_with_parameters.py"
    path: "D:/ROBOCZY/Python/help/Objects/decorators/"
    date: 2019-11-25
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
pwd
cd D:/ROBOCZY/Python/help/Objects/decorators
ls

#%%
"""
The syntax for decorators with arguments is a bit different
- the decorator with arguments should return a function that will take a function
and return another function.
So it should really return a normal decorator.

Better:
Decorators with parameter(s) are created via outer function
having only this parameter(s) as an argument
and returning a proper decorator utilising this parameter internally
as from its closure.
Notice though that this parameter is not an argument of the proper decorator function
(is not in its arguments).
"""
def decorator_factory(parameter):

    def decorator(function):

        def wrapper(*args, **kwargs):
            funny_stuff()

            something_with_argument(parameter)          #!!! taken from closure

            result = function(*args, **kwargs)
            more_funny_stuff()
            return result

        return wrapper

    return decorator

#%%
from functools import wraps

def surround(start, end):
    """
    Decorator with arguments is a function which
    return  decorator!
    """

    def decor(fun):

        @wraps(fun)       # to preserve name, doc, help, etc.
        def wrapper(*args, **kwargs):

            print(start)        # par1

            result = fun(*args, **kwargs)
            print([*args], {**kwargs})

            print(end)          # par2

        return wrapper

    return decor

#%%
@surround("start", "end")
def f(p, q, r, s):
    """This is doc for `f` function.
    args:
        p, q, r, s
    result:
        p + q, r + s
    """
    return p+q, r+s

#%%
f(1, 2, r=3, s=4)
help(f)
f.__name__
dir(f)

#%%
#%%
