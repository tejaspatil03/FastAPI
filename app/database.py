from pymongo import MongoClient

def getDB():
    MONGO_URL = "mongodb+srv://stepup:123@stepup.wztrxem.mongodb.net/"
    DB_NAME = "sms"

    server = MongoClient(MONGO_URL)
    db = server[DB_NAME]
    return db