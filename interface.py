import npc

class StartGame:

    def start_game(self,
                   start_items=[],
                   random_gold=0):
        print(f'Вы очнулись на полянке в лесу...\n'
              f'Похлопав по карманам вы обнаруживаете что у вас {random_gold} золота\n'
              f'Рядом с собой вы так же обнаруживаете мешок, в нем лежит : {start_items}\n'
              f'Но как же вас зовут?')
        name = input('Введите свое имя: ')
        return name

class Interface:

    def what_to_do(self):
        return print(f'Что будем делать?\n'
                     f'1. Пойти прямо\n'
                     f'2. Пойти налево\n'
                     f'3. Пойти направо\n'
                     f'4. Заглянуть в свою сумку\n'
                     f'5. Мои характеристики\n'
                     f'7. Быстрое перемещение')


class Fight:

    def __init__(self):
        print()

    def enemy_attack_player(self, enemy_name):
        return print(f'На вас напал {enemy_name}')

    def enemy_hp(self, enemy_hp):
        return print(f'Здоровье противника составляет: {enemy_hp}')

    def player_attack_turn(self, player_damage, enemy_name):
        return print(f'Вы нанесли {player_damage} по {enemy_name}')

    def player_turn(self):
        print(f'1. Attack\n'
              f'2. Run')

class Move:

    def forward(self):
        return print(f'Вы решаете пойти прямо...\n')

    def left_move(self):
        return print(f'Вы решаете пойти налево...\n')

    def right_move(self):
        return print(f'Вы решаете пойти направо...\n')

class Event:

    def wallet_with_gold(self, random_gold=0):
        return print(f'\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
                     f'Вы нашли мешочек с золотом, в нем было {random_gold} монет\n'
                     f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

    def player_see_enemy(self, monster_name):
        return print(f'Вы замечаете {monster_name} вдалеке, что вы решаете сделать? \n'
                     f'1. Атаковать\n'
                     f'2. Пройти мимо\n')

    def player_attacked_by_enemy(self, monster_name):
        return print(f'На вас напал {monster_name}!'
                     f'\nЗащищайтесь!\n')

    def nothink_event(self):
        return print(f'Vi prodoljaete idti...')

class BotInterface:
    def __init__(self, user, player):
         self.information = f'\nВаш персонаж:\n' \
                            f'Имя:{user.first_name}\n'\
                            f'Уровень: { player["level"] }\n'\
                            f'Предметов в инвентаре: {len(player["items"])}'
