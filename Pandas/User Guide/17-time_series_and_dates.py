# -*- coding: utf-8 -*-
#! python3
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Time series / date functionality
subtitle:
version: 1.0
type: tutorial
keywords: [time series, dates, NumPy, Pandas]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Pandas 1.1 User Guide
      chapter: Time series / date functionality
      link: https://pandas.pydata.org/docs/user_guide/timeseries.html
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: "17-time_series_and_dates.py"
    path: "D:/ROBOCZY/Python/Pandas/User Guide/"
    date: 2019-11-13
    authors:
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
from utils.ak.builtin import flatten, paste
from utils.ak.nppd import data_frame
import os

#PYWORKS = "D:/ROBOCZY/Python"
PYWORKS = "/home/arek/Roboczy/Python"

os.chdir(PYWORKS + "/Pandas/User Guide/")
print(os.getcwd())

#%%
import numpy as np
import pandas as pd
import datetime as dt     #!!!

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)

#%%
#%% Intro

dt.datetime(2012, 5, 1)                # datetime.datetime(2012, 5, 1, 0, 0)

pd.Timestamp(2012, 5, 1)               # Timestamp('2012-05-01 00:00:00')
pd.Timestamp(dt.datetime(2012, 5, 1))  # Timestamp('2012-05-01 00:00:00')
pd.Timestamp('2020-01')                # Timestamp('2020-01-01 00:00:00')

type(dt.datetime(2012, 5, 1))               # datetime.datetime
type(pd.Timestamp('2020-01'))               # pandas._libs.tslibs.timestamps.Timestamp    ???
type(pd.Timestamp('2020-01').to_numpy())    # numpy.datetime64

pd.Timestamp('2020-01').dtype               #! AttributeError: 'Timestamp' object has no attribute 'dtype'
pd.Series(pd.Timestamp('2020-01')).dtype    # dtype('<M8[ns]')
pd.Series(pd.Timestamp('2020-01')).dtype.__str__()    # 'datetime64[ns]'

# %%
pd.to_datetime('2020-01')       # Timestamp('2020-01-01 00:00:00')
type(pd.to_datetime('2020-01'))         # pandas._libs.tslibs.timestamps.Timestamp

pd.to_datetime(2012, 5, 1)  #! AssertionError
pd.to_datetime('2020/01')       # Timestamp('2020-01-01 00:00:00')

#%%
pd.Timedelta(5, 'h')    # value, unit; default unit is 'ns' (nanoseconds) !
pd.Timedelta('5h')

type(pd.Timedelta('5h'))             # pandas._libs.tslibs.timedeltas.Timedelta
type(pd.Timedelta('5h').to_numpy())  # numpy.timedelta64

pd.Timedelta('5h').dtype             #!AttributeError: 'Timedelta' object has no attribute 'dtype'
pd.Series(pd.Timedelta('5h')).dtype            # dtype('<m8[ns]')
pd.Series(pd.Timedelta('5h')).dtype.__str__()  # 'timedelta64[ns]'
pd.Series(pd.Timedelta('5h')).to_numpy().dtype  # dtype('<m8[ns]')
pd.Series(pd.Timedelta('5h')).to_numpy().dtype.__str__()  # 'timedelta64[ns]'

#%%
pd.Period(2012, 5, 1)  #! AttributeError: 'NoneType' object has no attribute 'n'
pd.Period(dt.datetime(2012, 5, 1))  #! ValueError: Must supply freq for datetime value
pd.Period(dt.datetime(2012, 5, 1), 'M')   # Period('2012-05', 'M')
pd.Period('2020-01')                      # Period('2020-01', 'M')

type(pd.Period('2020-01'))             # pandas._libs.tslibs.period.Period
type(pd.Period('2020-01').to_numpy())  #! AttributeError: 'Period' object has no attribute 'to_numpy'

