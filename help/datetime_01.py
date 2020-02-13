# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:01:00 2018

@author: kasprark
"""

import time
import datetime as dt

dt.date(2018, 1, 1)
tiff = dt.date(2018, 1, 1) -  dt.date(2017, 2, 3)
tiff

dt.date(2018, 9, 9) + dt.timedelta(days=3, hours=12, minutes=34)

fdate = dt.date.today() + dt.timedelta(days=3, hours=12, minutes=34)
fdate
fdate.replace(year = fdate.year + 1)

dt.date.today()
