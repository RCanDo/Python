#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: date & time
subtitle:
version: 1.0
type: tutorial
keywords: [date, time]
description: |
    About dates and time
remarks:
    - etc.
todo:
    - problem 1
sources:
      link: https://www.programiz.com/python-programming/datetime
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: D:/ROBOCZY/Python/datetime
    date: 2021-04-27
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import rcando.ak as ak
import os

ROOT = "E:/"
#ROOT = "~"
PYWORKS = os.path.join(ROOT, "ROBOCZY/Python")
##
WD = os.path.join(PYWORKS, "datetime")  ## adjust !!!
#DATA = os.path.join(ROOT, "Data/...")           ## adjust !!!

os.chdir(WD)
print(os.getcwd())

#%%
import datetime as dt
#import numpy as np

dir(dt)
#%%
dt.MINYEAR
dt.MAXYEAR

# %%
now = dt.datetime.now()
now
print(now)

today = dt.date.today()
today
print(today)
today.weekday()   # 0, 1, ..., 6  where  0 = Monday, ..., 6 = Sunday

# %%
d1 = dt.date(2021, 4, 12)
d1
print(d1)

len(d1)   #! ERROR
dir(d1)

d1.year
d1.month
d1.day
d1.resolution   # datetime.timedelta(days=1)
d1.ctime()      #  'Mon Apr 12 00:00:00 2021'
d1.isocalendar()   # (2021, 15, 1)
d1.isoformat()     # '2021-04-12'
d1.isoweekday()    # ISO:    1 = Monday, ..., 7 = Sunday,
d1.weekday()       # Python: 0 = Monday, ..., 6 = Sunday,
d1.timetuple()
 # time.struct_time(tm_year=2021, tm_mon=4, tm_mday=12, tm_hour=0, tm_min=0,
 #                  tm_sec=0, tm_wday=0, tm_yday=102, tm_isdst=-1)
d1.toordinal()     # 737892
d1.strftime('.')   #! big topic !

d1.replace(2022, 4, 12)  #? just new date... what's for?
d1  # unchanged

#%% methods inherited from dt.date - i.e. not specific for given date
d1.max # datetime.date(9999, 12, 31)
d1.min # datetime.date(1, 1, 1)
d1.today()  #! just today's date !

d1.today().weekday()
d1.fromisoformat('2021-04-12')
d1.fromordinal(1)    # datetime.date(1, 1, 1)
d1.fromordinal(1).ctime()  # 'Mon Jan  1 00:00:00 0001'
d1.fromordinal(737891)  # datetime.date(2021, 4, 11)
d1.fromordinal(737891).isoformat()  # '2021-04-11'
d1.fromtimestamp(.)

#%%
timestamp = dt.date.fromtimestamp(1326244364)
timestamp
print("Date =", timestamp)

#%%
#%%
t1 = dt.time()
t1    # datetime.time(0, 0)
print(t1) # 00:00:00

t2 = dt.time(11, 33, 56)
t2          # datetime.time(11, 33, 56)
str(t2)     # '11:33:56'
print(t2)   # 11:33:56

dt.time(hour = 11, minute = 34, second = 56)
dt.time(11, 34, 56, microsecond=234566)

#%%
dir(t2)
t2.dst()   #? see doc
t2.fold    #
t2.resolution   # datetime.timedelta(microseconds=1)
t2.isoformat()  # '11:33:56'
t2.tzinfo       # None
t2.tzname()     # None
t2.utcoffset()  # None
...

##
t2.max          # datetime.time(23, 59, 59, 999999)
t2.min          # datetime.time(0, 0)
t2.replace(.)
t2.fromisoformat(.)
t2.strftime(.)

#%%
## date and time together
dt1 = dt.datetime(2021, 4, 12, 17, 30, 15, 123456)
dt1   # datetime.datetime(2021, 4, 12, 17, 30, 15, 123456)
str(dt1)   # '2021-04-12 17:30:15.123456'
print(dt1) # 2021-04-12 17:30:15.123456

#%%
dir(dt1)
# all of the above + sth

dt1.timestamp()   #! 1618241415.123456  !!!

