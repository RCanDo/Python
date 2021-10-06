#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Practical Decorators
subtitle:
version: 1.0
type: examples
keywords: [decorators]
description: |
remarks:
todo:
sources:
    - title: Practical Decorators
      link: https://www.youtube.com/watch?v=MjHpMCIvwsY&feature=youtu.be
      authors:
          - fullname: Reuven M. Lerner
            email: reuven@lerner.co.il
      date: 2019
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "practical_decorators.py"
    path: "D:/ROBOCZY/Python/help/Objects/decorators/"
    date: 2019-12-18
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
              - akasp666@google.com
"""
#%%
cd D:/ROBOCZY/Python/help/Objects/decorators/

#%%
"""
`def name(...):` creates object (function) and assigns it to `name`
"""
#%% pattern:

# instead of
def add(a, b):
    return a + b

add = mydeco(add)
# where `add` is written 3 times

# we may write:
@mydeco
def add(a, b):
    return a + b
# where `add` is written only once

#%%
# three callables (sth. to execute = function or class):

@mydeco            # 2. decorator
def add(a, b):     # 1. decorated function
    return a + b
                   # 3. the returned value from mydeco(add) assigned back to `add`

#%% defining a decorator
def mydeco(func):  # 2. (1.)
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)}!!!'
    return wrapper  # 3.


#%% another perspective (in terms of time)
def mydeco(func):  # executes once, when we decorate function
    def wrapper(*args, **kwargs):    # executes each time the decorated function runs
        return f'{func(*args, **kwargs)}!!!'
    return wrapper

"""
https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/
legb - local enclosed global buit-in
"""

#%% Examples

#%% 1. logging run-time
import time

def logtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        time_info = f'{time.time()}\t{func.__name__}\t{end - start}\n'
        print(time_info)
        with open('timelog.txt', 'a') as outfile:
            outfile.write(time_info)
        return result
    return wrapper

@logtime
def slow_add(a, b):
    time.sleep(1)
    return a + b

@logtime
def slow_mul(a, b):
    time.sleep(1)
    return a * b

#%%
slow_add(1351341, 722409809)

slow_mul(1351341, 722409809)

#%% 2. once per minute
# raise an exception if we try to run a function more then twice in 60 secs
#! we need `nonlocal` !

class WaitAMinute(Exception): pass

def once_per_minute(func):
    last_invoked = 0

    def wrapper(*args, **kwargs):

        nonlocal last_invoked  # = look for it in the enclosing scope

        elapsed_time = time.time() - last_invoked
        if elapsed_time < 60:
            raise WaitAMinute(f'Only {elapsed_time} has passed')

        last_invoked = time.time()
        return func(*args, **kwargs)

    return wrapper

@once_per_minute
def my_add(a, b):
    return a + b

#%%
my_add(1, 2)
my_add(1, 2) # WaitAMinute: Only 1.055835485458374 has passed
my_add(1, 2) # WaitAMinute: Only 15.562716960906982 has passed
# wait a minute
my_add(1, 2)


#%% 3. once per n
# raise an exception if we try to run a function more then twice in n minutes
# We need decorators with arguments !!!

@once_per_n(5)
def add(a, b):
    return a + b

# equivalent to
def add(a, b):
    return a + b
add = once_per_n(5)(add)

# we've got 5 callables now:
def add(a, b):           # 1. the decorated function
    return a + b

add                      # 4. the return value from `once_per_n(5)(add)` assigned back to `add`
    = once_per_n         # 2. the decorator
      once_per_n(5)      # 3. the return value from `once_per_n(5)(add)` is itself a callable
                   (add) #    invoked on add

#%%
"""
Decorators with parameter are created via outer function
having only this parameter as an argument
and returning a proper decorator utilising this parameter internally
as from its closure.
"""

class WaitFewMinutes(Exception): pass

def once_per_n(n):

    def decor(func):
        last_invoked = 0

        def wrapper(*args, **kwargs):
            nonlocal last_invoked
            elapsed_time = time.time() - last_invoked

            if elapsed_time < n:          #! parameter
                raise WaitFewMinutes(f'One must wait {n} seconds before running {func.__name__} the second time.')
            last_invoked = time.time()

            return func(*args, **kwargs)

        return wrapper

    return decor

@once_per_n(10)
def slow_add(a, b):
    return a + b

#%%
slow_add(1341351, 4524987028)
slow_add(1341351, 4524987028) # WaitFewMinutes: One must wait 10 seconds before running slow_add the second time.
slow_add(1341351, 4524987028)


#%% 4. Memoization
# cache the result of function calls, so we don't need to call them again

#!!! this is implemented by  functools.lru_cache  (also decorator)  !!!

def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        nonlocal cache   # not needed here as we do not assign to variable but to cache[.] !!! ???
        if args not in cache:
            print(f'Caching NEW value for {func.__name__}({args})')
            cache[args] = func(*args, **kwargs)
        else:
            print(f'Using OLD value for {func.__name__}({args})')
        return cache[args]

    return wrapper

@memoize
def super_power(a):
    if a > 7:
        print('too much!')
        return None
    else:
        return a ** (a ** a)

#%%
super_power(1)
super_power(3)
super_power(3)
super_power(5)
super_power(6)
super_power(7)
super_power(7)
len(str(super_power(7)))

#%% 5. repeating attributes/methods across classes (which are also callables!)
# without resorting to (multiple) inheritance
# e.g.

def fancy_repr(self):
    return f"I'm a {self.__class__}, with vars {vars(self)}"

#%%
def better_repr(cls):
    cls.__repr__ = fancy_repr
    def wrapper(*args, **kwargs):
        return cls(*args, *kwargs)
    return wrapper

#%% wrapper is doing nothing so it can be done simpler
def better_repr(cls):
    cls.__repr__ = fancy_repr
    return cls

@better_repr
class Spam():
    def __init__(self, x, y):
        self.x = x
        self.y = y

sp = Spam(10, [1, 2, 3])
print(sp)

#%% 6. give each object its birthday
import time

def object_birthday(cls):
    def wrapper(*args, **kwargs):
        obj = cls(*args, **kwargs)
        obj._created_at = time.time()
        return obj
    return wrapper

@object_birthday
@better_repr
class Spam():
    def __init__(self, x, y):
        self.x = x
        self.y = y

sp = Spam(10, [1, 2, 3])
print(sp)
vars(sp)

#%% of course we may merge both decors into one:
def object_birthday(cls):
    cls.__repr__ = fancy_repr
    def wrapper(*args, **kwargs):
        obj = cls(*args, **kwargs)
        obj._created_at = time.time()
        return obj
    return wrapper

@object_birthday
class Spam():
    def __init__(self, x, y):
        self.x = x
        self.y = y

sp = Spam(10, [1, 2, 3])
print(sp)
vars(sp)

#%%


#%%


#%%


#%%


#%%
