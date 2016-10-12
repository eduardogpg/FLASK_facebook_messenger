from model import Model
from pymongo import ASCENDING

class Message(Model):

	def __init__(self, database, collection ):
		super(Message, self).__init__(database, collection)
	
	def find_by_order(self, **kwargs):
		return self.find_all(**kwargs).sort('order', ASCENDING)

	def set_number_messages(self):
		self.__number_messages = 10

	def get_number_messages(self):
		return self.__number_messages