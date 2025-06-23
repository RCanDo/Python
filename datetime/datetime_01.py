#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Time and Date
subtitle:
version: 1.0
keywords: [time, date, now, datetime, ]
sources:
    - title: time
      link: https://docs.python.org/3/library/time.html
    - title: datetime.timezone
      link: https://docs.python.org/3/library/datetime.html#timezone-objects
    - title: datetime.datetime
      link: https://docs.python.org/3/library/datetime.html#datetime-objects
    - title: datetime.timedelta
      link: https://docs.python.org/3/library/datetime.html#timedelta-objects
remarks:
    - Read the intro to `time` library (1st source).
    - GMT – Greenwich Mean Time, nowadays called:
    - UTC – Coordinated Universal Time;
    - DST – Daylight Saving Time,
      eg. for Poland (and most of EU) it is CET (Central European Time) which is UTC+01:00
      and additionally there is +1 hour at summer
      i.e. UTC+02:00 and this is called CEDT (Central European Daylight Time) or CEST (Central European Summer Time);
    - epoch – the point where the time starts:
      1970-01-01, 00:00:00 (UTC) on all platforms,
      the return value of `time.gmtime(0)`;
    - timestamp – number of seconds since epoch, i.e. since 1970-01-01, 00:00:00
      always and only UTC/GMT (hence no DST);
    - However, in some libraries (e.g. Pandas) "timestamp" is called "epoch", i.e.
      "epoch" means "seconds since 1970-01-01, 00:00:00 (UTC)"...
      Beware!
file:
    date: 2018-04-25
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

# %%
# %%
import time

t = time.time()
t                 # ! timestamp i.e. float
# !!! returns timestamp of the current GMT/UTC !!!

lt = time.localtime()
lt
# time.struct_time(tm_year=2024, tm_mon=11, tm_mday=9, tm_hour=19, tm_min=52, tm_sec=36, tm_wday=5, tm_yday=314, tm_isdst=0)
# compare with
time.gmtime()
# see  timezone_01.py  for more on time zone – it's important and tricky :(

type(lt)    # time.struct_time  ~=  named tuple
list(lt)    # [2024, 11, 9, 19, 52, 36, 5, 314, 0]
tuple(lt)   # (2024, 11, 9, 19, 52, 36, 5, 314, 0)
dict(lt)    #! TypeError:  ...

# %%
time.strftime("%H:%M:%S", lt)               # '19:52:36'
time.strftime("%Y-%m-%d %H:%M:%S", lt)      # '2024-11-09 19:52:36'
time.strftime("%Y-%m-%d %H:%M:%S %z", lt)   # '2024-11-09 19:52:36 +0100'

time.strptime('2024-11-09 19:52:36', "%Y-%m-%d %H:%M:%S")  # time.struct_time(tm_year=2024, tm_mon=11, tm_mday=9, tm_hour=19, tm_min=52, tm_sec=36, tm_wday=5, tm_yday=314, tm_isdst=-1)

# %%
# %%
import datetime as dt

# %%
# %%  datetime.datetime
dt.datetime     # class  datetime.datetime
dir(dt.datetime)
dt.datetime(2024, 4, 6, 10, 26, 27, 988654)    # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)

d = dt.datetime.now()       # current date and time
d = dt.datetime.today()     # exactly the same
d   # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)
# see next file  datetime_02.py

d.tzinfo        # None – no Time Zone
d.utcoffset()   # None
"""
! Remember !
By default  datetime.datetime  obj is time-zone unaware,
however it works exactly the same way as if time zone was set to local TZ.
Local TZ and DST are taken from OS if .tzinfo is None.
The same for  time  lib.

However,
e.g. in Pandas  pd.Timestamp  object works by default (i.e. when .tzinfo is None)
as if the obj represented  UTC/GMT time.

see  timezone_01.py, timezone_pandas.py  for more info on this (quite a complicated stuff).
"""

# %%  string representation
print(d)                #  2024-04-06 10:26:27.988654

# ISO
d.isoformat()           # '2024-04-06T10:26:27.988654'
help(d.isoformat)
d.isoformat(sep=' ')    # '2024-04-06 10:26:27.988654'
d.isoformat(' ')        # '2024-04-06 10:26:27.988654'
d.isoformat(' | ')      # ! TypeError: isoformat() argument 1 must be a unicode character, not str
dt.datetime.fromisoformat('2024-04-06 10:26:27.988654')
    # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)
dt.datetime.fromisoformat('2024-04-06 10:26:27.988654+01:00')
    # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654, tzinfo=datetime.timezone(datetime.timedelta(seconds=3600)))

# .strftime()  and  .strptime()  works the same as in time lib
d.strftime("%H:%M:%S")  # '20:22:24'
d.strftime("%y-%m-%d")  # '24-11-10'
d.strftime("%Y-%m-%d")  # '2024-11-10'
d.strftime("%Y-%m-%d %H:%M:%S %z")  # '2024-11-10 20:22:24 '  no time zone by default,
# to make it time zone aware (local!):
d.astimezone().strftime("%Y-%m-%d %H:%M:%S %z")     # '2024-11-10 20:22:24 +0100'

