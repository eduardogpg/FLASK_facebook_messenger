#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import datetime
from datetime import timedelta
import re
import threading
import time
import random

from models import UserModel
from models import MessageModel
from models import DecisionModel

from data_struct import create_text_message
from data_struct import create_image_message
from data_struct import create_video_message
from data_struct import create_typing_message
from data_struct import create_greeting_message
from data_struct import create_template_message
from data_struct import create_quick_replies_message
from data_struct import create_quick_replies_location

global_token = ''
global_username = ''
MIN_TIME = 1

def set_greeting_message():
    message = create_greeting_message()
    call_send_API(message)

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
    user = UserModel.find(user_id = user_id)
    if user is None:
        first_steps(user_id)
    else:
        try_send_message(user, message)

def first_steps(user_id):
    data = call_user_API(user_id) 
    user = UserModel.new( first_name = data['first_name'], last_name = data['last_name'], gender = data['gender'], user_id = user_id, created_at = datetime.datetime.now() )
    save_user_asyn(user)
    send_loop_messages(user, 'common', 'welcome')

def try_send_message(user, message):
    validate_quick_replies(user, message) 
    check_last_connection(user)

    if 'ayuda' in message['text']:
        send_loop_messages(user, type_message = 'help', context = 'help')
    elif 'contacto desarrollador' in message['text']:
        send_loop_messages(user, type_message = 'develop', context = 'develop')
    else:
        send_loop_messages(user, type_message = 'not_found', context = 'not_found')
    
def decision_tree(user, message):
    if 'bot facilito' in message:
        use_decision_tree(user, message, name = 'bot facilito')
    else:
        send_loop_messages(user, type_message = 'common', context = 'not_found')

def change_preference(user):
    send_single_message(user, identifier = 'set_preference')

def check_last_connection(user):
    date_now = datetime.datetime.now()
    last_message = user.get('last_message', date_now)

    #if  (last_message + datetime.timedelta(minutes = 1) ) > date_now:
    if 2 > 5:
        send_loop_messages(user, type_message='specific', context='return_user')
        programming_message()

    user['last_message'] = date_now
    UserModel.save(user)

def validate_quick_replies(user, message):
    quick_replie = message.get('quick_reply', {})
    attachments = message.get('attachments', [] )
    
    if quick_replie or attachments:
        if attachments:
            set_user_attachment(user, attachments)
        elif quick_replie:
            set_user_quick_replie(quick_replie, user)

def set_user_attachment(user, attachments):
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
    data_model = call_geosname_API(lat, lng)

    locations = user.get('locations', [])
    locations.append( {'lat': lat, 'lng': lng, 'city': data_model['city'], 'created_at': datetime.datetime.now()  } )
    user['locations'] = locations
    save_user_asyn(user)
    
    send_loop_messages(user, 'specific', 'temperature', data_model)
        
def validate_actions(user_id):
    message = 'Es bueno tenerte de regreso {name}'.format(name = user['first_name'])
    message_data = text_message(user_id, message)
    call_send_API(message_data)

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
    messages = MessageModel.find_by_order(type = type_message, context = context)
    
    for message in messages:
        send_message(user, message, data_model)

def send_single_message(user, identifier = ''):
    message = MessageModel.find(identifier = identifier)
    send_message(message, user)

def send_message(user, message, data_model = {} ):
    message_data = get_message_data(user, message, data_model)
    typing_data = create_typing_message(user)

    call_send_API( typing_data )
    call_send_API( message_data)

def get_message_data(user, message, data_model):
    type_message = message.get('type_message', '')
    
    if type_message == 'text_message':
        return create_text_message(user, message, data_model)
    
    elif type_message ==  'quick_replies':
        return create_quick_replies_message(user, message)
    
    elif type_message == 'quick_replies_location':
        return create_quick_replies_location(user, message)

    elif type_message == 'template':
        return create_template_message(user, message)

    elif type_message == 'image':
        return create_image_message(user, message)
        
    elif type_message == 'video':
        return create_video_message(user, message)
        
def call_send_API(data):
    res = requests.post('https://graph.facebook.com/v2.6/me/messages',
                params={ 'access_token': global_token},
                data= json.dumps( data ),
                headers={'Content-type': 'application/json'})

    if res.status_code == 200:
        print "Mensaje enviado exitosamente!"
    
def call_user_API(user_id):
    res = requests.get('https://graph.facebook.com/v2.6/'+ user_id, 
            params={ 'access_token': global_token} )
    data = json.loads(res.text)
    return data

def call_geosname_API(lat, lng):
    res = requests.get('http://api.geonames.org/findNearByWeatherJSON', 
        params={ 'lat': lat, 'lng': lng, 'username': global_username }   )

    if res.status_code == 200:
        res = json.loads(res.text)

        city = res['weatherObservation']['stationName']
        temperature = res['weatherObservation']['temperature']
        return {'city': city, 'temperature': temperature }

def get_preferences_user(user):
    preferences = user.get('preferences', [])
    if preferences:
        return 'reminder', random.choice(preferences)
    return 'reminder', 'configuraciones'

def save_user_asyn(user):
    def asyn_method(user):
        UserModel.save(user)
    asyn = threading.Thread( name='asyn_method', target= asyn_method, args=(user,))
    asyn.start()

def programming_message(user):
    def send_remainer(user, type_message='', context = '', data_model = {} ):
        time.sleep(20)
        send_loop_messages(user, type_message, context, data_model)

    type_message, context = get_preferences_user(user)
    message = threading.Thread( name='send_remainer', target= send_remainer, args=(user, type_message, context))
    message.start()


