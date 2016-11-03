from structs import greeting
from structs import text_message
from structs import image_message
from structs import video_message
from structs import video_message
from structs import audio_message
from structs import typing_message
from structs import replie_location
from structs import item_quick_replie
from structs import quick_replie_message

from structs import button_item_template_message
from structs import item_template_message
from structs import template_message_generic

def create_greeting_message():
    return greeting('Mensaje')

def create_quick_replies_message(user, data):
    replies = [ item_quick_replie(replie['title'], replie['payload']) for replie in data['replies'] ]
    return quick_replie_message( user['user_id'], data['content'], replies)

def create_text_message(user, data, data_model):
    message = data.get('content', '')
    if 'format' in data:
        message = message.format(**data_model) if 'data_model' in data else message.format(**user)
    return text_message(user['user_id'], message)

def create_quick_replies_location(user, data):
    return replie_location(data['content'], user['user_id'])

def create_typing_message(user):
	return typing_message(user['user_id'])

def create_template_message(user, data):
    print user
    elements = [create_elements(element) for element in data['elements'] ]
    return template_message_generic(user['user_id'], elements)

def create_elements(data):
    buttons = [ create_button(button) for button in data['buttons']  ]
    return item_template_message(data['title'], data['subtitle'], data['item_url'], data['image_url'], buttons )

def create_button(data):
    return button_item_template_message(data['url'], data['title'])

def create_image_message(user, data):
    return image_message( user['user_id'], data['url'])

def create_video_message(user, data):
    return video_message( user['user_id'], data['url'])

def create_audio_message(user, data):
    return audio_message( user['user_id'], data['url'])



