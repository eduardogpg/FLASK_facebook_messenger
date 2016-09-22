from pymongo import MongoClient, ASCENDING

client = MongoClient('localhost', 27017)
db = client.bot_codigo_facilito

class User(object):
	@staticmethod
	def get_new_preference():
		data = {'completed': False}
		return data

	@staticmethod
	def new_preference():
		preference = []
		preference.append( User.get_new_preference() )
		preference.append( User.get_new_preference() )
		return preference

	@classmethod
	def find(cls, **kwargs):
		user = db.users.find_one( kwargs )
		return user	

	@classmethod
	def new(cls, **kwargs):
		data = {}
		for key, value in kwargs.iteritems():
			data[key] = value
		return data

	@classmethod
	def save(cls, data):
		db.users.save(data)
		return data

	@classmethod
	def remove(cls, **kwargs):
		db.users.remove(kwargs)
		
class Preference(object):
	@classmethod
	def get_first(cls):
		#return db.preferences.find().sort("order").limit(1)
		return db.preferences.find_one()

class Message(object):
	@classmethod
	def find(cls, **kwargs):
		objects = db.common_messages.find(kwargs).sort("order", ASCENDING)
		return objects