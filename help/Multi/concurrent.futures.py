#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: concurrent.futures
subtitle: official docs
version: 1.0
type: examples
keywords: [concurrent.futures, multithreading, multiprocessing]
description: |
remarks:
todo:
sources:
    - link: https://docs.python.org/3/library/concurrent.futures.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: concurrent.futures.py
    path: D:/ROBOCZY/Python/Multi/
    date: 2019-12-05
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
"""
The concurrent.futures module provides a high-level interface
for asynchronously executing callables.

The asynchronous execution can be performed with
- threads, using ThreadPoolExecutor(),
- or separate processes, using ProcessPoolExecutor().
Both implement the same interface, which is defined by
the abstract Executor class.
"""

#%%
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


#%%
#%% class concurrent.futures.Executor
"""
An abstract class that provides methods to execute calls asynchronously.
It should NOT be used directly, but through its concrete subclasses.
"""
#%% .submit(fn, *args, **kwargs)
"""
Schedules the callable, fn, to be executed as fn(*args **kwargs)
and returns a Future object representing the execution of the callable.
"""
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())

#%% .map(func, *iterables, timeout=None, chunksize=1)
"""
Similar to map(func, *iterables) except:
- the iterables are collected immediately rather than lazily;
- func is executed asynchronously and several calls to func may be made concurrently.
...
When using ProcessPoolExecutor,
this method chops iterables into a number of chunks
which it submits to the pool as separate tasks.
The (approximate) size of these chunks can be specified by setting chunksize
to a positive integer.
For very long iterables, using a large value for chunksize
can significantly improve performance compared to the default size of 1.
With ThreadPoolExecutor, chunksize has no effect.
"""
#%% .shutdown(wait=True)
...


#%%
#%% class concurrent.futures.ThreadPoolExecutor(
#     max_workers=None, thread_name_prefix='', initializer=None, initargs=())
"""
An Executor subclass that uses a pool of at most max_workers threads
to execute calls asynchronously.
...
"""

#%% deadlocks possible
"""
Deadlocks can occur when the callable associated with a Future
waits on the results of another Future. For example:
"""

import time
def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

#%% waiting for itself

def wait_on_future():
    """This will never complete because there is only _one worker thread_ and
       it is executing this function.
    """
    f = executor.submit(pow, 5, 2)  #!? what executor? the one which calls THIS function?
    print(f.result())

executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)

# so, be carefull!!! avoid cross-calling and self-calling
#%%
"""..."""

#%% example
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))


#%%
#%% class concurrent.futures.ProcessPoolExecutor(
#    max_workers=None, mp_context=None, initializer=None, initargs=())
"""
The ProcessPoolExecutor class is an Executor subclass
that uses a pool of processes to execute calls asynchronously.
ProcessPoolExecutor uses the multiprocessing module,
which allows it to side-step the Global Interpreter Lock
but also means that only _picklable_ objects can be executed and returned.

The __main__ module must be importable by worker subprocesses.
This means that ProcessPoolExecutor will not work in the interactive interpreter.

Calling Executor or Future methods from a callable
submitted to a ProcessPoolExecutor will result in deadlock.
"""

#%%



#%%



#%%






