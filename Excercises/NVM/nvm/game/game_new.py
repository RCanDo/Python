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

    DIRECTION_TO_VECTOR = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    VECTOR_TO_DIRECTION = {v: k for k, v from Game.DIRECTION_TO_VECTOR.items()}

    DIRECTIONS = list(Game.DIRECTION_TO_VECTOR.keys())   # direction_idx = 0, 1, 2, 3

    def __init__(self, board_size=5):
        self.board_size = board_size
        self.position = [0, 0]
        self.direction_idx = 0

    def __backup(self):
        self.state_backup = self.position, self.direction_idx
        return True

    def __rollback(self):
        self.position, self.direction_idx = self.state_backup
        return True

    @property
    def state(self):
        return self.position, Game.DIRECTIONS[self.direction_idx]

    def reset(self):
        self.__init__(self.board_size)
        return True

    def turn_left(self):
        self.direction_idx -= 1
        self.direction_idx %= len(Game.DIRECTIONS)
        return True

    def turn_right(self):
        self.direction_idx += 1
        self.direction_idx %= len(Game.DIRECTIONS)
        return True

    def move(self):
        move = Game.DIRECTION_TO_VECTOR[Game.DIRECTIONS[self.direction_idx]]

        def new_coordinate(current_coordinate, step):
            return max(min((current_coordinate + step), self.board_size - 1), 0)

        self.position = list(map(new_coordinate, self.position, move))

        return True

    def play(self, actions):
        ACT = {'M': self.move,
               'L': self.turn_left,
               'R': self.turn_right
              }
        try:
            self.__backup()
            for a in actions.upper():
                ACT[a]()
        except Exception:
            self.__rollback()
            raise ValueError("Expected string of 'M', 'L' or 'R' e.g. 'MMRMLML'.")
        return self.state

