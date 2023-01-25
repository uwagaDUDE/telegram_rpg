import interface
import items
import player
import db
import scripts
import telebot
import os
weapon = items.Items().Weapons()
# name = interface.StartGame().start_game(weapon.WoodenSword().name, 2)
# player = player.Player(name)
move = scripts.Movement()
interface = interface.Interface()
bot = telebot.TeleBot("5855247722:AAGB3OF41dXmqqZQndYsuux5-2iIsxvP348")

@bot.message_handler(commands=['start'])  # /start - Главное меню
def handle_start(message):
    user = message.from_user
    player = db.getPlayer(user.id)
    if player == None:
        db.createPlayer(user.id)
        player = db.getPlayer(user.id)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('БЛОК1', 'БЛОК2')
    user_markup.row('БЛОК3', 'БЛОК4')
    print(player)
    bot.send_message(user.id, f'Добро пожаловать {user.first_name} \nВаш персонаж: \n   Уровень: {player}', reply_markup=user_markup)

bot.polling(none_stop=True, interval=0)
