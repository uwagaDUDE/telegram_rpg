from dotenv import dotenv_values
from pymongo import MongoClient

client = MongoClient(f'mongodb+srv://amogus:{dotenv_values(".env")["DB_PASSWORD"]}@cluster0.hearvjr.mongodb.net/?retryWrites=true&w=majority')
mongo = client.local


def getPlayer(playerId):
    return mongo.players.find_one({'id': playerId})


def createPlayer(id,userName):
    return mongo.players.insert_one({  # / изначальне характеристики, если игрок не найден
        'id': id,
        'userName':userName,
        'level': 1,
        'items': [],
    })

def updatePlayerInventory(id,items):
    return mongo.player.update_one({"id":str(id)}, {"push":{"items": items}},upsert= True)
def updatePlayer(id,updateObject):
    return mongo.players.update_one({"id":str(id)},{"$set":updateObject},upsert=True)
