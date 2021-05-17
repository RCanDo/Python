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
    - This is not a fast read - it should be meditated.
sources:
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: self_static.py
    path: ./help/Objects/
    date: 2019-07-10
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - akasp666@google.com
"""

#%%
"""
Summary
-------

Interpretation of the first argument (in def) according to the type of the method:

                              called from:    instance | class
1. class-method (`@classmethod`)                 C     |   C
2. instance (normal) method (default)            I     |   x
3. static-method (`@staticmethod`)               x     |   x

C -- first argument in a method definition is treated as Class within which
     the method is defined;
I -- first argument in a method definition is treated as Instance from which
     the method is called;
x -- first argument in a method definition is free i.e. has no special meaning;
     this allows the method definition to have no arguments at all.

The table (and examples!) implies:
- Static methods are like ordinary functions and
  may be called both from class and instance and all their arguments are free
  thus such methods may be also defined without arguments.
  Because of this, static methods do not have direct access to attributes
  of any instance nor class, where 'direct access' means
  'through the first argument' (usually `self` or `cls` pseudo-keywords).
  See (*).
- Instance methods called from the class behaves like static methods;
  hence if the instance method is defined without arguments then it may be
  called from the class BUT called from instance will throw an error unless
  we provide some dummy value for the first arg or provide a default value for it
  in a definition of a method. See (1) & (2).
- Class methods definitions must always have at least the first argument
  which is always treated as a class object.

(*) After all, 'standard' access to class attributes is always possible
  from within any function or method, simply by  `Class.attribute`  call.

Moreover:

(1)
For any normal (instance) method
    Class_instance.normal_method(...)
is equivalent to
    Class.normal_method(Class_instance, ...)
Also
    Class.normal_method(Class, ...)
will simply work as class-method.
Remember though, that the first argument (usally pseudo-keyword `self`)
which in above examples is substituted with class or instance
is utilised within a finction definition always the same way.
It means that code writted to use instance will rarely be sensible
for using a class.
The sensible scenario is to define normal method without using the first arg.
But this is equivalent to static method what is more readable.

(2)
It is possible for instance method to give the first argument a default value!
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
    def ret_x(x):  # (1)
        return x.x
    def square(x):
        return x * x
    def __mul__(x, y):
        # x and y must be instances of a class
        return ((x.x, y.x), A.x)  # we always have access to class attr.
    def self_print(x):
        print('self-print')

    # (2)
    # It is possible for instance method to give the first argument a default value!
    # This allows to use instance method in a static mode i.e. call them from class
    # with no need of passing a dummy argument;
    # default value is simply replaced with class instance when called from instance;
    def self_print_2(x=None):   #
        print('self-print')
    # also, in this scenario each consequtive arg must be provided default value
    def static_defined_as_normal(x=None, y=None, z=None):
        # do not use x at all
        return y, z  # or any processing of y, z, ...

    ## staticmethod ##
    # for static-methods all the arguments are always free
    # regardless of they are called from class or instance
    @staticmethod
    def static_meth(x):
        return x
    @staticmethod
    def static_meth_x(x):
        return x.x
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
    def class_meth_0():
        # this will not work! because class method needs the first argument
        # which is always substituted with the class object
        # regardless of it is called from class or instance
        return 42

#%%

A
A.x
a = A()
a
a.x

a.empty()    #! TypeError: .empty() takes 0 positional arguments but 1 was given
             # .empty() called from instance is treated as instance method
             # thus the instance is passed as the first argument but
             # there are no arguments in method definition...
A.empty()    # ('empty', 33)
             # -- that's OK because called from the class
             # a normal (instance) method is treated as a static method
             # -- all its arguments are free hence there may be no arguments.
             # notice that we stil have access to class attributes
             # (simply via name of a class),
             # but there is no way of accessing instance attributes
             # -- for this one must call the method from the instance but then...
             # ... remember about the first argument!

A.normal(3)  #  here x in  def normal(x)  is treated as argument of a static method
A.normal()   #! TypeError: normal() missing 1 required positional argument: 'x'
a.normal(3)  #! TypeError: normal() takes 1 positional argument but 2 were given
             #  here x in  def normal(x)  is treated as reference to class instance
