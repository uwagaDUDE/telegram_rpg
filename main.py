import interface
import items
import scripts
import TelegramBot

weapon = items.Items().Weapons()
# name = interface.StartGame().start_game(weapon.WoodenSword().name, 2)
# player = player.Player(name)
move = scripts.Movement()
interface = interface.Interface()

event = scripts.Event()

TelegramBot.botStart()

