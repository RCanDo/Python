# -*- coding: utf-8 -*-
"""
title: Python Tutorial Release 3.6.3
subtitle: based on "tutorial.pdf" (book) by Guido van Rossum and the Python development team
author: kasprark
date: Wed Jan  3 10:49:30 2018


3. AN INFORMAL INTRODUCTION TO PYTHON
=====================================
(p. 9)
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
3.1. Using Python as a Calculator
---------------------------------
'''
8/5
17/3
17//3
17%3
5**2

#%% the last answer _
_
4.6**1.3
_
6*_
_
round(_,3)

#%% ** has precedence over -
-3**2    ## -9
(-3)**2

#%% strings
"doesn't"
'doesn\'t'
'doesn"t'
## but this is wrong
'doesn't'

#%%
'"Isn\'t," she said.'
print('"Isn\'t," she said.')
s = 'First line.\nSecond line.' # \n means newline
s # without print(), \n is included in the output
print(s) # with print(), \n produces a new line

print('C:\some\name') # here \n means newline!
print(r'C:\some\name')                              ##!!!

#%% using '''...''' with \
print("""\
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""")

#%% using '''...''' without \
print("""
Usage: thingy [OPTIONS]
-h Display this usage message
-H hostname Hostname to connect to
""")

#%% concatenation
3*'un' + 'ium'

"Py" 'thon'
## but
s1 = "Py"
s1
s1 'thon'   ## ERROR

#%%
txt = ('very long string nr1'
       'another very long string')
txt

#%%
(s1
 'thon')     ## ERROR

#%%
word = 'Python'
word[0]
word[5]
word[6]    ## IndexError: string index out of range

word[-1]
word[-6]
word[-7]   ## IndexError: string index out of range

word[0:2]
word[2:5]
word[-2:]

word[-2:2]  ## empty

word[-5:-2]

#%%
word[7]     ## IndexError: string index out of range
word[3:7]   ## OK

len(s1)

#%%
'''
### 3.1.3. Lists
'''
ll = [1,2,3,4,5]
ll[0]
ll[1:4]

ll + [11,12,13]
ll                      ## ll not changed !!!

ll.append([11,12,13])
ll                      ## ll changed !!!
## but the last element is a whole list [11,12,13], so we got NESTED list

#%%

letters = ['a','b','c','d','e','f','g']
letters
len(letters)

## subsetting
letters[2:5] = ['C','D','E']
letters

## deleting items
letters[2:5] = []
letters

## emptying the whole list
letters[:] = []
letters

## nesting lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]

#%%
'''
3.2 First Steps Towards Programming
-----------------------------------
'''

a, b = 0, 1
while b < 20:
    print(b)
    a, b = b, a+b

#%%
a, b = 0, 1
while b < 50:
    print(b, end=', ')
    a, b = b, a+b