# %%
dir(d)
d.time()            # datetime.time(20, 22, 24, 349267)   # the same as  dt.time()  see below
d.date()            # datetime.date(2024, 11, 10)
d.toordinal()       # 739200  nr of days since 0000-01-01
dt.datetime.fromordinal(1)   # datetime.datetime(1, 1, 1, 0, 0)

d.today()           # datetime.datetime(2024, 11, 10, 20, 31, 36, 933701)
# the same as
dt.datetime.today()  # datetime.datetime(2024, 11, 10, 20, 35, 5, 278698)
# the same as
dt.datetime.now()

# %%  timetuple  ==  time.struct_time
d.timetuple()  # time.struct_time(tm_year=2024, tm_mon=11, tm_mday=10, tm_hour=20, tm_min=22, tm_sec=24, tm_wday=6, tm_yday=315, tm_isdst=-1)
"""
! Nothing like  dt.datetime.fromtimetuple()
"""

# %%
# %% datetime.time
dt.time                 # class  datetime.time
dir(dt.time)

dt.time()               #  datetime.time(0, 0)
dt.time().isoformat()   # '00:00:00'

dt.time(1, 2, 3)        #  datetime.time(1, 2, 3)
dt.time(1, 2, 3).isoformat()  # '01:02:03'

help(dt.time)
# time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
# ...

dt.time.now()   # !!! ERROR !!!
now = dt.datetime.now()
now
dt.time(now.hour, now.minute, now.second)

# %%  NO  timetuple  ==  time.struct_time
dt.time(1, 2, 3).timetuple()     # ! AttributeError: 'datetime.time' object has no attribute 'timetuple'

# %%
# %% datetime.date
dt.date                 # class  datetime.date
dir(dt.date)

dt.date()               #! TypeError: function missing required argument 'year'
dt.date(2018, 1, 1)     # datetime.date(2018, 1, 1)
tiff = dt.date(2018, 1, 1) -  dt.date(2017, 2, 3)
tiff                    # datetime.timedelta(days=332)

dt.date(2018, 9, 9) + dt.timedelta(days=3, hours=12, minutes=34)
                        # datetime.date(2018, 9, 12)

fdate = dt.date.today() + dt.timedelta(days=3, hours=12, minutes=34)
fdate
fdate.replace(year = fdate.year + 1)

# %%  timetuple  ==  time.struct_time
dt.date(2018, 1, 1).timetuple()  # time.struct_time(tm_year=2018, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=1, tm_isdst=-1)

#%%
today = dt.date.today() # current date
today                   # datetime.date(2020, 9, 11)
dir(today)

today == dt.date.fromtimestamp(time.time())    # True

today.weekday()
today.day
today.month
today.year

# %%  !!!  .combine()
dt.datetime.combine(today, dt.time(now.hour, now.minute, now.second))

# %%
# %%
my_birthday = dt.date(today.year, 6, 24)

if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
my_birthday

#%%
dt.date(2008, 6, 24)
time_to_birthday = abs(my_birthday - today)
type(time_to_birthday)         # datetime.timedelta
dir(time_to_birthday)

time_to_birthday.days
time_to_birthday

#%%
d = dt.date.fromordinal(730920) # 730920th day after 1. 1. 0001
d           # datetime.date(2002, 3, 11)
dt.date(2002, 3, 11)

dt.date.fromordinal(1)          # datetime.date(1, 1, 1)  # y, m, d

dir(d)

# %%
# %%
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
d.isoformat()  # '2002-03-11'
d.strftime("%d/%m/%y")  # '11/03/02'
d.strftime("%A %d. %B %Y")      # 'Monday 11. March 2002'
'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
# 'The day is 11, the month is March.'

#%%
ic = d.isocalendar()
ic
for i in ic: print(i)

"""
2002                # ISO year
11                  # ISO week number
1                   # ISO day number ( 1 = Monday )
"""


#%%
# from datetime import datetime, date, time

# Using datetime.combine()
d = dt.date(2005, 7, 14)
d                   # datetime.date(2005, 7, 14)
t = dt.time(12, 30)
t                   # datetime.time(12, 30)
dt.datetime.combine(d, t)   # datetime.datetime(2005, 7, 14, 12, 30)
dt.datetime(2005, 7, 14, 12, 30)
# Using datetime.now() or datetime.utcnow()
dt.datetime.now()
# dt.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1 DST
dt.datetime.utcnow()
# dt.datetime(2007, 12, 6, 15, 29, 43, 79060)

#%%
# Using datetime.strptime()
sdt = dt.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
sdt
dt.datetime(2006, 11, 21, 16, 30)
dt.datetime(2006, 11, 21, 16, 30).isoformat()

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

# %%
