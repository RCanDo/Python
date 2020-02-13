#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: concurrent.futures
subtitle: Manage Pools of Concurrent Tasks
version: 1.0
type: tutorial
keywords: [concurrent.futures, multithreading, multiprocessing]
description: |
remarks:
    - eg. work interactively (in Spyder)
todo:
sources:
    - title: concurrent.futures
      subtitle: Manage Pools of Concurrent Tasks
      link: https://pymotw.com/3/concurrent.futures/index.html
      date: 2018-03-18
      authors:
      usage:|
          not only copy
    - link: https://docs.python.org/3/library/concurrent.futures.html
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: pymotw-concurrent.futures.py
    path: D:/ROBOCZY/Python/Multi/
    date: 2019-11-30
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
from concurrent import futures
import threading
import time

#%%
"""
The concurrent.futures modules provides interfaces for running tasks
using `pools` of thread or process `workers`.
The APIs are the same, so applications can switch between threads and processes
with minimal changes.

The module provides two types of classes for interacting with the pools.
- `Executor`s are used for managing pools of workers, and
- `Future`s are used for managing results computed by the workers.
To use a `pool of workers`, an application creates an instance
of the appropriate `Executor` class and then submits tasks for it to run.
When each task is started, a `Future` instance is returned.
When the result of the task is needed, an application can use the `Future`
to block until the result is available.
Various APIs are provided to make it convenient to wait for tasks to complete,
so that the Future objects do not need to be managed directly.
"""

#%% some task
def task(n):
    print('{}: sleeping {}'.format(threading.current_thread().name, n))
    time.sleep(n/10)
    print('{}: done with {}'.format(threading.current_thread().name, n))
    return n/10

#%% two arguments tast
def task2(x, y):
    print('{}: sleeping; x={}, y={}'.format(threading.current_thread().name, x, y))
    time.sleep(.5)
    z = x ** y
    print(" {} ".format(z))
    print('{}: done with x={}, y={}'.format(threading.current_thread().name, x, y))
    return z

#%% basic types and usage:

#%% .ThreadPoolExecutor()

#%% task()
ex = futures.ThreadPoolExecutor(max_workers=2)
type(ex)    # <class 'concurrent.futures.thread.ThreadPoolExecutor'>
dir(ex)

f = ex.submit(task, 5)
type(f)     # <class 'concurrent.futures._base.Future'>
dir(f)
f._state   # 'FINISHED'
f._result  # 0.5

results = ex.map(task, range(3))
type(results)   # <class 'generator'>
dir(results)
list(results)

#%% task2()

f2 = ex.submit(task2, 100, 100)
f2._state
f2._result

results = ex.map(task2, range(2, 5), range(10, 7, -1))
results
list(results)

#%% .ProcessPoolExecutor()
# working with .ProecssPoolExecutor() may cause problems interactively, especially with .map()
# it's better to do via terminal: > python process_pool_example.py
# see the last eamples in this file

ex = futures.ProcessPoolExecutor(max_workers=2)
type(ex)    # <class 'concurrent.futures.process.ProcessPoolExecutor'>
dir(ex)

f = ex.submit(task, 5)
type(f)     # concurrent.futures._base.Future
dir(f)
f._state    # 'FINISHED'
f._result   # nothing
type(f._result)  # NoneType
f.result()  #! BrokenProcessPool: A process in the process pool was terminated abruptly while the future was running or pending.
# ???

results = ex.map(task, range(3))
type(results)   # <class 'generator'>
dir(results)
list(results) #! BrokenProcessPool: A process in the process pool was terminated abruptly while the future was running or pending.
# cannot use .map() _interactively_ with .ProcesPoolExecutor() (you can with .Thread...)


#%%

#%%
"""
The ThreadPoolExecutor manages a set of worker threads, passing tasks to them
as they become available for more work.
This example uses map() to concurrently produce a set of results
from an input iterable.
The task uses time.sleep() to pause a different amount of time
to demonstrate that, regardless of the order of execution of concurrent tasks,
map() always returns the values in order based on the inputs.
"""
#%%
ex = futures.ThreadPoolExecutor(max_workers=2)
print(type(ex))        # <class 'concurrent.futures.thread.ThreadPoolExecutor'>
print('main: starting')
results = ex.map(task, range(5, 0, -1))
print(type(results))   # <class 'generator'>
  # iterator (or generator?)
