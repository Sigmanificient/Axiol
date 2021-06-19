import os
from pymongo import MongoClient


MONGOCLIENT = MongoClient(os.environ.get("MONGO_URL")) #Client

#Databases
DATABASE = MONGOCLIENT["Axiol"] #Main DB
LEVELDATABASE = MONGOCLIENT["Leveling"]


#Collections
PLUGINS = DATABASE["Plugins"]
PREFIXES = DATABASE["Prefixes"]
REACTIONROLES = DATABASE["Reaction Roles"]
WELCOME = DATABASE["Welcome"]
VERIFY = DATABASE["Verify"]
CHATBOT = DATABASE["Chatbot"]
YOUTUBE = DATABASE["YouTube"]