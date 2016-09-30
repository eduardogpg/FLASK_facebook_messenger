#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import threading

from models import UserModel
from models import MessageModel

from data_struct import create_quick_replies_location
from data_struct import create_quick_replies_message
from data_struct import create_typing_message
from data_struct import create_text_message

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

    if user is None:
       first_steps(user_id)

def validate_quick_replies(user, message):
    quick_replie = message.get('quick_reply', {})
    attachments = message.get('attachments', [] )
    
    if quick_replie or attachments:
        if attachments:
            set_user_attachment(attachments, user)

def set_user_attachment(attachments, user):
    for attachment in attachments:
        if attachment['type'] == 'location':
            coordinates = attachment['payload']['coordinates']
            lat, lng = get_location(coordinates)
            send_message_location(lat, lng, user)

def set_user_location(coordinates, user):
    if user is not None:
        user['lat'], user['long'] = coordinates['lat'], coordinates['long']
        UserModel.save(user)

def get_location(coordinates):
    return coordinates['lat'], coordinates['long']

def send_message_location(lat, lng, user):
    res = requests.get('http://api.geonames.org/findNearByWeatherJSON',
                params={ 'lat': lat, 'lng': lng, 'username': 'eduardo_gpg'}   )

    if res.status_code == 200:
        res = json.loads(res.text)

        city = res['weatherObservation']['stationName']
        temperature = res['weatherObservation']['temperature']
        data_model = {'city': city, 'temperature': temperature }
        
        send_loop_messages(user, 'specific', 'temperature', data_model)
        

def validate_actions(user_id):
    message = 'Es bueno tenerte de regreso {name}'.format(name = user['first_name'])
    message_data = text_message(user_id, message)
    call_send_API(message_data)

def first_steps(user_id):
    data = call_user_API(user_id) 
    user = UserModel.new( first_name = data['first_name'], last_name = data['last_name'], gender = data['gender'], user_id = user_id)
    UserModel.save(user)
    send_loop_messages(user, 'common', 'welcome')

def send_loop_messages(user, type_message='', context = '', data_model = {} ):
    messages = MessageModel.find(type = type_message,  context = context)

    for message in messages:
        message_data = get_message_data(message, user, data_model)
        typing_data = create_typing_message(user)

        call_send_API( typing_data )
        call_send_API( message_data)


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



