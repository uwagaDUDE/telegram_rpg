import interface
import items
import postSql
import scripts

move = scripts.Movement()
weapon = items.Items().Weapons()

def main():

    print(f'Взмахивая своим {weapon.WoodenSword().name}, '
          f'вы наносите {weapon.WoodenSword().damage} урона!')
    print('123')
main()