a.normal()   #  returns instance
a.normal().x #  returns instance attribute x which is '3'

#%%
a.ret_x()  # '3' - an instance attribute
A.ret_x()  # TypeError: ret_x() missing 1 required positional argument: 'x'
           # normal method called from class is treted as static method i.e.
           # it's first argument is free (is not substituted with class object)
           # hence must be provided some value - see (2).
# but
A.ret_x(a) # '3' - an instance attribute
A.ret_x(A) # 33  - a class attribute

""" (1)
!!! Hence for any normal (instance) method
    Class_instance.method(...)
is equivalent to
    Class.method(Class_instance, ...)
Also
    Class.method(Class, ...)
will simply work as class-method - but only if the first argument is used
in the function body in a meaningful way (like in example).
"""

#%%
A.square(3)  #  here x in  def square(x)  is treated as argument of a static method
a.square(3)  #! TypeError: square() takes 1 positional argument but 2 were given
             #  here x in  def square(x)  is treated as reference to class instance
a.square()   #  so this works if only A * A is defined: A.__mul__(x, y)

a2 = A(2)
a * a2       # (('3', 2), 33)
a2 * a       # (('3', 2), 33)

#%%

a.self_print()  # self-print  # ok:  `x` treated as class instance
A.self_print()  #! TypeError: self_print() missing 1 required positional argument: 'x'
A.self_print(1) # self-print  # ok:  1 passed to `x` so it works
                # 1 is used as dummy value i.e. no meaning except muting Error

""" (2)
It is possible in instance method to give the first argument a default value!
It is replaced with class instance when called from instance
but when called from class (like static method) this default value is used.
"""

a.self_print_2()  # self-print  # ok:  `x` treated as class instance
A.self_print_2()  # self-print  # ok: default None passed to `x` so it works

# from instance
a.static_defined_as_normal(2, 3)   # (2, 3); it is equivalent to
a.static_defined_as_normal(y=2, z=3)

# from class
A.static_defined_as_normal(2, 3)   #!!! (3, None); it is equivalent to
A.static_defined_as_normal(x=2, y=3)
# hence in this mode one must remember to call args explicitely
A.static_defined_as_normal(y=2, z=3)

"""!!!
Hence it's possible but cumbersome and noisy.
Do better use  `@staticmethod`  explicitely!
"""

#%% staticmethod

A.static_meth()   #! TypeError: static_meth() missing 1 required positional argument: 'x'
                  #  this is static method with one argument - so it must be provided;
                  #  Is it called from class or instance - doesn't matter.
A.static_meth(4)
a.static_meth(4)

A.static_meth_x() #! TypeError: static_meth_x() missing 1 required positional argument: 'x'
a.static_meth_x() #! TypeError: static_meth_x() missing 1 required positional argument: 'x'

A.static_meth_x(3) #! AttributeError: 'int' object has no attribute 'x'
A.static_meth_x(a) #! '3'
A.static_meth_x(A) #! 33
a.static_meth_x(3) #! AttributeError: 'int' object has no attribute 'x'
a.static_meth_x(a) #! '3'
a.static_meth_x(A) #! 33

A.empty_static()  # ('empty_static', 33)
a.empty_static()  # ('empty_static', 33)   -- compare with  a.empty()
"""
So it is possible to access class attributes within static method
but not 'directly' i.e. via the first argument (usually pseudo-keyword `cls`)
but simply by calling `Class.attribute` as from within any other finction or method
or when you pass a class as first arg...
The same for instance attribute.
"""


#%% classmethod

A.class_meth()  # returns a class object
A.class_meth().x  # 33 - a class attribute
a.class_meth()  # returns a class object
a.class_meth().x  # 33 - a class attribute

A.class_meth_x()  # returns A.x == 33
A.class_meth_x().x  # A.x.x ... no!: AttributeError: 'int' object has no attribute 'x'
a.class_meth_x()  # returns A.x == 33   NOT a.x !!!
a.class_meth_x().x   # a.x.x ... doppelt gemoppelt!: AttributeError: 'int' object has no attribute 'x'

A.class_meth_0()  #! TypeError: class_meth_0() takes 0 positional arguments but 1 was given
a.class_meth_0()  #! TypeError: class_meth_0() takes 0 positional arguments but 1 was given


#%%
