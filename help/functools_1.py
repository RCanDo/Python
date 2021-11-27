python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: functools 1
subtitle:
version: 1.0
type: tutorial
keywords: [functools, partial, update_wrapper, partialmethod, wraps, total_ordering, cmp_to_key]
description: |
    functools library
    The functools module provides tools for adapting or extending functions and other callable objects,
    without completely rewriting them.
remarks:
    - etc.
todo:
    - problem 1
sources:
    - title: Python Module Of The Week
      chapter: functools — Tools for Manipulating Functions
      link: https://pymotw.com/3/functools/index.html
    - title: functools
      subtitle: Higher-order functions and operations on callable objects
      link: https://docs.python.org/3.7/library/functools.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: functools_1.py
    path: .../Python/help/
    date: 2021-09-24
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%
from rcando.ak.builtin import * #flatten, paste
from rcando.ak.nppd import * #data_frame
import os, sys, json

ROOT = json.load(open('root.json'))
WD = os.path.join(ROOT['Works'], "Python/help/")   #!!! adjust
os.chdir(WD)

print(os.getcwd())

#%%
from pprint import pprint
from functools import partial, update_wrapper, partialmethod, wraps, total_ordering, cmp_to_key
import inspect

#%%
"""
The functools module provides tools for adapting or extending functions and other callable objects,
without completely rewriting them.
"""
#%%
#%% Decorators
"""
The primary tool supplied by the functools module is the class partial,
which can be used to “wrap” a callable object with default arguments.
The resulting object is itself callable and can be treated as though it is the original function.
It takes all of the same arguments as the original,
and can be invoked with extra positional or named arguments as well.
A partial can be used instead of a lambda to provide default arguments to a function,
while leaving some arguments unspecified.
"""
#%% Partial Objects
"""
This example shows two simple partial objects for the function myfunc().
The output of show_details() includes the func, args, and keywords attributes of the partial object.
"""
def myfunc(a, b=2):
    "Docstring for myfunc()."
    print('  called myfunc with:', (a, b))

myfunc('a', 3)          # called myfunc with: ('a', 3)

#%%
def show_details(name, f, is_partial=False):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    if not is_partial:
        print('  __name__:', f.__name__)
    if is_partial:
        print('  func:', f.func)
        print('  args:', f.args)
        print('  keywords:', f.keywords)
    return

show_details('myfunc', myfunc)
#  myfunc:
#    object: <function myfunc at 0x000001968E32AEE0>
#    __name__: myfunc

#%%
# Set a different default value for 'b', but require the caller to provide 'a'.
p1 = partial(myfunc, b=4)
p1('passing a')            # called myfunc with: ('passing a', 4)
p1('override b', b=5)      # called myfunc with: ('override b', 5)

p1()                       #! TypeError: myfunc() missing 1 required positional argument: 'a'

show_details('partial with named default', p1, True)
#  partial with named default:
#  object: functools.partial(<function myfunc at 0x000001968E32AEE0>, b=4)
#    func:                   <function myfunc at 0x000001968E32AEE0>
#    args: ()
#    keywords: {'b': 4}

#%% Set default values for both 'a' and 'b'.
p2 = partial(myfunc, 'default a', b=99)
p2()                        # called myfunc with: ('default a', 99)
p2(b='override b')          # called myfunc with: ('default a', 'override b')
show_details('partial with defaults', p2, True)
#  partial with defaults:
#  object: functools.partial(<function myfunc at 0x000001968E32AEE0>, 'default a', b=99)
#    func: <function myfunc at 0x000001968E32AEE0>
#    args: ('default a',)
#    keywords: {'b': 99}


#%% example ak1
# see collections_1.py : example ak1  for Counter()


#%%
#%% Acquiring Function Properties
"""
The partial object does not have __name__ or __doc__ attributes by default,
and without those attributes, decorated functions are more difficult to debug.
Using update_wrapper(), copies or adds attributes from the original function to the partial object.
"""
def myfunc(a, b=2):
    "Docstring for myfunc()."
    print('  called myfunc with:', (a, b))

def show_details(name, f):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__:', f.__doc__)
    print()

show_details('myfunc', myfunc)
#  myfunc:
#    object: <function myfunc at 0x000001968E2E34C0>
#    __name__: myfunc
#    __doc__: Docstring for myfunc().

#%%
p1 = partial(myfunc, b=4)
show_details('raw wrapper', p1)

#  raw wrapper:
#    object: functools.partial(<function myfunc at 0x000001968E32A8B0>, b=4)
#    __name__: (no __name__)
#    __doc__: partial(func, *args, **keywords) - new function with partial application
#             of the given arguments and keywords.

#%%
"""
The attributes added to the wrapper are defined in WRAPPER_ASSIGNMENTS,
while WRAPPER_UPDATES lists values to be modified.
"""
import functools as ft
print('Updating wrapper:')
print('  assign:', ft.WRAPPER_ASSIGNMENTS)
    #   assign: ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
