#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: concurrent.futures
subtitle: Manage Pools of Concurrent Tasks
version: 1.0
type: running example
keywords: [concurrent.futures, multithreading, multiprocessing]
description: |
remarks:
    - only from command line OR in Spyder run whole file via F5;
    - this way doesn't show printing from task(); why???
    - in Windows doesn't run from terminal!
    - but it runs under Anaconda prompt :)
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
    - https://stackoverflow.com/questions/15900366/all-example-concurrent-futures-code-is-failing-with-brokenprocesspool
file:
    usage:
        interactive: False   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: concurrent-01.py
    path: D:/ROBOCZY/Python/Multi/
    date: 2019-12-03
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

from concurrent import futures
import time
import random
import os

def task(n):
    t = 10 * random.random()
    print("task {} at process {} is sleeping for {:1.2f}".format(n, os.getpid(), t))
    time.sleep(t)
    return (n, os.getpid(), t)

def main():
    ex = futures.ProcessPoolExecutor(max_workers=2)
    results = ex.map(task, range(5, 0, -1))
    for n, pid, t in results:
        print('ran task {} in process {} for time {:1.2f}'.format(n, pid, t))

if __name__ == "__main__":
    main()
    print("As with the thread pool, individual worker processes are reused for multiple tasks.")
