# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:27:59 2019

@author: kasprark
"""


#%%

"""
You're trying to access Outer's class instance, from inner class instance.
So just use factory-method to build Inner instance and pass Outer instance to it.
"""
class Outer(object):

    def __init__(self, a, b):
        self.inner = self.createInner(self)
        self.a = a
        self.b = b

    def somemethod(self, c):
        return self.a+c

    def anothermethod(self, c):
        return self.b+c


    def createInner(self, outer):
        return Outer.Inner(outer)

    class Inner(object):
        def __init__(self, outer):
            self.outer = outer
            #self.outer.somemethod()

        def inner_somemethod(self, d):
            return self.outer.anothermethod(d)

    def inner_from_outer(self, d):
        return self.inner.inner_somemethod(d)


#%%
outer = Outer(1, 2)
vars(outer)  # {'inner': <__main__.Outer.Inner at 0x1c2b1101520>, 'a': 1, 'b': 2}

vars(outer.inner)

outer.inner_from_outer(4)


#%%
#%%

class Outer():

    def __init__(self, nr):
        self.qq = "qq"
        self.nr = nr

    class Inner():
        def __init__():
            pass


#%%
#%%
class Classa():
    def __init__(self, nr):
        self.qq = "qq"
        self._nr = nr
    def action(self, nr):
        self._nr = nr
        return self
    @property
    def nr(self):
        return self._nr

#%%

cl = Classa(0)
cl.nr

cl.action(2)
cl.nr

cl.action(3).nr

vars(cl)    # {'qq': 'qq', '_nr': 3}

#%%