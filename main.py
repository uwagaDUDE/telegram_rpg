import interface
import items
import player
import scripts
import TelegramBot

load_dotenv()
weapon = items.Items().Weapons()
# name = interface.StartGame().start_game(weapon.WoodenSword().name, 2)
# player = player.Player(name)
move = scripts.Movement()
interface = interface.Interface()

event = scripts.Event()

TelegramBot.botStart()