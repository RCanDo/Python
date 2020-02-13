# -*- coding: utf-8 -*-
# this is solo_class_game.py
"""
title: Solo Learn Python
subtitle:
author: kasprark
date: Sun Dec 31 08:36:15 2017

xx. Object Oriented Programming
===============================

## •

A game
------
"""

%reset

pwd
cd C:/Users/akasprzy/OneDrive - HERE Global B.V-/arek/ROBOCZY/Python/help/solo
ls

dir()

import importlib ## may come in handy

#%%

def get_input():

    command = input(": ").split()

    if len(command) == 0:
        verb = say
        noun = None
    else:
        verb_word = command[0]

        if verb_word in verb_dict:
            verb = verb_dict[verb_word]     ## a function stored in verb_dict under key verb_word
        else:
            verb = wrong
            print('Unknown verb "{}".'.format(verb_word))

        if len(command) >= 2:
            noun = command[1]
        else:
            noun = None

    return verb(noun)

def wrong(noun):
    print('You have used wrong word. Repeat please.')
    return True

def say(noun):
    if noun == None:
        print("You said nothing.")
    else:
        print('You said "{}".'.format(noun))
    return True

def exit(noun):
    return False

#%%
## classes

class GameObject:
    class_name = ""
    description = ""
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.name] = self

    def get_description(self):
        return self.class_name + "\n" + self.description

class Goblin(GameObject):
    class_name = "goblin"
    description = "A foul creature."   ## now it serves no purpose
    
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._description = "a faul creature"
        super().__init__(name)
        
    @property
    def description(self):
        if self.health >= 3:
            return self._description
        elif self.health == 2:
            health_line = "it has a wound"
        elif self.health == 1:
            health_line = "it has a serious wound"
        elif self.health <= 0:
            health_line = "it's dead!"
        return self._description + "\n" + health_line
    
    @description.setter
    def description(self, value):
        self._description = value

goblin_a = Goblin("Gobbly")

#%% checking
GameObject.objects
goblin_a.name
goblin_a.class_name
type(goblin_a)


#%%

def examine(noun):
    if noun in GameObject.objects:
        print( GameObject.objects[noun].get_description() )
    else:
        print( "There is no {} here.".format(noun) )
    return True

def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        thing.health -= 1
        if thing.health <= 0:
            msg = "You killed the {}!".format(noun)
        else:
            msg = "You hit the {}.".format(noun)
    else: 
        msg = "There is no {} here.".format(noun)
    return msg

#%% checking
goblin_a.health    
examine(goblin_a)  ## nonsense
examine('Gobbly')
examine('gobbly')

#%%
verb_dict = {
    "say" : say,
    "exit": exit,
    "examine" : examine,
    "hit" : hit
    }


#%%
def game():
    while get_input():
        pass