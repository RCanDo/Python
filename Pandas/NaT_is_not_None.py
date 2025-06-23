#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 08:22:13 2025

@author: arek
"""
import pandas as pd

pd.NaT is None          # False
None is pd.NaT          # False
pd.NaT is pd.NaT        # True
pd.NaT == pd.NaT        # False
None == None            # True
if pd.NaT: print(1)     # 1

pd.Timestamp(None)      # NaT
pd.Timestamp(None) is pd.NaT        # True    ok
isinstance(pd.NaT, pd.Timestamp)    # False   !!!
isinstance(pd.Timestamp(None), pd.Timestamp)    # False
