#! python3
# -*- coding: utf-8 -*-
"""
title: Time Zone – pytz
subtitle:
version: 1.0
type: help, examples
keywords: [time zone, date, pytz,]
description: |
sources:
file:
    date: 2020-09-11
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
# %%
# import datetime as dt     # more formal
from datetime import datetime as ddt   # more convenient
from datetime import timezone as dtz   # more convenient
from datetime import timedelta as dtd  # more convenient
import time
import pytz

# %%
dir(pytz)
pytz.all_timezones

# %%
tz_pl = pytz.timezone('Europe/Warsaw')
tz_pl   # <DstTzInfo 'Europe/Warsaw' LMT+1:24:00 STD>
pytz.timezone('Poland')             # differet name but the same shift

tz_au = pytz.timezone('Australia/Sydney')
tz_au   # <DstTzInfo 'Australia/Sydney' LMT+10:05:00 STD>

# %% better to get some fixed time (and pretend it is NOW)
t = 1712391987.635630        # timestamp  ~= time.time()  back then
d = ddt.fromtimestamp(t)
d   # datetime.datetime(2024, 4, 6, _10_, 26, 27, 635630)

d.tzinfo    # None – no time zone
"""
BUT in fact this object is interpreted as if TZ (and DST) is the same as that of OS:
i.e. for interpreter it represents the local clock time.
"""
ddt.fromtimestamp(t, tz=tz_pl)
    # datetime.datetime(2024, 4, 6, _10_, 26, 27, 635630,
    #       tzinfo=<DstTzInfo 'Europe/Warsaw' CEST+2:00:00 DST>)
ddt.fromtimestamp(t, tz=tz_pl).timestamp() == t     # True

d_dub = ddt.fromtimestamp(t, tz=pytz.timezone('Europe/Dublin'))
d_dub   # datetime.datetime(2024, 4, 6, _9_, 26, 27, 635630,
        #       tzinfo=<DstTzInfo 'Europe/Dublin' IST+1:00:00 STD>)
d_dub.timestamp() == t  # True

d_utc = ddt.fromtimestamp(t, tz=pytz.timezone('UTC'))
d_utc   # datetime.datetime(2024, 4, 6, _8_, 26, 27, 635630,
        #       tzinfo=<UTC>)
d_utc.timestamp() == t  # True

d_au = ddt.fromtimestamp(t, tz=tz_au)
d_au    # datetime.datetime(2024, 4, 6, _19_, 26, 27, 635630,
        #       tzinfo=<DstTzInfo 'Australia/Sydney' AEDT+11:00:00 DST>)
d_au.timestamp() == t  # True

# %%
now_pl = ddt.now(tz_pl)
now_pl  # datetime.datetime(2024, 11, 11, _13_, 46, 55, 138774,
        #     tzinfo=<DstTzInfo 'Europe/Warsaw' CET+1:00:00 STD>)
now = ddt.now()
now     # datetime.datetime(2024, 11, 11, _13_, 47, 5, 19590)
# this is TZ unaware and works like local cloc taking info on TZ and DST from OS

now_pl.today()  # ! datetime.datetime(2024, 11, 11, 13, 49, 55, 609301)
                # ! TZ unaware ...
now.today()     # datetime.datetime(2024, 11, 11, 13, 49, 59, 560345)

now_au = ddt.now(tz_au)
now_au  # datetime.datetime(2024, 11, 11, _23_, 48, 23, 564991,
        #     tzinfo=<DstTzInfo 'Australia/Sydney' AEDT+11:00:00 DST>)

now_au.today()  # !!! not AU time !!! but local ...
                # ! TZ unaware ...


#%%
