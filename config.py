import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	VERIFY_TOKEN = 'my_scret_token'
	PAGE_ACCESS_TOKEN = 'EAAY5GGpEFxUBAKLcZA240PU2f5brYWaPlrI9U2xroXdHoGUvkVsKNvDdpRKLhkd1SSDTO11XLlDWIZBxYmp0kckAx0weI4fnvkEGzMhasPzZC6ZAHK1zKb8frVZAP7N0RbBqJVz5z7CPnuJsFRmKWHhBk21BOSREOv7eNT8J4d716gvu9dMZAr'

class DevelopmentConfig(Config):
	DEBUG = True	
