#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import threading
from time import sleep

from models import User as UserModel
from models import Preference as PreferenceModel
from models import Message as MessageModel

from structs import typing_message
from structs import create_quick_replies_message
from structs import create_text_message
from structs import create_quick_replies_location

global_token = ''

def received_message(event, token):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp'] 
    message = event['message']
    
    global global_token
    global_token = token

    handler_actions( sender_id, message)

def handler_actions(user_id, message):
    user = UserModel.find(user_id = user_id)
    validate_quick_replies(user, message)

    """
    if user is not None or user is not :
        validate_quick_replies(user, message)
    elif user is None:
        first_steps(user_id)
    """

def validate_quick_replies(user, message):
    quick_replie = message.get('quick_reply', {})
    attachments = message.get('attachments', [] )
    
    if quick_replie or attachments:
        if attachments:
            set_user_attachment(attachments, user)
        elif quick_replie:
            set_replies_user(quick_replie, user)

def set_user_attachment(attachments, user):
    for attachment in attachments:
        if attachment['type'] == 'location':
            coordinates = attachment['payload']['coordinates']

            set_user_location(coordinates, user)
            send_message_location(coordinates['lat'], coordinates['long'], user)

def set_user_location(coordinates, user):
    user['lat'] = coordinates['lat']
    user['long'] = coordinates['long']
    UserModel.save(user)

def send_message_location(lat, log, user):
    res = requests.get('http://api.geonames.org/findNearByWeatherJSON',
                params={ 'lat': str(lat), 'lng': str(log), 'username': 'eduardo_gpg'}   )

    print "Entro aqui "
    if res.status_code == 200:
        res = json.loads(res.text)

        print "El estatues es 200"

        city = res['weatherObservation']['stationName']
        temperature = res['weatherObservation']['temperature']
        data_model = {'city': city, 'temperature': temperature }
        send_loop_messages(user, 'specific', 'temperature', data_model)
        

def set_replies_user(quick_replie, user):
    pass

def delete_user(user_id):
    UserModel.remove(user_id = user_id)
    print "Some message"

def validate_actions(user_id):
    message = 'Es bueno tenerte de regreso {name}'.format(name = user['first_name'])
    message_data = text_message(user_id, message)
    call_send_API(message_data)

def first_steps(user_id):
    data = call_user_API( user_id) 
    user = UserModel.new( first_name = data['first_name'], last_name = data['last_name'], gender = data['gender'], user_id = user_id)
    UserModel.save(user)
    send_loop_messages(user, 'common', 'welcome')

def send_loop_messages(user, type_message='', context = '', data_model = {} ):
    messages = MessageModel.find(type = type_message,  context = context)


    for message in messages:
        message_data = get_message_data(message, user, data_model)

        if message_data is not None:

            typing_data = typing_message(user['user_id'])
            call_send_API( typing_data )
            call_send_API( message_data)

            sleep(1)

def get_message_data(message, user, data_model):
    type_message = message.get('type_message', '')
    
    if type_message == 'text_message':
        return create_text_message(message, user, data_model)
    
    elif type_message ==  'quick_replies':
        return create_quick_replies_message(message, user)
    
    elif type_message == 'quick_replies_location':
        return create_quick_replies_location(message, user)

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



