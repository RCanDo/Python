#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
---
title: pytest fixtures
subtitle:
version: 1.0
type: tutorial
keywords: [tests, pytest.fixture, ...]
description: |
remarks:
todo:
    -
sources:
    - title: pytest fixtures: explicit, modular, scalable
      link: https://docs.pytest.org/en/6.2.x/fixture.html
file:
    date: 2024-03-15
    authors:
        - fullname: Arkadiusz Kasprzyk
          email:
              - rcando@int.pl
"""
# %%
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):             # name of argument the same as of .fixture above
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):  # names of arguments the same as of .fixtures above
    assert my_fruit in fruit_basket


# %%
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


# %%