pd.Period('2020-01').dtype             #! AttributeError: 'Period' object has no attribute 'dtype'
pd.Series(pd.Period('2020-01')).dtype            # period[M]
pd.Series(pd.Period('2020-01')).dtype.__str__()  # 'period[M]'
pd.Series(pd.Period('2020-01')).to_numpy().dtype  # dtype('O')
pd.Series(pd.Period('2020-01')).to_numpy().dtype.__str__()  # object

#%% https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-python-datetimes
dr = pd.date_range('2020-08-30', periods=3)
dr
type(dr)                               # pandas.core.indexes.datetimes.DatetimeIndex
type(dr.to_numpy().dtype)              # numpy.dtype[datetime64]

dr.to_native_types()  #! The 'to_native_types' method is deprecated and will be removed in a future version.
                      # Use 'astype(str)' instead.
pd.to_datetime(dr)    # the same
pd.to_datetime(dr) == dr    # array([ True,  True,  True])

# ???

#%%
dti = pd.to_datetime(['2018-01-21', '21/1/2018',
                      np.datetime64('2018-01-21'),
                      dt.datetime(2018, 1, 21)])
dti     # DatetimeIndex(['2018-01-21', '2018-01-21', '2018-01-21', '2018-01-21'], dtype='datetime64[ns]', freq=None)

dti = pd.date_range('2018-01-01', periods=3, freq='H')
dti

dti = dti.tz_localize('UTC')
dti

dti.tz_convert('US/Pacific')

#%%
idx = pd.date_range('2018-01-01', periods=5, freq='H')
idx

ts = pd.Series(range(len(idx)), index=idx)
ts

ts.resample('2H').mean()
ts.resample('3H').mean()
#???

#%%
idx = pd.date_range('2018-01-01', periods=5, freq='3H')
idx     # DatetimeIndex(['2018-01-01 00:00:00', '2018-01-01 03:00:00', '2018-01-01 06:00:00', '2018-01-01 09:00:00', '2018-01-01 12:00:00'],
        #               dtype='datetime64[ns]', freq='3H')

idx = pd.date_range('2018-01-01', periods=5, freq='3D')
idx

idx = pd.date_range('2018-01-01', periods=5, freq='3M')
idx

idx = pd.date_range('2018-01-01', periods=5, freq='5m')
idx

help(pd.date_range)

#%%
day1 = pd.Timestamp('2018-01-05')
day1.day_name()

day2 = day1 + pd.Timedelta('1 day')
day2.day_name()

day3 = day1 + pd.offsets.BDay()
day3.day_name()

day4 = day3 + pd.offsets.BDay()
day4.day_name()

#%%  !!!
pd.period_range('01/12/2011', freq='M', periods=3)   # american format M/D/Y - default
pd.period_range('13/12/2011', freq='M', periods=3)   # NORMAL format D/M/Y - inferred from 13 (no such month)
    #! ... Provide format (???) or specify infer_datetime_format=True for consistent parsing.

help(pd.period_range)
#! no  format  in arguments ...

pd.period_range('01/12/2011', freq='M', periods=3, format="DD/MM/YYYY")
#! TypeError: period_range() got an unexpected keyword argument 'format'

# BUT
pd.to_datetime('01/12/2011', format="DD/MM/YYYY")   #! ValueError: time data '01/12/2011' does not match format 'DD/MM/YYYY' (match)
pd.to_datetime('01/12/2011', format="%d/%m/%Y")     # Timestamp('2011-12-01 00:00:00')
# american is default:
pd.to_datetime('01/12/2011')     # Timestamp('2011-01-12 00:00:00')
# ...


#%% !!! USE ISO !!! - no ambiguities
pd.period_range('2011-12-01', freq='M', periods=3)
pd.period_range('2011-13-01', freq='M', periods=3)   #! DateParseError: month must be in 1..12
# GOOD !!!

