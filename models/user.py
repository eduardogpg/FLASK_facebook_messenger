from model import Model

class User(Model):
	def __init__(self, database, collection ):
		super(User, self).__init__(database, collection)

	def new(self, **kwargs):
		return kwargs
