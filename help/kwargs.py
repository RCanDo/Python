# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:30:52 2019

@author: kasprark
"""

#%%
a,b,*c = [1,2,3,4,5]
print(a,b,c)

#%%
def fun(**kwargs):
    print(list(kwargs.keys()))
    print(kwargs.values())

#%%
fun(a='b', c=3)
fun(dict(a='b', c=3))
fun(**dict(a='b', c=3))

#%%
def fun(a=1, b=2, c=3):
    return a * b + c

fun()

dic = {"a":1, "b":2, "c":3}
dic

fun(**dic)

dic2 = {}
dic2 = {**dic}
dic2["p"] = 4.5


#%%
#%%
def some_function (a,b,c,d):
       print(a,b,c,d)

some_list = [1,2,3,4]
some_function(*some_list)

some_dictionary = {'a':1, 'b':2, 'c':13, 'd':14}
some_function(**some_dictionary)

#%%
# List Packing
def some_list_packing(*args):
       args = list(args)                        #!!!

       args[0] = 'I am about to'
       args[1] = 'pack lists'

       some_function(*args)

# use the previous function unpacking
some_list_packing('I am packing','','','')
# I am about to pack lists

#%% Dictionary Packing
def some_dictionary_packing(**kwargs):
    for key in kwargs:                          #!!!
        print(f'{key} = {kwargs[key]}')

some_dictionary_packing(a= "I", b= "am", c= "about", d= "to write..")


#%%
#%%
def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)
# 1, 0, 1

myfunc(**dict_vec)
# 1, 0, 1

#%%
def argskwargs(*args, **kwargs):
    print(args)
    print(list(args))
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

argskwargs(1, 2, 3)
argskwargs(a=1, b=2, c=3)
argskwargs(-1, 0, 4, a=1, b=3, c=3)

#%%
arguments = [-2, -1, 0]

kwarguments = dict(a=1, b=2, c=3)
kwarguments

argskwargs(arguments)     # works but not the way we expect
argskwargs(*arguments)    # OK

argskwargs(kwarguments)   # works but not the way we expect
argskwargs(**kwarguments) # OK

#%%
#%% how itworks with namedtuples

from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
Car
    ## ~= class with attributes 'color' and 'mileage'
Car()

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color
#'red'
my_car.mileage

#%%
argskwargs(my_car)
argskwargs(*my_car)   # OK
argskwargs(**my_car)  #! TypeError: argskwargs() argument after ** must be a mapping, not Car
argskwargs(**my_car._asdict())  #! OK


#%%





#%%