#%%
#%% Overview
# https://pandas.pydata.org/docs/user_guide/timeseries.html#overview
"""
Overview

pandas captures 4 general time related concepts:
- Date times: A specific date and time with timezone support.
    Similar to datetime.datetime from the standard library.
- Time deltas: An absolute time duration.
    Similar to datetime.timedelta from the standard library.
- Time spans: A span of time defined by a point in time and its associated frequency.
- Date offsets: A relative time duration that respects calendar arithmetic.
    Similar to dateutil.relativedelta.relativedelta from the dateutil package.

Concept     Scalar Class    Array Class     pandas Data Type    Primary Creation Method
---------------------------------------------------------------------------------------
Date times  Timestamp       DatetimeIndex   datetime64[ns] or   to_datetime or
                                            datetime64[ns, tz]  date_range

Time deltas Timedelta       TimedeltaIndex  timedelta64[ns]     to_timedelta or
                                                                timedelta_range

Time spans  Period          PeriodIndex     period[freq]        Period or period_range

Date        DateOffset      None            None                DateOffset
   offsets
"""

#%%
idxd = pd.date_range('2018-01-01', freq='M', periods=3)
idxd
# DatetimeIndex(['2018-01-31', '2018-02-28', '2018-03-31'], dtype='datetime64[ns]', freq='M')

idxp = pd.period_range('2018-01-01', freq='M', periods=3)
idxp
# PeriodIndex(['2018-01', '2018-02', '2018-03'], dtype='period[M]', freq='M')

#%%
pd.Series(idxd)
pd.Series(range(3), index=idxd)

pd.Series(idxp)
pd.Series(range(3), index=idxp)

#%%
pd.Series([pd.DateOffset(1), pd.DateOffset(2)])

#%%
pd.Timestamp(pd.NaT)
pd.Timedelta(pd.NaT)
pd.NaT == pd.NaT        # False

#%% Timestamps vs. time spans
# https://pandas.pydata.org/docs/user_guide/timeseries.html#timestamps-vs-time-spans

dt.datetime(2012, 5, 1)                # datetime.datetime(2012, 5, 1, 0, 0)
pd.Timestamp(2012, 5, 1)               # Timestamp('2012-05-01 00:00:00')
pd.Timestamp(dt.datetime(2012, 5, 1))  # Timestamp('2012-05-01 00:00:00')

pd.Timestamp('2012-05-01')
pd.Timestamp('1/12/2012')
pd.Timestamp('13/12/2012')

pd.Timestamp('1/12/2012', format="%d/%m/%Y")    #! TypeError: __new__() got an unexpected keyword argument 'format'

#%%
#%%
pd.Period('2020-01')
pd.Period('2020-01', 'M')    # default
pd.Period('2020-01-01')
pd.Period('2020-01-01', 'M') # not default
pd.Period('2020-01-01', 'D') # default

#%%
dates = [pd.Timestamp('2020-05-01'), pd.Timestamp('2020-05-02'), pd.Timestamp('2020-05-03')]
dates

ts = pd.Series(range(3), dates)
ts
type(ts.index)  # pandas.core.indexes.datetimes.DatetimeIndex
ts.index

#%%
periods = [pd.Period('2012-01'), pd.Period('2012-02'), pd.Period('2012-03')]
ts = pd.Series(range(3), periods)
ts
type(ts.index)  # pandas.core.indexes.period.PeriodIndex
ts.index

#%% Converting to timestamps
# https://pandas.pydata.org/docs/user_guide/timeseries.html#converting-to-timestamps

pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None]))   # Series
pd.to_datetime(['2005/11/23', '2010.12.31'])                      # DatetimeIndex

#%%
pd.to_datetime('04-01-2012 10:00')    # american -- M-D-Y -- default -- shit!
pd.to_datetime('04-01-2012 10:00', dayfirst=True)  # forced to normal -- D-M-Y
pd.to_datetime('13-01-2012 10:00')    # cast to normal -- no 13 month

#!!! USE ISO !!! Y-M-D -- NO AMBIGUITY!
pd.to_datetime('2012-01-04 10:00')    #
pd.to_datetime('2012-13-04 10:00')    #! ParserError: month must be in 1..12
## ERROR -- GOOD !!!

