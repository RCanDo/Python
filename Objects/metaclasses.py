#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Mataclasses
subtitle:
version: 1.0
type: tutorial
keywords: [class decorator, __new__, __init__, super, subclass, superclass]
description: |
remarks:
    - Big problems at the end of the file!!!
todo:
sources:
    - title: Mataclasses
      link: https://realpython.com/python-metaclasses/
      usage: |
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


#%% new-style class (Python 3.)
class Foo: pass

obj = Foo()
obj.__class__  # __main__.Foo
type(obj)      # __main__.Foo

obj.__class__ is type(obj)  # True

#%%
n = 5
d = {'a':1, 'b':2}
x = Foo()

for obj in (n, d, x):
    print(type(obj) is obj.__class__)

# True

#%%
type(x)    # __main__.Foo
type(Foo)  # type

for t in int, float, dict, list, tuple:
    print(type(t))
# <class 'type'>

type(type)  # type
"""
- x is an instance of class Foo.
- Foo is an instance of the type metaclass.
- type is also an instance of the type metaclass, so it is an instance of itself.

"""

#%% Defining a Class Dynamically
#%%

type(3)          # int
type([1, 2, 4])  # list
type(Foo())      # __main__.Foo

#%%
"""
You can also call type() with three arguments:
    type(<name>, <bases>, <dct>):

<name> specifies the class name. This becomes the __name__ attribute of the class.
<bases> specifies a tuple of the base classes from which the class inherits.
    This becomes the __bases__ attribute of the class.
<dct> specifies a namespace dictionary containing definitions for the class body.
    This becomes the __dict__ attribute of the class.

Calling type() in this manner creates a new instance of the type metaclass.
In other words, it dynamically creates a new class.
"""


#%% Ex.1
Foo = type('Foo', (), {})
x = Foo()
x  # <__main__.Foo at 0x1f517796b08>

Foo.__dict__  # mappingproxy({'__module__': '__main__', ...
x.__dict__    # {}

#%%
class Foo(): pass
x = Foo()
x  # <__main__.Foo at 0x1f5177fb548>

Foo.__bases__  # (object,)

#%% Ex 1.1
Foo = type('Foo', (), dict(attr0=1))
x = Foo()
x

x.attr0    # 1
Foo.attr0  # 1

#%% Ex.2
Bar = type('Bar', (Foo,), dict(attr=100))
x = Bar()
x.attr
x.attr0

x.__class__  # __main__.Bar
x.__class__.__bases__  # (__main__.Foo,)
Bar.__bases__  # (__main__.Foo,)

#%% Ex.3
Spam = type('Spam', (), dict(attr=100, attr_val=lambda x: x.attr))
s = Spam()
s.attr
s.attr_val()

Spam.__dict__
"""
mappingproxy({'attr': 100,
              'attr_val': <function __main__.<lambda>(x)>,
              '__module__': '__main__',
              '__dict__': <attribute '__dict__' of 'Spam' objects>,
              '__weakref__': <attribute '__weakref__' of 'Spam' objects>,
              '__doc__': None})
"""

#%%
class Spam():
    attr = 100
    def attr_val(self):
        return self.attr

s = Spam()
s.attr
s.attr_val()

#%% Ex.4
def fun(obj):
    print(f'attr = {obj.attr}')

Spam = type('Spam', (), {'attr': 100, 'attr_val': fun})

s = Spam()
s.attr
s.attr_val()

#%% Custom Metaclasses
#%%

class Spam(): pass

s = Spam()
s    # <__main__.Spam at 0x1f517a0ff08>

super(type(Spam))   # <super: type, None
super(type(s))      # <super: __main__.Spam, None>
#%%

class Spam():
    def __new__(cls):
        print(type(super(cls)))

Spam()  # <class 'super'>


