import interface
import telebot
import os
from dotenv import dotenv_values
import db
import random
import levelTexts

bot = telebot.TeleBot(dotenv_values(".env")["API_KEY"])

startGameButton = "Начать Путешествие"
checkInventoryButton = "Посмотреть инвентарь" # Для чистоты кода вывести переменные в отдельный файл
backButton = "Назад"
prevMessage = None
prevMarkup = None
player = None

@bot.message_handler(commands=['start'])  # /start - Главное меню
def handle_start(message):

    user = message.from_user #Упрощаем получение пользователя ТГ

    global player
    global prevMessage
    global prevMarkup

    #Работа с базой данных
    player = db.getPlayer(user.id)
    if player == None:
        db.createPlayer(user.id,user.username)
        player = db.getPlayer(user.id)
    
    bot_interface = interface.BotInterface(user, player)

    #Кнопки и сообщение бота
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(startGameButton, checkInventoryButton)
    user_markup.row('БЛОК3', 'БЛОК4')
    prevMarkup = user_markup
    prevMessage = bot.send_message(user.id, bot_interface.information, reply_markup=user_markup)


def bot_init():
    bot.polling(none_stop=True, interval=0)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text
    if text == startGameButton:
        first_level(message)
    elif text == checkInventoryButton:
        player_inventory_check(message)
    elif text == backButton:
        back_button(message)

@bot.message_handler(func=lambda m: True)
def first_level(message):
    global player
    global prevMessage

    gold = random.randint(1, 10)
    player["gold"]+gold # Добавляем голду персонажу
    player["items"].append({"testItem":{"cost":0,"description":"тестовая админ шмотка"}})
    
    db.updatePlayer(id, {"location":"forest","items":player["items"]})

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Осмотреться', 'Собрать банки', checkInventoryButton)
    prevMarkup=user_markup # Сделать отдельную функцию или декторатор, которые будут автоматом записывать текст и кнопки
    prevMessage= bot.send_message(message.from_user.id,levelTexts.start_location(player), reply_markup=user_markup)


def player_inventory_check(message):
    inventory = player["items"]
    text = ''
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    if len(inventory) > 0:
        user_markup.row('Использовать предмет')
        for item in inventory:
            text += f'\n {item}' # todo сделать нормальное отображение: НазваниеПредмета: Количество
    else:
        text = 'Инвентарь пуст'
    user_markup.row(backButton)
    bot.send_message(message.from_user.id,text, reply_markup=user_markup)
                
def back_button(message):
    bot.send_message(message.from_user.id,prevMessage.text, reply_markup=prevMarkup)
