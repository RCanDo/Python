# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:34:10 2017
@author: kasprark

Improved FIFO solution
a modified version where the queue variable is passed to every function
(! this is object oriented programming without objects)
"""

def length(queue):
    return len(queue)

def show(queue):
    for name in queue:
        print("Waiting customer: {}".format(name))

def add(queue, name):
    queue.insert(0, name)

def next(queue):
    return queue.pop()

q1 = []
add(q1, 'Spearing'); add(q1, 'Fanghor'); add(q1, "Takeda")

q2 = []
add(q2, 'John'); add(q2, 'Peter')

print("{} customers in q1:".format(length(q1))); show(q1)
print("{} customers in q2:".format(length(q2))); show(q2)

