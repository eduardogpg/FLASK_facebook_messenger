import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN') or 'EAAZAHkkZA6qWABABWRbsvmBCaelVucgAynrAehgAbJuWAuKOLzqy1dnY0rho6rctTMzoVSilYTQY0U2SYvizwD7IDYndquBAVLsNPZCchSg4tBaRf0c81KgvZBGbBx64C0m1vxcIS8WhlaVbXgebh1ZB7rMlNZAB6OhcgNjLydCQZDZD'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	

"""
https://developers.facebook.com/docs/graph-api/reference/user/picture/
http://findfacebookid.com/
"""