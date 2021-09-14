#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Exceptions
subtitle:
version: 1.0
type: tutorial
keywords: [try, catch, exception, finally]
description: |
    About exceptions
sources:
    - link: https://www.programiz.com/python-programming/user-defined-exception
    - link: https://www.programiz.com/python-programming/exception-handling
    - link: https://www.python-course.eu/python3_exception_handling.php
    - link: https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions

file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: E:/ROBOCZY/Python/help
    date: 2021-09-06
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""

#%%

s = 0
try:
    for k in [1, 2, '3']:
        s += k
finally:
    print(s)

#%%

s = 0
for k in [1, 2, '3', 4, '5', 6]:
    try:
        print("add {}".format(k))
        s += k
    except Exception as e:
        print('cannot add a string "{}"'.format(k))
    finally:
        print(s)


#%%
# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break    # if Error occur `break` is not attained; so it works!
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

#%%