#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Python Decorators
subtitle: Decorating functions with arguments; “Debuggable” Decorators
version: 1.0
type: tutorial
keywords: [functools.wraps, decorators]
description: |
remarks:
todo:
sources:
    - title:
      chapter:
      link: D:/bib/Python/the-power-of-python-decorators.pdf
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "power_of_decorators.py"
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

#%% decorating functions with arguments

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')
        return original_result
    return wrapper

#%%
@trace
def say(name, line):
    return f'{name}: {line}'

#%%
say('Marian', 'Ale jazz!')

#%% How to Write “Debuggable” Decorators
"""
When you use a decorator, really what you’re doing is replacing one
function with another. One downside of this process is that it “hides”
some of the metadata attached to the original (undecorated) function.
For example, the original function name, its docstring, and parameter
list are hidden by the wrapper closure:
"""

def uppercase(fun):
    def wrapper(*args, **kwargs):
        return fun(*args, **kwargs).upper()
    return wrapper

@uppercase
def hello(name):
    return f'hello {name}!'

#%%
hello('man')

#%%
def greet(name):
    """Return a friendly greeting."""
    return f'siema {name}!'

upper_greet = uppercase(greet)
upper_greet('man')

"""
If you try to access any of that function metadata, you’ll see the wrapper
closure’s metadata instead:
"""
dir(greet)
greet.__name__
help(greet)

dir(upper_greet)
upper_greet.__name__    # 'wrapper'
help(upper_greet)       # wrapper(*args, **kwargs)
#! Pity!

#%%
"""
This makes debugging and working with the Python interpreter
awkward and challenging. Thankfully there’s a quick fix for this: the
`functools.wraps` decorator included in Python’s standard library.4
You can use `functools.wraps` in your own decorators to copy over
the lost metadata from the undecorated function to the decorator closure.
Here’s an example:
"""

import functools

def uppercase(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        return fun(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name):
    """Return a friendly greeting."""
    return f'siema {name}!'

#%%
greet('stary')
dir(greet)
help(greet)
greet.__name__

#! BINGO!!!

#%%
#%%


#%%

