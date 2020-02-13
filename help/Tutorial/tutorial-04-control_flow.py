# -*- coding: utf-8 -*-
"""
title: Python Tutorial Release 3.6.3
subtitle: based on "tutorial.pdf" (book) by Guido van Rossum and the Python development team
author: kasprark
date: Wed Jan  3 11:33:57 2018


4. MORE CONTROL FLOW TOOLS
=====================================
(p. 19)
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/Tutorial/
ls

import importlib ## may come in handy

# importlib.reload(pd)

#%%
'''
4.1 if Statements
-----------------
'''
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

#%%
'''
4.2 for Statements
------------------
'''
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

#%%
'''
If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate
selected items), it is recommended that you first make a copy. Iterating over a sequence does not implicitly
make a copy. The slice notation makes this especially convenient:
'''
for w in words[:]: # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

words

##['defenestrate', 'cat', 'window', 'defenestrate']
'''
With for w in words:, the example would attempt to create an infinite list, inserting defenestrate over and
over again.
'''

#%%
'''
4.3 The range() Function
------------------------
'''
for i in range(5):
    print(i)

r = range(5, 10)
r
type(r)
## it is not a list!! it is  ITERABLE
list(r)

range(0, 10, 3)
range(-10, -100, -30)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

'''
In most such cases, however, it is convenient to use the enumerate() function, see Looping Techniques.
'''
enumarate()

#%%
'''
4.4 break and continue Statements, and else Clauses on Loops
------------------------------------------------------------
'''

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#%%
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

#%%
'''
4.5 pass Statements
-------------------
The pass statement does nothing. It can be used when a statement is required syntactically but the program
requires no action. For example:
'''

while True:
    pass # Busy-wait for keyboard interrupt (Ctrl+C)


#%% This is commonly used for creating minimal classes:
class MyEmptyClass:
    pass

MyEmptyClass

#%%
'''
Another place pass can be used is as a place-holder for a function or conditional body
when you are working on new code,
allowing you to keep thinking at a more abstract level.
The pass is silently ignored:
'''
def initlog(*args):
    pass # Remember to implement this!

initlog()

#%%
'''
4.6 Defining Functions
----------------------
'''
def fib(n): # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=', ')
        a, b = b, a+b
    print()

fib(2000)

#%%
f = fib
f(5000)

print(f(10))
print(f(0))

#%%

def fib2(n): # write Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)   ## see below
        a, b = b, a+b
    return result

fib2(2000)

#%%
'''
4.7 More on Defining Functions
------------------------------
'''

#%%
### 4.7.1 Default Argument Values

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('')
## ...

#%%  !!!!
i = 5

def f(arg=i):
    print(arg)

i = 6
f()     ## 5

#%%
'''
Important warning: The default value is evaluated only once.
This makes a difference when the default is a mutable object such as a list, dictionary,
or instances of most classes.
For example, the following function accumulates the arguments passed to it on subsequent calls:
'''
def f(a, L=[]):
    L.append(a)
    return(L)

f(1)
f(2)
f(3)
f(1)

'''
If you don’t want the default to be shared between subsequent calls,
you can write the function like this instead:
'''
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

f(1)
f(2)
f(3)

'''
What about this:
'''
i = 5

def f(x, arg=i):
    arg += x
    print(arg)

f(1)
f(1)

i = 6
f(1) 


#%%
'''
### 4.7.2 Keyword Arguments

Functions can also be called using _keyword_ arguments of the form  `kwarg=value`.
In a function call, _keyword_ arguments must follow _positional_ arguments.
...

fun(x              ## positional argument
    ,  *arguments  ## formal parameters
    , **keywords   ## dictionary
   )
'''
def fun(x, *arguments, **keywords):
    print(x)
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

fun( [1,2,3]
   , "a", [1,2,6]
   , w1 = [3,5], w2 = "sth"
   )

## from tutorial
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch"
           )

#%%
'''
### 4.7.3 Arbitrary Argument Lists

Finally, the least frequently used option
is to specify that a function can be called with an arbitrary number of arguments.

    These arguments will be wrapped up in a _tuple_ (see Tuples and Sequences).

Before the variable number of arguments, zero or more normal (positional) arguments may occur.
'''

def fun_sep( sep, *args):  ## if variadic args (*args) is second then first arg may not be named
    print(sep.join(args))  ## args is a _tuple_ now

fun_sep( "_", "qq", "ryqu", "na", "patyku" )

'''
    Normally, these variadic arguments will be last in the list of formal parameters,

because they scoop up all remaining input arguments that are passed to the function.
Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments,
meaning that they can only be used as keywords rather than positional arguments.
'''

def fun_sep2( *args, sep="/"):  ## if variadic args (*args) is the first then the rest of the arguments must be named
    print(sep.join(args))       ## args is a _tuple_ now

fun_sep2( "qq", "ryqu", "na", "patyku" )
fun_sep2( "qq", "ryqu", "na", "patyku" , sep="_")
fun_sep2( sep="_" , "qq", "ryqu", "na", "patyku" )  ## SyntaxError: positional argument follows keyword argument


#%%
'''
### 4.7.4 Unpacking Argument Lists

The reverse situation occurs when the arguments are already in a _list_ or tuple but need to be unpacked for
a function call requiring separate positional arguments.
For instance, the built-in range() function expects separate start and stop arguments.
If they are not available separately, write the function call with the
*-operator to unpack the arguments out of a list or tuple:
'''

list(range(3,6))
args = [3,6]
list(range(*args))  # call with arguments unpacked from a list

#%%
'''
In the same fashion, _dictionaries_ can deliver keyword arguments with the **-operator:
'''

def tubevol(height, radius, accuracy):
    pi = 3.141592653589793238462643
    return round( pi * radius**2 * height , accuracy)

args = { 'height' : 3 , 'radius' : 4 , 'accuracy' : 10 }
tubevol(**args)

args = { 'height' : 3 , 'radius' : 4 , 'accuracy' : 2 }
tubevol(**args)

acc = 3
args = { 'height' : 3 , 'radius' : 4 , 'accuracy' : acc }
tubevol(**args)

acc = 5
tubevol(**args)  ## not changes!!!

#%%
'''
### 4.7.5 Lambda Expressions
'''

def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
f(0)
f(2)

f = make_incrementor(-2)
f(0)
f(2)

#%%
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs

pairs.sort(key=lambda pair: pair[1])
pairs

#%%
'''
### 4.7.6 Documentation Strings
'''
