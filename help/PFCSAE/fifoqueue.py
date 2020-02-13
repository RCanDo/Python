# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:11:59 2017
@author: kasprark

the original FIFO-queue solution (using a global variable, generally not good)
"""

queue = []

def length():
    '''Returns number of waiting customers'''
    return len(queue)

def show():
    '''Print list of customers; logest waiting customer at the end'''
    for name in queue:
        print("waiting customer: {}".format(name))

def add(name):
    '''Customer with name "name" joining the queue'''
    queue.insert(0, name)

def next():
    '''Returns name of the next to serve, removes customer from queue'''
    return queue.pop()

add('Spearing'); add('Fanghor'); add('Takeda')