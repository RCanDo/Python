# -*- coding: utf-8 -*-
"""
title: Python For Computational Science And Engeneering
subtitle: based on "Python For Computational Science And Engineering (431sl).pdf" (slides) by Hans Fangor
author: kasprark
date: Mon Dec 11 10:48:22 2017

6. Exceptions
=============
"""

import sys

pwd
cd C:/PROJECTS/Python/tuts/PFCSAE
ls



#%%
##

def myread(file):
    try:
        f = open(file,'r')
    except FileNotFoundError:
        print("The file couldn't be found. " +
              "This program stops here."
              )
        sys.exit(1)     # a way to exit the program

    for l in f:
        print(l,end='')
    f.close()

#%%

myread('file')

%tb

myread('shopping_cost.txt')

#%%

def myread2(file):
    try:
        f = open(file,'r')
    except OSError as error:
        print("The file couldn't be found. " +
              "This program stops here."
              )
        print("Details: {}".format(error))
        sys.exit(1)     # a way to exit the program

    for l in f:
        print(l,end="")
    f.close()

#%%
myread2('file')

%tb

myread('shopping_cost.txt')

#%%
def myread3(file=''):
    nq = True
    while nq:
        try:
            f = open(file,'r')
            nq = False
            print(f.read())
        except OSError as error:
            print("The file {} couldn'd be found. ".format(file))
            print("Details: {}".format(error))
            nq = input("Continue? [y/n]: ")
            nq = nq == 'y'
            if nq:
                file = input("Give another file name: ")


myread3()

#%%
## summing numbers in lines (from a given file); if no number then put 0;

## exammple file

file = "not_only_numbers.txt"

f = open(file,'w')
f.write(
'''1 4 5 _ 3 + 1
1 3 4 n
q w e
0 _
''')
f.close()

with open(file,'r') as f:
    print(f.read())

#%%
def sumnum(file):
'''
summing numbers in lines (from a given file); if no number then put 0;
'''
    result = []
    with open(file,'r') as f:
        for l in f.readlines():
            s = 0
            ns = l.split()
            for n in ns:
                try:
                    s = s + int(n)
                except:
                    s
                    print("NaN: {}".format(n))
            result.append(s)
    print(result)
    return result

sumnum(file)



