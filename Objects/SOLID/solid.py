"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: SOLID
subtitle:
version: 1.0
type: review
keywords: [SOLID]
description: |
remarks:
todo:
sources:
    - title: SOLID Python
      subtitle: SOLID principles applied to a dynamic programming language
      chapter:
      link: D:/bib/Python/Solid_Python.pdf
      date: 2013-12
      authors:
          - fullname: Duncan Watson-Parris
          - email: duncan.watson-parris@tessela.com
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: SOLID.py
    path: D:/ROBOCZY/Python/help/Objects/SOLID/
    date: 2019-12-18
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
cd D:/ROBOCZY/Python/Objects/SOLID/

#%%
"""
https://www.slideshare.net/DrTrucho/python-solid
"""

#%%
"""
1. Single Responsibility Principle

- “The Single Responsibility Principle requires that each class is responsible for only one thing.“
- “An axis of change is an axis of change only if the changes actually occur.”

"""

# Given a class which has two responsibilities
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def draw(self):
        # Do some drawing
        pass
    def area(self):
        return self.width * self.height
#%%
"""
We have a trivial Rectangle class which is responsible for both
the geometric properties of the rectangle and also the GUI representation of it.
This may be acceptable early in the development of the system
but later on we realise we need to split the responsibility because
the GUI representation needs factoring out.
So we simply split the class:
"""
# We can split it into two...
class GeometricRectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class DrawRectangle:
    def draw(self):
        # Do some drawing
        pass

#%%
"""
1.2 Open/Closed Principle

- “Software entities (classes, modules, functions, etc)
  should be open for extension, but closed for modification.”

At first reading this statement may seem contradictory,
but in any OOP language this is trivially achieved through __abstraction__.

The base (or abstract) class is closed for modification
and we implement concrete subclasses in order to modify their behaviour.

Sub-classing is straight forward, the decorator pattern can also be useful,
and if we needed abstract base classes we could use the
ABC [4] package here,   (!!!)
but it’s interesting to note that Python offers us some other more exotic options
as explored below.

These are mostly exotic for a reason though!
Most of the time we can achieve OCP without resorting to these,
but as [2] says:

- “there will always be some kind of change against which
  [our module] is not closed”,

and this is where these options can be useful.
"""
#%%
"""
1.2.1 Mix-ins

https://stackoverflow.com/questions/533631/what-is-a-mixin-and-why-are-they-useful/533675#533675
https://books.google.pl/books?id=5zYVUIl7F0QC&pg=RA1-PA584&lpg=RA1-PA584&dq=programming+python+guimixin&source=bl&ots=HU833giXzH&sig=jwLpxSp4m_VbOYQ897UDkGNx_2U&hl=en&ei=x8iRSaTTF5iq-ganpbGPCw&sa=X&oi=book_result&ct=result&redir_esc=y#v=onepage&q=programming%20python%20guimixin&f=false
"""
#%%
"""
1.2.2 Monkey-Patching

https://blog.codinghorror.com/monkeypatching-for-humans/
"""
#%%
"""
1.2.3 Generic functions (using overloading)

@overload  ??? bad style !!!
https://stackoverflow.com/questions/39748842/python-3-5-method-overloading-with-overload
https://stackabuse.com/overloading-functions-and-operators-in-python/
"""
#%%
"""
1.3 Liskov Substitution Principle   ???

- “Objects in a program should be replaceable with instances of their base types
  without altering the correctness of that program.”

Most of the arguments and examples on this principle are equally valid in Python,
but I think you have to be particularly careful of this in Python
because it is so easy to override methods and variables – as we have seen above!

Changes in behaviour using e.g. _monkey patching_ will almost inevitably
break the Liskov Substitution Principle (but may be justified in some circumstances).

It’s interesting to consider for a moment how this principle relates
to classes with multiple inheritance.
For example if we had used mix-ins to satisfy OCP should our subclass be replaceable
with all of its base types? I would argue not.
The whole point of using mix-ins is that the behaviour of the subclass
is the sum of the behaviours of the base classes.
"""

#%%
"""
1.4 Interface Segregation Principle

- “Many client-specific interfaces are better than one general-purpose interface.”

This principle aims to ensure that clients are not forced to depend on methods
which they do not use.

For me this is a key principle in good Python programming,
and something I will come back to in the next section.

A good way of ensuring this is by separation through multiple inheritance.   !!!
In [1 & 2] this is done using _interfaces_ because that is the only way
of implementing multiple inheritance in Java.
In Python we are free to inherit from multiple concrete classes,
and this is precisely the purpose of the mix-ins discussed above
– to provide multiple clients specific behaviours.
"""

