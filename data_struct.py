from structs import text_message
from structs import typing_message
from structs import quick_replie_message
from structs import item_quick_replie
from structs import replie_location

""" Funciones Para crear las estructuras """
def create_quick_replies_message(data, user):
    replies = []
    for replie in data['replies']:
        item = item_quick_replie(replie['title'], replie['payload'])
        replies.append( item  )
    
    return quick_replie_message( user['user_id'], data['content'], replies)

def create_text_message(data, user, data_model):
    message = data.get('content', '')
    if 'format' in data:
        message = message.format(**data_model) if 'data_model' in data else message.format(**user)
    return text_message(user['user_id'], message)

def create_quick_replies_location(data, user):
    return replie_location(data['title'], user['user_id'])

def create_typing_message(user):
	return typing_message(user['user_id'])