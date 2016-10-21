import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEYS') or 'my_secret_key'
	PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN') or 'EAANYGKG7ZAMABALZArMOeZBn82TbbGZB4dLsGTVwx1U3L8cZBQJaGBiZAZCmwL9LLytNVxpZAOeHWF94PYhOUD2qHiVoRxIMu2ArHGZAC6H4ZCWXyt32GplcSzi2V4AsMcaq2OHqtHcuZBfoPgsNbavUKO8sGCxRIyTvuZBnBP6fG2RrCgZDZD'
	USER_GEOSNAME = os.environ.get('USER_GEOSNAME') or 'eduardo_gpg'

class DevelopmentConfig(Config):
	DEBUG = True	

"""
https://developers.facebook.com/docs/graph-api/reference/user/picture/
http://findfacebookid.com/
"""