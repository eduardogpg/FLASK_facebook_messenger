from pymongo import MongoClient, ASCENDING, DESCENDING

from user import User


client = MongoClient('localhost', 27017)
db = client.bot_codigo_facilito

UserModel = User(database = db, collection = 'usuarios')
print UserModel.find(nombre = 'Eduardo')