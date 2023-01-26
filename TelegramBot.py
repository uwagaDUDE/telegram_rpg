import telebot
import os
from dotenv import dotenv_values
import db
import levelTexts

bot = telebot.TeleBot(dotenv_values(".env")["API_KEY"])

startGameButton = "Начать Путешествие"
checkInventoryButton = "Посмотреть инвентарь"
backButton = "Назад"


@bot.message_handler(commands=['start'])  # /start - Главное меню
def handle_start(message):
    user = message.from_user
    player = db.getPlayer(user.id)
    if player == None:
        db.createPlayer(user.id)
        player = db.getPlayer(user.id)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(startGameButton, checkInventoryButton)
    user_markup.row('БЛОК3', 'БЛОК4')
    bot.send_message(
        user.id, f'Добро пожаловать {user.first_name} \nВаш персонаж: \n   Уровень: { player["level"] }   \n Предметов в инвентаре: {len(player["items"])}', reply_markup=user_markup,)


def botStart():
    bot.polling(none_stop=True, interval=0)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text
    if text == startGameButton:
        level1(message)
    elif text == checkInventoryButton:
        checkInventory(message)


def level1(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Осмотреться', 'Собрать банки')
    bot.send_message(message.from_user.id,
                     levelTexts.level1Text, reply_markup=user_markup)


def checkInventory(message):
    inventory = db.getPlayer(message.from_user.id)['items']
    text = ''
    if len(inventory) > 0:
        for item in inventory:
            text += f'\n {item}'
    else:
        text = 'Инвентарь пуст'
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(backButton, 'Использовать предмет')
    bot.send_message(message.from_user.id,
                     text, reply_markup=user_markup)
