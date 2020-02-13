# -*- coding: utf-8 -*-
"""
title: datetime
subtitle: based on datetime docs
author: kasprark
date: Wed Apr 25 10:17:59 2018

"""

import datetime as dt

#%%
today = dt.date.today()
today   # datetime.date(2007, 12, 5)
dir(today)

ttd = today.timetuple()
ttd

dir(ttd)

#%%
import time

tt = time.time()
tt
type(tt)

today == dt.date.fromtimestamp(time.time())    # True

#%%
my_birthday = dt.date(today.year, 6, 24)

if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
my_birthday

#%%
dt.date(2008, 6, 24)
time_to_birthday = abs(my_birthday - today)
type(time_to_birthday)
dir(time_to_birthday)

time_to_birthday.days
time_to_birthday

print(time_to_birthday.days)


#%%
d = dt.date.fromordinal(730920) # 730920th day after 1. 1. 0001
d
dt.date(2002, 3, 11)

#%%
t = d.timetuple()
for i in t: print(i)
"""    
2002                # year
3                   # month
11                  # day
0
0
0
0                   # weekday (0 = Monday)
70                  # 70th day in the year
-1
"""

#%%

ic = d.isocalendar()
for i in ic: print(i)

"""
2002                # ISO year
11                  # ISO week number
1                   # ISO day number ( 1 = Monday )
"""

#%%
d.isoformat()  # '2002-03-11'
d.strftime("%d/%m/%y")  # '11/03/02'
d.strftime("%A %d. %B %Y")      # 'Monday 11. March 2002'
'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
# 'The day is 11, the month is March.'

#%%
# from datetime import datetime, date, time

# Using datetime.combine()
d = dt.date(2005, 7, 14)
d
t = dt.time(12, 30)
t
dt.datetime.combine(d, t)
dt.datetime(2005, 7, 14, 12, 30)
# Using datetime.now() or datetime.utcnow()
dt.datetime.now()   
dt.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
dt.datetime.utcnow()   
dt.datetime(2007, 12, 6, 15, 29, 43, 79060)

#%%
# Using datetime.strptime()
sdt = dt.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
sdt
dt.datetime(2006, 11, 21, 16, 30)

# Using datetime.timetuple() to get tuple of all attributes
tt = sdt.timetuple()
tt

for it in tt: print(it)
"""
2006    # year
11      # month
21      # day
16      # hour
30      # minute
0       # second
1       # weekday (0 = Monday)
325     # number of days since 1st January
-1      # dst - method tzinfo.dst() returned None
"""

# Date in ISO format
ic = sdt.isocalendar()
for it in ic:   print(it)
"""
2006    # ISO year
47      # ISO week
2       # ISO weekday
"""

# Formatting datetime
sdt.strftime("%A, %d. %B %Y %I:%M%p")
# 'Tuesday, 21. November 2006 04:30PM'

'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time")
# 'The day is 21, the month is November, the time is 04:30PM.'

#%%

from datetime import timedelta, datetime, tzinfo


class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1) + self.dst(dt)
    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime(dt.year, 4, 1)   # ends last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)
    def tzname(self,dt):
         return "GMT +1"


class GMT2(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=2) + self.dst(dt)
    def dst(self, dt):
        d = datetime(dt.year, 4, 1)
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)
    def tzname(self,dt):
        return "GMT +2"


gmt1 = GMT1()
# Daylight Saving Time
dt1 = datetime(2006, 11, 21, 16, 30, tzinfo=gmt1)
dt1.dst()
datetime.timedelta(0)
dt1.utcoffset()
datetime.timedelta(0, 3600)
dt2 = datetime(2006, 6, 14, 13, 0, tzinfo=gmt1)
dt2.dst()
datetime.timedelta(0, 3600)
dt2.utcoffset()
datetime.timedelta(0, 7200)
# Convert datetime to another time zone
dt3 = dt2.astimezone(GMT2())
dt3     
datetime.datetime(2006, 6, 14, 14, 0, tzinfo=<GMT2 object at 0x...>)
dt2     
datetime.datetime(2006, 6, 14, 13, 0, tzinfo=<GMT1 object at 0x...>)
dt2.utctimetuple() == dt3.utctimetuple()
True

