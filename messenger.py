#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import threading
from time import sleep

from models import User as UserModel
from structs import (text_message, typing_message)

def received_message(event, token):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp'] 
    message = event['message']

    validate_user(token, sender_id)

def validate_user(token, user_id):
    user = UserModel.find(user_id = user_id)
    if user is not None:
        message = 'Es bueno tenerte de regreso {name}'.format(name = user['first_name'])
        message_data = text_message(user_id, message)
        call_send_API(token, message_data)
    else:
        say_hello_user(token, user_id)
   
def say_hello_user(token, user_id):
    typing = threading.Thread(name='send_typing_message', target=send_typing_message, args = (token, user_id) )
    typing.start()

    data = call_user_API(token, user_id) 
    user = UserModel.new(   first_name = data['first_name'], last_name = data['last_name'],
                            gender = data['gender'], user_id = user_id)
    UserModel.save(user)

    message = 'Te damos la bienvenida al nuevo curso de CódigoFacilito {name}'.format(name = user['first_name'])
    message_data = text_message(user_id, message)
    call_send_API(token, message_data)

def send_typing_message(token, user_id):
    message_data = typing_message(user_id)
    call_send_API(token, message_data)

def call_send_API(token, data):
    res = requests.post('https://graph.facebook.com/v2.6/me/messages',
                params={ 'access_token': token},
                data= json.dumps( data ),
                headers={'Content-type': 'application/json'})

    if res.status_code == 200:
        print "Mensaje enviado exitosamente!"
    
def call_user_API(token, user_id):
    res = requests.get('https://graph.facebook.com/v2.6/'+ user_id,
                params={ 'access_token': token} )

    data = json.loads(res.text)
    return data

