from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb://root:toor@localhost:27017')

# Creates a new database called 'lmao' if it doesn't exist
db = client.lmao

# Creates a new collection called 'not_lmao' in
# that database and inserts the object into it
db.not_lmao.insert_one({ "aye": "lmao" })