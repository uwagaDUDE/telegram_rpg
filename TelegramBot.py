import telebot
import os
from dotenv import dotenv_values
import db
import random
import levelTexts

bot = telebot.TeleBot(dotenv_values(".env")["API_KEY"])

startGameButton = "Начать Путешествие"
checkInventoryButton = "Посмотреть инвентарь"
backButton = "Назад"
prevMessage = None
prevMarkup = None
player = None

@bot.message_handler(commands=['start'])  # /start - Главное меню
def handle_start(message):
    user = message.from_user
    global player
    global prevMessage
    global prevMarkup
    player = db.getPlayer(user.id)
    if player == None:
        db.createPlayer(user.id,user.username)
        player = db.getPlayer(user.id)
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(startGameButton, checkInventoryButton)
    user_markup.row('БЛОК3', 'БЛОК4')
    test=message.text
    prevMarkup = user_markup
    prevMessage =bot.send_message(
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
    elif text == backButton:
        back(message)


def level1(message):
    global player
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Осмотреться', 'Собрать банки')
    gold = random.randint(1, 10)
    player["items"].append({"gold":gold}) # Добавляем голду персонажу
    item = 'А как выбрать рандомный элемент из множества классов?'
    player = db.updatePlayer(id, {"location":"forest","items":player["items"]}) # Обновляем перса в дб
    currentLevel = bot.send_message(message.from_user.id,levelTexts.level1Text(gold,item), reply_markup=user_markup)


def checkInventory(message):
    inventory = player["items"]
    text = ''
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    if len(inventory) > 0:
        user_markup.row('Использовать предмет')
        for item in inventory:
            text += f'\n {item}'
    else:
        text = 'Инвентарь пуст'
    user_markup.row(backButton)
    bot.send_message(message.from_user.id,text, reply_markup=user_markup)
                
def back(message):
    bot.send_message(message.from_user.id,prevMessage.text, reply_markup=prevMarkup)
