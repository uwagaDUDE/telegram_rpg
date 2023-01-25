import interface
import items, player
import postSql
import scripts
weapon = items.Items().Weapons()
name = interface.StartGame().start_game(weapon.WoodenSword().name, 2)
player = player.Player(name)
move = scripts.Movement()
interface = interface.Interface()

# bot = telebot.TeleBot(os.environ.get("API_KEY"))
db= postSql.DataBase(dbname='postgres', user='postgres')
db.connect()

def main():

    movement = True
    while movement == True:

        interface.what_to_do()
        user_choice = input('\nЧто будем делать: ')

        if user_choice == "1":
            move.forward_move()
        elif user_choice == "2":
            move.left_move()
        elif user_choice == "3":
            move.right_move()
        else:
            print('NOT REALISED')


#main()


# def getPlayer(playerId):
#     return db.players.find_one({'id': playerId})
#
# @bot.message_handler(commands=['start'])  # /start - Главное меню
# def handle_start(message):
#     user = message.from_user
#     player = getPlayer(user.id)
#     if player == None:
#         db.players.insert_one({  # / изначальне характеристики, если игрок не найден
#             'id': user.id,
#             'level': 1,
#             'stats': {
#                 'strength': 1,
#                 'agility': 1,
#                 'intellect': 1,
#             },
#             'items':[],
#         })
#         player = getPlayer(user.id)
#
#     user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
#     user_markup.row('БЛОК1', 'БЛОК2')
#     user_markup.row('БЛОК3', 'БЛОК4')
#     bot.send_message(user.id, f'Добро пожаловать {user.first_name} \nВаш персонаж: \n   Уровень: {player}', reply_markup=user_markup)
#
#
# bot.polling(none_stop=True, interval=0)