#%% Providing a format argument
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
""" In addition to the required datetime string, a format argument can be passed
to ensure specific parsing.
This could also potentially speed up the conversion considerably.
"""
pd.to_datetime('2010/11/12', format='%Y/%m/%d')
pd.to_datetime('01/12/2020', format='%d/%m/%Y')
pd.to_datetime('12-11-2010 00:00', format='%d-%m-%Y %H:%M')

#%%
"""
If you pass a single string to `to_datetime`, it returns a single Timestamp.
Timestamp can also accept string input, but it doesn’t accept string parsing options
like dayfirst or format, so use  `to_datetime`  if these are required.
"""
pd.to_datetime('04-01-2012 10:00')    # Timestamp
pd.to_datetime(['04-01-2012 10:00'])  # DatetimeIndex

pd.Timestamp('04-01-2012 10:00', dayfirst=True)  #! TypeError: __new__() got an unexpected keyword argument 'dayfirst'
pd.Timestamp(['04-01-2012 10:00'], dayfirst=True) #! "
pd.Timestamp('04-01-2012 10:00', format='%d-%m-%Y %H:%M') #! "
pd.Timestamp('04-01-2012 10:00')  # american
pd.Timestamp('14-01-2012 10:00')  # normal

#%%
pd.DatetimeIndex(['2018-01-01', '2018-01-03', '2018-01-05'])
# DatetimeIndex(..., freq=None)
pd.DatetimeIndex(['2018-01-01', '2018-01-03', '2018-01-05'], freq='infer')
# DatetimeIndex(..., freq='2D')


#%% Assembling datetime from multiple DataFrame columns
# https://pandas.pydata.org/docs/user_guide/timeseries.html#assembling-datetime-from-multiple-dataframe-columns

df = pd.DataFrame({'year': [2015, 2016],
                   'month': [2, 3],
                   'day': [4, 5],
                   'hour': [2, 3]})
print(df)
pd.to_datetime(df)
pd.DatetimeIndex(df)   #! Error
pd.DatetimeIndex(pd.to_datetime(df))

#%% Invalid data
# The default behavior, errors='raise', is to raise when unparseable:
pd.to_datetime(['2009/07/31', 'asd'], errors='raise')  # default
#! ParserError: Unknown string format

# Pass errors='ignore' to return the original input when unparseable:
pd.to_datetime(['2009/07/31', 'asd'], errors='ignore')
# Index(['2009/07/31', 'asd'], dtype='object')

# Pass errors='coerce' to convert unparseable data to NaT (not a time):
pd.to_datetime(['2009/07/31', 'asd'], errors='coerce')
# DatetimeIndex(['2009-07-31', 'NaT'], dtype='datetime64[ns]', freq=None)

#%% Epoch timestamps
# https://pandas.pydata.org/docs/user_guide/timeseries.html#epoch-timestamps
...

#%% Using the origin Parameter
pd.to_datetime([1, 2, 3], unit='D', origin=pd.Timestamp('1960-01-01'))
# The default is set at origin='unix', which defaults to 1970-01-01 00:00:00.
# Commonly called ‘unix epoch’ or POSIX time.
pd.to_datetime([1, 2, 3], unit='D')

#%% Generating ranges of timestamps
# https://pandas.pydata.org/docs/user_guide/timeseries.html#generating-ranges-of-timestamps

dates = [dt.datetime(2012, 5, 1),
         dt.datetime(2012, 5, 2),
         dt.datetime(2012, 5, 3)]
index = pd.DatetimeIndex(dates)
index   # DatetimeIndex(['2012-05-01', ...], dtype='datetime64[ns]', freq=None)

index = pd.Index(dates)
index   # DatetimeIndex(['2012-05-01', ...], dtype='datetime64[ns]', freq=None)

#%%
start = dt.datetime(2011, 1, 1)
end   = dt.datetime(2012, 1, 1)
index = pd.date_range(start, end)
index  # DatetimeIndex(['2011-01-01', '2011-01-02', ...], dtype='datetime64[ns]', freq='D')

# business days
index = pd.bdate_range(start, end)

