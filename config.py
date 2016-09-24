import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	VERIFY_TOKEN = 'my_scret_token'
	PAGE_ACCESS_TOKEN = 'EAAPyXlO5u5UBAAzMMTUc5YF4CYTliDiOmQu9hmtcqLJyZAzoje9iZAHA7SHWQigR2qV4WPG6b48kawplb4cWDDb1UcKhBMKpVADeYtD1abPwKZASM7yDi3jB0UhBcqBzS0xo9lqmnFGRy0U6vLnOZAIpF18NHcYt9IHJZARgx8wZDZD'

class DevelopmentConfig(Config):
	DEBUG = True	
