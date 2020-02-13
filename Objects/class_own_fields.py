# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:00:41 2019

@author: kasprark
"""

import shelve

cd D:/ROBOCZY/Python/help/

#%%

class Cls():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def save(self, file):
        f = shelve.open(file, 'n')
        for k in vars(self):
            f[k] = vars(self)[k]
        f.close()

    def load(self, file):
        f = shelve.open(file)
        kwargs = dict()
        for k in f:
            kwargs[k] = f[k]
        f.close()
        self.__init__(**kwargs)

    def print(self):
        for k in globals():
            print(k)
        print('qqryq')
        for k in dir(self):
            print(k)

    def myself(self):
        print(vars(self))

#%%

abc = Cls('1', 2, [2, 3])
abc
abc.print()

abc.myself()
vars(abc)
abc.__dict__

#%%

abc.save('abc')

pqr = Cls([0, 0], '0', 0)
pqr.myself()
pqr.load('abc')
pqr.myself()

del(abc)


