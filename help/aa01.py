# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:01:16 2018

@author: akasprzy
"""

#%% fast notes
'''
list[:]  ## slice copy
list.pop()

################
## set operators

## on sets  {}
| & - 
a ^ b    ## symmetric diff. == no common elements

## on lists  []
and  or
## but there's no  A - B
##  and not   except   do not work


dict.keys() .values() .items()


str.center()
str.zfill()
str.ljust()
str.rjust()
str.upper()
str.capitalize()
str.counts()
str.endswith()
str.split()
str....()

'''

#%%
a = 1
b = 1.0

a == b    ## true
a is b    ## false

id(a)
id(b)

c = a
id(c)
a is c


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
#%%

r = range(256)
for i in r: print(i)

#%%
#%%

import math as m

#%%
def print_fun_tab(xx,f):
    for x in xx:
        print("{}({:7.2f}) = {:7.2f} ".format(f.__name__, x, f(x)))

xx = range(-3,3)
print_fun_tab(xx,m.sin)

#%%
#%%
### 5.1.3 List Comprehensions

squares = []
for x in range(10):
    squares.append(x**2)
squares

squares = list(map(lambda x: x**2, range(10)))
squares

squares = [x**2 for x in range(10)]
squares

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
## [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs

#%%
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]

# apply a function to all the elements
[abs(x) for x in vec]

# call a method on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
[weapon.strip() for weapon in freshfruit]

# create a list of 2-tuples like (number, square)
[(x,x**2) for x in range(6)]

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]  ## SyntaxError: invalid syntax ; File "<stdin>", line 1, in <module>

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec
[elem for elem in vec]
[num for elem in vec for num in elem]     ## !!! ??? from outermost to innermost

#%%
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

#%%
### 5.1.4 Nested List Comprehensions

matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
matrix

[[row[i] for row in matrix] for i in range(4)]

## equivalent to

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
transposed

## equivalent to

transposed = []
for i in range(4):
    trans_row = []
    for row in matrix:
        trans_row.append(row[i])
    transposed.append(trans_row)
transposed

'''
In the real world, you should prefer built-in functions to complex flow statements.
The zip() function would do a great job for this use case:
'''

list(zip(*matrix))
zip(*matrix)          ## ???
