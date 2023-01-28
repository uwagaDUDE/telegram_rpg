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
class Bot:

    def bot(self):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('Начать путешестиве', 'Посмотреть инвентарь')
        user_markup.row('Об игре', 'БЛОК4')
        bot.send_message(
            user.id, f'Добро пожаловать {user.first_name} \n'
                     f'Ваш персонаж: \n   '
                     f'Уровень: {player["level"]}   '
                     f'\n Предметов в инвентаре: {len(player["items"])}',
            reply_markup=user_markup)
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

class BotPlayerInfo:
    def __init__(self, user, player):
         self.information = f'\nВаш персонаж:\n' \
                            f'\U0001F93A Имя: {user.first_name}\n'\
                            f'\U0001F2B0 Уровень: {player["level"]}\n' \
                            f'\U0001F276 Здоровье: {player["hp"]}\n' \
                            f'\U0001F4A7 Мана: {player["mana"]}\n'\
                            f'\U0001F392 Предметов в инвентаре: {len(player["items"])}'

    #Need translate, bcz net russkogo)
class Buttons:

    def empty_backpack(self):
        return "Inventory is empty"

    def start_game(self):
        return "Начать путешествие \U0001F9ED"

    def check_inventory(self):
        return "Посмотреть инвентарь \U0001F392"

    def back(self):
        return "Назад \U0001F519"

    def look_around(self):
        return "Осмотреться \U0001F441"

    def use_item(self):
        return "Использовать предмет"

    def empty(self):
        return "КНОПКА"

    def player_information(self):
        return "Ваш персонаж"

    def player_name(self, user):
        return f'\U0001F93A Имя: {user.first_name}'

    def player_level(self, player):
        return f'\U0001F2B0 Уровень: {player["level"]}'

    def player_health(self, player):
        return f'\U0001F276 Здоровье: {player["hp"]}'