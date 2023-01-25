from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
mongo = client.local


def getPlayer(playerId):
    return mongo.players.find_one({'id': playerId})


def createPlayer(id):
    return mongo.players.insert_one({  # / изначальне характеристики, если игрок не найден
        'id': id,
        'level': 1,
        'items': [],
    })
