# %%  !!!  pydantic object  dos NOT  validate input  when used as type hint  !!!
# %%
from pydantic import BaseModel

class Data(BaseModel):
    id: int
    name: str
    value: float

def fun(data: Data):    # type hint
    data = dict(data)
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
fun(dt)
# id : 1
# name : qq
# value : 2.718281828

# %%
# BUT
dt0 = Data(**data0)
# ValidationError: 1 validation error for Data
# name
#   str type expected (type=type_error.str)

# %% HENCE to do validation via Pydantic object, like Data,
# sth more must be done;
# e.g.

def fun0(data: Data):
    if not isinstance(data, Data):
        data = Data(**data)
    data = dict(data)
    for k in data:
        print(f"{k} : {data[k]}")

fun0(data)      # OK
fun0(data0)     # not "valid" types
# ValidationError: 1 validation error for Data
# name
#   str type expected (type=type_error.str)

# validation via Pydantic works ! but not at type-hint !

fun0(dt)        # OK

# %%
