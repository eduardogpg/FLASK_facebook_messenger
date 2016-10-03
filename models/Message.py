from model import Model

class Message(Model):
	def __init__(self, database, collection ):
		super(Message, self).__init__(database, collection)
