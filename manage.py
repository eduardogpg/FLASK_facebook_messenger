from flask import Flask
from flask import request

from config import DevelopmentConfig
from messenger import received_message

import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

def validate_verify_token(request):
	if request.args.get('hub.verify_token', '') == app.config['VERIFY_TOKEN']:
		return request.args.get('hub.challenge', '')
	return 'Error, wrong validation token'

@app.route('/', methods=['GET'])
def index():
	return 'Bienvenido al bot con Flaks!'

@app.route('/verify', methods=['GET', 'POST'])
def verify():
	if request.method == 'GET':
		return validate_verify_token(request)
	
	elif request.method == 'POST':
		payload = request.get_data()
		data = json.loads(payload)
			
		for page_entry in data['entry']:
			page_id = page_entry['id']
			time_of_event = page_entry['time']
			
			for message_event in page_entry['messaging']:
				if "message" in message_event:
					received_message(message_event, app.config['PAGE_ACCESS_TOKEN'])
						
		return "ok"

if __name__ == '__main__':
	app.run(port = 3000)