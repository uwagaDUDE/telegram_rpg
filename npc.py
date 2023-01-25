import json
import random


class Enemy:

    class Orcs:
        class Peon:
            def __init__(self):
                self.name = 'Орк-рабочий'
                self.hp = 100
                self.damage = random.randint(5,15)
                self.gold = random.randint(1,2)

    class Animals:

        class ForestWolf:

            def __init__(self):
                self.name = 'Лесной волк'
                self.hp = 50
                self.damage = random.randint(2,8)
                self.item = [1001, 1002]