print('main: unprocessed results {}'.format(results))
print('main: waiting for real results')
real_results = list(results)
  # list of result of workers in the order of calling
print('main: results: {}'.format(real_results))

#%%
"""!!!
The return value from map() is actually a special type of iterator
(of returned values from each worker)
that knows to wait for each response as the main program iterates over it.
"""

#%%
#%% Scheduling Individual Tasks
"""
In addition to using map(), it is possible to schedule an individual task
with an executor using submit(),
and use the Future instance returned to wait for that task’s results.
"""

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)      #!!! this way only one thread is run!!!
print(type(f))   # <class 'concurrent.futures._base.Future'>
print('main: future: {}'.format(f))
print('main: waiting for results')
result = f.result()
print('main: result: {}'.format(result))
print('main: future after result: {}'.format(f))

"""
The `status` of the future changes after the tasks is completed and the result
is made available.
"""
dir(f)
f._state  # 'FINISHED'
f._result # .5

#%%
#%% Waiting for Tasks in Any Order  .as_completed()
"""
Invoking the .result() method of a Future blocks until the task completes
(either by returning a value or raising an exception), or is canceled.
The results of multiple tasks can be accessed in the order the tasks were scheduled using map().
If it does not matter what order the results should be processed,
use as_completed() to process them as each task finishes.
"""
import random
def task(n):
    r = random.random() * 10
    print("thread: {}".format(threading.current_thread().name))
    time.sleep(r)
    return (r, n)


ex = futures.ThreadPoolExecutor(max_workers=5)
print('main: starting')

wait_for = [ex.submit(task, i) for i in range(5, 0, -1)] # list of threads

for f in futures.as_completed(wait_for):
    res = f.result()
    print('thread: {}, result: {:1.2f}, {}'. \
           format(threading.current_thread().name, res[0], res[1]))
"""
Workers start according to scheme but returns when they're finnished.
"""

#%% with .map() without .as_complete()
ex = futures.ThreadPoolExecutor(max_workers=5)
print('main: starting')

for res in ex.map(task, range(5, 0, -1)):
    print('thread: {}, result: {:1.2f}, {}'. \
           format(threading.current_thread().name, res[0], res[1]))
"""
returned in the order of calling
"""
#%% ! one cannot join .map() and .as_completed() !
"""
.as_completed() operates on list of `Futures` (workers)
while .map() returns generator of _results_ of the workers
"""

ex = futures.ThreadPoolExecutor(max_workers=5)
print('main: starting')

wait_for = list(ex.map(task, range(5, 0, -1)))

for res in futures.as_completed(list(wait_for)): #! NO !
    #! AttributeError: 'tuple' object has no attribute '_condition'
    #res = f.result()
    print('thread: {}, result: {:1.2f}, {}'. \
           format(threading.current_thread().name, res[0], res[1]))

#%% Future Callbacks
"""
To take some action when a task completed,
without explicitly waiting for the result, use add_done_callback() to specify
a new function to call when the `Future` is done.
The callback should be a callable taking a single argument, the `Future` instance.
"""
def task(n):
    print('{}: sleeping'.format(n))
    time.sleep(0.5)
    print('{}: done'.format(n))
    return n / 10

def done(fut):
    """
    The callback is invoked regardless of the reason the Future is considered “done”,
    so it is necessary to check the status of the object passed in to the callback
    before using it in any way.
    """
    if fut.cancelled():
        print('{}: canceled'.format(fut.arg))
            # Future object has no .arg attribute - it is custom here, see below
    elif fut.done():
        error = fut.exception()
        if error:
            print('{}: error returned: {}'.format(fut.arg, error))
        else:
            result = fut.result()
            print('{}: value returned: {}'.format(fut.arg, result))


ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)
    # arguments passed to task are NOT remembered in the Future object...
    # thus one need:
