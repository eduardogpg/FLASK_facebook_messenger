import json
import requests
import threading

import models


def received_message(event, token):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp'] 
    message = event['message']

    validate_user(token, sender_id)


def validate_user(token, user_id):
    user = models.get_user(user_id) #exist in the database?
    if user is None:
        user = user_API(token, user_id)
        new_user = models.new_user( user )
        if new_user is not None:
            print "Nuevo usuario registrado en la base de datos!"

    else:
        message = 'Es bueno tenerte de regreso {name}'.format(name = user['first_name'])
        send_text_message(token, user_id, message)
        

def sent_typing_message(token, recipient_id):
    message_data = {
        'recipient': {'id': recipient_id},
        'sender_action' : 'typing_on'
    }
    call_send_API(token, message_data)


def send_text_message(token, recipient_id, message_text):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': { 'text': message_text}
    }
    call_send_API(token, message_data)


def call_send_API(token, data):
    res = requests.post('https://graph.facebook.com/v2.6/me/messages',
                params={ 'access_token': token},
                data= json.dumps( data ),
                headers={'Content-type': 'application/json'})

    if res.status_code == 200:
        print "Mensaje enviado exitosamente!"
    

def user_API(token, user_id):
    res = requests.get('https://graph.facebook.com/v2.6/' + user_id,
                params={ 'access_token': token} )

    data = json.loads(res.text)
    data['user_id'] = user_id
    return data