#%% strings are accepted

pd.date_range('2011-01-01', '2012-01-01')   # OK!
pd.date_range('2011-01-01', '2012-01-01', periods=10)   # great !!!

"""
The start and end dates are strictly inclusive,
so dates outside of those specified will not be generated.
"""
pd.date_range(start, end, freq='BM')
pd.date_range(start, end, freq='W')

#%%
pd.date_range(start, periods=100, freq='M')

pd.bdate_range(start, periods=100, freq='BQS')

pd.bdate_range(end=end, periods=20)   #!!!
pd.bdate_range(end=end, periods=20, freq='W')   #!!!

#%% Custom frequency ranges
""" bdate_range can also generate a range of custom frequency dates
by using the weekmask and holidays parameters.
These parameters will only be used if a custom frequency string is passed.
"""
weekmask = 'Mon Wed Fri'
holidays = [dt.datetime(2011, 1, 5), dt.datetime(2011, 3, 14)]
pd.bdate_range(start, end, freq='C', weekmask=weekmask, holidays=holidays)

pd.bdate_range(start, end, freq='CBMS', weekmask=weekmask)
# https://pandas.pydata.org/docs/user_guide/timeseries.html#custom-business-days

#%%
pd.Timestamp.min
pd.Timestamp.max

#%%
#%% Indexing
# https://pandas.pydata.org/docs/user_guide/timeseries.html#indexing
rng = pd.date_range(start, end, freq='BM')
rng

ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts.index

ts[:5]
ts[::-1]
ts[::2]

#%%
ts['1/31/2011']
ts['31/1/2011']
ts['2011-01-31']
ts[dt.datetime(2011, 12, 25):]
ts[dt.datetime(2011, 11, 25):]
ts['10/31/2011':'12/31/2011']

#%%
ts['2011']
ts['2011-06']

#%%
"""The endpoints will be included.
This would include matching times on an included date:
"""
dft = pd.DataFrame(np.random.randn(200, 1), columns=['A'],
                   index=pd.date_range('20131001', periods=200, freq='D'))
dft.head()
dft.tail()

dft['2013'].head()
dft['2013'].tail()
dft['2014'].head()
dft['2014'].tail()

dft['2014-1':'2014-3']
dft['2014-1':'2014-3-13']

#%% DatetimeIndex partial string indexing also works
# on a DataFrame with a MultiIndex:
dft2 = pd.DataFrame(np.random.randn(20, 1), columns=['A'],
                    index=pd.MultiIndex.from_product(
                            [pd.date_range('20130101', periods=10, freq='12H'),
                            ['a', 'b']]))
dft2

dft2.loc['2013-01-05']

#%%
idx = pd.IndexSlice
dft2 = dft2.swaplevel(0, 1).sort_index()
dft2.loc[idx[:, '2013-01-05'], :]

#%% Slicing with string indexing also honors UTC offset.
df = pd.DataFrame([0], index=pd.DatetimeIndex(['2019-01-01'], tz='US/Pacific'))
df
# [2019-01-01 00:00:00-08:00 | 0]

df['2019-01-01 10:00:00+04:00':'2019-01-01 11:00:00+04:00']   # empty
df['2019-01-01 11:00:00+04:00':'2019-01-01 12:00:00+04:00']
df['2019-01-01 12:00:00+04:00':'2019-01-01 13:00:00+04:00']
df['2019-01-01 13:00:00+04:00':'2019-01-01 14:00:00+04:00']   # empty

#%% Slice vs. exact match
"""
The same string used as an indexing parameter can be treated either as a slice
or as an exact match depending on the resolution of the index.
If the string is less accurate than the index, it will be treated as a slice,
otherwise as an exact match.
"""

series_minute = pd.Series([1, 2, 3],
                          pd.DatetimeIndex(['2011-12-31 23:59:00',
                                            '2012-01-01 00:00:00',
                                            '2012-01-01 00:02:00']))

series_minute.index.resolution  # 'minute'

