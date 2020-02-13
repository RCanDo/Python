# -*- coding: utf-8 -*-
"""
title: Python Tutorial Release 3.6.3
subtitle: based on "tutorial.pdf" (book) by Guido van Rossum and the Python development team
author: kasprark
date: Fri Jan  5 12:07:42 2018


7. INPUT AND OUTPUT
===================
(p. 51)
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
7.1 Fancier Output Formatting
-----------------------------
'''
#%% .rjust()

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(4), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(5))

'''
Note that in the first example, one space between each column was added by the way print() works:
it always adds spaces between its arguments.
'''
#%%
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

#%% .ljust()

for x in range(1, 11):
    print(repr(x).ljust(2), repr(x*x).ljust(4), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).ljust(5))

#%%
for x in range(1, 11):
    print('{0:1d} {1:1d} {2:1d}'.format(x, x*x, x*x*x))   ## ????

#%%

"very_long_string".ljust(8)[:8]

#%% .center()

for x in range(1, 20):
    print(repr(x).center(2), repr(x*x).center(4), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).center(5))

#%%
for k in range(1,10):
    print(repr(int(eval("1e"+str(k)))).center(9))

#%%
'12'.zfill(5)
'-3.14'.zfill(7)
'3.14159265359'.zfill(5)

#%%

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format( food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))


#%%
'''
'!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr())
can be used to convert the value before it is formatted:
'''
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

content = "bułkę"
print("Give me {}".format(content))
print("Give me {!a}".format(content))

#%%
pi = 3.141592653589793238462643
print('The value of PI is approximately {0:.3f}.'.format(pi))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))
## 0 is dictionary `table` ['s'] is 's' entry of this table

## using **
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

## the same for list, then we use *
list(table.values())
print('Jack: {0:d}; Sjoerd: {1:d}; Dcab: {2:d}'.format(*list(table.values())) )

#%%
### 7.1.1 Old string formatting
print('The value of PI is approximately %5.3f.' % pi)

#%%
'''
7.2 Reading and Writing Files
-----------------------------
'''




