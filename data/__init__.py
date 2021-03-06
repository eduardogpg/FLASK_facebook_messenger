from structs import greeting
from structs import text_message
from structs import image_message
from structs import video_message
from structs import video_message
from structs import audio_message
from structs import file_message

from structs import typing_message
from structs import replie_location
from structs import item_quick_replie
from structs import quick_replie_message

from structs import template_message_generic
from structs import element_template_message
from structs import button_item_template_message_url
from structs import button_item_template_message_payload

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
    elements = [  create_element_template_message(element)  for element in data['elements'] ]
    return template_message_generic(user['user_id'], elements)  

def create_element_template_message(data):
    buttons = [ create_button_item_template_message(button)  for button in data['buttons']]
    return element_template_message(data['title'], data['subtitle'], data['item_url'], data['image_url'], buttons)

def create_button_item_template_message(data):
    if data.get('type', '') == 'web_url':
        return button_item_template_message_url(data['title'], data['url'])
    else:
        return button_item_template_message_payload(data['title'], data['payload'])

def create_image_message(user, data):
    url = data.get('url', '')
    if not url:
        url = 'http://i.imgur.com/T29iOcj.jpg' #Esto deberia ser dinamico mover esto a API
    return image_message( user['user_id'], url)

def create_video_message(user, data):
    url = data.get('url', '')
    if not url:
        url = 'http://techslides.com/demos/sample-videos/small.mp4'
    return video_message( user['user_id'], url)

def create_audio_message(user, data):
    url = data.get('url', '')
    if not url:
        url = 'http://techslides.com/demos/sample-videos/small.mp4'
    return audio_message( user['user_id'], url)

def create_file_message(user, data):
    url = data.get('url', '')
    if not url:
        url = 'http://techslides.com/demos/sample-videos/small.mp4'
    return file_message( user['user_id'], url)


