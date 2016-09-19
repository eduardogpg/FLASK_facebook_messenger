from pymongo import MongoClient

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

		data['preference'] = User.new_preference()
		return data

	@classmethod
	def save(cls, data):
		user_id = db.users.insert_one(data)
		return user_id

