#! python3
# -*- coding: utf-8 -*-
"""
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview

title: Types of methods vs their first argument
subtitle: The meaning of `self` and `cls`.
version: 1.0
type: examples and explanations
keywords: [method, class, instance, `self`, `cls`, attribute,
           `@staticmethod`, `@classmethod`, 'normal' method, instance method]
description: |
    'self' and 'cls' are regarded as keywords but they are only conventions.
    There is quite a mess about what these pseudo-keywords really means
    and how to use them.
    The clue of the problem lies in how _the first_ argument of a method
    is interpreted according to the type of the method --
    is it a normal (instance) method, static-method or class-method.
    The experimentation below should dispell all the doubts.
    Pseudo-keywords are deliberately replaced with ordinary x, y
    in order to inforce the focus on the position of a variable instead of its name.
remarks:
    - This is not for fast reading - it should be meditated.
sources:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: self_static.py
    path: D:/ROBOCZY/Python/help/Objects/
    date: 2019-07-10
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
              - akasp666@google.com
"""

#%%
"""
Summary
-------

Interpretation of the first argument (in def) according to the type of the method:

                              called from:  instance | class
1. class-method (@classmethod)                 C     |   C
2. instance (normal) method (default)          I     |   x
3. static-method (@staticmethod)               x     |   x

C -- first argument in a method definition is treated as Class within which
     the method is defined;
I -- first argument in a method definition is treated as Instance from which
     the method is called;
x -- first argument in a method definition is free i.e. has no special meaning;
     this allows the method definition to have no arguments at all.

The table (and examples!) implies:
- Static methods are like ordinary functions and
  may be called both from class and instance and all their arguments are free
  thus such methods may be also defined without arguments;
  Static methods do not have direct access to class or instance attributes.
- Instance methods called from the class behaves like static methods;
  hence if the instance method is defined without arguments then it may be
  called from the class BUT called from instance will throw an error.
- Class methods definitions must always have at least the first argument
  which is always treated as a class object.

"""
#%%
class A(object):
    x = 33
    def __init__(x, y='3'):
        x.x = y
    def empty():
        return ('empty', A.x)
    def normal(x):
        return x
    def square(x):
        return x * x
    def __mul__(x, y):
        # x and y must be instances of a class
        return ((x.x, y.x), A.x)  # we always have access to class attr.
    def ret_x(x):
        return x.x
    def self_print(x):
        print('self-print')

    #! it is possible for instance method to give the first argument a default value!
    # this allows to use instance method in a static mode i.e. call them from class
    # with no need of passing a dummy argument;
    # default value is simply replaced with class instance when called from instance;
    def self_print_2(x=None):   #
        print('self-print')

    ## staticmethod ##
    # for static-methods all the arguments are always free
    # regardless of they are called from class or instance
    @staticmethod
    def static_meth(x):
        return x
    @staticmethod
    def empty_static():
        return ('empty_static', A.x)

    ## classmethod ##
    @classmethod
    def class_meth(x):
        return x         # == A
    @classmethod
    def class_meth_x(x):
        return x.x       # == A.x
    @classmethod
    def class_meth_x0():
        # this will not work! because class method needs the first argument
        # which is always substituted with the class object
        # regardless of it is called from class or instance
        return 42

#%%

a = A()
a.empty()    #! TypeError: .empty() takes 0 positional arguments but 1 was given
             # .empty() called from instance is treated as instance method
             # thus the instance is passed as the first argument but
             # there is no arguments in method definition...
A.empty()    # ('empty', 33)
             # -- thtat's OK because called from the class
             # a normal (instance) method is treated as a static method
             # -- all its arguments are free hence there may be no arguments.
             # notice that we stil have access to class attributes,
             # but there is no way of accessing instance attributes
             # -- for this one must call the method from the instance but then...
             # ... remember about the first argument!

A.normal(3)  #  here x in  def normal(x)  is treated as argument of a static method
A.normal()   #! TypeError: normal() missing 1 required positional argument: 'x'
a.normal(3)  #! here x in  def normal(x)  is treated as reference to class instance
a.normal()   #  returns instance
a.normal().x #  returns instance attribute x which is '3'

A.square(3)  #  here x in  def square(x)  is treated as argument of a static method
a.square(3)  #! here x in  def square(x)  is treated as reference to class instance
a.square()   #  so this works if only A * A is defined: A.__mul__(x, y)

a2 = A(2)
a * a2       # (('3', 2), 33)
a2 * a       # (('3', 2), 33)

#%%

a.self_print()  # self-print  # ok:  `x` treated as class instance
A.self_print()  #! TypeError: self_print() missing 1 required positional argument: 'x'
A.self_print(1) # self-print  # ok:  1 passed to `x` so it works
                # 1 is used as dummy value i.e. no meaning except muting Error

#%% it is possible in instance method to give the first argument a default value!
# it is replaced with class instance when called from instance
# but when called from class (like static method) this default value is used

a.self_print_2()  # self-print  # ok:  `x` treated as class instance
A.self_print_2()  # self-print  # ok: default None passed to `x` so it works


#%% staticmethod

A.static_meth(3)
a.static_meth(3)

A.empty_static()  # ('empty_static', 33)
a.empty_static()  # ('empty_static', 33)   -- compare with  a.empty()

#%%
a.ret_x()  # '3' - an instance attribute
A.ret_x()  # TypeError: ret_x() missing 1 required positional argument: 'x'
# but
A.ret_x(a) # '3' - an instance attribute

#%% classmethod

A.class_meth()  # returns a class object
A.class_meth().x  # 33 - a class attribute
a.class_meth()  # returns a class object
a.class_meth().x  # 33 - a class attribute

A.class_meth_x()  # returns A.x == 33
A.class_meth_x().x  # A.x.x ... no!: AttributeError: 'int' object has no attribute 'x'
a.class_meth_x()  # returns A.x == 33
a.class_meth_x().x   # doppelt gemoppelt!: AttributeError: 'int' object has no attribute 'x'

A.class_meth_x0()  #! TypeError: class_meth_x0() takes 0 positional arguments but 1 was given
a.class_meth_x0()  #! TypeError: class_meth_x0() takes 0 positional arguments but 1 was given



#%%

