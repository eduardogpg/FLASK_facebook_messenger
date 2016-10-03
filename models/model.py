class Model(object):
	def __init__(self, database, collection ):
		self.database = database
		self.name_collection = collection
		self.collection = database[collection]

	def find(self,**kwargs):
		return self.collection.find_one(kwargs)

	def save(self, model):
		self.collection.insert_one(model).inserted_id
		return model

	def exist(self):
		return self.collection.count() > 0