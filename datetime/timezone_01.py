#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: Time Zone in time and datetime libs
sources:
    - title: time
      link: https://docs.python.org/3/library/time.html
    - title: datetime.timezone
      link: https://docs.python.org/3/library/datetime.html#timezone-objects
    - title: datetime.datetime
      link: https://docs.python.org/3/library/datetime.html#datetime-objects
    - title: datetime.timedelta
      link: https://docs.python.org/3/library/datetime.html#timedelta-objects
    - link: https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations
    - link: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
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
    - However, in some libraries (e.g. Pandas) "epoch" means "seconds from 1970-01-01, 00:00:00 (UTC)".
      Beware!
file:
    date: 2024-04-06
    authors:
        - email: akasp@int.pl
"""
# %%
import time
# import datetime as dt     # more formal
from datetime import datetime as ddt   # more convenient
from datetime import timezone as dtz   # more convenient
from datetime import timedelta as dtd  # more convenient

# %% How to get current local time
# !!! i.e. that of the clock of the OS where time zone is not None
d = ddt.now()            # datetime.datetime

# However
t = time.time()         # ! timestamp i.e. float
# !!! returns timestamp of the current GMT/UTC !!!

# %% What is timestamp and how it depends on TZ
# better to get some fixed time (and pretend it is NOW)
d = ddt(2024, 4, 6, 10, 26, 27, 988654)     # ~= dt.now()     back then
t = 1_712_391_987.635630                   # ~= time.time()

type(t)     # float
t               # 1'712'391'987.635630    !!!

type(d)     # datetime.datetime
d           # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)
d.timestamp()   # 1'712'391'987.988654    !!!   the same  !!!

"""
`t` is seconds from the epoch = 1970-01-01 00:00:00  ! always GMT / UTC !;
i.e. it's sun hour (basically) on meridian 0°.

