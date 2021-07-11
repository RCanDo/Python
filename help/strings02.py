# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:13:03 2021

@author: staar
"""

#%%
#%%
# 6. You can use "json.dumps()" to pretty-print Python dicts
#    as an alternative to the "pprint" module

# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
# {'b': 42, 'c': 12648430. 'a': 23}  #


# The "json" module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))
#{
#    "a": 23,
#    "b": 42,
#    "c": 12648430
#}

# Note this only works with dicts containing primitive types (check out the "pprint" module):
json.dumps({all: 'yup'}) #!!! TypeError: keys must be a string

## WHAT'S all TYPE ???

#%%
# In most cases I'd stick to the built-in "pprint" module though :-)
# https://pymotw.com/3/pprint/index.html
import pprint as pp

pp.pprint(my_mapping)
pp.pprint(my_mapping, indent=4, depth=1)  # ?
pp.pformat(my_mapping)  # ?

#%%
data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]

pp.pprint(data)  # what the hell... ???!!!
pp.pprint(data, indent=4)

#%% 25. Palindrome

def palindrome(a):
    return a == a[::-1]

palindrome('mom')
palindrome('mama')
palindrome('kobylamamalybok')

#%% 2. Anagrams
"""
This method can be used to CHECK IF two strings are anagrams.
An anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original letters
exactly once.
"""

from collections import Counter    #!!!

Counter("aabbbcddeeee")
Counter([1, 2, 1, 3, 2, 4, 3, 2, 1])

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb")
anagram("abcd3", "3acd")

#%%
#%% 5. Print a string N times without using loop

print("string"*2)

#%% 6. Capitalize first letters of every word

print("what the hell...!".title())

#%% 13. Decapitalize
"""
This method can be used to turn the first letter of the given string into lowercase.
"""
def decapitalize(ss):
    return ss[:1].lower() + ss[1:]

decapitalize('FooBar')

'FooBar'.lower()  # not the same!
'Foo Bar'.lower()
'Foo BAR'.lower()

#%% 11. Comma-separated
hobbies = ["basketball", "football", "swimming"]
print("My hobbies are:")
print(", ".join(hobbies))

#%% 12. Count vowels

import re  #!!!

def count_vowels(ss):
    return len(re.findall(r'[aeiouy]', ss, re.IGNORECASE))

count_vowels('foobar')
count_vowels('gym')

#%%
import re
len(re.findall('python','python is a programming language. python is python.'))

#%%
