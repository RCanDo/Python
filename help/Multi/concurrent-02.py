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
    - only from command line
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
    - link: https://stackoverflow.com/questions/28551180/how-to-kill-subprocess-python-in-windows
file:
    usage:
        interactive: False   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: concurrent-02.py
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
import os
import signal

def main():
    with futures.ProcessPoolExecutor(max_workers=2) as ex:
        print('getting the pid for one worker')
        f1 = ex.submit(os.getpid)
        pid1 = f1.result()

        print('killing process {}'.format(pid1))
        os.kill(pid1, -9) # Windows: -1 / -9 / signal.CTRL_C_EVENT / signal.CTRL_BREAK_EVENT)
                          # Linux: signal.SIGHUP

        print('submitting another task')
        f2 = ex.submit(os.getpid)
        try:
            pid2 = f2.result()
        except futures.process.BrokenProcessPool as e:
            print('could not start new tasks: {}'.format(e))

txt = """
The BrokenProcessPool exception is actually thrown when the results are processed,
rather than when the new task is submitted.
"""

if __name__ == "__main__":
    main()
    print(txt)