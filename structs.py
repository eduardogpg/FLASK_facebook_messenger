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

def quick_replies_message(recipient_id, title, replies ):
    message_data = {
        'recipient': {'id': recipient_id},
        'message': {    
            'text': title,
            'quick_replies': replies
        }
    }
    return message_data

def item_quick_replies(title, payload):
    data =  {
				"content_type":"text",
				"title": title,
				"payload": payload
		}
    return data

def quick_replies_by_model(user_id, data):
	options = []
	for option in data['options']:
		item = item_quick_replies(option['title'], option['payload'])
		options.append(item)

	replie = quick_replies_message(user_id, data['title'], options)
	return replie