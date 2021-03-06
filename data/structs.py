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

def greeting(title):
    message_data = {
        "setting_type": "greeting",
        "greeting":{
            "text": "Hi {{user_first_name}}, welcome to this bot."
        }
    }
    return message_data

def button_item_template_postback(title, payload):
    button = {  "type": "postback",
                "title": title,
                "payload": payload }
    return button

def button_item_template_url(title, url):
    button = {  "type": "web_url",
                "title": title,
                "url": url }
    return button

def button_item_template_message_url(title, url):
    button = {  "type": "web_url",
                "title": title,
                "url": url }
    return button

def button_item_template_message_payload(title, payload):
    button = {  "type": "postback",
                "title": title,
                "payload": payload }
    return button

def element_template_message(title, subtitle, item_url, image_url, buttons):
    item = { 
        "title": title,
        "subtitle": subtitle,
        "item_url": item_url,
        "image_url": image_url,
        "buttons": buttons
    }
    return item

def template_message_generic(recipient_id, elements):
    message_data = {
        "recipient":{ "id":recipient_id},
        "message":{
            "attachment":
                {
                    "type":"template",
                    "payload":
                    {
                        "template_type": "generic",
                        "elements": elements
                    }
                }
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
                    "url":url
                }
            }
        }
    }   
    return message_data

def video_message(recipient_id, url):
    message_data = {
        "recipient":{ "id":recipient_id},
        "message":{
            "attachment":{
                "type":"video",
                    "payload":{
                        "url": url
                    }
                }
        }
    }   
    return message_data

def audio_message(recipient_id, url):
    message_data = {
        "recipient":{ "id": recipient_id},
        "message":{
        "attachment":{
            "type":"audio",
                "payload":{
                    "url": url
                }
            }
        }
    }   
    return message_data


def file_message(recipient_id, url):
    message_data = {
        "recipient":{ "id": recipient_id},
        "message":{
        "attachment":{
            "type":"file",
                "payload":{
                    "url": url
                }
            }
        }
    }   
    return message_data
