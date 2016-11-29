import json
import requests

def get_data():
	data = { 
					'setting_type': 'call_to_actions',
					'thread_state': 'new_thread', 
					'call_to_actions' : [ { "payload":"USER_DEFINED_PAYLOAD" } ] #
				}
	return data

def call_set_started_button(token):
	res = requests.post('https://graph.facebook.com/v2.6/me/thread_settings',
								params={ 'access_token': token},
                data = json.dumps( get_data() ),
                headers={'Content-type': 'application/json'})

	if res.status_code == 200:
		print(json.loads(res.text))

def call_delete_started_button(token):
	res = requests.delete('https://graph.facebook.com/v2.6/me/thread_settings',
								params={ 'access_token': token},
                data = json.dumps( get_data() ),
                headers={'Content-type': 'application/json'})

	if res.status_code == 200:
		print(json.loads(res.text))

def call_send_API(data, token):
  res = requests.post('https://graph.facebook.com/v2.6/me/messages',
              params={ 'access_token': token},
              data= json.dumps( data ),
              headers={'Content-type': 'application/json'})

  if res.status_code == 200:
      print "Mensaje enviado exitosamente!"
  
def call_user_API(user_id, token):
  res = requests.get('https://graph.facebook.com/v2.6/'+ user_id, 
          params={ 'access_token': token} )
  data = json.loads(res.text)
  return data

def call_geosname_API(lat, lng, username):
  res = requests.get('http://api.geonames.org/findNearByWeatherJSON', 
      params={ 'lat': lat, 'lng': lng, 'username': username }   )

  if res.status_code == 200:
      res = json.loads(res.text)

      city = res['weatherObservation']['stationName']
      temperature = res['weatherObservation']['temperature']
      return {'city': city, 'temperature': temperature }
