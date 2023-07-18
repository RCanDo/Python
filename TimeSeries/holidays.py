#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 13:53:19 2023

@author: arek
"""
from datetime import date
import holidays

us_holidays = holidays.US()  # this is a dict
us_holidays
# the below is the same, but takes a string:
us_holidays = holidays.country_holidays('US')  # this is a dict
us_holidays
type(us_holidays)   # holidays.countries.united_states.US   NOT A DICT !!!

nyse_holidays = holidays.NYSE()  # this is a dict
# the below is the same, but takes a string:
nyse_holidays = holidays.financial_holidays('NYSE')  # this is a dict

date(2015, 1, 1) in us_holidays  # True
date(2015, 1, 2) in us_holidays  # False
us_holidays.get('2014-01-01')  # "New Year's Day"


# %%

hpl = holidays.PL()     # this is a dict
hpl                     # holidays.country_holidays('PL')

date(2015, 5, 3) in hpl  # True
date(2015, 5, 2) in hpl  # True
date(2015, 5, 1) in hpl  # True

# %%
ts

