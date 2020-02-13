#! python3
# -*- coding: utf-8 -*-
"""
title: Wandering on a board
type: tests - unittest
version: 1.0
date: 2019-12-10
authors:
    - fullname: Arkadiusz Kasprzyk
      email:
          - arek@staart.pl
          - akasp666@google.com
"""
from game import Game
import unittest


class TestGame(unittest.TestCase):

    def test_initial(self):
        game = Game()
        self.assertEqual(game.state, ([0, 0], 'N'),"improper initial state")

    def test_number(self):
        game = Game()
        with self.assertRaises(ValueError):
            game.play(1)                                            ## Consider throwing TypeError as the type of 
                                                                    ##  input variable does not match, not really value

    def test_none(self):
        game = Game()
        with self.assertRaises(ValueError):
            game.play(None)                                         ## Consider throwing TypeError as the type of 
                                                                    ##  input variable does not match, not really value


    def test_invalid_string(self):
        game = Game()
        with self.assertRaises(ValueError):                         ## Here ValueError is ok :)
            game.play('1')

    def test_empty_string(self):
        game = Game()
        self.assertEqual(game.play(''), ([0, 0], 'N'), "")

    def test_table(self):                                           ## Consider writing parametrized test case instead of iterating
        game = Game()
        test_table = [('R', ([0, 0], 'E')),
                      ('L', ([0, 0], 'W')),
                      ('RR', ([0, 0], 'S')),
                      ('RL', ([0, 0], 'N')),
                      ('LR', ([0, 0], 'N')),
                      ('LLLL', ([0, 0], 'N')),
                      ('MR' * 4, ([0, 0], 'N')),
                      ('MRML' * 4, ([4, 4], 'N')),
                      ('MRMLMRM', ([2, 2], 'E')),
                      ('RMMMLMM', ([3, 2], 'N')),
                      ('MMMMM', ([0, 4], 'N'))]
        for case in test_table:                                     ## Use for moves, expected_state in test_table
            game.reset()
            assert game.play(case[0]) == case[1], case              ## [0] and [1] is not very pythonic in this case


if __name__ == "__main__":
    unittest.main()
