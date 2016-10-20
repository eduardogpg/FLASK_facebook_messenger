from pymongo import MongoClient
from user import User
from message import Message
from decision_tree import DecisionTree
import os
import json

def pluralize_class(instance):
	return "{class_name}s".format( class_name = instance.__class__.__name__)

def get_path():
	return os.path.dirname(os.path.realpath(__file__))

def load_message_data(model, folder = 'data', file = '' ):
	path = "{path}/{folder}/{file}.json".format(file = pluralize_class(model), path = get_path(), folder = folder )
	model.delete_collection()

	with open(path) as data:
		list_json_data = json.load(data)
		for json_data in list_json_data:
			model.save(json_data)

URL = 'localhost'
PORT = 27017
USER_COLLECTION = 'users'
MESSAGE_COLLECTION = 'messages'
DECISION_COLLECTION = 'decisions'
DATABSE = 'bot_facilito'

client = MongoClient(URL, PORT)
database = client['bot_facilito']

UserModel = User(database = database, collection = USER_COLLECTION)
MessageModel = Message(database = database, collection = MESSAGE_COLLECTION)
DecisionModel = DecisionTree(database = database, collection = DECISION_COLLECTION)

UserModel.delete_collection()

load_message_data(MessageModel)
load_message_data(DecisionModel)

MessageModel.set_number_messages()

