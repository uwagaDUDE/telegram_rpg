import interface
import scripts
import telebot
import os
from dotenv import dotenv_values
import db
import random
import levelTexts
from items import Items

move = interface.Move()
events = scripts.Event()
bot = telebot.TeleBot(dotenv_values(".env")["API_KEY"])
button = interface.Buttons()
# startGameButton = "Начать Путешествие" UJE NE NUJO, ONI V interface
# checkInventoryButton = "Посмотреть инвентарь" # Для чистоты кода вывести переменные в отдельный файл
# backButton = "Назад"
prevMessage = None
prevMarkup = None
player = None
enemy = None
isPlayerMove = True
event = events.player_event_while_move()
weapons = Items().Weapons()

@bot.message_handler(commands=['start'])  # /start - Главное меню
def handle_start(message):
    
    user = message.from_user #Упрощаем получение пользователя ТГ

    global prevMessage
    global prevMarkup

    getPlayer(message)

    started_weapon = [weapons.WoodenStaff(),weapons.WoodenSword()] #ХЕЛП つ ◕_◕ ༽つ 


    player["items"].append(random.choice(started_weapon))
    db.update_player_data(user.id,player)
    player_information = interface.BotPlayerInfo(user, player)
    #Кнопки и сообщение бота
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    #user_markup.row(button.start_game(), button.check_inventory())
    user_markup.row(button.player_information())

    user_markup.row(button.player_name(user),button.player_health(player),
                    button.player_mana(player))

    user_markup.row(button.go_left(), button.go_forward(),
                    button.go_right())

    user_markup.row(button.check_inventory(), button.fast_trevel(),
                    button.player_stats(player))

    prevMarkup = user_markup
    prevMessage = bot.send_message(user.id, levelTexts.start_location(player), reply_markup=user_markup)


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
    elif text == button.go_forward():
        forward_button(message)
    elif text == 'fight':
        fight(message)
    elif text == 'cheat.admin_001':
        bot.send_message(message.from_user.id,'Не вижу деняк на киви, за такое твой аккаунт забанен')


@bot.message_handler(func=lambda m: True)
def first_level(message):
    global player
    global prevMessage
    started_weapon = [weapons.WoodenStaff(player.stats.intelegency,weapons.WoodenSword())]

    gold = random.randint(1, 10)
    player['gold'] = player["gold"]+gold # Добавляем голду персонажу # a ono work? i havnt gold anyway
    player["items"].append(random.choice(started_weapon))
    
    db.update_player_data(id, {"location": "forest", "items":player["items"], 'gold':player['gold']})

    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(button.look_around(), button.check_inventory())
    prevMarkup=user_markup # Сделать отдельную функцию или декторатор, которые будут автоматом записывать текст и кнопки
    prevMessage= bot.send_message(message.from_user.id,
                                  levelTexts.start_location(player),
                                  reply_markup=user_markup)


def player_inventory_check(message):
    inventory = player["items"]
    text = ''
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    if len(inventory) > 0:
        user_markup.row(button.use_item())
        for item in inventory:
            text += f'\n Название: {item.name} Урон: {item.damage}' # todo сделать нормальное отображение: НазваниеПредмета: Количество
    else:
        text = button.empty_backpack()
    user_markup.row(button.back())
    bot.send_message(message.from_user.id,text, reply_markup=user_markup)

def back_button(message):
    bot.send_message(message.from_user.id,prevMessage.text, reply_markup=prevMarkup)

def forward_button(message):
    bot.send_message(message.from_user.id, move.forward())

def forward_button(message):
    bot.send_message(message.from_user.id, move.forward())
    bot.send_message(message.from_user.id, event)


def fight(message):
    global enemy
    global player
    if player==None:
        getPlayer(message)
    if(player and player["hp"] <=0):
        return bot.send_message(message.from_user.id,'Ты умер, угомонись')

    if isPlayerMove:
        if enemy == None:
            enemys= list(db.getCollection('enemy'))
            enemy = random.choice(enemys)
            text=f'Ваш враг {enemy["name"]}\n' \
                 f'HP {enemy["hp"]}'
        else:
            enemy['hp'] -=10
            text= ''
            text+=f'Вы наносите 10урона'
            text+=f'Ваш враг {enemy["name"]}\n' \
                  f'HP {enemy["hp"]}'
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('fight')
        bot.send_message(message.from_user.id,text,reply_markup=user_markup)
    else:
        enemyAttack(message)
    togglePlayerMove()


def enemyAttack(message):
    enemyDamage = random.randint(enemy['damage']['min'], enemy['damage']['max'])
    player['hp']-=enemyDamage
    text=f'{enemy["name"]} наносит вам {enemyDamage} урона'
    text+=f'Ваше здоровье: {player["hp"]}'
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('fight')
    user_markup.row('Ваншотнуть врага: 100 руб')
    bot.send_message(message.from_user.id,text,reply_markup=user_markup)

def togglePlayerMove():
    global isPlayerMove
    isPlayerMove=not isPlayerMove

def getPlayer(message):
    user = message.from_user
    global player
    player = db.get_player(user.id)
    if player == None:
        db.create_new_player(user.id, user.username or user.first_name)
        player = db.get_player(user.id)
