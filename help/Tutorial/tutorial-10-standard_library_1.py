# -*- coding: utf-8 -*-
"""
title: Python Tutorial Release 3.6.3
subtitle: based on "tutorial.pdf" (book) by Guido van Rossum and the Python development team
author: kasprark
date: Tue Jan  9 11:10:29 2018


10. STANDARD LIBRARY
====================
(p. 81)
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
10.1 Operating System Interface
-------------------------------
The os module provides dozens of functions for interacting with the operating system:
'''
import os
dir(os)
help(os)   ## returns an extensive manual page created from the module's docstrings

os.getcwd()
os.chdir('..')
os.getcwd()
ls                         ## what is the os.command for this???  e.g. see below `import glob`
os.chdir('./Tutorial')

os.system('mkdir directory')
ls
os.system('rmdir directory')
ls


'''
For daily file and directory management tasks, 
the shutil module provides a higher level interface that is easier to use:
'''
import shutil
## e.g.
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

#%%
'''
10.2 File Wildcards
-------------------
The glob module provides a function for making file lists from directory wildcard searches:
'''
import glob

glob.glob('*.py')

#%%
'''
10.3 Command Line Arguments
---------------------------
Common utility _scripts_ often need to process command line arguments. 
These arguments are stored in the `sys` module’s `argv` attribute as a list. 
For instance the following output results from running python `demo.py` one two three at the command line:
'''
import sys
print(sys.argv)

'''
The `getopt` module processes `sys.argv` using the conventions of the Unix getopt() function. 
More powerful and flexible command line processing is provided by the `argparse` module.
'''
import getopt
import argparse

#%%
'''
10.4 Error Output Redirection and Program Termination
-----------------------------------------------------
The `sys` module also has attributes for `stdin`, `stdout`, and `stderr`. 
The latter is useful for emitting _warnings_ and _error messages_ 
to make them visible even when stdout has been redirected:
'''
sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
'''
    The most direct way to terminate a script is to use  `sys.exit().`
'''
#%%
'''
10.5 String Pattern Matching
----------------------------
'''
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.findall('\bf[a-z]*', 'which foot or hand fell fastest')    ## without r ???

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')         ## reducing double words 

#%%
'''
10.6 Mathematics
----------------
The `math` module gives access to the underlying C library functions for floating point math:
'''
import math
math.cos(math.pi/4)
math.log(1)
math.log(0)      ##  ValueError: math domain error     --  SHIT!!!!!
math.log(math.exp(1))
math.log(math.e)
math.exp(1j*math.pi)            ## TypeError: can't convert complex to float

import random
random.choice(['apple','pear','banana'])

random.sample(range(100),10)    ## sampling without replacement
random.random()                 ## random float
random.randrange(6)             ## random integer chosen from range(6)

'''
The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:
'''

import statistics
data = random.sample(range(100),10)
data
statistics.mean(data)
statistics.median(data)
statistics.variance(data)
statistics.mode(data)           ## StatisticsError: no unique mode; found 10 equally common values  -- SHIT!!!!!!!!!!!

import scipy                    ## many other modules for numerical computations.  

#%%
'''
10.7 Internet Access
--------------------
There are a number of modules for accessing the internet and processing internet protocols. 
Two of the simplest are `urllib.request` for retrieving data from URLs and `smtplib` for sending mail:
...    
'''

#%%
'''
10.8 Dates and Times
--------------------
'''
from datetime import date
now = date.today()
now
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1975, 12, 4)
age = now - birthday
age.days


#%%
'''
10.9 Data Compression
---------------------
Common data archiving and compression formats are directly supported by modules including: 
zlib, gzip, bz2, lzma, zipfile and tarfile.
'''
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)


#%%
'''
10.10 Performance Measurement
-----------------------------
'''
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()

'''
In contrast to timeit’s fine level of granularity, the `profile` and `pstats` modules provide tools 
for identifying time critical sections in larger blocks of code.
'''

#%%
'''
10.11 Quality Control
---------------------
'''
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()

#%%
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()

#%%
'''
10.12 Batteries Included
------------------------
'''