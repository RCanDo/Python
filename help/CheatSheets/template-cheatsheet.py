#! python3
"""
---  
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---  

title: 
subtitle: 
version: 1.0
type: cheat sheet
keywords: [kw1, kw2, ..., kwn]
description: code chunks
remarks:    # additional notes worth emphasising  
    - eg. work interactively (in Spyder)
    - install PackageX first
    - etc.
todo:
    - problem 1
    - problem 2   # and so on...
sources:   # there may be more sources
    - title:     # title of the book or internet page 
      chapter:   # if necessary
      pages:     # if necessary
      link: https://the_page/../xxx.domain
      date:    # date of issue or last edition of the page
      authors: 
          - nick: 
            fullname: 
            link: www.DataCamp.com 
      usage: copy & isnpiration for some investigations
file:
    usage: 
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 
    path: D:/ROBOCZY/Python/help/CheatSheets/
    date: 2019-10-29
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