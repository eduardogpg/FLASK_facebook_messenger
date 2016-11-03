import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKENS') or 'EAADDadiPqXQBAAiCECanhEc7a771lkUo4lrZAmq529oIqLkMhmZAmoZCWwGwGBsfOnowymqImaugpRsjv3pGpRvUIt4bU8pgbgsEdKUOzwXSzVH4OCaCNrmuTM6HzRmykioJuLEYCdW59BCG9vZBfbneUP7CyObbcHM6MVwXH7CLjVYDkiDv'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	
