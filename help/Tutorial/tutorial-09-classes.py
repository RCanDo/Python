# -*- coding: utf-8 -*-
"""
title: Python Tutorial Release 3.6.3
subtitle: based on "tutorial.pdf" (book) by Guido van Rossum and the Python development team
author: kasprark
date: Mon Jan  8 10:49:23 2018


9. CLASSES
==========
(p. 67)
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/Tutorial/
ls

import importlib ## may come in handy

# importlib.reload(fibo)

#%%
'''
9.2 Python Scopes and Namespaces
--------------------------------
'''

'''
### 9.2.1 Scopes and Namespaces Example
Although scopes are determined statically, they are used dynamically.
At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:

• the _innermost_ scope, which is searched first, contains the _local_ names
• the scopes of any _enclosing functions_, which are searched starting with the nearest enclosing scope,
  contains non-local, but also non-global names
• the _next-to-last_ scope contains the current module’s global names
• the _outermost_ scope (searched last) is the namespace containing _built-in_ names
'''
def scope_test():

    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam               ## ???
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

#%%
'''
9.3 A First Look at Classes
'''
class MyClass:
    """A simple example class"""
    i = 12345           ## class attr.

    def f(self):
        return 'hello world'

MyClass.__doc__

MyClass.i
MyClass.f()  ##!!!  TypeError: f() missing 1 required positional argument: 'self'

x = MyClass()
x
x.f()        ## `self` arg of f() is passed automatically when f() is called from an instance of a class
x.i


#%%
class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []          ## `data` defined within method (__init__ here) is not a class attribute

    def f(self):
        return 'hello world'

MyClass.i
MyClass.data  ## AttributeError: type object 'MyClass' has no attribute 'data'

x = MyClass()
x.data        ## `data` is an attribute of an object (class instance) and was created during initialisaton of it
              ## via __init__
x.i
x.f()

#%%
class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

x = Complex(3.,-4.5)
x       ## we haven't defined the way of displaying an object of class `Complex`
x.re, x.im

x.__class__

#%%
class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __repr__(self):         ## how to display an object of class `Complex`
        return "({}, {})".format(x.re, x.im)       ##!!! return NOT print()

x = Complex(3.,-4.5)
x
x.re, x.im


#%%
### 9.3.3 Instance Objects

## we may add any attribute to the object

x.counter = 1
x
x.counter

## and work on it
while x.counter < 10:
    x.counter = x.counter * 2
    print(x.counter)

x.counter
x

## you can also add attribute to class !!! :
Complex.aaa = 'qq, it is new attr'
x.aaa       ## and it's immediately visible for all instances of it !!!

## you can delete new object attr:
del x.counter

x.counter

## you cannot delete newly defined attr of class
del x.aaa
## but you can damage on object by deleting an attr. in the original class definition
del x.re
x
## moreover, deleting class attribute from instance of a class


y = Complex(1,2)
y           ## AttributeError: 'Complex' object has no attribute 're'

##
del Complex.aaa

y.aaa
y.im
y.counter
y.counter = 10
y.counter
x.counter  ## no `counter`, OK

#%%
class Dog:
    kind = 'canine'   # class variable shared by all instances
    def __init__(self, name):
        self.name = name     # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
d.kind
e.kind
d.name
e.name

#%%

class Dog:
    tricks = []                 ## mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

d.tricks            ## unexpectedly shared by all dogs
e.tricks

#%% Correct design of the class should use an instance variable instead:
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []        ## creates a new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

d.tricks
e.tricks

#%%
'''
Any function object that is a class attribute defines a method for instances of that class.
It is not necessary that the function definition is textually enclosed in the class definition:
assigning a function object to a local variable in the class is also ok. For example:
'''
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g

'''
Now f, g and h are all attributes of class C that refer to function objects,
and consequently they are all methods of instances of C —— h being exactly equivalent to g.
Note that this practice usually only serves to confuse the reader of a program.
Methods may call other methods by using method attributes of the self argument:
'''

x = C()
x.f(1,-2)   ## OK !!!

#%% Methods may call other methods by using method attributes of the self argument:
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

x = Bag()
x
x.data

x.add(1)
x.data
x.addtwice(2)
x.data

x.__class__  ## __main__.Bag

#%%
'''
9.5 Inheritance
---------------
'''

#%%
'''
9.6 Private Variables
---------------------
'''
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update    ## privat copy of original update() method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        ## provides new signature for update() but doesn't break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

mp = Mapping(range(3))
mp
mp.items_list

mp.update(range(3,6))
mp.items_list

mps = MappingSubclass(range(3))
mps.items_list

mps.update(['a','b','c'],[7,8,9])
mps.items_list
mps.update(range(10,11))  ## TypeError: update() missing 1 required positional argument: 'values'
## but
mps._Mapping__update(range(10,13))
mps.items_list

#%%
'''
9.7 Odds and Ends
-----------------

Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”,
bundling together a few named data items. An empty class definition will do nicely:
'''

class Employee:
    pass

john = Employee()  # Create an empty employee record

john
john.__class__
john.__repr__
john.__str__

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

john.name
john.dept
john.salary

'''
???
'''
mps

#%%
a=10
a
a.__class__
isinstance(a,int)
isinstance(a,str)

issubclass(bool,int)
issubclass(bool,float)
issubclass(float,int)


#%%
'''
9.8 Iterators
-------------
'''

for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

#%%
for key in {'one':1, 'two':2}:
    print(key)

for k in {'one':1, 'two':2}:
    print(k)

#%%

d = {'one':1, 'two':2}
for k in d:
    print(d[k])

#%%

for ch in "123":
    print(ch)

for line in open("fibo.py"):
    print(line, end="")

#%%
'''
    The use of iterators pervades and unifies Python.

Behind the scenes, the for statement calls iter() on the container object.
The function returns an **iterator** object that defines the method __next__()
which accesses elements in the container one at a time.
When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate.
You can call the __next__() method using the next() built-in function;
this example shows how it all works:
'''
s = 'abc'

for ch in s: print(ch)

for ch in iter(s): print(ch)

it = iter(s)
it

next(it)
next(it)
next(it)
next(it)    ## StopIteration

#%%
'''
Having seen the mechanics behind the iterator protocol, it is easy to add iterator behavior to your classes.
Define an __iter__() method which returns an object with a __next__() method.
If the class defines __next__(), then __iter__() can just return self:
'''

class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
rev
type(rev)
iter(rev)
type(iter(rev))

for char in rev:
    print(char)

next(rev)   ## StopIteration

rev = Reverse('spam')
next(rev)
next(rev)
rev.index
rev.index = 4
next(rev)
rev.__next__()
rev.__next__()
rev.__next__()
rev.__next__()   ## StopIteration


#%%
## 9.9 Generators
'''
_Generators_ are a simple and powerful tool for creating _iterators_.
They are written like regular functions but use the `yield` statement whenever they want to return data.
Each time next() is called on it, the generator resumes where it left off
(it remembers all the data values and which statement was last executed).
An example shows that generators can be trivially easy to create:
'''
def reverse(data):
    for idx in range(len(data)-1, -1, -1):
        yield data[idx]

for ch in reverse('extraordinary'):
    print(ch)

rev = reverse('spam')
rev

next(rev)
next(rev)
rev.next()     ## 'generator' object has no attribute 'next'
rev.__next__()
rev.__next__()
next(rev)      ## StopIteration


rev = reverse('spam')
rev

next(rev)

## HOW TO FIND/CONTROL CURRENT STATE OF INDEX???
rev.index ## AttributeError: 'generator' object has no attribute 'index'
rev.__iter__()
???...

#%%
## OTHER EXAMPLES

#%% 1*

def countdown(n):
    while n>0:
        yield(n)
        n -= 1

for i in countdown(7):
    print("{}!".format(i))

list(countdown(11))
tuple(countdown(5))

#%% 2*

def evens(n):
    for k in range(n):
        if k % 2 == 0:
            yield k

list(evens(13))
tuple(evens(13))

#%%
from numpy import array
array(range(5))

type(range(5))
type(evens(5))

iter

print(array(evens(11)))
array(evens(11)) ## ???

array(list(evens(11)))  ## OK !!!

array(list(countdown(10)))

#%%

evs = evens(5)
evs
next(evs)
next(evs)
evs.__next__()
next(evs)    ## StopIteration

#%%

for k in evens(11):
    print(k)

#%% 3*
## fibonaci

def fibopairs(n):
    a, b = 0, 1
    while b < n:
        a, b = b, b+a
        yield a, b

fibopairs(10)

 list(fibopairs(10))
tuple(fibopairs(10))

array(list(fibopairs(10)))
array(list(fibopairs(10))).T


#%%
for f in fibopairs(100):
    print(f)

#%%
fp = fibopairs(20)

next(fp)
next(fp)
next(fp)
fp.__next__()

list(fp)    ## only remaining set of values !!!!!!!!!!!
next(fp)    ## StopIteration

#%%
'''
    map() returns `map` which is similar to generator
'''
xx = list(range(10))
xx
yy = map(lambda x: x**2, xx)
yy
type(yy)

yy[1]    ## TypeError: 'map' object is not subscriptable

yy.

import pylab as pl
pl.plot(xx, yy)    ## RuntimeError: matplotlib does not support generators as input

next(yy)
next(yy)
next(yy)

list(yy)   ## only remaining elements
next(yy)   ## StopIteration

for y in yy:
    print(y)   ## nothing because we have already exhausted index of yy

## we have to recreate it
yy = map(lambda x: x**2, xx)

for y in yy:
    print(y)   ## nothing because we have already exhausted index of yy

## index exhausted thus
next(yy)    ## StopIteration

#%%
'''
9.10 Generator Expressions
--------------------------
Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions
but with parentheses instead of brackets. These expressions are designed for situations where the generator
is used right away by an enclosing function. Generator expressions are more compact but less versatile than
full generator definitions and tend to be more memory friendly than equivalent list comprehensions.
'''

sum(i*i for i in range(10))

[1,2,3,4,5]*10  ## NO!!!! it's not R nor Matlab...
xx = [i*10 for i in range(1,6)]
xx

## or
list(map(lambda k: k*10, range(1,6)))

xx
yy = [9,7,5,3,1]
yy

sum(x*y for x,y in zip(xx,yy))

#%%
from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
sine_table

## or better
xx = [x*pi/180 for x in range(0,91)]
yy = list(map(sin,xx))

import pylab as pl
pl.plot(xx, yy, label="sin(x)")
pl.xlabel("x")
pl.ylabel("y")
pl.legend()

#%%
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

#%%
unique_words = set(word for line in page for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)


