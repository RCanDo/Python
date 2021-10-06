# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:12:54 2019

@author: staar
"""
#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import collections
from collections.abc import Sequence

#%% objects and types

import abc       # abstract base class
import typing    # type hint

#%% functional, etc.

from functools import partial, wraps
import operator as op
import itertools
import contextlib

from toolz.functoolz import juxt
#creates a function that calls several functions with the same arguments
#and returns a tuple of results
# juxt([f1, ..., fn])(x)

#%% system

import sys
import os  # .getpid()
import glob
import signal  #.kill(pid, signal)

from time import time, sleep
import string

import argparse
import logging

#%% helpers

import pprint   # pretty printing
import tqdm     # progress bars

#%% multi

import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

#%% data persistence

import pickle
import shelve
#   d = shelve.open(filename, writeback=True)     # slow
#   d.sync()

#%% development tools

import unittest
import test

#%% networking
import socket

import urllib
# with urllib.request.urlopen(url, timeout=timeout) as conn:
#     return conn.read()

import request

#%% software packaging and distribution

import distutils
import ensurepip
import venv
import zipapp

#%%
#%% math & stats
import math
import fractions

import scipy
from scipy import stats
from scipy import signal

from dateutil.parser import parse
import matplotlib.pyplot as plt
import seaborn as sns

from pandas.plotting import autocorrelation_plot

#%%
import statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf
from statsmodels.tsa.stattools import grangercausalitytests
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.nonparametric.smoothers_lowess import lowess

from statsmodels.tsa.arima_model import ARIMA   # or
from statsmodels.tsa.api import ARIMA           # the same

import statsmodels.api as sm
import statsmodels.stats as st
import statsmodels.tsa.api as ts
import statsmodels.tsa.stattools as tst
import statsmodels.graphics.tsaplots as tsp

import quandl


#%%
