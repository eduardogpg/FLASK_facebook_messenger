from models import MessageModel

messages = MessageModel.find(context= 'welcome').order_by('order', asc = False)

"""
for message in messages:
	print message['order']
"""