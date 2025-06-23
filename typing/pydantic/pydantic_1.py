#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Pydantic Overview
version: 1.0
keywords: [types, dtypes, ...]
description: |
sources:
    - title: Overview
      link: https://docs.pydantic.dev/1.10/
file:
    date: 2023-11-25
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - arkadiusz.kasprzyk@quantup.pl
"""
# %%
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)
user
user.dict()
dict(user)
# {
#     'id': 123,
#     'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
#     'friends': [1, 2, 3],
#     'name': 'John Doe',
# }

for k, v in user:
    print(f"{k}: {v}; {type(v)}")
# id: 123; <class 'int'>
# signup_ts: 2019-06-01 12:22:00; <class 'datetime.datetime'>
# friends: [1, 2, 3]; <class 'list'>
# name: John Doe; <class 'str'>

user.id         # 123
user.friends    # [1, 2, 3]

# %%
import pandas as pd
pd.DataFrame(user)
#            0                    1
# 0         id                  123
# 1  signup_ts  2019-06-01 12:22:00
# 2    friends            [1, 2, 3]
# 3       name             John Doe

df = pd.DataFrame(user.dict())
df
#     id           signup_ts  friends      name
# 0  123 2019-06-01 12:22:00        1  John Doe
# 1  123 2019-06-01 12:22:00        2  John Doe
# 2  123 2019-06-01 12:22:00        3  John Doe
df.dtypes
# id                    int64
# signup_ts    datetime64[ns]
# friends               int64
# name                 object

# %%
external_data_2 = {
    'id': 1.23,
    'signup_ts': None,
    'friends': 1,
}
user2 = User(**external_data_2)
# ! ValidationError: 1 validation error for User
# friends
#   value is not a valid list (type=type_error.list)

# %%
external_data_3 = {
    'id': 1.23,
    'signup_ts': None,
    'friends': [1],
}
user3 = User(**external_data_3)
for k, v in user3:
    print(f"{k}: {v}; {type(v)}")
# id: 1; <class 'int'>
# signup_ts: None; <class 'NoneType'>
# friends: [1]; <class 'list'>
# name: John Doe; <class 'str'>

df = pd.DataFrame(dict(user3))
df
df.dtypes
# id            int64
# signup_ts    object
# friends       int64
# name         object


# %%  !!!  pydantic object  dos NOT  validate input  when used as type hint  !!!
# %%
from pydantic import BaseModel

class Data(BaseModel):
    id: int
    name: str
    value: float

def fun(data: Data):    # type hint ->
    for k in data:
        print(f"{k} : {data[k]}")

# %%
data = {"id": 1, "name": 'qq', "value": 2.718281828}  # types conform to Data

fun(data)
# id : 1
# name : qq
# value : 2.718281828

data0 = {"id": 1.1, "name": [1], "value": 2}    # not "valid" types

fun(data0)   # function works -- type hint is NOT automatically validated
# id : 1.1
# name : [1]
# value : 2

dt = Data(**data)
fun(dt)     # ! TypeError: 'Data' object is not subscriptable

# %%
def fun2(data: Data):
    data = dict(data)
    for k in data:
        print(f"{k} : {data[k]}")

fun2(data)      # ok
fun2(data0)     # ok  but should not !
fun2(dt)        # ok

# %% to do validation must be applied correctly
# e.g.

def fun0(data: Data):
    if not isinstance(data, Data):
        data = Data(**data)
    data = dict(data)
    for k in data:
        print(f"{k} : {data[k]}")

fun0(data)      # OK
fun0(data0)
# ValidationError: 1 validation error for Data
# name
#   str type expected (type=type_error.str)

fun0(dt)        # OK


# %%  ~ pandas
# %%
import numpy as np
import pandas as pd


class Data(BaseModel):
    id: int
    name: str
    value: float


data = {"id": pd.NA, "name": np.nan, "value": None}
dt = Data(**data)
# ValidationError: 2 validation errors for Data
# id
#   value is not a valid integer (type=type_error.integer)
# value
#   none is not an allowed value (type=type_error.none.not_allowed)

# %%
from typing import Optional

class Data(BaseModel):
    id: Optional[int]
    name: Optional[str]
    value: Optional[float]


data = {"id": pd.NA, "name": np.nan, "value": None}
dt = Data(**data)
# ValidationError: 1 validation error for Data
# id
#   value is not a valid integer (type=type_error.integer)

# %%
data = {"id": np.nan, "name": np.nan, "value": None}
dt = Data(**data)
# ValidationError: 1 validation error for Data
# id
#   value is not a valid integer (type=type_error.integer)

# %%
data = {"id": 1, "name": np.nan, "value": None}
dt = Data(**data)
dt  # Data(id=1, name='nan', value=None)

# %%
data = {"id": 1, "name": None, "value": np.nan}
dt = Data(**data)
dt  # Data(id=1, name=None, value=nan)

df = pd.DataFrame(dict(dt), index=[0])
df
#    id  name  value
# 0   1  None    NaN
df.dtypes
# id         int64
# name      object
# value    float64

# %%
data = {"id": 1, "name": pd.NA, "value": pd.NA}
dt = Data(**data)
dt  # Data(id=1, name=None, value=nan)
# ValidationError: 2 validation errors for Data
# name
#   str type expected (type=type_error.str)
# value
#   value is not a valid float (type=type_error.float)

# %%


# %%


