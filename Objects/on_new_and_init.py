#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Understanding __new__ and __init__
subtitle:
version: 1.0
type: tutorial
keywords: [__new__, __init__, super, subclass, superclass]
description: |
remarks:
todo:
sources:
    - title: Understanding __new__ and __init__
      link: https://spyhce.com/blog/understanding-new-and-init
      authors:
          - fullname: Andrei-George Hondrari
      usage: |
    - link: E:/ROBOCZY/Python/help/ExpertPython/14-DesignPatterns/01-singleton.py
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: on_new_and_init.py
    path: D:/ROBOCZY/Python/help/Objects/
    date: 2019-12-15
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%% old-style class has no __new__() method
class A:
    def __new__(cls):
        print("A.__new__ is called")  # -> this is never called in old-style class
A()

#%%
class A:
    def __init__(self):
        print("A.__init__ called")
A()

#%% cannot return from __init__:
class A:
    def __init__(self):
        return 29
A() # TypeError: __init__() should return None, not 'int'

#%%
class A(object):

    def __new__(cls):
        print("A.__new__ called")
        return super(A, cls).__new__(cls)
               # this is passed directly to __init__ as `self`

    def __init__(self):
        self.a = "I'm an A!"
        print("A.__init__ called")

a = A()
# A.__new__ called
# A.__init__ called
dir(a)
vars(a)

#%%
"""
__new__ is called automatically when calling the class name (when instantiating),
whereas __init__ is called every time an instance of the class is returned
by __new__ passing the returned instance to __init__ as the 'self' parameter,
.
therefore even if you were to save the instance somewhere globally/statically
and return it every time from __new__, then __init__ will be called every time
you do just that.

Knowing this it means that if we were not returning from __new__
then __init__ won't be executed. Let's see if that's the case:
"""
#%%
class A(object):

    def __new__(cls):
        print("A.__new__ called")

    def __init__(self):
        print("A.__init__ called")  # -> is actually never called

#%%
A()
a = A()
a
type(a)  # NoneType ...

print(A())
# A.__new__ called
# None

#%%
"""
Obviously the instantiation is evaluated to None since we don't return anything
from the constructor.
Wondering what might happen if we were to return something from __new__?
"""
class A(object):

    def __new__(cls):
        print("A.__new__ called")
        return 42

#%%
a =  A()
print(a)  # 42
type(a)   # int !!
"""
We didn't call super() (which is `object`) hence we returned just 42:
our new class is just an integer, and always 42!
"""
type(A)  # type

"""
more on this little later
"""

#%%
#%%
class Sample(object):
    def __str__(self):
        return "SAMPLE"

print(Sample)   # <class '__main__.Sample'>
print(Sample()) # SAMPLE

#%%
class A(object):
    def __new__(cls):
        return Sample()

A()  # <__main__.Sample at 0x1b9cb8fe888>
print(A())  # SAMPLE

#%% equiv.

class A(object):
    def __new__(cls):
        return super(A, cls).__new__(Sample)
        #return object.__new__(Sample)      # works too !

A()  # <__main__.Sample at 0x1b9cb8fe888>
print(A())  # SAMPLE

A.__bases__   # (object,)

a = A()
print(a)

type(a)   # __main__.Sample
a.__class__  # __main__.Sample


#%%
#%% return to experiments on __new__ and __init__
#
#%% when not calling  super().__new__()
# hence __new__ does not return `object` and __init__ is not run
class A(object):

    def __new__(cls, x):
        print("A.__new__")
        return 3 * x       # just number not object !


    def __init__(self, x):
        # will not be run because __new__ does not return `object` ...
        print("A.__init__")
        self.x = x + 1

a = A(2)  # A.__new__
          # while A.__init__() is not called!
a  # 6
print(a)  # 6
type(a)  # int

a.x  # AttributeError: 'int' object has no attribute 'x'

#%% calling  super().__new__()  to return `object`
class A(object):

    def __new__(cls, x):
        print("A.__new__")
        obj = super().__new__(cls)
        obj.x = 3 * x
        return obj

    def __init__(self, x):
        print("A.__init__")

a = A(2)
# A.__new__
# A.__init__
a  # <__main__.A at 0x1b9cb8c3508>
type(a)  # __main__.A
a.x  # 6
vars(a)

#%% __init__(x) overwrites __new__(x)
class A(object):

    def __new__(cls, x):
        print("A.__new__")
        obj = super().__new__(cls)
        obj.x = 3 * x
        return obj

    def __init__(self, x):
        print("A.__init__")
        self.x = x - 1

a = A(2)
a.x  # 1

#%% but it is enough to rename arguments
class A(object):

    def __new__(cls, x):
        print("A.__new__")
        obj = super().__new__(cls)
        obj.x = 3 * x
        return obj

    def __init__(self, y):
        print("A.__init__")
        self.y = y - 1

a = A(2)
a.x  # 6
a.y  # 1
vars(a)

#%% be carefull though not to use one variable twice

class A(object):

    def __new__(cls, x):
        print("A.__new__")
        obj = super().__new__(cls)
        obj.x = 3 * x
        return obj

    def __init__(self, y):
        print("A.__init__")
        self.x += y

a = A(2)
a.x  # 8 !!! = 3 * 2 + 2

#%% what about two variables

class A(object):

    def __new__(cls, x, y):
        print("A.__new__")
        obj = super().__new__(cls)
        obj.x = 3 * x
        return obj

    def __init__(self, x, y):
        print("A.__init__")
        self.x += y

a = A(2, 3)
a.x  # 9 !!! = 3 * 2 + 3

#%%