print('  update:', ft.WRAPPER_UPDATES)
    #   update: ('__dict__',)

update_wrapper(p1, myfunc)                                                     #!!!
    # functools.partial(<function myfunc at 0x000001968E350940>, b=4)
show_details('updated wrapper', p1)
#  updated wrapper:
#    object: functools.partial(<function myfunc at 0x000001968E350940>, b=4)
#    __name__: myfunc
#    __doc__: Docstring for myfunc().

#%%  Other Callables
"""
Partials work with any callable object, not just with standalone functions.
"""
class MyClass:
    "Demonstration class for functools"

    def __call__(self, e, f=6):
        "Docstring for MyClass.__call__"
        print('  called object with:', (self, e, f))

mc = MyClass()

mc()            #! TypeError: __call__() missing 1 required positional argument: 'e'
mc(1)           # called object with: (<__main__.MyClass object at 0x000001968E33ECD0>, 1, 6)
mc(1, 2)        # called object with: (<__main__.MyClass object at 0x000001968E33ECD0>, 1, 2)

#%%
def show_details(name, f):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__:', f.__doc__)
    return

show_details('MyClass instance', mc)
#  MyClass instance:
#    object: <__main__.MyClass object at 0x000001968E33ECD0>
#    __name__: (no __name__)
#    __doc__: Demonstration class for functools

#%%
pmc = partial(mc, f=0)
show_details('MyClass instance - partial', pmc)
#  MyClass instance - partial:
#    object: functools.partial(<__main__.MyClass object at 0x000001968E33ECD0>, f=0)
#    __name__: (no __name__)
#    __doc__: partial(func, *args, **keywords) - new function with partial application
#             of the given arguments and keywords.

#%%
update_wrapper(pmc, mc)
show_details('instance wrapper', pmc)
#  instance wrapper:
#    object: functools.partial(<__main__.MyClass object at 0x000001968E33ECD0>, f=0)
#    __name__: (no __name__)
#    __doc__: Demonstration class for functools

#%% Methods and Functions
"""
While partial() returns a callable ready to be used directly, partialmethod()
returns a callable ready to be used as an __unbound method of an object__.    ???

In the following example, the same standalone function is added as an attribute of MyClass twice,
once using partialmethod() as method1() and again using partial() as method2().
"""
def standalone(self, a=1, b=2):
    "Standalone function"
    print('  called standalone with:', (self, a, b))
    if self is not None:
        print('  self.attr =', self.attr)

class MyClass:
    "Demonstration class for functools"

    def __init__(self):
        self.attr = 'instance attribute'

    method1 = partialmethod(standalone)

    method2 = partial(standalone)


#%%
"""
method1() can be called from an instance of MyClass,
and the instance is passed as the first argument just as with methods defined normally.

method2() is not set up as a __bound method__, and so the `self` argument must be passed explicitly,  !!!
or the call will result in a TypeError.
"""

mc = MyClass()

standalone(None)        # called standalone with: (None, 1, 2)

mc.method1()
#  called standalone with: (<__main__.MyClass object at 0x000001968E33E520>, 1, 2)
#  self.attr = instance attribute

mc.method2()
#! TypeError: standalone() missing 1 required positional argument: 'self'

#%% Acquiring Function Properties for Decorators
"""
Updating the properties of a wrapped callable is especially useful when used in a decorator,
since the transformed function ends up with properties of the original “bare” function.
"""

def show_details(name, f):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    print('  __name__:', end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print('  __doc__:', f.__doc__)
    print()

def simple_decorator(f):
    @wraps(f)                                       #!!!
    def decorated(a='decorated defaults', b=1):
        print('  decorated:', (a, b))
        print('  ', end=' ')
        return f(a, b=b)
    return decorated

def myfunc(a, b=2):
    "myfunc() is not complicated"
    print('  myfunc:', (a, b))
    return

#%%
show_details('myfunc', myfunc)
#  myfunc:
#    object: <function myfunc at 0x000001968E350430>
#    __name__: myfunc
#    __doc__: myfunc() is not complicated

myfunc('unwrapped, default b')
#  myfunc: ('unwrapped, default b', 2)

myfunc('unwrapped, passing b', 3)
#  myfunc: ('unwrapped, passing b', 3)

# Wrap explicitly
wrapped_myfunc = simple_decorator(myfunc)
wrapped_myfunc()
#    decorated: ('decorated defaults', 1)
#       myfunc: ('decorated defaults', 1)

wrapped_myfunc('args to wrapped', 4)
#    decorated: ('args to wrapped', 4)
#       myfunc: ('args to wrapped', 4)

show_details('wrapped_myfunc', wrapped_myfunc)
#  wrapped_myfunc:
#    object: <function myfunc at 0x000001968E350820>
#    __name__: myfunc
#    __doc__: myfunc() is not complicated             # __doc__ copied from original

#%%  Wrap with decorator syntax
@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)
    return

