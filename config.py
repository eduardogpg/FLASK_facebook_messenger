import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKENS') or 'EAAEnoMJ8LxgBAHkemioduWDaSSbZAofehZCZCVCXuSFK6qa0FEvyZCIZCDM10qYwXsIlZAuNiaLQv7rwJBwCYHdBNO0Ggw1pKiWbS8kjQlIInnhOn8ZBrU2oRG7U2ublZBFQG5HOAxEVLMCfa3d8tcTBtY6VXiOZAr1tFQDHCIMJGggZDZD'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	
