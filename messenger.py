#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import threading
from time import sleep

from models import User as UserModel
from models import Preference as PreferenceModel
from models import Message as MessageModel

from structs import text_message 
from structs import typing_message
from structs import create_quick_replies_message
from structs import create_text_message

global_token = ''

def received_message(event, token):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp'] 
    message = event['message']

    global global_token
    global_token = token

    handler_actions( sender_id)

def handler_actions(user_id):
    user = UserModel.find(user_id = user_id)
    if user is not None:
        first_steps(user_id)

def validate_actions(user_id):
    message = 'Es bueno tenerte de regreso {name}'.format(name = user['first_name'])
    message_data = text_message(user_id, message)
    call_send_API(message_data)

def first_steps(user_id):
    data = call_user_API( user_id) 
    user = UserModel.new( first_name = data['first_name'], last_name = data['last_name'], gender = data['gender'], user_id = user_id)
    UserModel.save(user)
    send_loop_messages(user, 'common', 'welcome')

def send_loop_messages(user, type_message='', context = ''):
    messages = MessageModel.find(type = type_message,  context = context)
    for message in messages:
        message_data = get_message_data(message, user)
        if message_data is not None:

            msg_send = threading.Thread(name='call_send_API', target=call_send_API, args = (message_data,) )
            msg_send.start()
            sleep(1)
        
def get_message_data(message, user):
    type_message = message.get('type_message', '')
    if type_message == 'text_message':
        return create_text_message(message, user)

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
