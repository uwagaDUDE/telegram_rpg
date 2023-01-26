from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
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
