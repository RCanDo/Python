# -*- coding: utf-8 -*-
"""
Created on Sat May  2 09:13:27 2020

link: https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns-of-a-pandas-dataframe
"""


import pandas as pd

pd.options.display.width = 0  # autodetects the size of your terminal window

pd.set_option('display.max_rows', 500)
#pd.options.display.max_rows = 500         # the same

pd.set_option('display.max_columns', 500)

pd.set_option('max_colwidth', None)
#pd.options.display.max_colwidth = 500         # the same

pd.set_option('display.width', 1000)
pd.set_option('display.max_seq_items', None)

pd.set_option('display.expand_frame_repr', False)

pd.set_option('display.precision', 2)

pd.set_option('display.large_repr', 'truncate')    # ?

#%%

