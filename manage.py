#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

from config import DevelopmentConfig
from handler import received_message

import json

__author__ = 'Eduardo Ismael García Pérez'
__lastupdated__ = '2016 September 23'


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/', methods=['GET'])
def index():
	return 'Welcome to Mrs. Bot with Flask!'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	if request.method == 'GET':
		verify_token = request.args.get('hub.verify_token', '')
		if verify_token == app.config['SECRET_KEY']:
			return request.args.get('hub.challenge', '')
		return 'Error, wrong validation token'
	
	elif request.method == 'POST':
		payload = request.get_data()
		data = json.loads(payload)
			
		for page_entry in data['entry']:
			for message_event in page_entry['messaging']:
				if "message" in message_event:
					received_message(message_event, app.config['PAGE_ACCESS_TOKEN'])
						
		return "ok"

if __name__ == '__main__':
	app.run(port = 8000)

