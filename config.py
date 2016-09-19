import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	VERIFY_TOKEN = 'my_scret_token'
	PAGE_ACCESS_TOKEN = 'EAARSKyrJT5sBAEWy2ClXVPeplpe5IsbbB8Njl6WestqAclR9KmNvZAvlZBoOZBXdSYCz0Bs9qnyhDx8zZCMOYZBSoFZCQ6rEZA0k5NEssJ925O0xkqZAWyZBmEG6jGU8aGTrRP8Kz1YexFXT42pnNlFHqOJoxfDZBcjk7QQ9TZCsDEZAFFbug8P3v335'

class DevelopmentConfig(Config):
	DEBUG = True	
