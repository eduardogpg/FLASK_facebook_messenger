class Model(object):
	def __init__(self, database, collection ):
		self.database = database
		self.collection = collection

	def find(self,**kwargs):
		return self.database[self.collection].find_one(kwargs)

	