!!! It takes into account OS Time Zone !!!
i.e. values provided to dt() are interpreted as given in local time
where TZ is taken from OS and DST (Daylight Saving Time) from very special table
(see https://docs.python.org/3/library/time.html)
– then it is internally turned to GMT/UTC (there is never DST of course)
and already then number of seconds from epoch is calculated.

I.e. timestamp is calculated as follows:
1° take clock time "here" (locally at some given TZ and DST known from OS);
2° see what it is GMT clock time – i.e. subtract TZ translation and DST;
3° calculate number of seconds from epoch = 1970-01-01 00:00:00.
"""

# %%  timestamp  vs  datatime.datetime

# datetime from timestamp
ddt.fromtimestamp(d.timestamp())   # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)
ddt.fromtimestamp(t)               # datetime.datetime(2024, 4, 6, 10, 26, 27, 635630)
# these are "TZ unaware":
d.tzinfo    # None – no Time Zone
"""
BUT only FORMALLY as interpreter knows TZ from the OS
and uses it for turning datetime obj into timestamp and vice versa;
THUS ! de facto ! "TZ unaware" works like `tzinfo` set to local TZ.
I.e. even if TZ is not set in datetime object the interpreter is still very aware of the system TZ
and assumes this is the TZ which shall be taken into account when calculating timestamp
or when creating datetime object from timestamp.

!!! timestamp is always GMT/UTC !!! (no DST!)
and is interpreted (translated to clock time) according to TZ and DST provided directly or taken from OS.

This is true for both time and datetime libs (and probably any other date/time library).
"""

# %%
# %%  time  library
"""
See https://docs.python.org/3/library/time.html and READ THE INTRO there.
"""
# Interpreting timestamp directly – do not take local TZ nor DST (from OS) into account
tg = time.gmtime(t)      # TRUE  GMT/UTC  clock time
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=8 !!, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=0)
time.gmtime(d.timestamp())
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=8 !!, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=0)
time.strftime("%Y-%m-%d %H:%M:%S", tg)  # '2024-04-06 08:26:27'

# #  To get local clock time
# !!! use .localtime() !!!
tl = time.localtime(t)   # TRUE  local clock time
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=10 !!, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=1)
time.strftime("%Y-%m-%d %H:%M:%S", tl)  # '2024-04-06 10:26:27'

""" !!!
Notice that we always begin with timestamp
    t = time.time()
which is always current standard GMT/UTC
and is calculated by interpreter from local clock time and local TZ + DST (taken from OS)
as already described above.
"""

# time.struct_time  is named tuple with 9 elements always displayed,
# one of which is info about DST (taken from OS in general)
tg.tm_isdst     # 0
tl.tm_isdst     # 1
# There are also 2 attributes not displayed, namely info about TZ
tg.tm_zone      # 'GMT'
tg.tm_gmtoff    # 0
tl.tm_zone      # 'CEST'
tl.tm_gmtoff    # 7200  =  1 hour for CET + 1 hour for DST  (?)

# %%  Check on reader's current time
# What is current GMT/UTC:
here_now = time.time()  # timestamp – current seconds since epoch at meridian 0°

# current GMT clock time
thn_gmt = time.gmtime(here_now)
thn_gmt             # time.struct_time(tm_year=2024, tm_mon=11, tm_mday=7, tm_hour=8, tm_min=30, tm_sec=35, tm_wday=3, tm_yday=312, tm_isdst=0)
thn_gmt.tm_zone     # 'GMT'
thn_gmt.tm_gmtoff   # 0  always!
thn_gmt.tm_isdst    # 0  always!

# current local clock time:
thn_loc = time.localtime(here_now)
thn_loc             # time.struct_time(tm_year=2024, tm_mon=11, tm_mday=7, tm_hour=9, tm_min=30, tm_sec=35, tm_wday=3, tm_yday=312, tm_isdst=0)
thn_loc.tm_zone     # 'CET' in winter (DST off); 'CEST' in summer (DST on)
thn_loc.tm_gmtoff   # 3600  in winter (DST off); 7200   in summer (DST on)
thn_loc.tm_isdst    #    0  in winter (DST off);    1   in summer (DST on)

# %%  To get timestamp from  time.struct_time

#  use .mktime() which is the inverse function of .localtime():

t                               # 1712391987.63563
time.mktime(time.localtime(t))  # 1712391987.0      # OK    # seconds since the epoch in GMT/UTC no DST

# ! hence (and this is really confusing):
time.mktime(time.gmtime(t))     # 1712388387.0      # ! -3600 ???
time.mktime(time.gmtime(0))     # -3600
# Looks like always corrected for TZ but taken from OS not from .tm_gmtoff.
# What about DST?
"""
    mktime(tuple) -> floating point number

    Convert a time tuple in _local_ time to seconds since the Epoch.
    ! Thus it looks like it ignores info on TZ given by  time.struct_time
    ! and always corrects for local TZ (taken from OS) but never for DST !
    ! Total mess !
    Note that mktime(gmtime(0)) will not generally return zero for most
    time zones; instead the returned value will either be equal to that
    of the timezone or altzone attributes on the time module.

See also table in the Intro to time lib. https://docs.python.org/3/library/time.html
where the following solution is indicated
"""
import calendar
calendar.timegm(time.gmtime(t)) # 1712391987        # OK    # seconds since the epoch in GMT/UTC no DST

# %% creating  time.struct_time  directly
tl   # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, tm_hour=10, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=1)
tst = time.struct_time((2024, 4, 6, 10, 26, 27, 5, 97, 1))  # the only way!
# thus be carefull with order or args, or better,
# ! don't do it at all !
# instead, use  datetime.datetime()  like at the top of this doc.

tst == tl       # True
tst.tm_gmtoff   # None
tst.tm_zone     # None
time.mktime(tst)    # 1712391987.0
t                   # 1712391987.63563

# %% other time lib stuff
time.time_ns()          # super precise version of current time (always GMT/UTC)
# constants  https://docs.python.org/3/library/time.html#timezone-constants
time.altzone    # -7200
time.daylight   # 1
time.timezone   # -3600
time.tzname     # ('CET', 'CEST')
"""
For the above Timezone constants (altzone, daylight, timezone, and tzname),
the value is determined by the timezone rules in effect at module load time or the last time tzset() is called
and may be incorrect for times in the past.
!!!  It is recommended to use the tm_gmtoff and tm_zone results from localtime() to obtain timezone information.

How to work with arbitrary TZ, other then local or UTC, see
https://docs.python.org/3/library/time.html#time.tzset
It's quite tricky and it's only possible via setting environment constants 'TZ' by `os.environ['TZ'] = ...`.
"""

# %%
# %%  datetime  library;  see  datetime_01.py  for more info on this;
dir(d)

# %% link to  time.struct_time
d.timetuple()   # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, tm_hour=10, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=-1)

# ! Nothing like  ddt.fromtimetuple()

# %% SETTING TIMEZONE
d       # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)
d.tzinfo        # None – no time zone
d.utcoffset()   # None
"""
BUT in fact, as stated above, this object is interpreted as if TZ & DST are the same as that of OS:
i.e. for interpreter it represents the local clock time.
"""
# %% Turn datetime obj into TZ aware
# ! This seems to be very good practice – fixing TZ + DST into the object – no ambiguities then!

d.astimezone()
# datetime.datetime(2024, 4, 6, 10, 26, 27, 988654,
#                   tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), 'CEST'))

# One may also get actual (i.e. proper for current local) TZ + DST offset from this:
d.astimezone().utcoffset()  # datetime.timedelta(seconds=7200)

# %% At creation from timestamp

d1 = ddt.fromtimestamp(t, tz=dtz.utc)
d1      # datetime.datetime(2024, 4, 6, !! 8 !!, 26, 27, 635630, tzinfo=datetime.timezone.utc)
"""
This is OK as the  timestamp  is always standard GMT/UTC and this way
we have consistantly created GMT/UTC clock time from GMT/UTC timestamp.
In other words:
dt.fromtimestamp(.) creates clock time for given TZ and DST (taken from OS if not passed directly)
from timestamp i.e. seconds from epoch at GMT/UTC.
"""
d1.timestamp()          # 1712391987.63563      # !  the same  !
ddt.fromtimestamp(d1.timestamp())     # datetime.datetime(2024, 4, 6,  10,  26, 27, 635630)   OK
# We got proper local clock time: TZ + DST = utcoffset – taken from OS.

d2 = ddt.fromtimestamp(t, tz=dtz(dtd(hours=2), name='CET'))    # name is arbitrary
d2      # datetime.datetime(2024, 4, 6, !! 10 !!, 26, 27, 635630,
        #                   tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), 'CET'))
d2.timestamp()  # 1712391987.63563    !!!   the same  !!!

# %% Setting tzinfo at creation from clock values – via timezone(timedelta(hours))

ddt(2024, 4, 6, 10, 26, 27, tzinfo='CET')   # ! TypeError: tzinfo argument must be None or of a tzinfo subclass, not type 'str'
# CET
ddt(2024, 4, 6, 10, 26, 27, tzinfo=dtz(dtd(hours=2)))
        # datetime.datetime(2024, 4, 6, 10, 0,
        #                   tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))
# !!! -------------
ddt(2024, 4, 6, 10, 26, 27, tzinfo=dtz(dtd(hours=2))).timestamp()  # 1712391987 == t
# -----------------
ddt(2024, 4, 6, 10, 26, 27, tzinfo=dtz(dtd(hours=2), name='my_zone'))
        # datetime.datetime(2024, 4, 6, 10, 0,
        #                   tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), 'my_zone'))
"""
Notice that setting TZ directly is NOT necessary as long as one needs to work on local time
and remembers to use time.localtime() to get time.struct_time objects.
Interpreter is always aware of the local TZ and DST (from OS).
"""

# %% Setting TZ via .replace() after creation is dangerous!
# !!! THIS IS ANTIPATTERN !!!
d0 = d.replace(tzinfo=dtz.utc)
d0      # datetime.datetime(2024, 4, 6, !! 10 !!, 26, 27, 988654, tzinfo=datetime.timezone.utc)
d0.tzinfo   # datetime.timezone.utc
# !!! and this is FALSE as we used LOCAL clock time (with DST) in constructing this datetime obj
# and now we falsly claim that it was standard GMT/UTC (no DST) clock time...
d0.timestamp()  # 1712399187.988654   # !!! NOT the same !!!  +7200
ddt.fromtimestamp(d0.timestamp())    # datetime.datetime(2024, 4, 6, !! 12 !!, 26, 27, 988654)  ! WRONG !
"""
Thus don't use .replace() for setting TZ unless you are sure that the clock time used at datetime creation
was for the same TZ you are setting via .replace().
"""
# See how WRONG (inconsistent) `d0` leads to wrong clock time inference
d0.timestamp()  # 1712399187.988654     # kind of true "local timestamp" = seconds since "local epoch"
d0.timestamp() - d.timestamp()  # 7200. sec i.e. 2 hours
d0 - d   # ! TypeError: can't subtract offset-naive and offset-aware datetimes
time.gmtime(d0.timestamp())     # true local clock BUT it should be relevant GMT clock
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=10 !! , tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=0)
time.localtime(d0.timestamp())  # ! WRONG !
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=12 !! , tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=0)
# We got complete nonsense – this is apparent doppelt-gemoppelt.

# %%  don't use .utcnow()
dn = ddt.now()           # datetime.datetime(2024, 10, 13,  19,  35, 56, 600870)
du = ddt.utcnow()        # datetime.datetime(2024, 10, 13,  17,  35, 56, 698579)
# they are "TZ unaware"
dn.tzinfo
du.tzinfo
"""
This is the cause of the serious confusion:
`du` is current GMT/UTC clock time while it is TZ unaware
hence interpreter gets TZ + DST from OS
i.e. interpretes it as LOCAL clock time when getting timestamp from it.
"""
dnt = dn.timestamp()  # 1728840956.60087    always GMT seconds from epoch AFTER subtracting TZ from OS
dut = du.timestamp()  # 1728833756.698579
dnt - dut             # 7200 (in summer: DST on);  3600 (in winter: DST off)

ddt.fromtimestamp(dnt)   # datetime.datetime(2024, 10, 13,  19,  35, 56, 600870)
ddt.fromtimestamp(dut)   # datetime.datetime(2024, 10, 13,  17,  35, 56, 698579)

time.localtime(dnt)     # OK
    # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=13, tm_hour= 19,  tm_min=35, tm_sec=56, tm_wday=6, tm_yday=287, tm_isdst=0)
time.localtime(dut)     # ! wrong !
    # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=13, tm_hour= 17,  tm_min=35, tm_sec=56, tm_wday=6, tm_yday=287, tm_isdst=0)

time.gmtime(dnt)        # OK
    # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=13, tm_hour= 17,  tm_min=35, tm_sec=56, tm_wday=6, tm_yday=287, tm_isdst=0)
time.gmtime(dut)        # ! wrong !
    # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=13, tm_hour= 15,  tm_min=35, tm_sec=56, tm_wday=6, tm_yday=287, tm_isdst=0)

# %%  !!!  DON'T USE  dt.utcfromtimestamp(t)
#
d1 = ddt.fromtimestamp(t, tz=dtz.utc)
    # datetime.datetime(2024, 4, 6, 8, 26, 27, 635630, tzinfo=datetime.timezone.utc)
# is almost the same as
ddt.utcfromtimestamp(t)
    # datetime.datetime(2024, 4, 6, 8, 26, 27, 635630)
# which, however, is  ! misleading !  as is TZ unaware
# and will be further interpreted as LOCAL time, not UTC!
# !!! This is nasty inconsistence, subtle, difficult to spot and explain.

ddt.utcfromtimestamp(t).timestamp()          # 1712384787.63563
ddt.utcfromtimestamp(t).timestamp() - t      # -7200.0
ddt.fromtimestamp(t, tz=dtz.utc).timestamp()  # 1712391987.63563 == t  # OK

ddt.utcfromtimestamp(ddt.utcfromtimestamp(t).timestamp())
    # datetime.datetime(2024, 4, 6, !! 6 !!, 26, 27, 635630)
# i.e. .utcfromtimestamp() is not the reverse of .timestamp()

# %% correcting for localtime depends on the context
# !!! DO IT PROPERLY (what is rather tricky)
d.astimezone().utcoffset()      # datetime.timedelta(seconds=7200)
d + d.astimezone().utcoffset()  # datetime.datetime(2024, 4, 6, !! 12 !! , 26, 27, 988654)  # ok?
d - d.astimezone().utcoffset()  # datetime.datetime(2024, 4, 6,     8    , 26, 27, 988654)  # ok?  -- it depends!

# %%  TZ ~ SQL servers like Redshift or Postgres
"""
Notice that there is an issue with timezone in SQL servers like Redshift or Postgres
"""

def to_timestamp(d: dt.datetime, tz_correct: bool = True) -> int:
    """"""
    if tz_correct:
        d = d + d.astimezone().utcoffset()  # !!! it works as expected in context of SQL query, see below
    return int(d.timestamp())

""" !!!
use this for "proper" timestamp-ing from dt.datetime to pass it to SQL query, e.g.
"""
def time_clause(
        column: str,
        start_time: dt.datetime = None,
        end_time: dt.datetime = None
) -> tuple[str, tuple]:
    """"""
    match (start_time, end_time):
        case (None, None):
            return None
        case (None, _):
            return f"{column} <= %s", (to_timestamp(end_time),)
        case (_, None):
            return f"{column} >= %s", (to_timestamp(start_time),)
        case _:
            return f"{column} BETWEEN %s AND %s", (to_timestamp(start_time), to_timestamp(end_time))

# %%