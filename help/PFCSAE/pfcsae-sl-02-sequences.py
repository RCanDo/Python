# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Thu Dec  7 10:35:02 2017


2. Sequences
============
"""

#%%
## strings (immutable)
## lists (mutable)
## tupels (immutable)
## arrays (mutable, part of numpy)

#%%
'''
strings
-------
'''

s = "string"
s
print(s)
type(s)
len(s)

ss = '''a very
long
text
'''
ss
print(ss)
len(ss)

## you may use " and ' interchangeably; moreover
sq = "I'm O'conor is possible"
print(sq)

sp = 'the quotes "QUOTES" too'
sp

sp + sq
print(sp + sq)
print(sq + sp)

ss + sq
print(ss + sq)

print(ss*3)
3*s

## strings are like lists

s[0]
s[1]
s[len(s)]  #!!!  bang!!!
s[len(s)-1]  #!!!

s[0]
s[0:1]     ## JUST FIRST LETTER
s[0:2]     ## when you pass range then the right limit is "open" i.e. not included

s[range(len(s))]  ## TypeError: string indices must be integers
s[0:len(s)]

s[:len(s)]
s[0:]
s[1:]

s[0:len(s)-1]
s[1:len(s)-1]

s[-1]           ## first element from right
s[1]            ## not a first element!, the second in fact!!!
s[-0]           ## first element
s[-2]           ## second from right
s[2]            ## third from left

#%%
# checking includes

's' in s
'tr' in s
'ss' in s
not 'ss' in s
'ss' not in s


#%%
'''
### Exercise - strings
'''
ss = '''My first look at Python was an
accident, and I didn't much like what
I saw at the time
'''

dir(ss)

## count the numbers of (i) letters 'e' and (ii) substrings 'an'
ss.count('e')
ss.count('an')

## replace all letters 'a' with 'o'
print(ss.replace('a','o'))

## make all uppercase
print(ss.upper())

## revert case
print(ss.swapcase())

#%%
## strings are immutable
sp
sp[0]
sp[0] = 's'  ## TypeError: 'str' object does not support item assignment

#%%
'''
Lists
-----
'''

#%% !!!!!!!!!!!!!!
'''
Lists indexing - BE CAREFUL as indexing starts from 0 !!!
'''

## and range(n) means 0,...,n-1 i.e. integers in [0,n)
ll = list(range(5))
print(ll)
ll[4]
ll[len(ll)]  ## ERROR
ll[len(ll)-1]
ll[0]
ll[1]

## BUT
for k in range(len(ll)):   ## here you od not have to subtract 1
    print(k)

## more on this in Iterators (below) and in Loops (next file)
## !!!!!!!!!!!!!!!!

#%%
## 

[]          ## empty list
len([])
l = []
len(l)
print(l)
l[0]        ## IndexError: list index out of range

l1 = [42]
print(l1)
print(l1[0])
l1[1]       ## IndexError: list index out of range

l2 = [5,l1,2,'hello',range(3)]
l2

#%%
## Lists are MUTABLE (changeable)
l1[0]
l1[0] = 44
l1

l2
l2[1]
l2[1] = [1,2]
l2

#%%
## btw:
type(range(3))      ## range
rng = range(3)
print(rng)

rng.               ## ???

#%%
l2[0]
type(l2[0])
l2[0][0]    ## TypeError: 'int' object is not subscriptable


l2[1]
l2[1][0]

## slice
l2[0:1]
type(l2[0:1])
type(l2[0:1][0])

## list of lists

ll = [[1,2],[3,4],[5,6]]
print(ll)
ll[1][1]
ll[1,1]     ## TypeError: list indices must be integers or slices, not tuple

## list.append()

l2.append(['qq',2,(1,2)])
l2
l2[5][2]        ## this is tuple !!!
l2[5][2][1]


max(l2) ## TypeError: '>' not supported between instances of 'list' and 'int'
max(ll)
max(max(ll))
min(ll)

ll2 = [ [1,6] , [2,5] , [3,4] ]
min(ll2)
max(ll2)
min(ll2[0])

[1,6] in ll2
6 in ll2            ## false

## hence checking inclusions works only on the first level

#%%
## Lists arithmetic

l1
l2
ll
ll2

ll*3
l*3
ll + ll2

ll + 1  ## TypeError: can only concatenate list (not "int") to list  -- this is CONCATENATION!!!
1 + ll  ## TypeError: unsupported operand type(s) for +: 'int' and 'list'

l2 + [1]  ## OK !!!    Compare it with tuples below
## the same as append
l2.append(1) ## but this is permanent (no need for doing assignment)
l2

#%%
## LIST COMPREHENSIONS -- generating lists

## NOTICE that things like this (from R or Matlab) doesn't work:
1:10            ## SyntaxError: illegal target for annotation
[1:10]          ## SyntaxError: invalid syntax
## : works only on slices for already defined list

range(3)  ## it works but it's not a sequence 0,1,2 as a list;
## you cannot even see it as a sequence:
r = range(3)
r
type(r)

## !!! simplest solution
list(range(10))

## BUT you may also do sth like this

l3 = [k for k in range(10)]  ## this is LIST COMPREHENSION
l3

l4 = [k for k in range(-2,2)]
l4

[2*k for k in range(10)]

[k for k in range(20) if k%2==0]  ## the same as above

## BE CAREFULL WITH SIZE!!!YOU MAY FILL UP THE WHOLE MEMORY!!! eg
# [k for range(10**100) ]  ## DO NOT RUN!!!!


#%%
'''
Tuples
------
'''

## Tuples are IMMUTABLE !!! (unchangeable)

t = (1,20,3e3,'jazz')
t
type(t)

t[0]
t[2]
t[3]

## try changing value
t[0] = 0        #!#!  TypeError: 'tuple' object does not support item assignment
## Tuples are IMMUTABLE !!! (unchangeable) what makes them less convienient but FASTER !!!

## beside this they are like lists
len(t)
max(t)
max(t[:3])

t*3
t + t
t + 1    ## TypeError: can only concatenate tuple (not "int") to tuple
         ## compare with lists (above)
t + (1)  ## TypeError: can only concatenate tuple (not "int") to tuple
t + (1,) #!#!#!  THAT'S OK!!!

#%%
tt = ( t , ll )
tt
## try changing value in internal list
tt[1][0][0]
tt[1][0][0] = 0         ## NO ERROR!!!

## i.e.
## It is not possible to change tuple's element but it IS POSSIBLE to change values within this elements
t2 = (0,[1],[(2,)],[([3],)])
t2

t2[0] = 1  ## ERROR
t2[1] = 0  ## ERROR
t2[1][0] = 0  ## OK !!!
t2


tt
##
#%%
## tuples are defined just by commas
t4 = 1,2,3,4
t4

#%%
## tuples are addressed like lists

t4[:3]
t4[2:]
t4[1:4]

#%%

x,y,z = 0,-1,1
x,y,z
x
y
z

x,y,z,s = t4
x,y,z,s
x
y
z
s

## this allows instantaneous swap of values:
x,y = y,x
x
y

#%%
## functions may return tuples

def funt(a=1,b=2):
    return b,a

funt()
funt(0,1)

p,q = funt(0,1)
p,q




#%%
## How to generate big tuple?

## !!!
tuple(range(10))

## maybe?
t3 = (k for k in range(10))     ## generator !!!
t3
type(t3)  ## generator! this is not a tuple...

t3(1)   ## TypeError: 'generator' object is not callable
t3[1]   ## TypeError: 'generator' object is not subscriptable

[k for k in t3]  ## works!
[k for k in t3]  #!#!#! BUT ONLY ONCE !!!
## it means that ...

for k in t3:    print(k)
## nothing...

def ff1(): 
    for k in t3: 
        print(k)

ff1() ## nothing...

#%%
'''
list and tuple comprehension
----------------------------
'''

## TUPLE COMPREHENSION
tuple(k for k in range(10))    ## great!!

tuple(t3)           ## empty...
len(tuple(t3))      ## 0

gen = (k for k in range(10))    ## generator !!!
tuple(k for k in gen)       ## works!
tuple(k for k in gen)       ## BUT only ONCE !!!

gen = (k for k in range(10))    ## generator !!!
tuple(gen)                  ## works!
tuple(gen)                  ## BUT only ONCE !!!

#%%
## LIST COMPREHENSION
list(k for k in range(10))

gen = (k for k in range(10))    ## generator !!!
list(k for k in gen)       ## works!
list(k for k in gen)       ## BUT only ONCE !!!

gen = (k for k in range(10))    ## generator !!!
list(gen)                  ## works!
list(gen)                  ## BUT only ONCE !!!



#%%
'''
iterators: tuple(), list() and iter()
------------------
'''

r = range(10)
type(r)

## in general 'range' is iterator

## list and tuple from iterator
list(r)
list(r)   ## works many times unlike `generators` !!!
tuple(r)

r = range(-3,3)
list(r)
tuple(r)
list(tuple(r))
tuple(list(r))

r = range(-3,3,2)   ## (start,stop,step)
list(r)

#%%
## tuple from list
tuple(10)       ## TypeError: 'int' object is not iterable
tuple([10])     ## OK, one element tuple
tuple([10,11])  ## OK

#%%
## list from tuple
list(10)        ## TypeError: 'int' object is not iterable
list((10,))     ## OK, one element list
list((10,11))

#%%
## iterator from list
itr = iter([1,2,4,7,9])
itr
type(itr)  ##   list_iterator  
## and back: list from iterator
list(itr)
list(itr)   ## BUT ONLY ONCE !!!
            
## so it's the same behaviuor as in case of `generator`:

t3 = (k for k in range(10))     ## generator !!!
t3
type(t3)  ## generator! this is not a tuple...

[k for k in t3]  ## works!
[k for k in t3]  #!#!#! BUT ONLY ONCE !!!

##

## you  must recreate list_iterator
tuple(itr)
tuple(itr)  ## ONLY ONCE !!!

## if you recreate generator 
t3 = (k for k in range(10))
tuple(t3)
tuple(t3)


#%%
## iterator from tuple
itrt = iter((1,2,4,7,9))  
itrt
type(itrt)  ## tuple_iterator
## and back: tuple from iterator
tuple(itrt)
tuple(itrt)   ## BUT ONLY ONCE !!!
## you  must recreate iterator
list(itrt)
list(itrt)  ## ONLY ONCE !!!

## HENCE
## * iterator can be made out of tuple or list
## * list and tuple can be made out of iterator,
## * iterators remember their state
##   How to change this state without recreating iterator???

