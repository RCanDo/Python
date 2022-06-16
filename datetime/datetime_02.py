#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Current Time and Date
subtitle:
version: 1.0
type: help, examples
keywords: [time, date, now, datetime, ]
description: |
remarks:
todo:
sources:
    - title: Python Get Current time
      link: https://www.programiz.com/python-programming/datetime/current-time
      date:
      authors:
          - nick:
            fullname:
            email:
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: datetime_2.py
    path: D:/ROBOCZY/Python/help/
    date: 2020-09-11
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

#%%
import numpy as np

#%% 1
import time

time.time()           # float
tt = time.time()
tt                    # costant

t = time.localtime()
t                     # constat
type(t)               # time.struct_time ==  .timetuple()            #!!! (*)
time.strftime("%H:%M:%S", t)
dir(t)

list(t)
tuple(t)

sum(t)
np.prod(t)


#%% 2
import datetime as dt
now = dt.datetime.now()
now
# run it few times - it's constant - the moment of creation
type(now)

now.strftime("%H:%M:%S")
now.strftime("%y-%m-%d")
now.strftime("%Y-%m-%d")

dir(now)
now.time()                # constant, only time
now.date()
now.toordinal()           # constant
now.today()               # changes - time of running                #!!!

now.timetuple()           # constatnt
type(now.timetuple())     # time.struct_time                         #!!! see (*) above

now.today().timetuple()   # changes
dict(now.today().timetuple())   #! TypeError: cannot convert dictionary update sequence element #0 to a sequence
list(now.today().timetuple())   # OK
tuple(now.today().timetuple())  # OK

sum(now.timetuple())      # constant                                 #!!!
sum(now.today().timetuple())   # changes

np.prod(now.today().timetuple())


#%% 3: Current time of a timezone
import pytz
dir(pytz)
pytz.all_timezones

tz_pl = pytz.timezone('Europe/Warsaw')
tz_pl
pytz.timezone('Poland')             # differet name but the same shift
now_pl = dt.datetime.now(tz_pl)
now_pl
now = dt.datetime.now()
now

tz_au = pytz.timezone('Australia/Sydney')
tz_au
now_au = dt.datetime.now(tz_au)
now_au

now_pl.today()
now.today()
now_au.today()     # not AU time... ???


#%%
