from structs import greeting
from structs import text_message
from structs import image_message
from structs import typing_message
from structs import replie_location
from structs import item_quick_replie
from structs import quick_replie_message

def create_greeting_message():
    return greeting('Mensaje')

def create_image_message(data, user):
    return image_message( user['user_id'], "https://petersapparel.com/img/shirt.png")

def create_quick_replies_message(data, user):
    replies = [ item_quick_replie(replie['title'], replie['payload']) for replie in data['replies'] ]
    return quick_replie_message( user['user_id'], data['content'], replies)

def create_text_message(data, user, data_model):
    message = data.get('content', '')
    if 'format' in data:
        message = message.format(**data_model) if 'data_model' in data else message.format(**user)
    return text_message(user['user_id'], message)

def create_quick_replies_location(data, user):
    return replie_location(data['content'], user['user_id'])

def create_typing_message(user):
	return typing_message(user['user_id'])