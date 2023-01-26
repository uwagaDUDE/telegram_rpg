import telebot
import os
from dotenv import dotenv_values
import db

bot = telebot.TeleBot(dotenv_values(".env")["API_KEY"])
@bot.message_handler(commands=['start'])  # /start - Главное меню
def handle_start(message):
    user = message.from_user
    player = db.getPlayer(user.id)
    if player == None:
        db.createPlayer(user.id)
        player = db.getPlayer(user.id)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Начать путешестиве', 'Посмотреть инвентарь')
    user_markup.row('БЛОК3', 'БЛОК4')
    bot.send_message(user.id, f'Добро пожаловать {user.first_name} \nВаш персонаж: \n   Уровень: { player["level"] }   \n Предметов в инвентаре: {len(player["items"])}', reply_markup=user_markup,)
        
def botStart():
    bot.polling(none_stop=True, interval=0)