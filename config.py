import os

class Config(object):
	SECRET_KEY = 'my_secret_key'
	VERIFY_TOKEN = 'my_scret_token'
	PAGE_ACCESS_TOKEN = 'EAAERYS5Wty4BACvRWHofwZBMX9ArVJNOyaudEjN6vDT2cgxndamvfCgl9QmXObvEka61eZAlT3XJrARIrGiMqRjXWmHeI8BFhb7WiVxlvHDs3XZCSxM1uZC00IyYgTxZCmmfO9yuC7QhxW6nZCbPmBuv3ZAeN0AZAfJWGSBVkSbfkq3QtmKiq2ty'

class DevelopmentConfig(Config):
	DEBUG = True	
