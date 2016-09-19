import json
import requests

def received_message(event, token):
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp'] 
    message = event['message']

    send_text_message(token, sender_id, 'Por ahora solo se decir Hola')


def send_text_message(token, recipient_id, message_text):
    message = {
        'recipient': {'id': recipient_id},
        'message': { 'text': message_text}
    }
    call_send_API(token, message)


def call_send_API(token, data):
    request = requests.post('https://graph.facebook.com/v2.6/me/messages',
                params={ 'access_token': token},
                data= json.dumps( data ),
                headers={'Content-type': 'application/json'})

    print request.status_code
  