# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Wed Dec 13 12:31:12 2017

13. Dictionaries
================
"""
## •

## Dictionaries are also called “associative arrays” and “hash tables”.

#%%
## Dictionaries are unordered sets of key-value pairs.
## An empty dictionary can be created using curly braces:

d = {}
d

d['today'] = '22 deg C'
d
d['yesterday'] = '19 deg C'
d

d[0]   ## KeyError

list(d) #!!!  only keys !!!
list(d)[0]

d['today']
d['yesterday']
d['tomorow']        ## KeyError: 'tomorow'

#%%

d.keys()
type(d.keys())  ## dict_keys

isinstance(d.keys(), list)  ## False

d.keys()[0]     ## TypeError: 'dict_keys' object does not support indexing

list(d.keys())     ## OK
list(d.keys())[1]  ## OK

#%%

order = { 'Peter' : 'Pint of bitter' ,
          'Paul' : 'Half pint of Hoegarden' ,
          'Mary' : 'Gin Tonic'
        }

order

for person in order.keys():
    print("{:6s} requests {} ".format(person, order[person]))

#%%
## Iterate over the dictionary itself is equivalent to iterating over the keys. Example:

# iterating over keys:
for person in order.keys():
    print(person, "requests", order[person])

# is equivalent to iterating over the dictionary:
for person in order:
    print(person, "requests", order[person])

#%%
'''
Some more technicalities:

• The dictionary key can be any (immutable) Python object.
  This includes:
    • numbers
    • strings
    • tuples.
Dictionaries are very fast in retrieving values (when given the key)

• Python provides dictionaries
    • very powerful construct
    • a bit like a data base (and values can be dictionary objects)
    • fast to retrieve value
    • likely to be useful if you are dealing with two lists at the same time
      (possibly one of them contains the keyword and the other the value)
    • useful if you have a data set that needs to be indexed by strings or tuples (or other IMMUTABLE objects)
'''