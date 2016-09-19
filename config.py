import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	VERIFY_TOKEN = 'my_scret_token'
	PAGE_ACCESS_TOKEN = 'EAACzsB3nkAIBADk6MPZC5dQcUqzOaZB4S9POQr5kpFmYEv4HfjwrIhH0yA8ynlzK919K7zNfJ1n1DnF97OwGzlin6aX48ZCXE2a5LPkzPu4yzZCwbxd9ZBlClkBdmprqLQOBW2F110xlTy5FFejJyZAzGhcBqiU2uCeEHhZCcvq0xZA4dAhzZCDFc'

class DevelopmentConfig(Config):
	DEBUG = True	
