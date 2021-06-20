#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Sorting
version: 1.0
type: examples
keywords: [sorted, sorting, reverse, ascending, descending, operator, itemgetter, attrgetter]
description: |
    Tutorial on sorting.
remarks:
todo:
sources:
    - title: Sorting HOW TO
      link: https://docs.python.org/3/howto/sorting.html#sortinghowto
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: sorting.py
    path: ~/Python/help/
    date: 2020-09-19
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando as ak
import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Works/Python"

os.chdir(PYWORKS + "/help/")
print(os.getcwd())

#%% Block delimiters allows to run separated blocks of code by one key-stroke
# e.g. Shift+Enter in Spyder

"""
link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""
import numpy as np
import pandas as pd

#pd.options.display.width = 0  # autodetects the size of your terminal window - does it work???
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
# pd.options.display.max_rows = 500         # the same
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 3)

#%% other df options
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500         # the same

# %%
#%% In short

sorted([5, 2, 3, 1, 4])
a = [5, 2, 3, 1, 4]
a.sort()
a

# list.sort() method is only defined for lists;
# the sorted() function accepts any iterable.
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs

sorted(xs.items(), key=lambda x: x[1])
## [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

sorted(xs, key=lambda x: x[1])  # IndexError: string index out of range
#! because
[x for x in xs]  # only indices

# Or:

import operator
sorted(xs.items(), key=operator.itemgetter(1))  #???

#%%
#%% Key Functions
sorted("This is a test string from Andrew".split(), key=str.lower)

"""
The value of the key parameter should be a function that takes a single argument
and returns a key to use for sorting purposes.
This technique is fast because the key function is called exactly once
for each input record.
"""
#%%
"""
A common pattern is to sort complex objects using some of the object’s indices as keys.
For example:
"""
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age

#%% The same technique works for objects with named attributes. For example:

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

student_objects

sorted(student_objects, key=lambda student: student.age)   # sort by age

#%% Operator Module Functions
from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(2))
sorted(student_tuples, key=itemgetter(2, 1))

## how itemgetter() works (it's constructor of an object)
ig2 = itemgetter(2)
ig2    # operator.itemgetter(2)
dir(ig2)
ig2([0, 1, 2])
ig2([[0,0], [1,1], [2,2]])
list(map(ig2, student_tuples))

#%% for objects use
sorted(student_objects, key=attrgetter('age'))
sorted(student_objects, key=attrgetter('age', 'grade'))

agage = attrgetter('age')
agage  # operator.attrgetter('age')
dir(agage)
agage(Student('john', 'A', 15))
agage(Student('john', 'A', 'fifteen'))
list(map(agage, student_objects))

#%% Ascending and Descending¶
sorted(student_tuples, key=itemgetter(2))
sorted(student_tuples, key=itemgetter(2), reverse=True)
sorted(student_tuples, key=itemgetter(2, 1))
sorted(student_tuples, key=itemgetter(2, 1), reverse=True)

sorted(student_objects, key=attrgetter('age'))
sorted(student_objects, key=attrgetter('age'), reverse=True)
sorted(student_objects, key=attrgetter('age', 'grade'))
sorted(student_objects, key=attrgetter('age', 'grade'), reverse=True)

#%% Sort Stability and Complex Sorts
"""
Sorts are guaranteed to be
[stable](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability).
That means that when multiple records have the same key,
their original order is preserved.
"""
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
sorted(data, key=itemgetter(0))
"""
Notice how the two records for blue retain their original order so that
('blue', 1) is guaranteed to precede ('blue', 2).
"""
#%%
"""
This wonderful property lets you build complex sorts in a series of sorting steps.
For example, to sort the student data by descending grade and then ascending age,
do the age sort first and then sort again using grade:
"""
student_objects
s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending

#%%
"""
This can be abstracted out into a wrapper function that can take a list
and tuples of field and order to sort them on multiple passes.
"""
def multisort(xs, specs):
    for key, reverse in reversed(specs):    #!!! reversed()
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs

multisort(list(student_objects), (('grade', True), ('age', False)))

"""
The Timsort algorithm used in Python does multiple sorts efficiently because
it can take advantage of any ordering already present in a dataset.
"""

#%% The Old Way Using Decorate-Sort-Undecorate
# https://docs.python.org/3/howto/sorting.html#the-old-way-using-decorate-sort-undecorate
"""
This idiom is called Decorate-Sort-Undecorate after its three steps:
 1. the initial list is decorated with new values that control the sort order.
 2. the decorated list is sorted.
 3. the decorations are removed, creating a list that contains only the initial values in the new order.
For example, to sort the student data by grade using the DSU approach:
"""

decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
decorated.sort()
[student for grade, i, student in decorated]               # undecorate

#%%
"""
This idiom works because tuples are compared lexicographically;
the first items are compared;
if they are the same then the second items are compared, and so on.

It is not strictly necessary in all cases to include the index i in the decorated list,
but including it gives two benefits:
 1. The sort is stable – if two items have the same key,
    their order will be preserved in the sorted list.
 2. The original items do not have to be comparable because the ordering of
    the decorated tuples will be determined by at most the first two items.
    So for example the original list could contain complex numbers
    which cannot be sorted directly.

Another name for this idiom is Schwartzian transform, after Randal L. Schwartz,
who popularized it among Perl programmers.

Now that Python sorting provides key-functions, this technique is not often needed.
"""

#%%


#%%


#%%



