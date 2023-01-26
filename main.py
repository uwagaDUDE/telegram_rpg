import interface
import items
import player
import db
import scripts
import telebot
from dotenv import load_dotenv
import os

load_dotenv()
weapon = items.Items().Weapons()
# name = interface.StartGame().start_game(weapon.WoodenSword().name, 2)
# player = player.Player(name)
move = scripts.Movement()
interface = interface.Interface()
bot = telebot.TeleBot(os.environ.get('API_KEY'))

event = scripts.Event()


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
    bot.send_message(
        user.id, f'Добро пожаловать {user.first_name} \nВаш персонаж: \n   Уровень: { player["level"] }   \n Предметов в инвентаре: {len(player["items"])}', reply_markup=user_markup)


bot.polling(none_stop=True, interval=0)
