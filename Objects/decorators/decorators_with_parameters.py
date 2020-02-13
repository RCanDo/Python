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
A bit confusing, right? What I mean is:
"""
def decorator_factory(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            funny_stuff()
            something_with_argument(argument)
            result = function(*args, **kwargs)
            more_funny_stuff()
            return result
        return wrapper
    return decorator

#%%



#%%


