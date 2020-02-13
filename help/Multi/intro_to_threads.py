#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Intro to Threads and Processes in Python
version: 1.0
type: tutorial
keywords: [..., multithreading, multiprocessing]
description: |
remarks:
    - eg. work interactively (in Spyder)
todo:
sources:
    - title: Intro to Threads and Processes in Python
      subtitle: Beginner’s guide to parallel programming
      link: https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b
      date: 2017-08-27
      authors:
          - fullname: Brendan Fortuner
      usage:|
          not only copy
    - link: https://github.com/bfortuner/ml-study/blob/master/multitasking_python.ipynb
    - link: https://docs.python.org/3/library/concurrent.futures.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: intro_to_threads.py
    path: D:/ROBOCZY/Python/Multi/
    date: 2019-11-29
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
cd D:/ROBOCZY/Python/Multi/
ls

#%%
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
    # https://docs.python.org/3/library/concurrent.futures.html
import numpy as np
import matplotlib.pyplot as plt
import random
import string
import time
import glob
from PIL import Image   # https://pillow.readthedocs.io/en/stable/handbook/index.html
from urllib.request import urlopen

#%%
def multithreading(func, args, workers):
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [t0 for t in range(len(args))])
    return list(res)

def multiprocessing(func, args, workers):
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=workers) as executor:
        res = executor.map(func, args, [t0 for t in range(len(args))])
    return list(res)

#%%
#%% API calls
def download(url):
    start = time.time()
    try:
        res = urlopen(url)
    except Exception as e:
        print(e)
    stop = time.time()
    return start, stop

#%%
URL = "http://www.math.uni.wroc.pl/~kasprzyk/dydaktyka/ModLin.pdf"
URL1 = "http://www.cs.toronto.edu/~tingwuwang/REINFORCE.pdf"
URL2 = "http://faculty.marshall.usc.edu/gareth-james/ISL/ISLR%20Seventh%20Printing.pdf"

N = 16
urls = [URL]*N

#%% serial
%timeit -n 1 list(map(download, urls))
%timeit -n 1 [download(url) for url in urls]
%timeit -n 10 list(map(download, urls))

#%% Multi-
#%%
#%% -threading

t0 = time.time()
with ThreadPoolExecutor(max_workers=1) as executor:
    res = executor.map(download, urls, [t0 for t in range(len(urls))])
list(res)

res = multithreading(download, urls, 1)


#%% -processing


#%%



#%%

