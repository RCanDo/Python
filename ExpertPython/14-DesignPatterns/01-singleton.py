#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Singleton
subtitle:
version: 1.0
type: tutorial
keywords: [singleton, design pattern]
description: |
remarks:
todo:
sources:
    - title: Expert Python Programming
      chapter: 14 - Design Patterns
      pages: 468-
      link: d:/bib/Python/expertpythonprogramming.pdf
      date: 2016
      authors:
          - fullname: Michał Jaworski
          - fullname: Tarek Ziadé
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-singleton.py
    path: D:/ROBOCZY/Python/help/ExpertPython/14-DesignPatterns/
    date: 2019-12-12
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
"""
This pattern is considered by many developers as a heavy way to deal with
uniqueness in an application.

If a singleton is needed, why not use a module with functions instead,         !!!
since a Python module is already singleton?

The most common pattern is to define a module-level variable as an instance of a class
that needs to be singleton.
This way, you also don't constrain the developers to your initial design.

The singleton factory is an implicit way of dealing with the uniqueness of your application.
    You can live without it.                                                   !!!

Unless you are working in a framework à la Java that requires such a pattern,
use a module instead of a class.
"""

#%%
class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

#%%

a = Singleton()
b = Singleton()
id(a) == id(b)
a is b
a == b

#%%
"""
I call this a semi-idiom because it is a really dangerous pattern.
The problem starts when you try to subclass your base singleton class
and create an instance of this new subclass if you already created
an instance of the base class:
"""

class ConcreteClass(Singleton): pass

Singleton()
ConcreteClass()
# The same address!!!

"""
This may become even more problematic when you notice that this behavior is
affected by an instance creation order
"""
# del ConcreteClass
# del a, b
ConcreteClass()
Singleton()

""" ( maybe in older Pythons 3.5- )
"""

#%%
"""
It is a lot safer to use a more advanced technique — metaclasses.
By overriding the __call__() method of a metaclass,
you can affect the creation of your custom classes.
This allows creating a reusable singleton code:
"""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

#%%
class Single(metaclass=Singleton): pass

"""
By using this Singleton as a metaclass for your custom classes, you are able to get
singletons that are safe to subclass and independent of instance creation order:
"""

Single() == Single()  # True
a = Single()
b = Single()
a == b   # True
a is b   # True
id(a) == id(b)   # True

class SingleTwo(Single): pass

SingleTwo() == SingleTwo()   # True
SingleTwo() == Single()      # False    # that's rather OK

#%%
#%%
"""
Another way to overcome the problem of trivial singleton implementation is to use
what Alex Martelli proposed.
He came out with something similar in behavior to singleton
but completely different in structure.
This is not a classical design pattern coming from the GoF book,
but it seems to be common among Python developers.
It is called Borg or Monostate.

The idea is quite simple.
What really matters in the singleton pattern is not the number of living instances a class has,
but rather the fact that they all share the same state at all times.
So, Alex Martelli came up with a class that makes all instances of
the class share the same __dict__:
"""
class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls, *args, **kwargs)  # !!!
                                 # now you cannot pass any argument to __init__
        ob.__dict__ = cls._state
        return ob

    def __init__(self, x):
        self.x = x

b = Borg(1)  #! TypeError: object.__new__() takes exactly one argument (the type to instantiate)
# the same with subclass

class SubBorg(Borg):
    def __init__(self, x):
        self.x = x

sb = SubBorg(1)  #! TypeError: object.__new__() takes exactly one argument (the type to instantiate)


#%% remove  *args, **kwargs  from super().__new__(...)
# remember that super() means `object` which is super simple and object.__new__()
# accepts only `self` and no other argument, but
# when calling Borg(x=1) then `x` is first passed to Borg.__new__()
# which then passes it to object.__new__() which accepts only `self` argument...

class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super().__new__(cls)   # , *args, **kwargs)  # !!!
                                    # otherwise you cannot pass any argument to __init__
        ob.__dict__ = cls._state
        return ob

    def __init__(self, x):
        self.x = x

b = Borg(1)
c = Borg(2)
b.x
c.x

b.__dict__  # {'x': 2}
c.__dict__  # {'x': 2}

# nevertheless
b is c   # False
b == c   # False


#%%
#%%
"""
This fixes the subclassing issue but is still dependent on how the subclass code
works. For instance, if __getattr__ is overridden, the pattern can be broken.
Nevertheless, singletons should not have several levels of inheritance.
A class that is marked as a singleton is already specific.
"""