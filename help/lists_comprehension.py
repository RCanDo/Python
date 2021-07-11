# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:16:53 2021

@author: staar
"""

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

#%% Space Separated integers to a List
['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0
  else 'Buzz' if i%5==0 else i for i in range(1,20)]

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
[x, x**2 for x in range(6)]     #! SyntaxError: invalid syntax ; File "<stdin>", line 1, in <module>

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
vec
[elem for elem in vec]
[num for elem in vec for num in elem]     ## !!! ??? from outermost to innermost
[num for num in elem for elem in vec]     #! NameError: name 'elem' is not defined

#%%
from math import pi
[str(round(pi, i)) for i in range(1, 6)]

#%%
### 5.1.4 Nested List Comprehensions

matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
matrix

[[row[i] for row in matrix] for i in range(4)]                                  #!!!

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

list(zip(*matrix))                                                              #!!!
[list(l) for l in list(zip(*matrix))]

zip(*matrix)          ## ???
