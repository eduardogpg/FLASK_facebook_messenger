from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.bot_codigo_facilito

def get_user(user_id):
	user = db.users.find_one( {"user_id": user_id } )
	return user

def new_user(user_instance):
	user_id = db.users.insert_one(user_instance)
	return user_id