#%%
"""
The expression Spam() creates a new instance of class Spam.
When the interpreter encounters Spam(), the following occurs:
- The __call__() method of Spam’s parent class is called.
   Since Spam is a standard new-style class,
   its parent class is the `type` metaclass, so `type`’s __call__() method is invoked.
- That __call__() method in turn invokes the following:
        __new__()
        __init__()
If Spam does not define __new__() and __init__(),
default methods are inherited from Spam’s ancestry.
But if Spam does define these methods, they override those from the ancestry,
which allows for customized behavior when instantiating Spam.

In the following, a custom method called new() is defined
and assigned as the __new__() method for Spam:
"""
#%%
def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x

Spam.__new__ = new

s = Spam()
s.attr      # 100

r = Spam()
r.attr      # attr

"""
(Code like this would more usually appear in the __init__() method
and not typically in __new__().
This example is contrived for demonstration purposes.)
"""
#%%
# Spoiler alert:  This doesn't work!
def new(cls):
    x = type.__new__(cls)
    x.attr = 100
    return x

type.__new__ = new
#! TypeError: can't set attributes of built-in/extension type 'type'
"""
metaclass `type` cannot be modified! that's good!
"""

#%%
#   HOW TO CUSTOMIZE INSTANTIATION OF A CLASS ???
#
#%%
class Meta(type):
    def __new__(cls, name, bases, dct):
        obj = super().__new__(cls, name, bases, dct)
        obj.attr = 100
        return obj

type(Meta)   # type

#%%
A = type('A', (Meta,), {'z':10})
A
A.attr  # AttributeError: type object 'A' has no attribute 'attr'
A.__bases__   # (__main__.Meta,)
A.z   # 10

#%%
"""
The definition header class Meta(type): specifies that Meta derives from `type`.
Since `type` is a metaclass, that makes Meta a metaclass as well.

Note that a custom __new__() method has been defined for Meta.
It wasn’t possible to do that to the `type` metaclass directly.
The __new__() method does the following:
- Delegates via super() to the __new__() method of the parent metaclass (type)
  to actually create a new class
- Assigns the custom attribute attr to the class, with a value of 100
- Returns the newly created class

Now the other half of the voodoo:
Define a new class Spam and specify that its metaclass is the custom metaclass Meta,
rather than the standard metaclass type.
This is done using the metaclass keyword in the class definition as follows:
"""

#%%
class Spam(metaclass=Meta): pass
Spam.attr  # 100

Spam.__bases__   # (object,)
# hence Spam does not inherit from any class, but
type(Spam)  # __main__.Meta
# compare it with
type(Foo)   # type
# !!! ???
type(Spam())  # __main__.Spam
type(Foo())   # __main__.Foo
"""
In the same way that a class functions as a template for the creation of objects,
a metaclass functions as a template for the creation of classes.
Metaclasses are sometimes referred to as class factories.
"""
#%% Object Factory:
class Foo():
    def __init__(self):
        self.attr = 100

x = Foo()
x.attr

y = Foo()
y.attr

type(Foo)   # type
type(x)     # __main__.Foo

#%% Class Factory
class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100

class Spam(metaclass=Meta): pass

Spam.attr
s = Spam()
s.attr

type(Spam)    # __main__.Meta
type(Spam())  # __main__.Spam

class Egg(metaclass=Meta): pass

Egg.attr
e = Egg()
e.attr

Egg.__bases__   # (object,)

#%%
#%% Class decorator

def decor(cls):
    class NewClass(cls):
        attr = 100
    return NewClass

@decor
class A: pass

A.attr

#%%

class B: pass
dir(B)

#%%

#%%
#  cannot pass argument to metaclass...
#
#%%
"""
define a metaclass
"""
class DoubleX(type):
    def __new__(cls, name, bases, dct, x):
        print("DoubleX.__new__")
        obj = super().__new__(cls, name, bases, dct)
        obj.x = 2 * x
        return obj

#%%
class A(metaclass=DoubleX):
    def __init__(self, x):
        print("A.__init__")

#! TypeError: __new__() missing 1 required positional argument: 'x'
#%%
a = A(2)
a.x
#%%