# A timestamp string less accurate than a minute gives a Series object.
series_minute['2011-12-31 23']

# A timestamp string with minute resolution (or more accurate), gives a scalar instead,
# i.e. it is not casted to a slice.
series_minute['2011-12-31 23:59']
series_minute['2011-12-31 23:59:00']

#%%
series_second = pd.Series([1, 2, 3],
                          pd.DatetimeIndex(['2011-12-31 23:59:59',
                                            '2012-01-01 00:00:00',
                                            '2012-01-01 00:00:01']))

series_second.index.resolution  # 'second'
series_second['2011-12-31 23:59']

#%%
# If the timestamp string is treated as a slice,
# it can be used to index DataFrame with [] as well.

dft_minute = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]},
                          index=series_minute.index)

dft_minute['2011-12-31 23']

#%%
"""!!!
Note also that DatetimeIndex resolution cannot be less precise than day.
"""
series_monthly = pd.Series([1, 2, 3],
                           pd.DatetimeIndex(['2011-12', '2012-01', '2012-02']))

series_monthly.index.resolution   # day

series_monthly['2011-12']  # Series
series_monthly.loc['2011-12']  # Series

"""
Thus you cannot get a sheer value for a given month -- always Series !!!
When indexing with months like 'yyyy-mm'.
You may overcome it only with indexing like 'yyyy-mm-01' what is sometimes clumsy.
"""

#%% Exact indexing
"""
As discussed in previous section, indexing a DatetimeIndex with a partial string
depends on the “accuracy” of the period, in other words how specific the interval
is in relation to the resolution of the index.

In contrast, indexing with Timestamp or datetime objects is exact,
because the objects have exact meaning.
These also follow the semantics of including both endpoints.

These Timestamp and datetime objects have exact hours, minutes, and seconds,
even though they were not explicitly specified (they are 0).
"""
dft = pd.DataFrame(np.random.randn(10000, 1), columns=['A'],
                   index=pd.date_range('20130101', periods=10000, freq='T'))

dft[dt.datetime(2013, 1, 1):dt.datetime(2013, 1, 6)]
dft[dt.datetime(2013, 1, 1, 10, 12, 0):dt.datetime(2013, 1, 6, 10, 12, 0)]

#%%



#%% Truncating & fancy indexing
"""
A truncate() convenience function is provided that is similar to slicing.
Note that truncate assumes a 0 value for any unspecified date component
in a DatetimeIndex in contrast to slicing which returns any partially matching dates:
"""
rng2 = pd.date_range('2011-01-01', '2012-01-01', freq='W')
ts2 = pd.Series(np.random.randn(len(rng2)), index=rng2)
ts2
ts2.truncate(before='2011-11', after='2011-12')
ts2['2011-11':'2011-12']

#%%
"""
Even complicated fancy indexing that breaks the DatetimeIndex frequency regularity
will result in a DatetimeIndex, although frequency is lost:
"""
ts2[[0, 2, 6]].index

#%% Time/date components
# https://pandas.pydata.org/docs/user_guide/timeseries.html#time-date-components

#%%
# .dt accessor
# https://pandas.pydata.org/docs/user_guide/basics.html#basics-dt-accessors
s = pd.Series(pd.date_range('20130101 09:10:12', periods=4))
s
s.dt.hour
s.dt.second
s.dt.day

s[s.dt.day == 2]

## time zone
s.dt.tz    # None

stz = s.dt.tz_localize('US/Eastern')
stz
stz.dt.tz  # <DstTzInfo 'US/Eastern' LMT-1 day, 19:04:00 STD>

s.dt.tz_localize('UTC').dt.tz_convert('US/Eastern')

## strftime()
s = pd.Series(pd.date_range('20130101', periods=4))
s
s.dt.strftime('%Y/%m/%d')

# PeriodIndex
s = pd.Series(pd.period_range('20130101', periods=4))
s
s.dt.year
s.dt.day

# timedelta
s = pd.Series(pd.timedelta_range('1 day 00:00:05', periods=4, freq='s'))
s
s.dt.days
s.dt.seconds
s.dt.components

