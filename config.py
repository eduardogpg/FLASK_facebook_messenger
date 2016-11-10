import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKENS') or 'EAAOy7GNeZBxwBACFLhnZA1WPz8Y15GOzaPmhZBYyZArWYxeKWdjpLBypUEjajFPNjBZCfiDHtEFOHHNzLMiSmNexAZAe9AFZA7YswZBa8AtcMPfaGZAZCrjVm35BtpzPcHJGJYp2ZBwFvWWCDTG2ZBjOTbu0fPL1WJPTXoUVmiPZC1laCwQZDZD'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	
