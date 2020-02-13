#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Accessing methods from superclasses
subtitle:
version: 1.0
type: tutorial
keywords: [super, subclass, superclass, ]
description: |
remarks:
todo:
sources:
    - title: Expert Python Programming
      chapter: 03 - Syntax Best Practices
      pages: 80-
      link: d:/bib/Python/expertpythonprogramming.pdf
      date: 2016
      authors:
          - fullname: Michał Jaworski
          - fullname: Tarek Ziadé
      usage: |
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 02-accessing_methods_from_superclass.py
    path: D:/ROBOCZY/Python/help/ExpertPython/03-SyntaxBestPractices/
    date: 2019-12-15
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
"""
Best practices
To avoid all the mentioned problems, and until Python evolves in this field, we need
to take into consideration the following points:
• Multiple inheritance should be avoided: It can be replaced with some
design patterns presented in Chapter 14, Useful Design Patterns.
• super() usage has to be consistent: In a class hierarchy, super should be
used everywhere or nowhere. Mixing super and classic calls is a confusing
practice. People tend to avoid super, for their code to be more explicit.
• Explicitly inherit from `object` in Python 3 if you target Python 2 too: Classes
without any ancestor specified are recognized as old-style classes in Python
2. Mixing old-style classes with new-style classes should be avoided in
Python 2.
• Class hierarchy has to be looked over when a parent class is called:
To avoid any problems, every time a parent class is called, a quick glance
at the involved MRO (with __mro__) has to be done.
"""
#%%
cd D:/ROBOCZY/Python/help/ExpertPython/0x-chapter

#%%
"""
The Python official documentation lists super as a built-in function.
But it's a built-in class, even if it is used like a function:
"""
super          # super
super(type)    # <super: type, None>
super(object)  # <super: object, None>

#%%
class A(): pass
super(A)  # <super: __main__.A, None>
super(A())  # TypeError: super() argument 1 must be type, not A

#%% Ex. 1

class Mama:
    def says(self):
        print("do your homework")

class Sister(Mama):
    def says(self):
        Mama.says(self)     # a static usage of an instance method
                            # `self` here used only as dummy argument, see below
        print("and clean your bedroom")

#%%
Mama.says()  #! not a static method but one may use fake variable:
Mama.says(1)

m = Mama()
m.says()
# do your homework

s = Sister()
s.says()  # do your homework | and clean your bedroom

#%%
"""
Notice that `self` in  Mama.says(self)  is used as a dummy argument, i.e.
has no influence on result of .says() but must be passed because
.says() is defined as an instance method while used here in a static mode
(called from the class);
thus the first argument is not substituted with instance (and has no default);
"""

class Sister(Mama):
    def says(self):
        Mama.says(1)   # a static usage of an instance method
                       # 1 used only as dummy argument, see above
        print("and clean your bedroom")

s = Sister()
s.says()  # do your homework | and clean your bedroom

#%% it is better to use  super(type, object).

class Sister(Mama):
    def says(self):
        super(Sister, self).says()
        print("and clean your bedroom")

s = Sister()
s.says()  # do your homework | and clean your bedroom

#%%

class Sister(Mama):
    def says(self):
        super(Sister, self).says()      # `self` necessary here ...
        print("and clean your bedroom")

s = Sister()
s.says()  # do your homework | and clean your bedroom

#%% !!!
class Sister(Mama):
    def says(self):
        super(Mama).says()      # only one argument
        print("and clean your bedroom")

s = Sister()
s.says()  # do your homework | and clean your bedroom

#%%
class Sister(Mama):
    def says(self):
        super().says()      # or leave super() empty
        print("and clean your bedroom")

s = Sister()
s.says()  # do your homework | and clean your bedroom

#%%
"""
The shorter form of super (without passing any arguments) is allowed inside the
methods but super is not limited to methods. It can be used in any place of code
where a call to the given instance superclass method implementation is required.
Still, if super is not used inside the method, then its arguments are mandatory:
"""
anita = Sister()
super(anita.__class__, anita)  # <super: __main__.Sister, <__main__.Sister at 0x1f517a9c748>>
super(anita.__class__, anita).says()   # do your homework

#%%
"""
The last and most important thing that should be noted about super is that its second
argument is optional. When only the first argument is provided, then super() returns
an _unbounded type_. This is especially useful when working with `classmethod`:
"""
super(anita.__class__)  #  <super: __main__.Sister, None>
super(anita.__class__).__class__  # super
type(super(anita.__class__))   # super
# ???

