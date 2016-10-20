import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN') or 'EAAEXNLPXgL0BAOrEBuKMYeiDtYEyokd5ZBZAc0igUP1OZBAyOqNW0C7cEjTLfrkZAwokIqE47auOFG2boTX0jPeQVymsnV6eXMzWBeO15axfZAPiXcsePDvV2tNYIYGk2Q0n0WOTYZCDKZCiwap0nCdpLG5DAYGnCoHlQBgbi8sZBgZDZD'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	

"""
https://developers.facebook.com/docs/graph-api/reference/user/picture/
http://findfacebookid.com/
"""