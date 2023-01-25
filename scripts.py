import random

import interface


class Fight:

    def new_fight(self):

        enemy_hp = enemy.Enemy().hp()
        enemy_name = enemy.Enemy().name()

    def start_fight(self):
        interface_fight.enemy_attack_player(self.new_fight().enemy_name)

class Movement:

    def forward_move(self):
        return interface.Move().forward()

    def right_move(self):
        return interface.Move().right_move()

    def left_move(self):
        return interface.Move().left_move()

class Event:

    def random_gold(self):
        return random.randint(1,10)

class Backpack:

    def backpack(self):
        return []