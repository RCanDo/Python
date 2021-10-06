# -*- coding: utf-8 -*-
"""
title: Decorators
author: kasprark
date: Fri Jan 19 10:57:02 2018
"""

%reset

pwd
cd D:/ROBOCZY/Python/help/Objects/decorators
ls

#%% solo learn
#%%
def printx(): print("Uozaaa!")

printx()

def decor( fun ):  ## returns function
    def wrap():
        print('========')
        fun()
        print('========')
    return wrap

decorated = decor(printx)
decorated()

#%%

@decor
def printx():
    print("Uozaaa!")

printx()


#%%  https://realpython.com/blog/python/primer-on-python-decorators/
#%%
def foo(bar):
    return bar + 1

print(foo(2) == 3)

## In Python, functions are first-class objects. This means that functions can be passed around,
## and used as arguments, just like any other value (e.g, string, int, float).

print(foo)
print(foo(2))
print(type(foo))

def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))

#%%
## Nested Functions
## Because of the first-class nature of functions in Python, you can define functions inside other functions.
## Such functions are called nested functions.

def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())

parent()

#%%
## Returning Functions
## Python also allows you to return functions from other functions.
# Let’s alter the previous function for this example.

def parent(num):

    def if_ten():
        return "10 passed"

    def if_not_ten():
        return "10 NOT passed"

    try:
        assert num == 10
        return if_ten
    except AssertionError:
        return if_not_ten


foo = parent(10)
bar = parent(11)

foo
bar

foo()
bar()

#%%
## Decorators
## Let’s look at two examples …

def my_decorator(some_function):

    def wrapper(*args, **kwargs):
        print("Something is happening before some_function() is called.")
        some_function(*args, **kwargs)
        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)

just_some_function()

#%%

def my_decorator(some_function):

    def wrapper():
        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")
        some_function()
        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")

just_some_function = my_decorator(just_some_function)

just_some_function()

#%%
from decorator07 import my_decorator

@my_decorator
def just_some_function():
    print("Wheee!")

just_some_function()

#%%
## Real World Examples

import time

def timing_function(some_function):
    """ Outputs the time a function takes to execute.
    """
    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str(sum(num_list)))


print(my_function())

#%%

from time import sleep

def sleep_decorator(function):
    """Limits how fast the function is called.
    """
    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper

@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))

#%%
'''
One of the most used decorators in Python is the login_required() decorator,
which ensures that a user is logged in/properly authenticated
before s/he can access a specific route (/secret, in this case):
'''
from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass

#%%

