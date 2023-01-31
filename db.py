import npc
from dotenv import dotenv_values
from pymongo import MongoClient
from enums import location
client = MongoClient(
    f'mongodb+srv://amogus:{dotenv_values(".env")["DB_PASSWORD"]}@cluster0.hearvjr.mongodb.net/?retryWrites=true&w=majority')
mongo = client.test
item = npc.Enemy().Humans().Necromant()
Location = location.Location

def get_player(playerId):
    return mongo.players.find_one({'id': playerId})


def create_new_player(id, userName):
    return mongo.players.insert_one({  # / изначальне характеристики, если игрок не найден
        'id': id,
        'userName': userName,
        'level': 1,
        'hp': 100,
        'mana': 100,
        'gold': 0,
        'stats': {
            'strenght': 1,
            'agility': 1,
            'intelegency': 1,
        },
        'items': [],
        'location': Location.Lobby.value
    })


def pusher():
    mongo.enemy.insert_one(
        {
            'name': item.name,
            'hp': item.hp,
            'damage': item.damage,
            'gold': item.gold
        })
    print(f'Было добавлено в базу: {item.name}')


# пока не используется, и возможно не планируется
def update_player_inventory(id, items):
    return mongo.player.update_one({"id": str(id)}, {"push": {"items": items}}, upsert=True)


def update_player_data(id, updateObject):
    return mongo.players.update_one({"id": str(id)}, {"$set": updateObject}, upsert=True)
