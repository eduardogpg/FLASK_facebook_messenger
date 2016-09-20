from models import Message

if __name__ == '__main__':
	data = Message.find(context= 'welcom')
	for message in data:
		print message['title']