#!/usr/bin/env python
# -*- coding: utf-8 -*-
def text_message(recipient_id, message_text):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': { 'text': message_text}
    }
    return message_data

def typing_message(recipient_id):
    message_data = {
        'recipient': {'id': recipient_id},
        'sender_action' : 'typing_on'
    }
    return message_data

def quick_replie_message(recipient_id, title, replies ):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {    
            'text': title,
            'quick_replies': replies
        }
    }
    return message_data

def item_quick_replie(title, payload):
    item =  {
			'content_type':'text',
			'title': title,
			'payload': payload
		  }
    return item

def replie_location(title, recipient_id):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {    
            'text': title,
            'quick_replies':[
              {
                'content_type':'location',
              }
            ]
        }
    }
    return message_data

def image_message(recipient_id, url):
    message_data = {
        "recipient":{ "id":recipient_id},
        "message":{
        "attachment":{
            "type":"image",
                "payload":{
                    "url":"http://i.imgur.com/SOFXhd6.jpg"
                }
            }
        }
    }   
    return message_data

def greeting(title):
    message_data = {
        "setting_type": "greeting",
        "greeting":{
            "text": "Hi {{user_first_name}}, welcome to this bot."
        }
    }
    return message_data