import npc
import telebot
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

    def bot(self, bot):
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
        return f'Вы решаете пойти прямо...\n'

    def left_move(self):
        return f'Вы решаете пойти налево...\n'

    def right_move(self):
        return f'Вы решаете пойти направо...\n'

class Event:

    def wallet_with_gold(self, random_gold=0):
        return f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'\
               f'Вы нашли мешочек с золотом, в нем было {random_gold} монет\n'\
               f'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'

    def player_see_enemy(self, monster_name):
        return f'Вы замечаете {monster_name} вдалеке, что вы решаете сделать? \n'\
               f'1. Атаковать\n'\
               f'2. Пройти мимо\n'

    def player_attacked_by_enemy(self):
        return f'На вас напал !'\
               f'\nЗащищайтесь!\n'

    def nothink_event(self):
        return f'Ничего интересного'

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

    def go_forward(self):
        return "\U00002B06"
    def go_left(self):
        return "\U00002B05"
    def go_right(self):
        return "\U000027A1"
    def empty_backpack(self):
        return "Inventory is empty"

    def start_game(self):
        return "Начать путешествие \U0001F9ED"

    def check_inventory(self):
        return "\U0001F392"

    def back(self):
        return "Назад \U0001F519"

    def look_around(self):
        return "Осмотреться \U0001F441"

    def use_item(self):
        return "Использовать предмет"

    def empty(self):
        return "КНОПКА"

    def player_information(self): #Ваш персонаж О_О
        return "\U0001F93AВаш персонаж\U0001F93A"

    def player_name(self, user): #Ник
        return f'Имя: {user.first_name}'

    def player_level(self, player): #Уровень
        return f'\U0001F2B0 Уровень: {player["level"]}'

    def player_health(self, player): #ХП
        return f'\U0001FA78\n{player["hp"]}'

    def player_mana(self, player): #Мана
        return f'\U0001F4A7\n{player["mana"]}'

    def player_stats(self, player): #Характеристики
        return f'\U00002139'

    def fast_trevel(self): #Быстрое перемещение
        return "\U0001F9ED"