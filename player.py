import json
import random


class Player:

    def __init__(self, name='', location = None):
        self.name = name
        self.hp = 100
        self.mana = 100
        self.strenght = 1
        self.agility = 1
        self.intelegency = 1
        self.damage = random.randint(1,5)
        self.location = location

