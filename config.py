import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN') or 'EAAFLRYo5sXoBAKuQ5dnSYyeaQgaUAKz38B7g4eJH2iIDqSleHff1HawBjG7yETRp546QMJ7q4j54cHGoC1uiwtKzjUHpXIgCZA6zhTV7LdYIR5HSb5bPeBPmLl9qOvnuOS2Tp3DTy74ZBwy0gdMPfNmL4aMtWXurUBcgUL5QZDZD'

class DevelopmentConfig(Config):
	DEBUG = True	
