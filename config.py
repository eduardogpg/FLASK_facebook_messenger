import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKENS') or 'EAADHS13mCc8BAFKZBsPZBlFqO397aD8ndXnT9W6INmeOTqPRZBDdI0eLdMzkmLZC8M2t93yw9DZATG33K292qWVNNlZCt44csKP9gSNLoqIxRxbcEjO8TwyoVvRJZCIY1lK6ygHwZB1fCbmmuVuXLpyMGZBOCmiKAGqQtRzxdZCytyfPTU9KTiNjjk'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	
