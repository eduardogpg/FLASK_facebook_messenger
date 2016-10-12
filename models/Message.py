from model import Model
from pymongo import ASCENDING

class Message(Model):
	def __init__(self, database, collection ):
		super(Message, self).__init__(database, collection)

	def find_order(self,**kwargs):
		self.find_all(kwargs).sort('order', ASCENDING)