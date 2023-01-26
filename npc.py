import json
import random


class Enemy:

    class Orcs:

        class Peon:
            def __init__(self):
                self.name = 'Орк рабочий'
                self.hp = 100
                self.damage = random.randint(5,15)
                self.gold = random.randint(1,2)

        class Warrior:
            def __init__(self):
                self.name = 'Рубака'
                self.hp = 110
                self.damage = random.randint(15,30)
                self.gold = random.randint(1,15)

        class Shaman:
            def __init__(self):
                self.name ='Орк шаман'
                self.hp = 50
                self.damage = random.randint(60)
                self.gold = random.randint(1, 20)

        class Hunter:
            def __init__(self):
                self.name ='Орочий фуражир'
                self.hp = 200
                self.damage = random.randint(10, 20)
                self.gold = random.randint(1,50)

        class Warlord:
            def __init__(self):
                self.name ='Вождь'
                self.hp = 500
                self.damage = random.randint(50,100)
                self.gold = random.randint(50,200)

        class HighShaman:
            def __init__(self):
                self.name ='Верховный шаман'
                self.hp = 250
                self.damage = random.randint(70, 150)
                self.gold = random.randint(50, 150)

        class Rider:
            def __init__(self):
                self.name ='Волчий наездник'
                self.hp = 150
                self.damage = random.randint(20,30)
                self.gold = random.randint(1,37)

    class Animals:

        class ForestWolf:
            def __init__(self):
                self.name = 'Лесной волк'
                self.hp = 50
                self.damage = random.randint(2,8)
                self.item = [1001, 1002]

    class Humans:

        class Robber:
            def __init__(self):
                self.name = 'Разбойник'
                self.hp = 100
                self.damage = random.randint(12,20)
                self.gold = random.randint(1, 30)

        class HighRobber:
            def __init__(self):
                self.name ='Главарь разбойников'
                self.hp = 200
                self.damage = random.randint(20, 50)
                self.gold = random.randint(20,50)

        class Murder:
            def __init__(self):
                self.name ='Заказной убийца'
                self.hp = 30
                self.damage = random.randint(80, 150)
                self.gold = random.randint(100,250)

        class EvilKnight:
            def __init__(self):
                self.name ='Рыцарь отступник'
                self.hp = 200
                self.damage = random.randint(20, 50)
                self.gold = random.randint(1,50)

        class Necromant:
            def __init__(self):
                self.name ='Некромант'
                self.hp = 100
                self.damage = random.randint(1, 20)
                self.gold = random.randint(1,20)

    class Undeads:

        class Skeleton:
            def __init__(self):
                self.name ='Скелет'
                self.hp = 15
                self.damage = random.randint(10, 50)
                self.gold = random.randint(1,20)

        class Zombie:
            def __init__(self):
                self.name ='Зомби'
                self.hp = 50
                self.damage = random.randint(20, 50)
                self.gold = random.randint(1,20)

        class Ghost:
            def __init__(self):
                self.name ='Призрак'
                self.hp = 100
                self.damage = random.randint(30, 50)
                self.gold = random.randint(0,0)