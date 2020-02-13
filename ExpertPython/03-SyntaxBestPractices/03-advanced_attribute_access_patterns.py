#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Advanced attribute access patterns
subtitle:
version: 1.0
type: tutorial
keywords: [slots, descriptor, property, lazy property, super, subclass, superclass]
description: |
remarks:
todo:
sources:
    - title: Expert Python Programming
      chapter: 03 - Syntax Best Practices
      pages: 91-
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
    name: 03-advanced_attribute_access_patterns.py
    path: D:/ROBOCZY/Python/help/ExpertPython/03-SyntaxBestPractices/
    date: 2019-12-16
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%% Data Descriptors
"""
The descriptor classes are based on three special methods that form the
_descriptor protocol_:
• __set__(self, obj, value): This is called whenever the attribute is
set. In the following examples, we will refer to this as a setter.
• __get__(self, obj, type=None): This is called whenever the attribute is read
(referred to as a getter).
• __delete__(self, obj): This is called when del is invoked on the
attribute.
A descriptor that implements __get__() and __set__() is called a _data descriptor_.
If it just implements __get__(), then it is called a _non-data descriptor_.
"""
#%%
class RevealAccess(object):
    """A data descriptor that sets and returns values
    normally and prints a message logging their access.
    """
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name
    def __get__(self, obj, cls):
        print('Retrieving', self.name)
        return self.val
    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val
    def __delete__(self, obj):
        print('Deleting', self.name)
        self.val = None                # how to delete ???

class MyClass(object):
    # static use
    x = RevealAccess(10, 'var "x"')   # a class attribute
    y = 5

#%%
MyClass.x      # 10
m = MyClass()
m.x            # 10

type(m.x)   # int !!!
dir(m.x)    # no __get__, __set__
m.x.name    #! AttributeError: 'int' object has no attribute 'name'

m.x += 10
m.x         # 20
MyClass.x   # 20    !!!

del m.x    # None

m.__dict__ # {}   # ???
MyClass.__dict__  # !!!

MyClass.x
type(MyClass.x)  # int
MyClass.x = 1

#%% it doesn't work in a non-static version
class MyClass(object):
    def __init__(self, y=5):
        self.x = RevealAccess(10, 'var "x"')
        self.y = y

#%%
m = MyClass()
m
dir(m)
m.x   # <__main__.RevealAccess at 0x1b9cb9e36c8>
m.y
m.x = 2
m.x   # 2

#%%
"""
The difference between data and non-data descriptors is important due to the fact
stated at the beginning. Python already uses the descriptor protocol to bind class
functions to instances as a methods. They also power the mechanism behind the
classmethod and staticmethod decorators. This is because, in fact, the function
objects are non-data descriptors too:
"""
def function(): pass
hasattr(function, '__get__') # True
hasattr(function, '__set__') # False
# And this is also true for functions created with lambda expressions:
hasattr(lambda: None, '__get__') # True
hasattr(lambda: None, '__set__') # False


#%%
#   lazily evaluated attributes
#
#%%
class InitOnAccess:
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            self._initialized = self.klass(*self.args, **self.kwargs)
            print('initialized!')
        else:
            print('cached!')
        return self._initialized

class MyClass:
    """hop sa sa"
    """
    lazily_initialized = InitOnAccess(list, "argument")
    __doc__ = """qq ryq"""

    def __init__(self, x=1):
        self.x = x

#%%
dir(MyClass)
MyClass.lazily_initialized

m = MyClass()
m
dir(m)
m.lazily_initialized
m.lazily_initialized
dir(m.lazily_initialized)
type(m.lazily_initialized)   # list

m.__dict__  # {'x': 1}
MyClass.__dict__   # !!!
MyClass.__doc__   # !!!

#%%
ion = InitOnAccess(list, "argument")
ion
ion._initialized
ion()   #! TypeError: 'InitOnAccess' object is not callable


#%%
#%%
"""
The official OpenGL Python library available on PyPI under the PyOpenGL name
uses a similar technique to implement lazy_property that is both a decorator and
a data descriptor:
"""
class lazy_property(object):
    def __init__(self, func):
        self.fget = func
    def __get__(self, obj, cls):
        value = self.fget(obj)
        setattr(obj, self.fget.__name__, value)   # what for ???
        return value

#? How to use it?
#? As decorator???

#%% usage
def middle(obj):
    return (max(obj.lst) + min(obj.lst)) / 2

