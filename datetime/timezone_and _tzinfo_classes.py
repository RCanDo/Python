#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: datetime.timezone and .tzinfo classes
sources:
    - title: dt.timezone
      link: https://docs.python.org/3/library/datetime.html#timezone-objects
file:
    date: 2024-10-13
    authors:
        - email: akasp@int.pl
"""
# %%
# import datetime as dt     # more formal
from datetime import datetime as ddt   # more convenient
from datetime import timezone as dtz   # more convenient
from datetime import timedelta as dtd  # more convenient
import time

# %%
"""
Read  timezone_01.py  intro first to get proper understanding
of what timestamp really is and how it is interpreted by time and datetime libs.
"""

# %% better to get some fixed time (and pretend it is NOW)
t = 1712391987.635630        # timestamp  ~= time.time()  back then
d = ddt.fromtimestamp(t)
d   # datetime.datetime(2024, 4, 6, 10, 26, 27, 635630)

d.tzinfo    # None – no time zone
"""
BUT in fact this object is interpreted as if TZ (and DST) is the same as that of OS:
i.e. for interpreter it represents the local clock time.
"""

# %%  datetime.timezone  class
# https://docs.python.org/3/library/datetime.html#timezone-objects

"""
The timezone class is a subclass of tzinfo,
each instance of which represents a time zone defined by a fixed offset from UTC.
! It does not facilitate setting DST !
"""
dtz(offset=dtd(hours=2))  # datetime.timezone(datetime.timedelta(seconds=7200))
dtz(dtd(hours=2))         # datetime.timezone(datetime.timedelta(seconds=7200))
dtz(dtd(hours=0))         # datetime.timezone.utc

# let's create Time Zone object
tzo = dtz(dtd(hours=2), name='WRT')     # `name` is optional and is arbitrary
tzo     # datetime.timezone(datetime.timedelta(seconds=7200), 'WRT')

d2 = ddt.fromtimestamp(t, tz=tzo)
d2  # datetime.datetime(2024, 4, 6, 10, 26, 27, 635630,
    #      tzinfo=datetime.timezone(datetime.timedelta(seconds=7200), 'WRT'))
d2.tzinfo       # datetime.timezone(datetime.timedelta(seconds=7200), 'WRT')
d2.tzname()     # 'WRT'

# methods & attrs
# ---------------
# # .utcoffset(None | datetime.datetime)
tzo.utcoffset()     # ! TypeError: timezone.utcoffset() takes exactly one argument (0 given)
tzo.utcoffset(None) # datetime.timedelta(seconds=7200)
tzo.utcoffset(d)    # datetime.timedelta(seconds=7200)
# arg to .utcoffset(None | datetime.datetime) is IGNORED but mandatory! ...

# # .tzname(dt)
# arg to .tzname(None | datetime.datetime) is IGNORED but mandatory! ...
tzo.tzname()        # TypeError: timezone.tzname() takes exactly one argument (0 given)
tzo.tzname(None)    # 'WRT'
dtz(dtd(hours=2)).tzname(None) # 'UTC+02:00'
dtz(dtd(hours=2)).tzname(d)    # 'UTC+02:00' the same of course
dtz(dtd(hours=0))
dtz(dtd(hours=0)).tzname(None)    # 'UTC'

# # .fromutc(ddt)
# Return dt + offset.
# ? The dt argument must be an aware datetime instance, with tzinfo set to self.
tzo.fromutc(d)  # ! ValueError: fromutc: dt.tzinfo is not self
tzo.fromutc(d0)  # ! ValueError: fromutc: dt.tzinfo is not self  # ???
tzo.fromutc(d1)  # ! ValueError: fromutc: dt.tzinfo is not self  # ???

# arg to .dst(None | datetime.datetime) is IGNORED but mandatory! ...
tzo.dst(None)   # ! ALWAYS return None

# # .utc
tzo.utc    # datetime.timezone.utc  ! ALWAYS !
dtz.utc    # datetime.timezone.utc   the same
dtz(dtd(0))

# %%  datetime.timezone.utc
"""
This is the only predefined TZ.
"""
dtz.utc     # datetime.timezone.utc
dtz.utc.utcoffset(None)     # datetime.timedelta(0)
dtz.utc.tzname(None)        # 'UTC'

# %%
"""
! Remember !
Set the TZ when creating the datetime.datetime obj, NOT after!
"""
# setting UTC at creation from timestamp
d1 = ddt.fromtimestamp(t, tz=dtz.utc)
d1      # datetime.datetime(2024, 4, 6, !! 8 !!, 26, 27, 635630, tzinfo=datetime.timezone.utc)
# this is OK as the  timestamp  is always standard GMT/UTC and this way
# we have consistantly created GMT/UTC clock time from GMT/UTC timestamp
d1.timestamp()          # 1712391987.63563  == t     OK

# However, when `tz` is not set directly, then is left None
# what is interpreted as if local TZ (and DST) is working (taken from OS)
ddt.fromtimestamp(t)     # datetime.datetime(2024, 4, 6, !! 10 !!,  26, 27, 635630)   OK
ddt.fromtimestamp(t).timestamp()     # 1712391987.63563 == t    OK
# It's apparent when using time lib
time.localtime(t)
    # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, ! tm_hour=10 ! , tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=1)
time.gmtime(t)
    # time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, ! tm_hour=8 !, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=0)

# !!! Moreover, notice the difference:
# setting time zone after creation
d0 = d.replace(tzinfo=dtz.utc)
d0      # datetime.datetime(2024, 4, 6, !! 10 !!, 26, 27, 988654, tzinfo=datetime.timezone.utc)
d0.tzinfo   # datetime.timezone.utc
# and this is FALSE as we used LOCAL clock time (with DST) in constructing this datetime obj
# and now we falsly claim that it was standard GMT/UTC (no DST) clock time...
d0.timestamp()  # 1712399187.988654   # !!! NOT the same !!!  +7200

# %%
# %% datetime.tzinfo  class
"""
In short: do not bother!
This class is meant to facilitate definitions of own time zone with arbitrary DST.
Hard to imagine what for...
Moreover, it's complicated.

https://docs.python.org/3/library/datetime.html#tzinfo-objects

This is an abstract base class, meaning that
!!! this class should not be instantiated directly !!!

Define a subclass of tzinfo to capture information about a particular time zone.

An instance of (a concrete subclass of) tzinfo can be passed to the constructors for datetime and time objects.
!!!  The latter objects view their attributes as being in local time,  !!!
and the tzinfo object supports methods revealing offset of local time from UTC,
the name of the time zone, and DST offset, all relative to a date or time object passed to them.

You need to derive a concrete subclass,
and (at least) supply implementations of the standard tzinfo methods needed by the datetime methods you use.

The datetime module provides timezone,
a simple concrete subclass of tzinfo which can represent time zones with fixed offset from UTC
such as UTC itself or North American EST and EDT.

Special requirement for pickling:
A tzinfo subclass must have an __init__() method that can be called with no arguments,
otherwise it can be pickled but possibly not unpickled again.
This is a technical requirement that may be relaxed in the future.

A concrete subclass of tzinfo may need to implement the following methods.
Exactly which methods are needed depends on the uses made of aware datetime objects.
If in doubt, simply implement all of them.
"""
...

#%% examples

from datetime import timedelta, datetime, tzinfo


class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=1) + self.dst(dt)
    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime(dt.year, 4, 1)
        self.dston = d - timedelta(days=d.weekday() + 1)
        # ends last Sunday in October
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
dt2.utctimetuple() == dt3.utctimetuple()    # True

# %%
