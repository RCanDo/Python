# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec 28 09:17:48 2017

28. Object Oriented Programming
===============================
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/PFCSAE
ls

import importlib ## may come in handy


#%%
'''
• Motivation and terminology
• Time example
• encapsulation
• defined interfaces to hide data and implementation
• operator overloading
• inheritance
• (teaching example only: normally datetime and others)
• Geometry example
• Objects we have used already
• Summary
'''

#%%
'''
1. Motivation
-------------

• When programming we often _store_ data
• and _do_ something with the data.
• For example:
    - an array keeps the data and
    - a function does something with it.
• Programming driven by actions (i.e. calling functions to do
things) is called _imperative_ or _procedural_ programming.

Object Orientation
• merge data and functions (that operate on this data) together into _classes_.
  (…and objects are “instances of a class”)
• a _class_ combines data and functions
  (think of a _class_ as a _blue print_ for an object)
• _objects_ are instances of a _class_
  (you can build several objects from the same blue print)
• a _class_ contains _members_:
    - _attributes_ -- _members_ of classes that store data,
    - _methods_ (or _behaviours_)-- _members_ of classes that are _functions_.

'''

#%%
'''
Example 1: a class to deal with time
------------------------------------

The code in  oop_time_class.py
'''

## class definition from the file
class Time:

    def __init__(self, hour, min):      ## constructor
        self.hour = hour
        self.min = min

    def print24h(self):             ## all methods in a class need self as the first argument.
                                    ## Self represents the object. (This will make more sense later.)
        print("{:2d}:{:2d}".format(self.hour, self.min))

    def print12h(self):
        if self.hour < 12:
            ampm = "am"
        else:
            ampm = "pm"

        print("{:2}:{:2} {}".format(self.hour % 12, self.min, ampm))

## ...

#%%

import oop_time_class as ot
# importlib.reload(ot)

ot.t

t = ot.Time(15, 45)

print("print as 24h: "); t.print24h()
print("print as 12h: "); t.print12h()

print("The time is %d hours and %d minutes." % (t.hour, t.min))

#%%
"""
### Members of an object
In Python, we can use dir(t) to see the members of an object t. For example:
"""
t = ot.Time(15, 45)
dir(t)

## We can also modify attributes of an object using for example

t.hour = 10.
t
t.print24h()

##  However, direct access to attributes is sometimes supressed
##  (although it may look like direct access -> property).

#%%
"""
2. Data Hiding
--------------

A well designed class provides methods to _get_ and _set_ attributes.
These methods define the interface to that class.
This allows:

• to perform _error checking_ when values are set, and
• to hide the implementation of the class from the user. This is good because
    - the user doesn’t need to know what is going on behind the scenes
    - we can change the implementation of the class without changing the interface.
• The next slides show an extended version of the Time class with such _get_ and _set_ methods.
• We introduce _set_ and _get_ methods as one would use in Java and C++
  to reflect the common ground in OO class design.

    In Python, the use of _property_ is often recommended over _set_ and _get_ methods.

"""

#%%
"""
Example 2: a class to deal with time
------------------------------------

The code in  oop_time_class_2.py
"""

import oop_time_class_2 as ot2
## importlib.reload(ot2)

ot2.t

t = ot2.Time(15,45)
t
t.print24h()
t.print12h()

print("that is %d hours and %d minutes" % (t.getHour(), t.getMin()))

"""
Providing set() and get() methods for attributes of an object

• prevents incorrect data to be entered
• ensures that the internal state of the object is consistent
• hides the implementation from the user (more black box),
• and make future change of implementation easier.

There are more sophisticated ways of “hiding” variables from users:
using Python properties we can bind certain functions to be called
when _attributes_ in the class are accessed. (See for example here).
"""

#%%
"""
3. Operator overloading
-----------------------

  The code in  oop_time_class_2.py

• We constantly use operators to “do stuff” with objects.
• What the operator does, depends on the objects it operates on. For example:
"""
a = "Hello "; b = "World"
a + b # concatenation
    ## 'Hello World'
c = 10; d = 20
c + d # addition
    ## 30

"""
• This is called _operator overloading_ because the operation is overloaded with more than one meaning.
• Other operators include -,* , **, [], (), >, >=, ==, <=, <, str(), repr(), ...
• We can overload these operators for our own objects.
  The next slide shows an example that overloads the `>` operator for the Time class.
• It also overloads the “str” and “repr“ functions.
"""

%reset

import oop_time_class_2 as ot2
# importlib.reload(ot2)


ot2.

t1 = ot2.Time(15,45)
t1
type(t1)
t1.
t1.print24h()
t1.print12h()

t2 = ot2.Time(10, 55)

t1 < t2
t1 > t2

t1.minutes()

#%%
"""
4. Inheritance
--------------

  The code in  oop_time_class_3.py

Sometimes, we need classes that share certain (or very many, or all) attributes but are slightly different.

### Example 1: Geometry
• a point (in 2 dimensions) has an x and y attribute
• a circle is a point with a radius
• a cylinder is a circle with a height

### Example 2: People at universities
• A person has an address.
• A student is a person and selects modules.
• A lecturer is a person with teaching duties.
• …

In these cases, we define a base class and derive other classes from it.
This is called _inheritance_.
"""


%reset
import importlib

import oop_time_class_2 as ot2
# importlib.reload(ot2)

ot2.

t1 = ot2.Time(15, 45)
t2 = ot2.Time(10, 55)

print("String representation of the object t1: %s" % t1)
print("Representation of object = %r" % t1)
print("compare t1 and t2: ")

if t1 > t2:
    print("t1 is greater than t2")

t3 = ot2.TimeUK(15,45)

print("TimeUK object = %s" % t3)
print(t3)
print("TimeUK object = %r" % t3)


t4 = ot2.Time(16, 15)
print("Time object = %s" % t4)
print("compare t3 and t4: ")
if t3 > t4:
    print("t3 is greater than t4")
else:
    print("t3 is not greater than t4")

#%%
"""
Inheritance example Geometry
----------------------------

  The code in  oop_geometry.py

"""

%reset
import importlib

import oop_geometry as g
# importlib.reload(g)


d = g.Circle(x=0, y=0, radius=1)
d
d.radius

print("Circle circumference: ", d.circum())
print("Circle area: ", d.area())
print([name for name in dir(d) if name[:2] != "__"])

c = g.Cylinder(x=0, y=0, radius=1, height=2)
print("Cylinder area: ", c.area())
print("Cylinder volume: ", c.volume())
print([name for name in dir(c) if name[:2] != "__"])

