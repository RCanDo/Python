#! python3
# -*- coding: utf-8 -*-
"""
title: Wandering on a board
type: code
version: 1.0
date: 2019-12-10
authors:
    - fullname: Arkadiusz Kasprzyk
      email:
          - arek@staart.pl
          - akasp666@google.com
description: |
remarks:
    - A bow towards functional programming: function is an expression i.e.
      always return a value (even if it's always True - still better then None).
    - backup/rollback should be managed via some custom context manager (`with`)
      but this would be overkill for such a simple task.
      After all it was assumed that input is always valid.
"""

## Overall Code Review Notes:
##  The code does its job. 
##  I like the functional approach.
##  Small plus for rollback mechanism.
## 
## Things to improve and consider:
##  Clearer separation of business logic and internal logic (Namings, etc)
##  Inner dependency on some of the variables.
##  Changing self.direction to something else, e.g. self.direction_index at least
##    Consider solution to represent value of direction as (1, 0), (0, 1) etc "vectors" this way
##    The variable itself is more descriptive and also casting it back to direction "letters" would be easy e.g:
##    DIRECTION_TO_VECTOR = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
##    VECTOR_TO_DIRECTION = {v: k for k, v in DIRECTION_TO_VECTOR.items()}
##    or else...
## 
##    Consider using Type hinting for clearer intention.
##    Those are just my quick ideas and concernes.
## 
## Verdict:
##  Code in present format is not easily comprehensible.
##  Some namings do not carry proper information.
##  Catching general Exception is very bad idea.
##


class Game(object):

    TURN = {'L', 'R'}  # +1, -1                                     ## Unused variable

    MOVE = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}   ## MOVE variable does not describe the purpose clearly,
                                                                    ## I'd call "North", "East" ... as Directions
                                                                    ## MOVE suggests choices like "Forward", "Right" etc. 

    DIR = list('NESW')  # direction = 0, 1, 2, 3                    ## Why not list(MOVE.keys()) ?
                                                                    ## Notice that this ordering introduces implicit constraint
                                                                    ## on turns. I.e. if someone changes here 'NESW' to 'NWSE'
                                                                    ## Then turns will behave badly. This is huge assumption
                                                                    ## But introduced  implicitly.

    def __init__(self, size=5):
        self.size = size
        self.position = [0, 0]
        self.direction = 0                                          ## consider changing variable name to move_index because
                                                                    ## what it actually holds is the index of current direciton
                                                                    ## from DIR variable.
                                                                    ## This might be hard to comprehend while using in other parts
                                                                    ## of the system.

    @property
    def state(self):
        return self.position, Game.DIR[self.direction]

    def turn_left(self):
        self.direction -= 1                                         
        self.direction %= 4                                         ## Consider len(DIR)
        return True

    def turn_right(self):
        self.direction += 1
        self.direction %= 4                                         ## Cosider len(DIR)
        return True

    def move(self):
        move = Game.MOVE[Game.DIR[self.direction]]                  ## Naming does not clearly communicate the purpose 

        def new_coordinate(a, b):                                   ## Consider changing a, b to curr_coord, step
            return max(min((a + b), self.size - 1), 0)              ##  or something in that direction. 

        self.position = list(map(new_coordinate, self.position, move))  ## Consider list comprehension, much more readable
        return True

    def play(self, actions):
        ACT = {'M': self.move,                                      ## Why ACT is local to this function? This could be somehow
               'L': self.turn_left,                                 ## connected to other variables like MOVE, DIR etc.
               'R': self.turn_right
              }
        try:
            state_backup = self.position, self.direction   # backup
            for a in actions.upper():
                ACT[a]()
        except Exception:                                           ## Too general Exception handling. 
            self.position, self.direction = state_backup   # rollback
            raise ValueError("Expected string of 'M', 'L' or 'R' e.g. 'MMRMLML'.")
        return self.state

    def reset(self):                                                ## It might be painfull to remember to change reset()
        self.direction = 0                                          ## each time new variable in __init__() was added.
        self.position = [0, 0]                                      ## consider just calling self.__init__(params) to remove
        return True                                                 ## redundancy with constructor itself
        
