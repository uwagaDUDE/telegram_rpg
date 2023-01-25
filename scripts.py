import random
import npc
import interface
import player, items
event = interface.Event()

class Fight:
    print()
    def __init__(self):

        self.enemy_hp = npc.Enemy().Orcs().Peon().hp
        self.enemy_name = npc.Enemy().Orcs().Peon().name

    def start_fight(self):
        interface.Fight().enemy_attack_player(self.enemy_name)

class Movement:

    def forward_move(self):
        return interface.Move().forward()

    def right_move(self):
        return interface.Move().right_move()

    def left_move(self):
        return interface.Move().left_move()

class Event:

    def random_event(self):
        return random.randint(1,100)

    def player_event_while_move(self, monster_name):
        #Napadeniye igroka na monstra
        if self.random_event() >= 1 and self.random_event() < 10:
            event.player_see_enemy(monster_name)
            is_player_attack = input(f'1. Attack\n'
                                     f'2. Go away')
            if is_player_attack == "1":
                fight = True
                enemy_health = Fight().enemy_hp
                while fight == True:
                    Fight().start_fight()
                    interface.Fight().player_turn()
                    player_attack = input('What to do: ')
                    if player_attack == "1":
                        damage = player.Player().damage+items.Items().Weapons().WoodenSword().damage
                        interface.Fight().player_attack_turn(damage, Fight().enemy_name)
                        enemy_health = enemy_health-damage
                        print(enemy_health)
                        if enemy_health <= 0:
                            fight = False
            else:
                print('You turn around and go away...')
        elif self.random_event() >= 10 and self.random_event() < 15:
            event.wallet_with_gold(self.random_gold())
        elif self.random_event() >= 15 and self.random_event() < 30:
            event.player_attacked_by_enemy(monster_name)
        else:
            event.nothink_event()


    def random_gold(self):
        return random.randint(1,10)

class Backpack:

    def backpack(self):
        return []