dt1.resolution    # datetime.timedelta(microseconds=1)
dt1.isoformat()   # '2021-04-12T17:30:15.123456'
...

#%%


#%%
#%% TIMEDELTA

t1 = dt.date(year = 2018, month = 7, day = 12)
t2 = dt.date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
t3   # datetime.timedelta(days=201)
print(t3)
dir(t3)
t3.total_seconds()   # 17366400.0

#%%
t4 = dt.datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = dt.datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
t6         # datetime.timedelta(days=-333, seconds=4460)
print(t6)  # -333 days, 1:14:20
abs(t6)    # datetime.timedelta(days=332, seconds=81940)
print(abs(t6))  # 332 days, 22:45:40

type(t3)   # datetime.timedelta
type(t6)   # datetime.timedelta
t3 - t6    # datetime.timedelta(days=533, seconds=81940)

#%%
td1 = dt.timedelta(seconds = 33)
td2 = dt.timedelta(seconds = 54)
td3 = td1 - td2
td3   # datetime.timedelta(days=-1, seconds=86379)
print(td3)       # -1 day, 23:59:39
print(abs(td3))  #!  0:00:21

#%%
dir(t6)
#! max unit is `days` !!!
# NO strftime() nor strptime() !!!

#%%
#%% strftime()  -- date/time to string
## is defined for  date, time, datetime  ONLY !!! NOT for timedelta

dt1
dt1.strftime('%Y')
dt1.strftime('%m')   # month
dt1.strftime('%d')   # day
dt1.strftime('%H')   # hour
dt1.strftime('%M')   # minutes
dt1.strftime('%S')   # seconds
dt1.strftime('%f')  # miliseconds ???

dt1.strftime("%d.%m.%Y, %H:%M:%S")

#%% strptime()  -- string to date/time

dt.datetime.strptime("21 June, 2018", "%d %B, %Y")

#%% timezone
...

#%%
"""
Directive	Meaning	                                Example
%a          Abbreviated weekday name.       		Sun, Mon, ...
%A          Full weekday name.                      Sunday, Monday, ...
%w          Weekday as a decimal number.            0, 1, ..., 6
%d          Day of the month as a zero-padded decimal.  01, 02, ..., 31
%-d         Day of the month as a decimal number.       1, 2, ..., 30
%b          Abbreviated month name. 				Jan, Feb, ..., Dec
%B          Full month name.                        January, February, ...
%m          Month as a zero-padded decimal number.  01, 02, ..., 12
%-m         Month as a decimal number.              1, 2, ..., 12
%y          Year without century as a zero-padded
            decimal number.         				00, 01, ..., 99
%-y         Year without century as a decimal number.   0, 1, ..., 99
%Y          Year with century as a decimal number.
				2013, 2019 etc.
%H
				Hour (24-hour clock) as a zero-padded decimal number.
				00, 01, ..., 23
%-H
				Hour (24-hour clock) as a decimal number.
				0, 1, ..., 23
%I
				Hour (12-hour clock) as a zero-padded decimal number.
				01, 02, ..., 12
%-I
				Hour (12-hour clock) as a decimal number.
				1, 2, ... 12
%p
				Locale’s AM or PM.
				AM, PM
%M
				Minute as a zero-padded decimal number.
				00, 01, ..., 59
%-M
				Minute as a decimal number.
				0, 1, ..., 59
%S
				Second as a zero-padded decimal number.
				00, 01, ..., 59
%-S
				Second as a decimal number.
				0, 1, ..., 59
%f
				Microsecond as a decimal number, zero-padded on the left.
				000000 - 999999
%z
				UTC offset in the form +HHMM or -HHMM.
%Z
				Time zone name.
%j
				Day of the year as a zero-padded decimal number.
				001, 002, ..., 366
%-j
				Day of the year as a decimal number.
				1, 2, ..., 366
%U
				Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.
				00, 01, ..., 53
%W
				Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.
				00, 01, ..., 53
%c
				Locale’s appropriate date and time representation.
				Mon Sep 30 07:06:05 2013
%x
				Locale’s appropriate date representation.
				09/30/13
%X
				Locale’s appropriate time representation.
				07:06:05
%%
				A literal '%' character.
				%
"""
#%%


#%%


#%%