class MyList(object):
    mid = lazy_property(middle)
    def __init__(self, lst = [0, 1, 3, 7]):
        self.lst = lst

#%%
ml = MyList()
dir(ml)

ml.lst
ml.mid
dir(ml)
ml.middle

#%% usage as decorator -- better
class MyList(object):
    def __init__(self, lst = [0, 1, 3, 7]):
        self.lst = lst

    @lazy_property
    def middle(self):
        return (max(self.lst) + min(self.lst)) / 2

#%%
dir(MyList)
MyList.middle  # AttributeError: 'NoneType' object has no attribute 'lst'
               # no instance yet

ml = MyList()
dir(ml)

ml.lst
ml.middle
dir(ml)
ml.lst.append(8)
ml.middle        # didn't change !!! so it is called only once !!!

#%%  extending built-in
#%%
def middle(lst):
    return (max(lst) + min(lst)) / 2

class MyList(list):
    mid = lazy_property(middle)
    def __init__(self, x):
        super().__init__(x)


#%%
MyList.mid   #! TypeError: 'NoneType' object is not iterable
             # no instance yet
ml = MyList([1, 2])
ml
ml.mid
ml.middle
ml.append(4)
ml.mid
ml.middle        # didn't change !!! so it is called only once !!!
dir(ml)

#%% with decorator -- better

class MyList(list):
    def __init__(self, *args):
        super().__init__(args)

    @lazy_property
    def middle(self):
        return (max(self) + min(self)) / 2

#%%
MyList.middle   #! TypeError: 'NoneType' object is not iterable
                # no instance yet

ml = MyList(1, 2, 4)
ml
ml.middle
ml.append(7)
ml.middle        # didn't change !!! so it is called only once !!!

#%%
#   Properties
#
#%%
"""
The properties provide a built-in descriptor type that knows
how to link an attribute to a set of methods.
prop = property(fget, fset, fdel, doc)
`doc` can be provided to define a docstring that is linked to the
attribute as if it were a method.
"""

class Rectangle(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    def _width_get(self):
        return self.x2 - self.x1

    def _width_set(self, val):
        self.x2 = self.x1 + val

    def _height_get(self):
        return self.y2 - self.y1

    def _height_set(self, val):
        self.y2 = self.y1 + val

    width = property(_width_get, _width_set,
                     doc = """rectangle width measured from left""")

    height = property(_height_get, _height_set,
                     doc = """rectangle height measured from top""")

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.x1}, {self.y1}, {self.x2}, {self.y2})'

#%%
rec = Rectangle(1, 1, 3, 4)
rec # Rectangle (1, 1, 3, 4)
help(rec)
help(Rectangle)

rec.width
rec.height
rec.x2
rec.width = 5
rec.x2

rec.__weakref__
rec.__dict__

#%%
"""
however due to issue with subclassing it is better to use decorators:
@property, @prop.setter
"""

class Rectangle(object):

    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2

    @property
    def width(self):
        """rectangle width measured from left"""
        return self.x2 - self.x1

    @width.setter
    def width(self, val):
        self.x2 = self.x1 + val

    @property
    def height(self):
        """rectangle height measured from top"""
        return self.y2 - self.y1

    @height.setter
    def height(self, val):
        self.y2 = self.y1 + val

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.x1}, {self.y1}, {self.x2}, {self.y2})'

#%%
rec = Rectangle(1, 1, 3, 4)
rec # Rectangle (1, 1, 3, 4)
help(rec)

rec.width
rec.height
rec.x2
rec.width = 7
rec.x2

#%%
#   Slots
#
#%%
class Frozen:
    __slots__ = ['ice', 'cream']

dir(Frozen)  # no  __dict__
             # `ice` and `cream` present
frozen = Frozen()
frozen
frozen.ice  # AttributeError: ice
frozen.ice = True
frozen.ice
frozen.cream  # AttributeError: cream
frozen.cream = 'mniam!'
frozen.cream

# __slots__ blocks adding new attrs:
frozen.icy  #! AttributeError: 'Frozen' object has no attribute 'icy'
frozen.icy = 1  #! AttributeError: 'Frozen' object has no attribute 'icy'

#%%
"""
however the new attributes can be added to the derived
class if it does not have its own slots defined:
"""

class Unfrozen(Frozen): pass

unfrozen = Unfrozen()
dir(unfrozen)    # __dict__ present!
unfrozen.cream   # AttributeError: cream
unfrozen.cream = True

unfrozen.icy = 1  # ok
unfrozen.icy
