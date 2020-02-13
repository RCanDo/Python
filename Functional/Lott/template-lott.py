#! python3
"""
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview      

title: 
subtitle:
version: 1.0
type: examples and explanations
keywords: [kw1, kw2, ..., kwn]   # there are always some keywords!
description: |
remarks:    
    - _
todo:
    - problem 1
sources:
    - title: Functional Python Programming
      chapter: 
      pages: 
      link: "D:/bib/Python/Functional/Functional Python Programming - Steve Lott - 2015.pdf"
      date: 2015
      authors: 
          - fullname: Steven Lott
      usage: | 
file:
    usage: 
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: .py
    path: D:/ROBOCZY/Python/Functional/Lott/
    date: 2019-07-
    authors:   
        - nick: kasprark
          fullname: Arkadiusz Kasprzyk
          email: 
              - arkadiusz.kasprzyk@tieto.com
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