EXAMPLE !!!
#%%
"""
1.5 Dependency Inversion Principle

“
a. High-level modules should not depend on low-level modules. Both should depend on abstractions.
b. Abstractions should not depend on details. Details should depend on abstractions.
”
...
interface
duck-typing

I would argue in Python that you often don’t need interfaces at all:
You shouldn't separate the definition of the behaviour from the implementation
unless you have to.
A given client can assume an argument has a given property and it is up to the programmer
and his unit tests to ensure it does.
A well-documented function should describe the behaviours it expects of an argument
– not the type of an argument.

There are situations when you might need to define an interface in order
to make an explicit contract, such as for APIs or classes which you expect
to be extended as part of a library or framework.
In this case you can use abstract base classes [ABC] which,
because Python allows multiple inheritance, are essentially the same as interfaces. !!!
"""

#%%
"""
2 Easier to Ask for Forgiveness than Permission (EAFP)
  == try...except...finally...

contrary to  Look Before You Leap (LBYL)
== if...elif...else...
"""
#%%  LBYL
if i > 0.0:
    v = cmath.sqrt(i)
else:
    #handle
    print(i)

#%%  EAFP
try:
    v = cmath.sqrt(i)
except ValueError:
    # handle
    print(v)

#%%
"""
https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
"""
from contextlib import contextmanager
import os

@contextmanager
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_dir)

with working_directory("data/stuff"):
    # do something within data/stuff
    # here I am back again in the original working directory

"""
This probably doesn’t help with checking real numbers but it does get you
into the mind-set of EAFP.
"""
#%%
"""
I think the EAFP idiom runs right through Python, and hopefully
the arguments for using interfaces as little as possible make more sense in this light.

When we use strongly typed languages the language is in effect performing LBYL
on every function call, checking that what you passed in
is what you said you were going to (whether this is at run-time or compile time).

This in its very nature inhibits flexibility,
flexibility which we can exploit if we assume the object we were given
has the properties we need it to.
...

...if you've chosen to develop in Python and then start using _interfaces_
all over the place then you've probably missed the point of Python!
"""


#%%
#%%
"""
5 Other tips
"""

#%% 1. list comprehension
ll = [x.attr for x in collection]

#%% 2. generator
gen = (x.attr for x in collection)    # this way will be alway finite

def gen():
    # may be infinite, like e.g. Fibbonacci
    result = init_val
    while condition:
        #...
        result = ...
        yield result

next(gen)
[a for a in gen()]   # carefuly if gen() is infinite
for k, a in enumerate(gen()): ...
for k, a in zip(range(n), gen()): ...

from itertools import islice
for a in islice(gen(), stop)
for a in islice(gen(), start, stop, step)

#%% 3. dictionary comprehension
my_dict = { key.attr: val.attr  for key in keys for val in vals}

#%% 4. Dictionary values as functions / Classes
my_new_obj = my_dict[key]() # where my_dict contains key:Class mappings

#%% 5 The 'map' function
squares = map(sqrt, range(10))

#%% 6 Unpacking arguments
val = my_func(*my_list, **my_dict)

#%% 7 Unpacking return values
val, idx = my_func()
a, b = b, a

#%% 8 For (almost) any numerical work use Numpy!

#%% 9 Chained comparisons
if 1 < five() < 6:

#%% 10 Advanced indexing
lst[-1]
lst[::-1]
lst[::2]
# All of the above work on strings!

#%% 11 Using enumerate
for i, x in enumerate(my_list):
    # do something

#%% 12 Default dictionary values
val = my_dict.get(key, default)

"""
Also - there is a `defaultdict` collection which gives keys default values,
or use `my_dict.setdefault` to set a default on a standard dict.
There are some subtle differences though about when the default is created,
and some code might expect a KeyError, so take care with this one.
"""
dic = {'a':1, 'b':3}
help(dic.setdefault)
dic.setdefault('c', 33)
dic
dic.setdefault('c', 22)

#%% 13 Named formatting
print("The {foo} is {bar}".format(foo='answer', bar=42))
# Note that you can also unpack a dict into format!

dic = {'foo':'answer', 'bar':42}
print("The {foo} is {bar}".format(**dic))
# Note that you can also unpack a dict into format!

#%% 14 Much more readable ternary operators
x = 3 if (y==1) else 2

#%% 15 Classes can be created at run-time
"""
This one is definitely not for the feint hearted.
Because classes are first class objects in Python it is possible to define them
at run-time, e.g. within if statements or even functions.
Use with care!
"""

#%%


