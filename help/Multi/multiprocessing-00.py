#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: multiprocessing
subtitle: package
version: 1.0
type: running example
keywords: [multithreading, multiprocessing]
description: |
remarks:
todo:
sources:
    - link: https://stackoverflow.com/questions/28551180/how-to-kill-subprocess-python-in-windows
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: multiprocessing-00.py
    path: D:/ROBOCZY/Python/Multi/
    date: 2019-12-03
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
              - akasp666@google.com
"""
import multiprocessing as mp
import time

def work():
    while True:
        print('work process')
        time.sleep(.5)

if __name__ == '__main__':
    p = mp.Process(target=work)
    p.start()
    for i in range(3):
        print('main process')
        time.sleep(1)
    p.terminate()
    for i in range(3):
        print('main process')
        time.sleep(.5)
