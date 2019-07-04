#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        self.sides = randint(1, 6)

die = Die()
die.roll_die()

print(die.sides)