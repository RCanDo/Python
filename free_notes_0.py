# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:10:21 2019

@author: kasprark
"""

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

import numpy as np

lst = np.array([0] + [2] + [3], ndmin=2)
lst
lst[0, 0]
lst[0, 1]

#%%

lst = [k**2 for k in range(-3, 3)]
lst
lst[-1]
lst[:2]

#%%
#%%

import json
import numpy as np

file = "C:/Projects/AIML/car-agent/agents_setup/agent_car.json"
car = json.load(open(file))
type(car)

car
len(car)
car.keys()
dir(car)

print(json.dumps(car, indent=3))

car1 = car['agent 1']
car1.keys()             # dict_keys(['close_connection', 'sensors', 'agent_config'])
car1['agent_config']


car1['sensors']

np.array(car1['sensors'])

#%%
def get_env_state(data):
    return np.array(
        [data["sensors"]["engine_power"]] +
        [data["sensors"]["car_point_angle"]] +
        [data["sensors"]["collision"]] +
        [data["sensors"]["steering_angle"]] +
        [data["sensors"]["angular_velocity"]] +
        [data["sensors"]["distance"][0]["value"] / 20] +
        [data["sensors"]["distance"][1]["value"] / 20] +
        [data["sensors"]["distance"][2]["value"] / 20] +
        [data["sensors"]["distance"][3]["value"] / 20] +
        [data["sensors"]["distance"][4]["value"] / 20] +
        [data["sensors"]["distance"][5]["value"] / 20] +
        [data["sensors"]["distance"][6]["value"] / 20] +
        [data["sensors"]["distance"][7]["value"] / 20],
        ndmin=2), data["sensors"]["collision"], data["close_connection"]

#%%

env1 = get_env_state(car1)
env1
print(json.dumps(car1, indent=3))