#!!! Series.dt will raise a TypeError if you access with a non-datetime-like values.

#%% NOTICE that accessor doesn't work (nor is needed) on  DatetimeIndex:

z = pd.Series(range(4), index=s.values)
z
z.index
type(z.index)   # DatetimeIndex

z.index.dt.day  # AttributeError: 'DatetimeIndex' object has no attribute 'dt'
#!!! But it's no worry:
z.index.day
z.index.year

#%%
#%% DateOffset objects
# https://pandas.pydata.org/docs/user_guide/timeseries.html#dateoffset-objects

...
...
...


#%%
#%% Time series-related instance methods
# https://pandas.pydata.org/docs/user_guide/timeseries.html#time-series-related-instance-methods

#%% Shifting / lagging
rng = pd.bdate_range('2011-01-31', periods=10, freq='B')
rng
ts = pd.Series(range(len(rng)), index=rng)
ts
ts[:5]

#%% two types of shifting - changing alignment vs shifting index

# changing alignment
ts.shift(1)             # index not changed (NaN appeared)

# shifting index via `freq` arg
ts.shift(1, freq='D')
ts.shift(1, freq='B')  # see the difference !

ts.shift(1, freq=pd.offsets.BDay())

#%% Frequency conversion
dr = pd.date_range('1/1/2010', periods=4, freq=3 * pd.offsets.BDay())
dr
ts = pd.Series(range(4), index=dr)
ts
ts.asfreq()   #! TypeError: asfreq() missing 1 required positional argument: 'freq'

ts.asfreq(freq=pd.offsets.BDay())
ts.asfreq(freq=3)  # ValueError: Invalid frequency: 3
ts.asfreq(freq='D')    # upsampling
ts.asfreq(freq='3D')   # downsampling (?)
ts.asfreq(freq='12H')  # upsampling

ts.asfreq(pd.offsets.BDay(), method='ffill') # == 'pad'
ts.asfreq(pd.offsets.BDay(), method='bfill') # == 'backfill'
ts.asfreq(pd.offsets.BDay(), fill_value=-1)  # not fills NaNs present before

#%%
#%% Resampling
# https://pandas.pydata.org/docs/user_guide/timeseries.html#resampling
"""
resample() is a time-based groupby, followed by a reduction method on each of its groups.
See some [cookbook](https://pandas.pydata.org/docs/user_guide/cookbook.html#resampling)
examples for some advanced strategies.

The resample() method can be used directly from DataFrameGroupBy objects,
see the [groupby docs]
(https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform-window-resample).


Note
----
See (https://pandas.pydata.org/docs/user_guide/computation.html#window-functions)
and
.resample() is similar to using a rolling() operation with a time-based offset,
see a discussion
[here](https://pandas.pydata.org/docs/user_guide/computation.html#stats-moments-ts-versus-resampling).
"""

#%% Basics
rng = pd.date_range('1/1/2012', periods=100, freq='S')
rng
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts
ts.resample('5Min')    # pandas.core.resample.DatetimeIndexResampler object

ts.resample('5Min').sum()
ts.resample('20S').sum()
ts.resample('20S').ohlc()    #!!!
ts.resample('20S').mean()

ts.resample('20S', closed='right').mean()
ts.resample('20S', closed='left').mean()     # default

"""
Parameters like label are used to manipulate the resulting labels.
label specifies whether the result is labeled with the beginning
or the end of the interval.
"""
ts.resample('20S', label='left').mean()
ts.resample('20S', label='right').mean()

#%% Upsampling
# from secondly to every 250 milliseconds
ts[:3].resample('250L')  # pandas.core.resample.DatetimeIndexResampler object
ts[:3].resample('250L').asfreq()    #!!! compare  ts.asfreq()  above
ts[:3].resample('250L').ffill()
ts[:3].resample('250L').ffill(limit=2)
ts[:3].resample('250L').bfill()

#%% Sparse resampling



#%%



#%%



#%%
