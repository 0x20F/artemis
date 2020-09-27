from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://root:toor@localhost:27017')
db = client.admin
status = db.command('serverStatus')
pprint(status)