import interface
import telebot
import os
from dotenv import dotenv_values
import db
import random
import levelTexts

bot = telebot.TeleBot(dotenv_values(".env")["API_KEY"])
button = interface.Buttons()
# startGameButton = "Начать Путешествие" UJE NE NUJO, ONI V interface
# checkInventoryButton = "Посмотреть инвентарь" # Для чистоты кода вывести переменные в отдельный файл
# backButton = "Назад"
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
    player = db.get_player(user.id)
    if player == None:
        db.create_new_player(user.id, user.username)
        player = db.get_player(user.id)


    player_information = interface.BotPlayerInfo(user, player)
    #Кнопки и сообщение бота
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(button.start_game(), button.check_inventory())
    user_markup.row('БЛОК3', 'БЛОК4')
    prevMarkup = user_markup
    prevMessage = bot.send_message(user.id, player_information.information, reply_markup=user_markup)


def bot_init():
    bot.polling(none_stop=True, interval=0)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text
    if text == button.start_game():
        first_level(message)
    elif text == button.check_inventory():
        player_inventory_check(message)
    elif text == button.back():
        back_button(message)

@bot.message_handler(func=lambda m: True)
def first_level(message):
    global player
    global prevMessage

    gold = random.randint(1, 10)
    player['gold'] = player["gold"]+gold # Добавляем голду персонажу # a ono work? i havnt gold anyway
    player["items"].append({"testItem":{"cost":0,"description":"тестовая админ шмотка"}})
    
    db.update_player_data(id, {"location": "forest", "items":player["items"], 'gold':player['gold']})

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Осмотреться', 'Собрать банки', button.check_inventory())
    prevMarkup=user_markup # Сделать отдельную функцию или декторатор, которые будут автоматом записывать текст и кнопки
    prevMessage= bot.send_message(message.from_user.id,
                                  levelTexts.start_location(player),
                                  reply_markup=user_markup)


def player_inventory_check(message):
    inventory = player["items"]
    text = ''
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    if len(inventory) > 0:
        user_markup.row('Использовать предмет')
        for item in inventory:
            text += f'\n {item}' # todo сделать нормальное отображение: НазваниеПредмета: Количество
    else:
        text = button.empty_backpack()
    user_markup.row(button.back())
    bot.send_message(message.from_user.id,text, reply_markup=user_markup)

def back_button(message):
    bot.send_message(message.from_user.id,prevMessage.text, reply_markup=prevMarkup)
