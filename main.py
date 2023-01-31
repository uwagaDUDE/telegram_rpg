import db
import interface
import items
import scripts
import telegram_bot


# name = interface.StartGame().start_game(weapon.WoodenSword().name, 2)
# player = player.Player(name)
move = scripts.Movement()
interface = interface.Interface()

event = scripts.Event()
#db.pusher()
telegram_bot.bot_init()


