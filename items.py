import random
#items ids:
# 100 - Weapon
# 200 - Armor
# 300 - Food
# 500 - Quests items
# 1000 - Craft items
class Items:
    class Weapons:
        class WoodenSword:
            def __init__(self):
                self.name = 'Деревянный меч'
                self.damage = random.randint(5, 8)
                self.sell_price = 5
                self.buy_price = 10
                self.item_id = 100

        class IronSword:
            def __init__(self):
                self.name = 'Железный меч'
                self.damage = random.randint(10, 30)
                self.sell_price = 50
                self.buy_price = 100
                self.item_id = 101

        class IronPike:
            def __init__(self):
                self.name = 'Железная пика'
                self.damage = random.randint(15, 25)
                self.sell_price = 50
                self.buy_price = 100
                self.item_id = 102
    class Armor:

        class VillagerCloth:

            def __init__(self):
                self.name = 'Крестьянская одежда'
                self.armor = 5
                self.sell_price = 10
                self.buy_price = 50
                self.item_id = 201
#
    class Food:
        class Apple:

            def __init__(self):
                self.name = 'Яблоко'
                self.heal = 5
                self.sell_price = 0
                self.buy_price = 5
#     def __init__(self, name, damage, armor, sell_cost, buy_cost, id):
#         self.name = name
#         self.damage = damage
#         self.armor = armor
#         self.sell_cost = sell_cost
#         self.buy_cost = buy_cost
#         self.id = id
# class Item:
#     # def wooden_sword(self):
#     #     return Items(name='Деревяннй меч',
#     #                  damage=random.randint(5,8),
#     #                  sell_cost=5,
#     #                  buy_cost=10,
#     #                  id=0)
#
#     def wooden_sword(self):
#         return Items('Деревяннй меч',
#                      random.randint(5,8),
#                      5,
#                      10,
#                      0)

    #def wooden_sword(self, name='Деревяннй меч', damage=random.randint(5,8), sell_cost=5, buy_cost=10, id=0):
        #return name, damage, sell_cost, buy_cost, id



# def get_random_item(list):
#     return random.choice(list)
#
#
# spawn_items = [wooden_sword, gowno]
#
#
# class Player:
#     def __init__(self):
#         self.hp = 100
#         self.items = []
#         self.damage = 0
#
#     def calc_damage(self):
#         calculated_value = 0;
#         for item in self.items:
#             calculated_value += item.damage
#         self.damage = calculated_value
#
#
# player = Player()
# player.items.append(get_random_item(spawn_items))
# player.calc_damage()
# print(player.damage)