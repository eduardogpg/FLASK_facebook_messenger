
class Message(object):
	def __init__(self, database):
		self.database = database

	@classmethod
	def find(cls, **kwargs):
		return cls.db.common_messages.find(kwargs)

