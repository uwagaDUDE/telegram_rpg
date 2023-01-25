import json
import random


class Enemy:

    def __init__(self):
        x = open('player.json', 'rt', encoding='UTF-8')
        self.load = json.load(x)
        random_enemy = random.randint(1,3)
        self.enemy_data = self.load[random_enemy]


    def hp(self):
        return self.enemy_data['default_player_health']

    def damage(self):
        return self.enemy_data['default_player_damage']

    def name(self):
        return self.enemy_data['player_name']