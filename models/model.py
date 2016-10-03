class Model(object):
	def __init__(self, database, collection ):
		self.database = database
		self.name_collection = collection
		self.collection = database[collection]

	def find_all(self,**kwargs):
		return self.collection.find(kwargs)

	def find(self,**kwargs):
		return self.collection.find_one(kwargs)

	def save(self, model):
		self.collection.save(model)
		return model

	def delete_collection(self):
		self.collection.delete_many({})
		
	def exist(self):
		return self.collection.count() > 0

