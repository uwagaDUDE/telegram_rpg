items = \
    {
    'wooden_sword':0,
    'healing_flask':0,
    'iron_sword':0
    }

print(f'Взять деревянный меч в руки - 1, взять железный - 2, выбросить - 3, оружие в руке - 4')
def pick_up_sword():
    stop = False
    weapon_in_hand = []
    while stop != True:
        pick_up = input('(1/2/3): ')
        if pick_up == "1":
            if len(weapon_in_hand) == 0:
                items['wooden_sword'] = items['wooden_sword']+1
                item_check = {v: k for k, v in items.items()}
                for i in items.values():
                    if i > 0:
                        weapon_in_hand.append(item_check[i])
                        print(weapon_in_hand)
            else:
                print(f'У вас уже есть оружие в руках - {weapon_in_hand}')
        elif pick_up == "2":
            if bool(weapon_in_hand) is False:
                items['iron_sword'] = items['iron_sword'] + 1
                item_check = {v: k for k, v in items.items()}
                for i in items.values():
                    if i > 0:
                        weapon_in_hand.append(item_check[i])
                        print(weapon_in_hand)
            else:
                print(f'У вас уже есть оружие в руках - {weapon_in_hand}')
        elif pick_up == "4":
            print(f'У вас в руке - {weapon_in_hand}')
        else:
            for a in weapon_in_hand:
                if a in items:
                    print(f'Вы выбросили - {weapon_in_hand}')
                    items[a] = 0
            weapon_in_hand.clear()


pick_up_sword()