f.arg = 5   # if one comments it then...  AttributeError: 'Future' object has no attribute 'arg'
f.add_done_callback(done)  #!
    # argument of done() is f, so it works like done() is a method of f
# result = f.result()
# print(result)    # not needed as result is printed by done()


#%% Canceling Tasks
"""
A Future can be canceled, if it has been submitted but not started,
by calling its .cancel() method.
"""
def done(fn):
    if fn.cancelled():
        print('{}: canceled'.format(fn.arg))
    elif fn.done():
        print('{}: not canceled'.format(fn.arg))

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
tasks = []

for i in range(10, 0, -1):
    print('main: submitting {}'.format(i))
    f = ex.submit(task, i)
    f.arg = i
    f.add_done_callback(done)
    tasks.append((i, f))

# cancelling all the tasks which are not done yet
for i, t in reversed(tasks):
    if not t.cancel():
        # cancel() returns a Boolean indicating whether or not the task was able to be canceled.
        print('main: did not cancel {}'.format(i))

ex.shutdown()

#%% Exceptions in Tasks
"""
If a task raises an unhandled exception, it is saved to the Future for the task
and made available through the .result() or .exception() methods.
"""

def task(n):
    print('{}: starting'.format(n))
    raise ValueError('the value {} is no good'.format(n))


ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)

# If result() is called after an unhandled exception is raised
# within a task function...
error = f.exception()
print('main: error: {}'.format(error))

# ...the same exception is re-raised in the current context.
try:
    result = f.result()
except ValueError as e:
    print('main: saw error "{}" when accessing result'.format(e))

#%% Context Manager
"""
Executors work as _context managers_, running tasks concurrently
and waiting for them all to complete.
When the context manager exits, the .shutdown() method of the executor is called.
"""
def task(n):
    print(n)

# as a context manager
with futures.ThreadPoolExecutor(max_workers=2) as ex:
    print('main: starting')
    ex.submit(task, 1)
    ex.submit(task, 2)
    ex.submit(task, 3)
    ex.submit(task, 4)

print('main: done')

"""
This mode of using the executor is useful when the thread or process resources
should be cleaned up when execution leaves the current scope.
"""

#%%
#%% Process Pools
"""
The ProcessPoolExecutor works in the same way as ThreadPoolExecutor,
but uses processes instead of threads.
This allows CPU-intensive operations to use a separate CPU
and not be blocked by the CPython interpreter’s global interpreter lock
(GIL)[https://wiki.python.org/moin/GlobalInterpreterLock].
"""
# concurrent-01.py   # run from Anaconda prompt
# does not run interactively!
# https://stackoverflow.com/questions/15900366/all-example-concurrent-futures-code-is-failing-with-brokenprocesspool
# .map() is guilty; the next example uses .submit() and then it works interactively
import os

def task(n):
    return (n, os.getpid())

ex = futures.ProcessPoolExecutor(max_workers=1)
results = ex.map(task, range(5, 0, -1))
for n, pid in results:
    print('ran task {} in process {}'.format(n, pid))

"""
As with the thread pool, individual worker processes are reused for multiple tasks.
"""

#%%
"""
If something happens to one of the worker processes to cause it to exit unexpectedly,
the ProcessPoolExecutor is considered “broken” and will no longer schedule tasks.
"""
# concurrent-02.py
import os
import signal

with futures.ProcessPoolExecutor(max_workers=2) as ex:
    print('getting the pid for one worker')
    f1 = ex.submit(os.getpid)
    pid1 = f1.result()

    os.kill(pid1, -1) # Windows: -1 / -9 / signal.CTRL_C_EVENT / signal.CTRL_BREAK_EVENT)
                      # Linux: signal.SIGHUP

    print('submitting another task')
    f2 = ex.submit(os.getpid)
    try:
        pid2 = f2.result()
    except futures.process.BrokenProcessPool as e:
        print('could not start new tasks: {}'.format(e))

"""
The BrokenProcessPool exception is actually thrown when the results are processed,
rather than when the new task is submitted.
"""

#%%


#%%


#%%