# ... the same results


#%%
#%%  Comparison
"""
Under Python 2, classes could define a __cmp__() method that returns -1, 0, or 1
based on whether the object is less than, equal to, or greater than the item being compared.
Python 2.1 introduced the rich comparison methods API
(__lt__(), __le__(), __eq__(), __ne__(), __gt__(), and __ge__()),
which perform a single comparison operation and return a boolean value.

Python 3 deprecated __cmp__() in favor of these new methods
and functools provides tools to make it easier to write classes
that comply with the new comparison requirements in Python 3.
"""

#%%  Rich Comparison
"""
The rich comparison API is designed to allow classes with complex comparisons
to implement each test in the most efficient way possible.
However, for classes where comparison is relatively simple,
there is no point in manually creating each of the rich comparison methods.

The total_ordering() class decorator takes a class that provides some of the methods,
and adds the rest of them.
"""

@total_ordering         #!!!
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print('  testing __eq__({}, {})'.format(self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print('  testing __gt__({}, {})'.format(self.val, other.val))
        return self.val > other.val

pprint(inspect.getmembers(MyObject, inspect.isfunction))

"""
[('__eq__', <function MyObject.__eq__ at 0x000001968E350D30>),
 ('__ge__', <function _ge_from_gt at 0x00000196854F58B0>),
 ('__gt__', <function MyObject.__gt__ at 0x000001968E350E50>),
 ('__init__', <function MyObject.__init__ at 0x000001968E350A60>),
 ('__le__', <function _le_from_gt at 0x00000196854F5940>),
 ('__lt__', <function _lt_from_gt at 0x00000196854F5820>)]
"""

#%%
a = MyObject(1)
b = MyObject(2)

a < b
#   testing __gt__(1, 2)
#   testing __eq__(1, 2)
# True

a <= b
#   testing __gt__(1, 2)
# True

a == b
#   testing __eq__(1, 2)
# False

a >= b
#   testing __gt__(1, 2)
#   testing __eq__(1, 2)
# False

a > b
#   testing __gt__(1, 2)
# False

"""
The class must provide implementation of __eq__() and one other rich comparison method.
The decorator adds implementations of the rest of the methods that work by using the comparisons provided.
If a comparison cannot be made, the method should return  `NotImplemented `
so the comparison can be tried using the reverse comparison operators on the other object,
before failing entirely.
"""

#%%  Collation Order
"""
Since old-style comparison functions are deprecated in Python 3,
the `cmp` argument to functions like sort() are also no longer supported.
Older programs that use comparison functions can use cmp_to_key() to convert them
to a function that returns a collation key,
which is used to determine the position in the final sequence.
"""

class MyObject:

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'MyObject({})'.format(self.val)


def compare_obj(a, b):
    """Old-style comparison function.
    """
    print('comparing {} and {}'.format(a, b))
    if a.val < b.val:
        return -1
    elif a.val > b.val:
        return 1
    return 0

#!!! cmp_to_key()
get_key = cmp_to_key(compare_obj)

def get_key_wrapper(o):
    """Wrapper function for get_key to allow for print statements."""
    new_key = get_key(o)
    print('key_wrapper({}) -> {!r}'.format(o, new_key))
    return new_key

#%%
objs = [MyObject(x) for x in range(5, 0, -1)]

for o in sorted(objs, key=get_key_wrapper):  print(o)

#%%
"""
Normally cmp_to_key() would be used directly,
but in this example an extra wrapper function is introduced to print out more information
as the key function is being called.

The output shows that sorted() starts by calling get_key_wrapper()
for each item in the sequence to produce a key.
The keys returned by cmp_to_key() are instances of a class defined in functools
!!! that implements the rich comparison API using the __old-style__ comparison function passed in.  !!!
After all of the keys are created, the sequence is sorted by comparing the keys.

key_wrapper(MyObject(5)) -> <functools.KeyWrapper object at 0x000001968E3442F0>
key_wrapper(MyObject(4)) -> <functools.KeyWrapper object at 0x000001968E344F30>
key_wrapper(MyObject(3)) -> <functools.KeyWrapper object at 0x000001968E344FB0>
key_wrapper(MyObject(2)) -> <functools.KeyWrapper object at 0x000001968E344DD0>
key_wrapper(MyObject(1)) -> <functools.KeyWrapper object at 0x000001968E3441D0>
comparing MyObject(4) and MyObject(5)
comparing MyObject(3) and MyObject(4)
comparing MyObject(2) and MyObject(3)
comparing MyObject(1) and MyObject(2)
MyObject(1)
MyObject(2)
MyObject(3)
MyObject(4)
MyObject(5)
"""

#%%

