# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Fri Dec  8 11:50:11 2017

5. Reading and Writing Files
============================
"""
#%%
'''
Python distinguishes between
• text files ('t')
• binary files 'b')
If we don’t specify the file type, Python assumes we mean text files.
'''

#%% Prolog (from other sources)
# Checking if a File Exists
import os.path
from os import path

def check_for_file():
	print("File exists: ", path.exists("data.txt"))

check_for_file()  # in current dir

#%%
#%%
## Writing

f = open("test.txt", "tw")  ## open (&create if not exists) file to write ("w")
                           ## "t" means "text" and is default - no need to write it
f.write("first line\nsecond line")   ## writing sth to file using .write() method
                                     ## returns number of chars written
f
f.close()
f

#%%
## reading

f = open("test.txt", "r")   ## "r" for read
lines = f.readlines()
lines
type(lines)


longstring = f.read()
longstring
longstring = f.read()  ## BUT it works only ones!!! again some pointer/index is not restated
longstring

f.close()
f

#%%
## Use text file f as an iterable object: process one line in each iteration (important for large files):
f = open("test.txt", "r")

for line in f:
    print(line, end="")

#%%
## using context manager i.e. with()
with open('test.txt', 'r') as f:
    data = f.read()
## with automatically closes open files
data

## It is good practice to close a file as soon as possible !!!
del(lines)

with open('test.txt', 'r') as f:
    lines = f.readlines()
lines

#%%
## .split() method
help("".split)

ss = "This is a string which is quite long."

ss.split('is')
ss.split(' ')
ss.split()     ## space is default separator
ss.split('')   ## ERROR

#%%
## suppose we have a list of items

pwd
pwd()

with open('shopping_list.txt', 'tw') as f:
    f.write(
'''bread       1   1.39
tomatoes    6   0.26
milk        3   1.45
cofee       3   2.99
'''
    )

ls

## Write program that computes total cost per item, and writes to  shopping_cost.txt:

with open('shopping_list.txt', 'tr') as f:
    lines = f.readlines()
print(lines)

## check
for l in lines:
    print(l, end='')

#%%
## solution

fout = open('shopping_cost.txt', 'tw')
for l in lines:
    entry = l.split()
    item = entry[0]
    nr = int(entry[1])
    price = float(entry[2])
    # just to see
    out = [item, nr*price]
    print(out)
    #
    fout.write("{:20} {}\n".format(item, nr*price))
fout.close()

## check
with open('shopping_cost.txt', 'tr') as f:
    print(f.read(), end='')

#%%
##
with open('numbers.txt','tw') as f:
    f.write(
'''1 2 4 67 -34 340
0 45 3 2
17
'''
    )

#%%
def sumnum(fin, fout):

    with open(fin, 'r') as f:
        lines = f.readlines()

    with open(fout, 'w') as f:

        result = []
        for l in lines:
            nrs = l.split()
            s = 0
            for n in nrs:
                s = s + int(n)
            f.write("{}\n".format(s))
            result.append(s)

    with open(fout, 'r') as f:
        print(f.read())

    return(result)

sumnum('numbers.txt', 'numbers_sums.txt')


#%%


'''
197659
'''


#%%
'''
Reading and writing binary data is outside the scope of
this introductory module. If you need it, do learn about
the 'struct' module.
'''




