#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:32:46 2023

@author: arek
"""

# %%
# %%  use of super()
class P:
    def __init__(self, x):
        self.x = 2 * x

class Q(P):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        self.z = self.x - self.y

# %%
q = Q(1, 2)
q.x
q.y
q.z

# %% BUT
class Q1(P):
    def __init__(self, x, y):
        P.__init__(x)
        self.y = y
        self.z = self.x - self.y

# %%
q = Q1(1, 2)    # TypeError: P.__init__() missing 1 required positional argument: 'x'

# %% must be
class Q1(P):
    def __init__(self, x, y):
        P.__init__(self, x)
        self.y = y
        self.z = self.x - self.y

q = Q(1, 2)
q.x
q.y
q.z

# %%

# %%  multiple inheritance
# %%
class A:

    classarg = "I'm class A"

    def __init__(self):
        self.a = 1
        self.b = self.qq(self.a)

    @staticmethod
    def qq(b):
        return b * 2

    @property
    def diff(self):
        return self.a - self.b

    def sum(self):
        return self.a + self.b

# %%
A.classarg
a = A()
a.classarg
a.a
a.b
a.sum()
a.diff

a.qq(2)
A.qq(2)

# %%
# %%
class B:
    def __init__(self):
        self.obj_a = A()

    def __getattr__(self, attr):
        return getattr(self.obj_a, attr)

# %%
# composition does not allow for "inheritance" of class attributes
B.classarg  # ! AttributeError: type object 'B' has no attribute 'classarg'

b = B()
b.classarg
b.a
b.b
b.sum()
b.diff

b.qq(2)
B.qq(2)     # AttributeError: type object 'B' has no attribute 'qq'


# %%
# %%
class C:
    """ the same as B but checking for proper "parent"
    """
    def __init__(self):
        self.obj_a = A()

    def __getattr__(self, attr):
        if attr in dir(self.obj_a): # .__dict__:
            print('true')
            attr = getattr(self.obj_a, attr)
        return attr


# %%
# composition does not allow for "inheritance" of class attributes
C.classarg  # ! AttributeError: type object 'B' has no attribute 'classarg'

c = C()
c.a
c.b
c.sum()     # ! TypeError: 'str' object is not callable
c.diff

c.qq(2)     # ! TypeError: 'str' object is not callable


# %%
class  A1:
    classarg1 = "I'm A1"
    def __init__(self):
        self.a1 = 11
        self.b1 = self.qq(self.a1)

    @staticmethod
    def qq(b):
        return b * 3

    def sum(self):
        return self.a1 + self.b1

    def sum1(self):
        return self.a1 + self.b1


# %%
class C1:
    """"""
    def __init__(self):
        self.obj_a = A()
        self.obj_a1 = A1()

        print(self.a1)

    def __getattr__(self, attr):
        # attr = getattr(self.obj_a1, attr) or getattr(self.obj_a)      # doesn't work
        if attr in dir(self.obj_a):
            print('a')
            attr = getattr(self.obj_a, attr)
        elif attr in dir(self.obj_a1):
            print('a1')
            attr = getattr(self.obj_a1, attr)
        return attr

    def __dir__(self):
        return list(set(dir(self.obj_a)).union(set(dir(self.obj_a1))))

# %%
# composition does not allow for "inheritance" of class attributes
C1.classarg  # ! AttributeError: type object 'C' has no attribute 'classarg'

c1 = C1()
c1.classarg
c1.classarg1

c1.a
c1.a1
c1.b
c1.b1
c1.sum()
c1.sum1()
c1.diff

dir(c1)


# %%
