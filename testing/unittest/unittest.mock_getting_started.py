#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
title: unittest.mock — getting started
version: 1.0
type: tutorial
keywords: [unittest, mock, ...]
description: |
remarks:
todo:
    -
sources:
    - title: unittest.mock — getting started
      link: https://docs.python.org/3/library/unittest.mock-examples.html
file:
    date: 2023-12-31
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
# %%
from unittest.mock import MagicMock, Mock, patch, call

# %%
"""
Common uses for Mock objects include:

    Patching methods

    Recording method calls on objects

You might want to replace a method on an object
to check that it is called with the correct arguments by another part of the system:
"""

# %%
class SomeClass():
    def method():
        pass

real = SomeClass()
real.method = MagicMock(name='method')
real.method(3, 4, 5, key='value')

"""
Once our mock has been used (real.method in this example)
it has methods and attributes that allow you to
    make assertions about how it has been used.
"""
real.method.assert_called_once_with(1, 2, 3)
"""
Traceback (most recent call last):

  Cell In[7], line 1
    real.method.assert_called_once_with(1, 2, 3)

  File ~/programming/anaconda3/envs/e3a/lib/python3.10/unittest/mock.py:941 in assert_called_once_with
    return self.assert_called_with(*args, **kwargs)

  File ~/programming/anaconda3/envs/e3a/lib/python3.10/unittest/mock.py:929 in assert_called_with
    raise AssertionError(_error_message()) from cause

AssertionError: expected call not found.
Expected: method(1, 2, 3)
Actual: method(3, 4, 5, key='value')
"""

# %%  Mock Patching Methods
class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

real = ProductionClass()
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1, 2, 3)
real.something.assert_called_once_with(1, 2, 4)
"""
Traceback (most recent call last):

  Cell In[11], line 1
    real.something.assert_called_once_with(1, 2, 4)

  File ~/programming/anaconda3/envs/e3a/lib/python3.10/unittest/mock.py:941 in assert_called_once_with
    return self.assert_called_with(*args, **kwargs)

  File ~/programming/anaconda3/envs/e3a/lib/python3.10/unittest/mock.py:929 in assert_called_with
    raise AssertionError(_error_message()) from cause

AssertionError: expected call not found.
Expected: mock(1, 2, 4)
Actual: mock(1, 2, 3)
"""

# %%  Mock for Method Calls on an Object
class ProductionClass:
    def closer(self, something):
        something.close()

real = ProductionClass()
mock = Mock()
real.closer(mock)
mock.close.assert_called_with()
mock.close2.assert_called_with()
"""
Traceback (most recent call last):

  Cell In[18], line 1
    mock.close2.assert_called_with()

  File ~/programming/anaconda3/envs/e3a/lib/python3.10/unittest/mock.py:920 in assert_called_with
    raise AssertionError(error_message)

AssertionError: expected call not found.
Expected: close2()
Actual: not called.
"""

# %%  Mocking Classes
def some_function():
    instance = module.Foo()             # what module?
    return instance.method()

with patch('module.Foo') as mock:
    instance = mock.return_value
    instance.method.return_value = 'the result'
    result = some_function()
    assert result == 'the result'

#! ModuleNotFoundError: No module named 'module'        ???

# %%  Naming your mocks
mock = MagicMock(name='foo')
mock
mock.method

# %%  Tracking all Calls
# Often you want to track more than a single call to a method.
# The `.mock_calls` attribute records all calls to child attributes of the mock - and also to their children.

mock = MagicMock()

mock.method()
# <MagicMock name='mock.method()' id='125297755480480'>
mock.attribute.method(10, x=53)
# <MagicMock name='mock.attribute.method()' id='125297755545248'>

mock.mock_calls
"""
[call.method(),
 call.attribute.method(10, x=53),
]
"""

# If you make an assertion about mock_calls and any unexpected methods have been called,
# then the assertion will fail.
# This is useful because as well as asserting that the calls you expected have been made,
# you are also checking that they were made in the right order and with no additional calls:

# You use the call object to construct lists for comparing with mock_calls:

expected = [call.method(), call.attribute.method(10, x=53)]
mock.mock_calls == expected     # True

# run it again
mock.attribute.method(1, x=5)
mock.method()
mock.mock_calls == expected     # False
mock.mock_calls
"""
[call.method(),
 call.attribute.method(10, x=53),
 call.attribute.method(1, x=5),
 call.method()]
"""

# However, parameters to calls that return mocks are not recorded,
# which means it is not possible to track nested calls where the parameters used to create ancestors are important:

m = Mock()
m.factory(important=True).deliver()
# <Mock name='mock.factory().deliver()' id='125297753827808'>

m.mock_calls[-1] == call.factory(important=False).deliver()  # True

# %%  Setting Return Values and Attributes

# Setting the return values on a mock object is trivially easy:
mock = Mock()
mock.return_value   # <Mock name='mock()' id='125297753829296'>

mock.return_value = 3
mock()  # 3
mock.return_value   # 3

# Of course you can do the same for methods on the mock:
mock = Mock()
mock.method.return_value = 3
mock.method()

# The return value can also be set in the constructor:
mock = Mock(return_value=3)
mock()

# If you need an attribute setting on your mock, just do it:
mock = Mock()
mock.x = 3
mock.x

# Sometimes you want to mock up a more complex situation,
# like for example
mock.connection.cursor().execute("SELECT 1")
# <Mock name='mock.connection.cursor().execute()' id='125297753833088'>

# If we wanted this call to return a list, then we have to configure the result of the nested call.
# We can use call to construct the set of calls in a “chained call” like this for easy assertion afterwards:
mock = Mock()
cursor = mock.connection.cursor.return_value
cursor  # <Mock name='mock.connection.cursor()' id='125297753827088'>

cursor.execute.return_value = ['foo']
mock.connection.cursor().execute("SELECT 1")
# ['foo']

cursor.execute.return_value     # ['foo']
mock.connection.cursor.execute.return_value  # <Mock name='mock.connection.cursor.execute()' id='125297753822048'>

expected = call.connection.cursor().execute("SELECT 1").call_list()
mock.mock_calls
# [call.connection.cursor(), call.connection.cursor().execute('SELECT 1')]

mock.mock_calls == expected     # True

# It is the call to .call_list() that turns our call object into a list of calls representing the chained calls.

# %%  Raising exceptions with mocks
# A useful attribute is side_effect.
# If you set this to an exception class or instance then the exception will be raised when the mock is called.
mock = Mock(side_effect=Exception('Boom!'))
mock()  # Exception: Boom!

# %%  Side effect functions and iterables
# side_effect can also be set to a function or an iterable.
# The use case for side_effect as an iterable is where your mock is going to be called several times,
# and you want each call to return a different value.
# When you set side_effect to an iterable every call to the mock returns the next value from the iterable:

mock = MagicMock(side_effect=[4, 5, 6])
mock()  # 4
mock()  # 5
mock()  # 6

# For more advanced use cases,
# like dynamically varying the return values depending on what the mock is called with,
# side_effect can be a function.
# The function will be called with the same arguments as the mock.
# Whatever the function returns is what the call returns:

vals = {(1, 2): 1, (2, 3): 2}
def side_effect(*args):
    return vals[args]

mock = MagicMock(side_effect=side_effect)
mock(1, 2)  # 1
mock(2, 3)  # 2
mock(2, 4)  # !  KeyError: (2, 4)

# %%
# %%
