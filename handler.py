#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import datetime
import re
import threading
import time

from models import UserModel
from models import MessageModel
from models import DecisionModel

from data_struct import create_quick_replies_location
from data_struct import create_quick_replies_message
from data_struct import create_typing_message
from data_struct import create_image_message
from data_struct import create_text_message
from data_struct import create_greeting_message
from data_struct import create_template_message

global_token = ''
global_username = ''

def set_greeting_message():
    message = create_greeting_message()
    call_send_API(message)

def show_start_messaged(event, token, username):
    print event

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
    user = UserModel.new( first_name = data['first_name'], last_name = data['last_name'], gender = data['gender'], user_id = user_id)
    UserModel.save(user)
    send_loop_messages(user, 'common', 'welcome')

def try_send_message(user, message):
    validate_quick_replies(user, message) 
    
    if 'ayuda' in message['text']:
        send_loop_messages(user, type_message = 'help', context = 'help')
    
    elif 'eggs' in message['text']:
        send_loop_messages(user, type_message = 'eggs', context = 'eggs')
        #programming_message(user)
    else:
        decision_tree(user, message['text'])

def decision_tree(user, message):
    if 'bot facilito' in message:
        use_decision_tree(user, message, name = 'bot facilito')
    else:
        send_loop_messages(user, type_message = 'common', context = 'not_found')

def change_preference(user):
    send_single_message(user, identifier = 'set_preference')

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
        
        user['preference'] = preferences
        UserModel.save(user)
        send_loop_messages(user, type_message = 'quick_replies', context = payload )

def check_actions(user, action):
    actions = user.get('actions', [])
    action_struct = { action: 'Done' }

    if action_struct not in actions:
        actions.append(action_struct)
        user['actions'] = actions
        UserModel.save(user)
        send_loop_messages(user, type_message='Done', context = action )

def get_location(coordinates):
    return coordinates['lat'], coordinates['long']

def add_user_location(user, lat, lng):
    data_model = call_geosname_API(lat, lng)

    locations = user.get('locations', [])
    locations.append( {'lat': lat, 'lng': lng, 'city': data_model['city'], 'created_at': datetime.datetime.now()  } )
    user['locations'] = locations
    UserModel.save(user)

    send_loop_messages(user, 'specific', 'temperature', data_model)
        
def validate_actions(user_id):
    message = 'Es bueno tenerte de regreso {name}'.format(name = user['first_name'])
    message_data = text_message(user_id, message)
    call_send_API(message_data)

def use_decision_tree(user, message, name = "" ):
    print "Vamos a buscar el arbol con el nombre"
    print name + "\n\n\n\n"

    decision = DecisionModel.find(name = name)

    if decision:
        for option in decision.get('options', []):
            if option['key'] in message:
                
                execute = option['execute']
                print "El tipo de mensaje es "+  execute['type'] +" \n\n\n\n"

                if execute['type'] == 'message':
                    print "Vamos Enviar mensajes"
                    send_loop_messages(user, type_message = execute['type_message'] , context = execute['context'] )
                
                elif execute['type'] == 'tree_decision':
                    print "Vamos a buscar los arboles , vamos a hacer recursivo \n\n\n\n"
                    use_decision_tree(user, message, execute['tree_decision_name'])
    else:
        print "Lo siento no hay nada :("
            
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
    
    elif type_message == 'image':
        return create_image_message(user, message)
    
    elif type_message == 'template':
        return create_template_message(user, message)

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

def programming_message(user):
    message = threading.Thread( name='send_remainer',
                                target= send_remainer,
                                args=(user, 'Reminder', 'configuraciones'))
    message.start()
    
def send_remainer(user, type_message='', context = '', data_model = {} ):
    time.sleep(20)
    send_loop_messages(user, type_message, context, data_model)
