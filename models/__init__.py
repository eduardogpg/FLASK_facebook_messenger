from pymongo import MongoClient
from user import User
from message import Message
import os
import json

def load_message_data(model):
	with open('models/data/messages.json') as data:
		list_json_data = json.load(data)
		for json_data in list_json_data:
			model.save(json_data)

URL = 'localhost'
PORT = 27017
USER_COLLECTION = 'users'
MESSAGE_COLLECTION = 'messages'

client = MongoClient(URL, PORT)
database = client.bot_facilito

UserModel = User(database = database, collection = USER_COLLECTION)
MessageModel = Message(database = database, collection = MESSAGE_COLLECTION)

load_message_data(MessageModel)