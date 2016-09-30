from pymongo import MongoClient, ASCENDING, DESCENDING

client = MongoClient('localhost', 27017)
db = client.bot_codigo_facilito


class UserModel(object):
	def __init__(self, database):
		self.db = database
		
	@staticmethod
	def find(**kwargs):
		return db.users.find_one( kwargs )
		 
	@staticmethod
	def new(**kwargs):
		return { key:value for key, value in kwargs.iteritems()  }
		
	@staticmethod
	def save(data):
		db.users.save(data)
		
class MessageModel(object):
	cls_object = None

	@staticmethod
	def find(**kwargs):
		return db.common_messages.find(kwargs)

	@staticmethod
	def order_by(model, field = '', asc = True):
		type_sort = ASCENDING if asc else DESCENDING
		return model.sort(field, type_sort)




