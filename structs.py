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
    data =  {
			"content_type":"text",
			"title": title,
			"payload": payload
		  }
    return data

def replie_location(title, recipient_id):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {    
            'text': title,
            "quick_replies":[
              {
                "content_type":"location",
              }
            ]
        }
    }
    return message_data
