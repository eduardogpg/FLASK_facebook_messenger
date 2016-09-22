import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	VERIFY_TOKEN = 'my_scret_token'
	PAGE_ACCESS_TOKEN = 'EAAZAIjk0fM4sBAIosYFHrPMMnP1B6bU58YgzKHZCh2CJYWr1qTGb9eUick5BYVLXNA745CNd57U7bactmxnUuVZA7O1ZCDGrz4RLJmlKZBcMMRXPONb4Er0keZBhYKeFrN1Wn5ZC53ZBYXOGTCZBALhAboPF2afYAobAT6w6x165ZAH4dH4L7BgbyE'

class DevelopmentConfig(Config):
	DEBUG = True	
