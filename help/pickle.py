# -*- coding: utf-8 -*-
#! python3
"""
---  
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---  

title: pickle
subtitle:
version: 1.0
type: example
keywords: [pickling, serialization]   # there are always some keywords!
description: 
sources:
    - title: Python Pickle Module for saving Objects by serialization
      link: https://pythonprogramming.net/python-pickle-module-save-objects-serialization/
      usage: code snippets copy
file:
    usage: 
        interactive: False
        terminal: True
    name: pickle.py
    path: D:/ROBOCZY/Python/help/
    date: 2019-09-12
    authors:   
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email: 
              - arkadiusz.kasprzyk@tieto.com
              - akasp666@google.com
              - arek@staart.pl      
"""   

import pickle

#%% some data

dd = {1:"6", 2:"2", 3:"f"}

#%%

fout = open("dict.pickle","wb")
pickle.dump(dd, fout)
fout.close()

#%%

fin = open("dict.pickle","rb")
ddn = pickle.load(fin)
fin.close()

print(ddn)
print(ddn[3])

dd == ddn

#%%


