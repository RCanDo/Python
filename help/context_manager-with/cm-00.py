#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: context manager
subtitle: minimal working example
version: 1.0
type: examples
keywords: [with, context manager]
description: |
    1. minimal working example.
    2. minimal sensible example
remarks:
todo:
sources:
    - link: https://stackoverflow.com/questions/28031210/best-way-to-roll-back-actions-when-an-exception-is-raised-with-python
    - link: https://stackoverflow.com/questions/4752356/changes-inside-try-except-persist-after-exception-is-caught
    - link: https://docs.python.org/3/library/stdtypes.html#typecontextmanager
      remark: read very carefully looking at the first example !!!
    - link: https://docs.python.org/3/reference/compound_stmts.html#with
    - link: https://docs.python.org/3/reference/datamodel.html#context-managers
    - link: https://pymotw.com/3/contextlib/index.html
      remark: there is dedicated file for this link
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    date: 2019-12-11
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
              - akasp666@google.com
"""

#%% A problem:
"""
try...exept...finally... has no ROLLBACK
i.e. some operation may fail in the middle but what has been executed is not undone.
This is not always problem however most often it is a problem!
Context managers (i.e. `with...` statements/expressions?) are solutions to this.
Some examples before:
"""

#%% example 1. try...except...finally...

s = 0
try:
    for k in list('12x4'):
        s += int(k)
        print(s)
except Exception as e:
    print(f"{e.__class__}: {e}")
    print(f'Cannot add "{k}".')
finally:
    print(s)

#! ValueError: invalid literal for int() with base 10: 'x'
# Notice that `s` changed its value - operation failed in the middle
# but there is no ROLLBACK!
# The context managers (`with ...`) makes it for us.

#%% example 2.
a = [0]
a.extend(int(k) for k in list('1234'))
a
# ok, no surprises
# by the way: compare it with .append(...)

#%% but for wrong data...
a = [0]
a.extend(int(k) for k in list('12x4'))  #! ValueError: invalid literal for int() with base 10: 'x'
a
# Oooops!!! operation failed in the middle but there is no ROLLBACK!
# state of `a` has changed!

#%% SOLUTION
#%% For this simple example we may use some functional prog.; sth. like this:

from functools import reduce

def add(a, b):
    return a + int(b)

s = 0
s = reduce(add, list('1234'), s)
s
# OK, no surprises
#%% now for wrong data:
s = 0
s = reduce(add, list('12x4'), s)
s   # didn't change, OK!


#%%
# GENERAL SOLUTION: CONTEXT MANAGER
#
#%% minimal working example

class Context(object):

    def __init__(self, s):
        self.sum = s

    def __enter__(self):
        """things to do when we enter the context"""
        return self  # this self is bound to `c` in  `with Context(x) as c: ...`

    """ methods needed for the context"""
    def add(self, k):
        self.sum += int(k)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """things to do when we exit the context"""
        # return False # exceptions revealed - in case of Exception
                      # - stops executing after exiting context
        return True   # exceptions supressed - in case of Exception
                      # - continues executing after exiting context

#! Read carefully: https://docs.python.org/3/library/stdtypes.html#typecontextmanager  !!!

#%% example 0.
s = 0
with Context(s) as c:
    for k in list('1234'):
        c.add(k)
    s = c.sum
    print(f's={s} within context')
print(f's={s} out of context')


#%% example 1.
# set `return False` in  .__exit__() method
s = 0
with Context(s) as c:
    for k in list('12x4'):
        c.add(k)
    s = c.sum
    print(f's={s} within context')
print(f's={s} out of context')

#! ValueError: invalid literal for int() with base 10: 'x'
s
# Notice that `s` did not changed i.e. `with` gives kind of a ROLLBACK
# in case of Exception. This is really good!!!
#
# Moreover: when .__exit__() return False then Exception is revealed and
# code after is not executed.

#%%
#%% example 2.
# now set `return True` in  .__exit__() method
s = 0
with Context(s) as c:
    for k in list('12x4'):
        c.add(k)
    s = c.sum
    print(f's={s} within context')
print(f's={s} out of context')

# The 'ValueError: ...' message was supressed - not only message!
# Execution goes on after exiting from 'with'.
# Moreover `s` did not changed i.e. `with` still gives kind of a ROLLBACK.

# Of course it's better to be informed that Error (Exception) occured.
# It needs some rewriting of our Context().

#%%
#%% minimal sensible example

class Context(object):

    def __init__(self, s):
        self.sum = s

    def __enter__(self):
        return self

    def add(self, k):
        self.sum += int(k)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'{exc_type}: {exc_val}')
        #return False # exceptions reveald - in case of Exception
                      # - stops executing after exiting context
        return True   # exceptions supressed - in case of Exception
                      # - continues executing after exiting context

#%%
s = 0

with Context(s) as c:
    for k in list('12x4'):
        c.add(k)
    s = c.sum
    print(f's={s} within context')
print(f's={s} out of context')

# now in case of Exception we now that it happens and
# we have initial value returned intact

#%% this example little more elegant

class Context(object):

    def __init__(self, s):
        self._sum = s

    def __enter__(self):
        return self

    def sum(self, seq):
        for k in list(seq):
            self._sum += int(k)
        return self._sum

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'{exc_type}: {exc_val}')
        return True

#%%
s = 0
with Context(s) as c:
    s = c.sum('1234')
s

#%%
s = 0
with Context(s) as c:
    s = c.sum('12x4')
s

#%%

