import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKENS') or 'EAAEyM9wOnnIBAMZBt1oT7p0IgZBRa7k6tsU1Xst0llXAfOFIBYko5GnUN7TQujpyM6yEH2tCk5ZAByjSwhF2cVeSEx7iXvXFgfHuUyknJfkWS7X8ZCNZBqFuN05hxS2LIX28M2Hc61UiKURHmEX9NZCmMRGPWcbTZAeHJhjH12PI8ufMZCnCuiZAp'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	
