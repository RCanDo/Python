#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title:
subtitle:
version: 1.0
type:          # possible values: ...
keywords: [kw1, kw2, ..., kwn]   # there are always some keywords!
description: |
    Description of what is in the file.
    Detailed but do not make lectures here!
remarks:    # additional notes worth emphasising
    - eg. work interactively (in Spyder)
    - install PackageX first
    - etc.
todo:
    - problem 1
    - problem 2   # and so on...
sources:   # there may be more sources
    - title: Introduction to Geospatial Data in Python
      link: https://www.datacamp.com/community/tutorials/geospatial-data-python
      date: 2018-10-24
      authors:
          - fullname: Duon Vu
      usage: |
          In this tutorial, you will use geospatial data to plot the path of Hurricane Florence
          from August 30th to September 18th.
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name:
    path: D:/ROBOCZY/Python/...
    date: 2020-07-05
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
              - akasp666@google.com
              - arek@staart.pl
"""

#%% This is block delimiter very useful for interactive work like e.g. in Spyder (part of Anaconda)

import gym
import numpy as np

#%% Block delimiters allows to run separated blocks of code by one key-stroke
# e.g. Shift+Enter in Spyder

""" choose one of the environment,
i.e. run only one of the lines
(place the cursor on the line and click black arrow in Spyder or F9)
"""
env_nam = 'CartPole-v0'
env_nam = 'MountainCar-v0'
env_nam = 'MountainCarContinuous-v0'
env_nam = 'CarRacing-v0'      # needs Box2D
env_nam = 'MsPacman-v0'       # needs Atari
env_nam = 'Hopper-v2'         # needs MuJoCo

#%% However, some style checkers like Flake may complain on #%% - there should be space after #

""" run the whole block
in Spyder: Shift+Enter or the icon: green arrow with red arrow
"""

env = gym.make(env_nam)
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())  # take a random action


#%%

"""
Interactive work style is very useful when debugging or learning.

Of course the block delimiters are allowed in Python (it's just the comment)
thus the whole file may be smoothly run.
"""


