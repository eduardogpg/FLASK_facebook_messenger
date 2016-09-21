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


""" Funciones Para crear las estructuras """
def create_quick_replies_message(user_id, data_model):
    replies = []
    for item in data_model['quick_replies']:
        new_item = item_quick_replie(item['title'], item['payload'])
        replies.append(new_item)

    data = quick_replie_message(user_id, data_model['title'], replies)
    return replies

def create_text_message(data, user):
    message = data.get('content', '')
    if 'format' in message:
        message = message.format(username = user.first_name)
    return text_message(user['user_id'], message)