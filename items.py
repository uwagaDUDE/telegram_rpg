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
                self.item_id = 300

        class GrilledChicken:
            def __init__(self):
                self.name = 'Жареная курица'
                self.heal = 50
                self.sell_price = 0
                self.buy_price = 40
                self.item_id = 301
                
    class QuestItems:

        class TestItem:
            def __init__(self):
                self.name = 'Ветка'
                self.item_id = 500

    class CraftItem:

        class RawChicken:
            def __init__(self):
                self.name = 'Сырая курица'
                self.buy_price = 10
                self.item_id = 1000
