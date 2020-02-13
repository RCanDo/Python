# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:39:42 2019

@author: kasprark
"""

#%%
"""
https://stackoverflow.com/questions/16060899/alphabet-range-on-python
"""

#%%

import string

dir(string)
help(string)

string.ascii_lowercase

string.ascii_lowercase[5]
string.ascii_lowercase[:6]

string.ascii_lowercase[::-1]

list(string.ascii_lowercase[:6])

string.ascii_uppercase
string.ascii_letters

#%%

list(map(chr, range(97, 123))) 

list(map(chr, range(ord('a'), ord('z')+1)))


#%%

def letter_range(start, stop="{", step=1):
    """Yield a range of lowercase letters.""" 
    for ord_ in range(ord(start.lower()), ord(stop.lower()), step):
        yield chr(ord_)
        
list(letter_range("a", "f"))        

list(letter_range("a", "f", step=2))

#%%
#%% combinations of numbers and letters
"""
https://stackoverflow.com/questions/4719850/python-combinations-of-numbers-and-letters
"""

# doesn't work
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

#%% 
        
[k for k in product('ABCD', 'xy')]

#%%

def lists_grid(l1, l2):
    return [[str(i) + str(j) for i in l1] for j in l2]

np.array(lists_grid(['a', 'b', 'c'], [1, 2, 3, 4])).ravel()






