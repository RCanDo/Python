#! python3
"""
---  
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---  

title: Pandas
subtitle: 
version: 1.0
type: cheat sheet
keywords: [data frame, pandas, numpy]
description: code chunks
remarks:
todo:
sources:   # there may be more sources
    - title: Python For Data Science Cheat Sheet
      chapter: Pandas basics
      link: D:/bib/...
      authors: 
          - link: www.DataCamp.com 
      usage: copy & isnpiration for some investigations
file:
    usage: 
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 
    path: D:/ROBOCZY/Python/help/CheatSheets/
    date: 2019-11-13
    authors:   
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email: 
              - arkadiusz.kasprzyk@tieto.com
              - akasp666@google.com
              - arek@staart.pl      
"""              

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

#%%
cd "D:/ROBOCZY/Python/help/CheatSheets/"

#%%
import numpy as np
import pandas as pd

#%%
df = pd.DataFrame({'Date':  ['2019-03-01', '2019-03-02', '2019-03-01', '2019-03-03', '2019-03-02', '2019-03-03'],
                   'Type':  ['a', 'b', 'c', 'a', 'a', 'c'],
                   'Value': [11, 13, 20, 99, 1, -4],
                   'X':     [.1, 1.3, 4.2, .03, 3.1, 0]})
df

#%%

dfp1 = df.pivot(index='Date', columns='Type', values='Value')
dfp1
type(dfp1)  # .DataFrame
# or
pd.pivot_table(df, index='Date', columns='Type', values='Value')

dfp2 = df.pivot(index='Date', columns='Type', values=['Value', 'X'])
dfp2
# or
pd.pivot_table(df, index='Date', columns='Type', values=['Value', 'X'])

#%% stuck - unstack

df = pd.DataFrame({})




