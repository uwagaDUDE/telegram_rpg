import json

class Player:

    def __init__(self):
        x = open('player.json', 'rt', encoding='UTF-8')
        self.load = json.load(x)
        self.player_data = self.load['player']


    def hp(self):
        return self.player_data['default_player_health']

    def damage(self):
        return self.player_data['default_player_damage']

