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

class Game(object):

    TURN = {'L', 'R'}  # +1, -1

    MOVE = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    DIR = list('NESW')  # direction = 0, 1, 2, 3

    def __init__(self, size=5):
        self.size = size
        self.position = [0, 0]
        self.direction = 0

    @property
    def state(self):
        return self.position, Game.DIR[self.direction]

    def turn_left(self):
        self.direction -= 1
        self.direction %= 4
        return True

    def turn_right(self):
        self.direction += 1
        self.direction %= 4
        return True

    def move(self):
        move = Game.MOVE[Game.DIR[self.direction]]

        def new_coordinate(a, b):
            return max(min((a + b), self.size - 1), 0)

        self.position = list(map(new_coordinate, self.position, move))
        return True

    def play(self, actions):
        ACT = {'M': self.move,
               'L': self.turn_left,
               'R': self.turn_right
              }
        try:
            state_backup = self.position, self.direction   # backup
            for a in actions.upper():
                ACT[a]()
        except Exception:
            self.position, self.direction = state_backup   # rollback
            raise ValueError("Expected string of 'M', 'L' or 'R' e.g. 'MMRMLML'.")
        return self.state

    def reset(self):
        self.direction = 0
        self.position = [0, 0]
        return True
