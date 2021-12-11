import os
from pymongo import MongoClient

client = MongoClient()
db = client.FoodTracker
users = db.users
entries = db.entries
loggers = db.loggers