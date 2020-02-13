# -*- coding: utf-8 -*-
"""
title: Python Tutorial Release 3.6.3
subtitle: based on "tutorial.pdf" (book) by Guido van Rossum and the Python development team
author: kasprark
date: Thu Jan  4 16:50:56 2018


6. MODULES
==========
(p. 43)
"""
## •

%reset

pwd
cd c:/PROJECTS/Python/tuts/Tutorial/
ls

import importlib ## may come in handy

# importlib.reload(fibo)

#%%
'''
6.1 More on Modules
-------------------
'''

import fibo
fibo.__name__

fibo.fib(1000)

fibo.fib2(1000)

fib = fibo.fib

fib(1000)

#%%
'''
6.2 Standard Modules
--------------------
'''

import sys

sys.path    ## where Python looks for modules

sys.path.append('c:/PROJECTS/Python/tuts/Tutorial/')
sys.path.pop()

sys.ps1
sys.ps2

sys.stdout

#%%
'''
6.3 The dir() Function
----------------------
'''
dir(fibo)

dir(sys)

dir()

'''
dir() does not list the names of built-in functions and variables.
If you want a list of those, they are defined in the standard module builtins:
'''
import builtins
dir(builtins)

#%%
'''
6.4 Packages
------------
'''

#%%



