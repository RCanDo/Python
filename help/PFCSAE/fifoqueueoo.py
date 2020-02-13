# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:53:54 2017
@author: kasprark

an object oriented version (where the queue data is part of the queue object).
Probably the best solution, see OO programming for details.
"""

class fifoqueue:
    def __init__(self):
        self.queue = []

    def length(self):
        return len(self.queue)

    def show(self):
        for name in self.queue:
            print("waiting customer: {}".format(name))

    def add(self, name):
        self.queue.insert(0, name)

    def next(self):
        return self.queue.pop()

q1 = fifoqueue()
q1.add("Spearing"); q1.add("Fanghor"); q1.add("Takeda")

q2 = fifoqueue()
q2.add('John'); q2.add('Peter')

print("{} customers in queue1:".format(q1.length())); q1.show()
