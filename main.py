import interface
import items, player
# import postSql
import scripts
weapon = items.Items().Weapons()
name = interface.StartGame().start_game(weapon.WoodenSword().name, 2)
player = player.Player(name)
move = scripts.Movement()
interface = interface.Interface()

def main():

    movement = True
    while movement == True:

        interface.what_to_do()
        user_choice = input('\nЧто будем делать: ')

        if user_choice == "1":
            move.forward_move()
        elif user_choice == "2":
            move.left_move()
        elif user_choice == "3":
            move.right_move()
        else:
            print('NOT REALISED')


main()