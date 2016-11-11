import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKENS') or 'EAAFd4CHXgCQBAD5XYqaQ5ZCYIq2xKImst9tL5VedxpSXlt0tva8gt0QpQ43HAZARHBbFgbZAONzdh0OYKZAHezMX0TAIi8VIr0ZA8CMim6tZBX82QVva4ZBSPuN6ZAs4Vem6tNIJugzmR0v2ptmCZCKT0KfDi8Ihri3WrWp3ZBP2ZAVUQZDZD'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	
