#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:13:20 2024

@author: arek

https://pandas.pydata.org/docs/user_guide/timeseries.html#time-zone-handling
"""

# %%
# %%  pandas  timestamp
# https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html
import pandas as pd
# import datetime as dt     # more formal
from datetime import datetime as ddt   # more convenient
from datetime import timezone as dtz   # more convenient
from datetime import timedelta as dtd  # more convenient
import time

# %%
d = ddt(2024, 10, 7, 8)
d   # datetime.datetime(2024, 10, 7, 8, 0)

# 1°
pdt = pd.to_datetime(d)
pdt     # Timestamp('2024-10-07 08:00:00')
pdt == d  # True    ???
type(pdt) # pandas._libs.tslibs.timestamps.Timestamp

"""
Notice that Pandas uses "timestamp" and "epoch"
in a different meaning from that used in datetime and time libs (which is the same as in POSIX standard).
In the latter case "timestamp" is the number of seconds since "epoch" = 1970-01-01 00:00:00 at meridian 0°
(i.e. timestamp is always GMT/UTC, no DST of course)
while "epoch" in Pandas has the meaning of "timestamp" in datetime and time libs.
See also remark below in `pd.Timestamp` description.
"""

# %% tz makes it difficult
d.tzinfo      # None – no timezone
pdt.tzinfo    # None – no timezone

pdts = pd.to_datetime(d, utc=True)
pdts            # Timestamp('2024-10-07 08:00:00+0000', tz='UTC')
pdts.tzinfo     # datetime.timezone.utc
pdts == d                           # False
pdts == d.replace(tzinfo=dtz.utc)   # True

# 2°
# pandas timestamp – standard datetime format in pandas
type(pdts)   # pandas._libs.tslibs.timestamps.Timestamp

# but in pd.Series it's   dtype: datetime64[ns]
pdtss = pd.Series([ddt(2024, 10, 7, k) for k in range(5, 8)])
pdtss   # dtype: datetime64[ns]
pdtss.dtype     # dtype('<M8[ns]')   ?!?!
type(pdtss[0])  # pandas._libs.tslibs.timestamps.Timestamp
pdtss[0].tzinfo     # None

pdtss0 = pd.to_datetime(pdtss, utc=True)
pdtss0      # dtype: datetime64[ns, UTC]

# !!! notice that
pdtss.tz_convert('UTC')     # TypeError: index is not a valid DatetimeIndex or PeriodIndex
pdtss.tz_localize('UTC')     # TypeError: index is not a valid DatetimeIndex or PeriodIndex
# !!! what a SHIT !!!

# %%  pd.Timestamp  class  basics
#  https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html

# pandas.Timestamp
class pandas.Timestamp(
        ts_input=<object>,
        year=None,
        month=None,
        day=None,
        hour=None,
        minute=None,
        second=None,
        microsecond=None,
        tzinfo=None,
        *,
        nanosecond=None,
        tz=None,
        unit=None,
        fold=None
) -> pandas._libs.tslibs.timestamps.Timestamp
"""
Pandas  replacement  for python  datetime.datetime  object.

Timestamp is the pandas equivalent of python’s  datetime.datetime
and is interchangeable with it in most cases.

It’s the type used for the entries that make up a DatetimeIndex,
and other timeseries oriented data structures in pandas.

Parameters:
    ts_input : datetime-like, str, int, float
        Value to be converted to Timestamp.
    year, month, day : int
    hour, minute, second, microsecond : int, optional, default 0
    tzinfo : datetime.tzinfo, optional, default None
    *,
    nanosecond : int, optional, default 0
    tz : str, pytz.timezone, dateutil.tz.tzfile or None
        Time zone for time which Timestamp will have.
    unit : str
        Unit used for conversion if `ts_input` is of type  int  or  float.
        The valid values are ‘D’, ‘h’, ‘m’, ‘s’, ‘ms’, ‘us’, and ‘ns’.
        For example, ‘s’ means seconds and ‘ms’ means milliseconds.
        For float inputs, the result will be stored in nanoseconds,
        and the unit attribute will be set as 'ns'.
    fold : {0, 1}, default None, keyword-only
        Due to daylight saving time,
        one wall clock time can occur twice when shifting from summer to winter time;
        fold describes whether the datetime-like corresponds to the first (0) or the second time (1)
        the wall clock hits the ambiguous time.

