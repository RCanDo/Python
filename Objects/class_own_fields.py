# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:00:41 2019

@author: kasprark

"""

import shelve

cd E:/ROBOCZY/Python/Objects/

#%%

class Cls():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def save(self, file):
        f = shelve.open(file, 'n')     #!!! see help(shelve) !!!
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
abc.print()     # globals + dir(self)

# notice that  dir(self)  is much MORE then  self.__dict__
dir(abc)

abc.__dict__    # only  attributes! (no methods, magics and hiddens)
                # the same  as
vars(abc)       # the same  as
abc.myself()    # print(vars(self))

#%%

abc.save('abc')

pqr = Cls([0, 0], '0', 0)
pqr.myself()
pqr.load('abc')
pqr.myself()

del(abc)

#%%
help(shelve)
#   d = shelve.open(filename, writeback=True)     # slow
#   d.sync()

#%%
