import random

class Items:
    class Weapons:
        class WoodenSword:
            def name(self):
                return 'Деревянный меч'
            def damage(self):
                return random.randint(5,8)
            def sell_price(self):
                return 5
            def buy_price(self):
                return 10
            def item_id(self):
                return 0

        # class Items:
#
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