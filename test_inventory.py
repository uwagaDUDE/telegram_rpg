items = \
    {
    'wooden_sword':0,
    'healing_flask':0,
    'iron_sword':0
    }
player = {
    'items':'',
    'test':''
}
item_movement = []
second_item_movement = []
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

class Pizdos:
    #ДОБАВЛЯЕМ НАЗВАНИЕ ПРЕДМЕТА В СПИСОК
    def add_item_in_inventory(self):
       return item_movement.append('Test')
    #ИЗ СПИСКА ДЕЛАЕМ СТРОКУ, ХЗ ЗАЧЕМ ЕСЛИ МОЖНО БЫЛО СРАЗУ В СТРОКУ ДОБАВЛЯТЬ А НЕ В СПИСОК
    def into_str(self):
        stroka = ''
        for i in item_movement:
            stroka += i
        return stroka
    #ТО ЖЕ САМОЕ ПРОДЕЛЫВАЕМ С КОЛИЧЕСТВОМ
    def second_add_item_in_inventory(self):
        return second_item_movement.append(1)

    def sec_into_str(self):
        stroka = 0
        for i in second_item_movement:
            stroka += i
        return stroka
    #ЗАБРАСЫВАЕМ В ИНВЕНТАРЬ
    def back_to_dict(self):
        global player
        player['items'] = {self.into_str():self.sec_into_str()}
        return player['items']
    #GUI
    def put_in_inv(self):
        print('Полож на место и не трогай!')
        return input('Взять (нажми 1): ')
    #ПОРЯДОК ВЫПОЛНЕНИЯ
    def print_dict(self):
        if self.put_in_inv() == "1":
            self.add_item_in_inventory()
            self.second_add_item_in_inventory()
            print(self.back_to_dict())
#ВЫВОДИМ
test = Pizdos()
test.print_dict()

