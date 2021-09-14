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

#%%

#%%
