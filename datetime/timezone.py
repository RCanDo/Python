#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:23:19 2024

@author: arek
"""

from datetime import datetime
import time

# %%
d = datetime.now()
t = time.time()

# %%
type(d)     # datetime.datetime
d           # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)
d.timestamp()   # 1712391987.988654

type(t)     # float
t               # 1712391987.63563
datetime.fromtimestamp(t)               # datetime.datetime(2024, 4, 6, 10, 26, 27, 635630)

datetime.fromtimestamp(d.timestamp())   # datetime.datetime(2024, 4, 6, 10, 26, 27, 988654)

# ! BUT
time.gmtime(d.timestamp())
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=8 !!, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=0)
time.gmtime(t)
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=8 !!, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=0)

time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t))  # '2024-04-06 08:26:27'

#! use rather
time.localtime(t)
# time.struct_time(tm_year=2024, tm_mon=4, tm_mday=6, !! tm_hour=10 !!, tm_min=26, tm_sec=27, tm_wday=5, tm_yday=97, tm_isdst=1)

# %% correcting for localtime depends on the context
# !!! DO IT PROPERLY (what is rather tricky)
d.astimezone().utcoffset()      # datetime.timedelta(seconds=7200)
d + d.astimezone().utcoffset()  # datetime.datetime(2024, 4, 6, !! 12 !! , 26, 27, 988654)    # ok?
d - d.astimezone().utcoffset()  # datetime.datetime(2024, 4, 6,     8    , 26, 27, 988654)    # ok?    -- it depends!

# %%  BUT
"""
Notice that there is an issue with timezone in SQL servers like Redshift or Postgres
"""
import datetime as dt

def to_timestamp(d: dt.datetime, tz_correct: bool = True) -> int:
    """"""
    if tz_correct:
        d = d + d.astimezone().utcoffset()          # !!! it works as expected in context of SQL query, see below
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

# %% btw
datetime.fromtimestamp(t).isoformat()           # '2024-04-06T10:26:27.635630'
help(d.isoformat)
datetime.fromtimestamp(t).isoformat(sep=' ')    # '2024-04-06 10:26:27.635630'

# %%