Notes
-----
There are essentially three calling conventions for the constructor.
The primary form accepts four parameters.
They can be passed by position or keyword.

The other two forms mimic the parameters from datetime.datetime.
They can be passed by either position or keyword,
but not both mixed together.

Examples
--------
"""
# Using the primary calling convention:
# This converts a datetime-like string
pd.Timestamp('2017-01-01T12')   # Timestamp('2017-01-01 12:00:00')
pd.Timestamp('2017-01-01 12')   # Timestamp('2017-01-01 12:00:00')
pd.Timestamp('2017-01-01 12:38+01')     # Timestamp('2017-01-01 12:38:00+0100', tz='UTC+01:00')
pd.Timestamp('2017-01-01 12:38+01:30')  # Timestamp('2017-01-01 12:38:00+0130', tz='UTC+01:30')

# This converts a float representing "a Unix epoch" in units of seconds
pd.Timestamp(1_513_393_355.5, unit='s')     # Timestamp('2017-12-16 03:02:35.500000')
""" !!!
Notice a different meaning of "epoch" from that used in time and datetime libs:
here it is: time elapsed from  1970-01-01 00:00:00,
while in time & datetime libs this very date is called "epoch"
while time elapsed from `epoch = 1970-01-01 00:00:00`
is called "timestamp" and is in 's' (by default and probably always).
"""

# This converts an int representing a Unix-epoch in units of seconds and for a particular timezone
pd.Timestamp(1513393355, unit='s', tz='US/Pacific')  # Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')
pd.Timestamp(1513393355, unit='s', tz='UTC')         # Timestamp('2017-12-16 03:02:35+0000', tz='UTC')
pd.Timestamp(1513393355, unit='s')                   # Timestamp('2017-12-16 03:02:35')
pd.Timestamp(1513393355, unit='s', tz='CET')         # Timestamp('2017-12-16 04:02:35+0100', tz='CET')
pd.Timestamp(1513393355, unit='s', tz='CEST')        # ! UnknownTimeZoneError: 'CEST'
pd.Timestamp(1513393355, unit='s', tz='CEDT')        # ! UnknownTimeZoneError: 'CEDT'

# ! Cannot find the list of all time zone names !
# see: https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones

# Using the other two forms that mimic the API for datetime.datetime:
pd.Timestamp(2017, 1, 1, 12)    # Timestamp('2017-01-01 12:00:00')

pd.Timestamp(year=2017, month=1, day=1, hour=12)    # Timestamp('2017-01-01 12:00:00')

# ...
# %%
"""
https://pandas.pydata.org/docs/user_guide/timeseries.html#time-zone-handling
"""
# %%
d       # datetime.datetime(2024, 10, 7, _8_, 0)
d.timestamp()   # 1728280800.0   seconds since epoch = 1970-01-01 00:00:00
pd.Timestamp(d.timestamp(), unit='s')     # Timestamp('2024-10-07  _06_:00:00')
# !!!  hence we get by defult the GMT/UTC clock time
# not local (taken from OS) like it is by default in time & datetime libs
ddt.fromtimestamp(d.timestamp())  # datetime.datetime(2024, 10, 7, _8_, 0)

# ! Moreover, default unit is 'ns' (unlike in time and datetime libs)
pd.Timestamp(d.timestamp())     # Timestamp('1970-01-01 00:00:01.728280800')

#
pd.Timestamp(d.timestamp(), unit='s', tz='CET') # Timestamp('2024-10-07 _08_:00:00+0200', tz='CET')  ok

# %% Be carefull then when working with local "now":
dn = ddt.now()

# better fix it for future ref:
dn = ddt(2024, 10, 16, 12, 27, 24, 454661)
dn      # datetime.datetime(2024, 10, 16, 12, 27, 24, 454661)
dn.timestamp()  # 1729074444.454661
# in datetime lib .timestamp() and .fromtimestamp() are mutually consistent (reversible)
ddt.fromtimestamp(dn.timestamp())   # datetime.datetime(2024, 10, 16, _12_, 27, 24, 454661)
# as default TZ + DST are taken from OS

# BUT when going to pandas.Timestamp things get more complicated:
pd.Timestamp(dn.timestamp(), unit='s')       # Timestamp('2024-10-16 _10_:27:24.454660892')
# as default TZ is GMT/UTC and one must set local TZ (with DST) directly
pd.Timestamp(dn.timestamp(), unit='s', tz='CET')    # Timestamp('2024-10-16 _12_:27:24.454660892+0200', tz='CET')

# %%
dn.timestamp()      # 1729074444.454661
pdtn = pd.Timestamp(dn.timestamp(), unit='s', tz='CET')
pdtn    # Timestamp('2024-10-16 12:27:24.454660892+0200', tz='CET')
pdtn.timestamp()    # 1729074444.454661

pd.Timestamp(pdtn.timestamp(), unit='s', tz='CET')
        # Timestamp('2024-10-16 12:27:24.454660892+0200', tz='CET')   ok
pdtn0 = pd.Timestamp(pdtn.timestamp(), unit='s')
pdtn0
        # Timestamp('2024-10-16 _10_:27:24.454660892')    GMT/UTC clock time by default
# unlike
ddt.fromtimestamp(pdtn.timestamp())
        # datetime.datetime(2024, 10, 16, _12_, 27, 24, 454661)   local clock time by default

pdtn.tzinfo     # <DstTzInfo 'CET' CEST+2:00:00 DST>
pdtn0.tzinfo    # None

# %% getting  time.struct_time
pdtn.timetuple()
    # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=16, tm_hour=_12_, tm_min=27, tm_sec=24, tm_wday=2, tm_yday=290, tm_isdst=1)
pdtn.timetuple().tm_zone        # None   WHY ?   pdtn is TZ aware !
pdtn.timetuple().tm_gmtoff      # None   WHY ?
#
pdtn0.timetuple()
    # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=16, tm_hour=_10_, tm_min=27, tm_sec=24, tm_wday=2, tm_yday=290, tm_isdst=-1)
pdtn0.timetuple().tm_zone        # None
pdtn0.timetuple().tm_gmtoff      # None

# compare with
pdtntt = time.localtime(pdtn.timestamp())
pdtntt  # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=16, tm_hour=12, tm_min=27, tm_sec=24, tm_wday=2, tm_yday=290, tm_isdst=1)
pdtntt.tm_zone      # 'CEST'
pdtntt.tm_gmtoff    # 7200

pdtn0tt = time.gmtime(pdtn.timestamp())
pdtn0tt  # time.struct_time(tm_year=2024, tm_mon=10, tm_mday=16, tm_hour=10, tm_min=27, tm_sec=24, tm_wday=2, tm_yday=290, tm_isdst=0)
pdtn0tt.tm_zone      # 'GMT'
pdtn0tt.tm_gmtoff    # 0

# %% getting  datetime.time
pdtn.timetz()   # datetime.time(12, 27, 24, 454660, tzinfo=<DstTzInfo 'CET' CEST+2:00:00 DST>)
pdtn0.timetz()   # datetime.time(10, 27, 24, 454660)

pdtn.time()   # datetime.time(12, 27, 24, 454660)
pdtn0.time()   # datetime.time(10, 27, 24, 454660)

# %%
pdtn.to_pydatetime()    # datetime.datetime(2024, 10, 16, _12_, 27, 24, 454660, tzinfo=<DstTzInfo 'CET' CEST+2:00:00 DST>)
pdtn0.to_pydatetime()   # datetime.datetime(2024, 10, 16, _10_, 27, 24, 454660)

# %%