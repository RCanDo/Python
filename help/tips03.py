# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:20:13 2021

@author: staar

https://allwin-raju-12.medium.com/50-python-one-liners-everyone-should-know-182ea7c8de9d
"""

#%% 1. Anagram

from collections import Counter

s1 = 'below'
s2 = 'elbow'

print('anagram') if Counter(s1) == Counter(s2) else print('not an anagram')

#%% 2.
# Binary to decimal
int('1010', 2)   # 10

# Octal to decimal
int('30', 8)     # 24

#%% 3. Converting string to lower case

"Hi my name is Allwin".casefold()                           #!!!
# 'hi my name is allwin'

"""
casefold() method of builtins.str instance
    Return a version of the string suitable for caseless comparisons.
i.e. == .lower()
"""

#%% 5. Converting string to byte

"convert string to bytes using encode method".encode()
# b'convert string to bytes using encode method'

#%% 38. Get a string of lower-case alphabets

import string; print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz

#%% 39. Get a string of upper case alphabets

import string; print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

#%% 40. Get a string of digits from 0 to 9

import string; print(string.digits)
# 0123456789

#%% 42. Human readable DateTime

import time; print(time.ctime())
# Thu Aug 13 20:16:23 2020

#%% 47. Remove numbers from a string

''.join(list(filter(lambda x: x.isalpha(), 'abc123def4fg56vcg2')))
# abcdeffgvcg



#%% 6. Copy files

import shutil
shutil.copyfile('source.txt', 'dest.txt')

#%% 24. Write to a file using the print statement

print("Hello, World!", file=open('file.txt', 'w'))



#%% 7. Quicksort
def qsort(l):
     return l if len(l)<=1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])

#%% 10. Fibonacci series

def fib(x):
    return x if x<=1 else fib(x-1) + fib(x-2)

#%% 34. Get quotient and remainder
quotient, remainder = divmod(4,5)


#%% 11. Combine nested lists to a single list

[item for sublist in main_list for item in sublist]             #???

#%% 16. Longest string from a list

words = ['This', 'is', 'a', 'list', 'of', 'words']

max(words, key=len)# 'words'
sorted(words, key=len)# 'words'


#%% 25. Count the frequency of a given character in a string

print("umbrella".count('l'))

#%% 26. Merge two lists

list1.extend(list2)# contents of list 2 will be added to the list1

#%% 27. Merge two dictionaries

dict1.update(dict2)
# contents of dictionary 2 will be added to the dictionary 1

#%% 28. Merge two sets

set1.update(set2)
# contents of set2 will be copied to the set1

#%% 30. Most frequent element

lst = [9, 4, 5, 4, 4, 5, 9, 5, 4]
lst.count(9)
max(set(lst), key=lst.count)





#%% 44. Sort dictionary with keys

d = {'one': 1, 'four': 4, 'eight': 8}
{key: d[key] for key in sorted(d.keys())}
# {'eight': 8, 'four': 4, 'one': 1}

#%% 45. Sort dictionary with values

# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

