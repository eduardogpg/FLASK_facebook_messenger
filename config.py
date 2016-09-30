import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN') or 'EAASJNooj21kBAOuozwFuhW99MFQ0VHktGxsY7wrtLw4k8PZBfOBW1nRXWRZBUi9e09dZBSq6ee8zh51zmTOULOZBmnziqT1XZCsSxtNcn1WSkNyBvv0ZCOQQRcwfsUytSkTgp5aGPCYXsjLXafHSA7ZBGg2kfiMDucfbp6ZBmMfUGwZDZD'

class DevelopmentConfig(Config):
	DEBUG = True	
