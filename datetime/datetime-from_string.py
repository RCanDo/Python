#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:20:23 2023

@author: arek
"""

# %%
import datetime as dt

d = dt.date.fromisoformat('2022-02-22')
d       # datetime.date(2022, 2, 22)

d = dt.datetime.fromisoformat('2022-02-22 02:22:12')
d       # datetime.datetime(2022, 2, 22, 2, 22, 12)

# %%
d = dt.date.strptime('2022/12/13', '%Y/%m/%d')     #! AttributeError: type object 'datetime.date' has no attribute 'strptime'

d = dt.datetime.strptime('2022/12/13', '%Y/%m/%d')
d       # datetime.datetime(2022, 12, 13, 0, 0)

d = dt.datetime.strptime('2022/12/13 - 23:14:55', '%Y/%m/%d - %H:%M:%S')
d       # datetime.datetime(2022, 12, 13, 23, 14, 55)

# %%
d = dt.datetime.fromtimestamp(123456)
d       # datetime.datetime(1970, 1, 2, 11, 17, 36)

d = dt.date.fromtimestamp(123456)
d       # datetime.date(1970, 1, 2)

# %%
d = dt.datetime.fromordinal(123456)
d       # datetime.datetime(339, 1, 5, 0, 0)

d = dt.date.fromordinal(123456)
d       # datetime.date(339, 1, 5)


# %%    What about timezone ???