#%% Ex. 2
class Pizza:
    def __init__(self, toppings=[]):
        self.toppings = toppings

    def __repr__(self):
        return "Pizza with " + " and ".join(self.toppings)

    @classmethod
    def recommend(cls):
        """Recommend some pizza with arbitrary toppings,"""
        return cls(['spam', 'ham', 'eggs'])

class VikingPizza(Pizza):
    @classmethod
    def recommend(cls):
        """Use same recommendation as super but add extra spam"""
        #print(super(VikingPizza))  # <super: <class 'VikingPizza'>, NULL>
        #print(dir(super(VikingPizza)))
        #recommended = super(VikingPizza).recommend()
            #! AttributeError: 'super' object has no attribute 'recommend'
            # so you really cannot call super() with one argument from Python 3.8 at least
        recommended = super(VikingPizza, cls).recommend()  # ok!
        #recommended = super().recommend()  # ok!
        recommended.toppings += ['spam'] * 5
        return recommended

#%%

p = Pizza()
p
p.recommend()

vp = VikingPizza()
vp.recommend()

#%%
# MRO -- Method Resolution Order
#
#%%
"""
L(Class) -- linearisation of Class i.e. linearly ordered all ancestors

C3 algorithm (Python 3):

L(C(A, B)) = C + merge(L(A), L(B), A, B)

where merge(.) works like:
Take the head of the first list, that is, L[A][0]; if this head is not in the tail of
any of the other lists, then add it to the linearization of C and remove it from
the lists in the merge, otherwise look at the head of the next list and take it, if it is a
good head.
Then, repeat the operation until all the classes are removed or it is impossible to
find good heads. In this case, it is impossible to construct the merge, Python 2.3
will refuse to create the class MyClass and will raise an exception.

head(list) = list[0]
tail(list) = list[1:]
"""

#%% super() pitfalls

class A:
    def __init__(self):
        print("A", end=" ")
        super().__init__()

class B:
    def __init__(self):
        print("B", end=" ")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C", end=" ")
        A.__init__(self)    # C instance is passed and super(). in A.__init__ calls B
        B.__init__(self)    # here A is not called again according to C3

#%%
C.mro()   # [__main__.C, __main__.A, __main__.B, object]
C.__mro__ # (__main__.C, __main__.A, __main__.B, object)
print("MRO:", [x.__name__ for x in C.__mro__])  # MRO: ['C', 'A', 'B', 'object']

cmroindex = C.__mro__.index
cmroindex
cmroindex(A)
cmroindex(B)
cmroindex(C)


C()  # C A B B ...  -- double B !!!

#%% static use of __init__'s
class C(A, B):
    def __init__(self):
        print("C", end=" ")
        # A.__init__(1)     #! super(type, obj): obj must be an instance or subtype of type
        A.__init__(None)    # not using `self`
        B.__init__(None)

C()  # C A B   # now OK

#%% or better
class C(A, B):
    def __init__(self):
        print("C", end=" ")
        super(A, self).__init__()    #
        super(B, self).__init__()

C()  # C B   # now OK?

#%%
#  Heterogeneous arguments
#
#%%
"""
Another issue with super usage is the argument passing in initialization. How can
a class call its base class __init__() code if it doesn't have the same signature?
This leads to the following problem:
"""
class CommonBase:
    def __init__(self):
        print('CommonBase')
        super().__init__()

class Base1(CommonBase):
    def __init__(self):
        print('Base1')
        super().__init__()

class Base2(CommonBase):
    def __init__(self, arg):
        print('base2')
        super().__init__()

class MyClass(Base1 , Base2):
    def __init__(self, arg):
        print('my base')
        super().__init__(arg)    # which __init_() ?

MyClass.mro()  # [__main__.MyClass, __main__.Base1, __main__.Base2, __main__.CommonBase, object]

#%%
MyClass(1)  #! TypeError: __init__() takes 1 positional argument but 2 were given
            #  Base1.__init__()  is called first but it accepts only `self`

#%%
class MyClass(Base1 , Base2):
    def __init__(self, arg):
        print('my base')
        super(Base2, self).__init__()    # which __init_() ?

MyClass(1)   # OK

#%%  static use of __init__()
class MyClass(Base1 , Base2):
    def __init__(self, arg):
        print('my base')
        Base2.__init__(None, arg)    # which __init_() ?

MyClass(1)   # OK

#%%

