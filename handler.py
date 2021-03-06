#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from datetime import timedelta
from collections import OrderedDict
import threading
import time
import random

import data
import models
from api import *

from models import DecisionModel

global_token = ''
global_username = ''
MAX_TIME = 600

def received_post_back(event, token):
    print("postback recived")

    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_post_back = event['timestamp'];
    payload = event['postback']['payload']

    global global_token
    global_token = token
    
    handler_postback(sender_id, payload)

def received_message(event, token, username):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp'] 
    message = event['message']

    global global_token, global_username
    global_token = token
    global_username = username

    handler_actions( sender_id, message)

def handler_actions(user_id, message):
    user = models.UserModel.find(user_id = user_id)
    try_send_message(user, message)

def handler_postback(user_id, payload):
    if payload == 'USER_DEFINED_PAYLOAD':
        first_steps(user_id)
    else:
        user = models.UserModel.find(user_id = user_id)
        send_loop_messages(user, type_message='postback', context=payload)

def first_steps(user_id):
    data = call_user_API(user_id, global_token) 
    user = models.UserModel.new( first_name = data['first_name'], last_name = data['last_name'], gender = data['gender'], user_id = user_id, created_at = datetime.datetime.now() )
    save_user_asyn(user)
    send_loop_messages(user, 'common', 'welcome')

def try_send_message(user, message):
    actions =  validate_quick_replies(user, message) or check_last_connection(user)
    #send_messsage_by_preference(user)
    
    if 'ayuda' in message['text']:
        send_loop_messages(user, type_message = 'help', context = 'help')

    elif 'contacto desarrollador' in message['text']:
        send_loop_messages(user, type_message = 'develop', context = 'develop')

    elif 'imagen random' in message['text']:
        #Un consejo obtener la imagen de lo que el usuario quiera!
        send_loop_messages(user, type_message = 'image', context = 'random')
    
    elif 'video random' in message['text']:
        send_loop_messages(user, type_message = 'video', context = 'random')

    else:
        if not actions:
            send_loop_messages(user, type_message = 'not_found', context = 'not_found')
    
def decision_tree(user, message):
    if 'bot facilito' in message:
        use_decision_tree(user, message, name = 'bot facilito')
    else:
        send_loop_messages(user, type_message = 'not_found', context = 'not_found')

def change_preference(user):
    send_single_message(user, identifier = 'set_preference')

def check_last_connection(user):
    now = datetime.datetime.now()
    last_message = user.get('last_message', now)

    user['last_message'] = now
    save_user_asyn(user)

    if (now - last_message).seconds >= MAX_TIME:
        send_loop_messages(user, type_message='specific', context='return_user')
        programming_message()
        return True

def validate_quick_replies(user, message):
    quick_replie = message.get('quick_reply', {})
    attachments = message.get('attachments', [] )
    
    if quick_replie or attachments:
        if attachments:
            set_user_attachment(user, attachments)
        elif quick_replie:
            set_user_quick_replie(quick_replie, user)
        return True

def set_user_attachment(user, attachments):
    print attachments
    print "\n\n\n\n"

    for attachment in attachments:
        if attachment['type'] == 'location':
            coordinates = attachment['payload']['coordinates']
            lat, lng = get_location(coordinates)
            add_user_location(user, lat, lng)
            check_actions(user, 'location')

def set_user_quick_replie(quick_replie, user):
    if user is not None:
        payload = quick_replie['payload']
        preferences = user.get('preferences', [])
        if not preferences or payload not in preferences:
            preferences.append(payload)
        
        user['preferences'] = preferences
        save_user_asyn(user)
        print(payload)
        send_loop_messages(user, type_message = 'quick_replies', context = payload )

def check_actions(user, action):
    actions = user.get('actions', [])
    action_struct = { action: 'Done' }

    if action_struct not in actions:
        actions.append(action_struct)
        user['actions'] = actions
        save_user_asyn(user)
        send_loop_messages(user, type_message='Done', context = action )

def get_location(coordinates):
    return coordinates['lat'], coordinates['long']

def add_user_location(user, lat, lng):
    data_model = call_geosname_API(lat, lng, global_username)

    locations = user.get('locations', [])
    locations.append( {'lat': lat, 'lng': lng, 'city': data_model['city'], 'created_at': datetime.datetime.now()  } )
    user['locations'] = locations
    save_user_asyn(user)
    send_loop_messages(user, 'specific', 'temperature', data_model)
        
def use_decision_tree(user, message, name = "", completed = False):
    decision = DecisionModel.find(name = name)
    if decision:
        for option in decision.get('options', []):
            if option['key'] in message:
                completed = True
                execute = option['execute']

                if execute['type'] == 'message':
                    send_loop_messages(user, type_message = execute['type_message'] , context = execute['context'] )

                elif execute['type'] == 'tree_decision':
                    use_decision_tree(user, message, execute['tree_decision_name'])
                
        if not completed:
            send_loop_messages(user, type_message = 'common', context = 'not_found')

def send_loop_messages(user, type_message='', context = '', data_model = {} ):
    messages = models.MessageModel.find_by_order(type = type_message, context = context)
    for message in messages:
        send_message(user, message, data_model)

def send_single_message(user, identifier = ''):
    message = models.MessageModel.find(identifier = identifier)
    send_message(message, user)

def send_message(user, message, data_model = {} ):
    message_data, typing_data = get_message_data(user, message, data_model)

    call_send_API( typing_data, global_token)
    call_send_API( message_data, global_token)

def get_message_data(user, message, data_model):
    type_message = message.get('type_message', '')
    final_message = None

    if type_message == 'text_message':
        final_message = data.create_text_message(user, message, data_model)
    
    elif type_message ==  'quick_replies':
        final_message = data.create_quick_replies_message(user, message)
    
    elif type_message == 'quick_replies_location':
        final_message = data.create_quick_replies_location(user, message)

    elif type_message == 'template':
        final_message = data.create_template_message(user, message)

    #Hasta aqui vamos
    elif type_message == 'image':
        final_message = data.create_image_message(user, message)
        
    elif type_message == 'video':
        final_message = data.create_video_message(user, message)

    elif type_message == 'audio':
        final_message = data.create_audio_message(user, message)

    elif type_message == 'file':
        final_message = data.create_file_message(user, message)

    return final_message, data.create_typing_message(user)

def get_preferences_user(user):
    preferences = user.get('preferences', [])
    if preferences:
        return 'reminder', random.choice(preferences)
    return 'reminder', 'configuraciones'

def save_user_asyn(user):
    def asyn_method(user):
        models.UserModel.save(user)
    asyn = threading.Thread( name='asyn_method', target= asyn_method, args=(user,))
    asyn.start()

def send_message_by_weather(user):
    send_loop_messages(user, type_message='remainer', context= 'WEATHER')

def send_messsage_by_preference(user):
    preference = get_preference(user)
    if preference is not None:
        menu[preference](user) #Ejecutamos la función asociada
       
menu = OrderedDict([
    ('WEATHER', send_message_by_weather)
]) 

def get_preference(user):
    preferences = user.get('preferences', [])
    if preferences:
        return random.choice(preferences)

def programming_message(user):
    def send_reaminer(user):
        today = datetime.datetime.today()
        future = datetime.datetime( today.year, today.month, today.day, 13, 21 )
        
        time.sleep( (future - today).seconds )
        send_loop_messages(user, type_message='remainer', context= 'remainer')

    message = threading.Thread(name='send_reaminer', target= send_reaminer, args=(user, ))
    message.start()

