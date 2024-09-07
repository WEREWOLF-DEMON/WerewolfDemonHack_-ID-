from env import MONGO_URL
from logger import LOGGER
from WEREWOLF-DEMON.database.mongo import Mongo

DB = None
if MONGO_URL:
    LOGGER(__name__).info('Database Intialised')
    DB = Mongo(MONGO_URL)
