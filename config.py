import os
from pymongo import read_preferences

def get_from_env(environment_variable, default_value=None):
	var = os.environ.get(environment_variable, default_value)
	return var

class Config(object):
    DEBUG = get_from_env('DEBUG', False)
    TESTING = get_from_env('TESTING', False)
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    MONGODB_HOST = get_from_env('MONGODB_HOST', 'localhost')    
    MONGODB_USERNAME = get_from_env('MONGODB_USERNAME', '')
    MONGODB_PASSWORD = get_from_env('MONGODB_PASSWORD', '')
    MONGODB_DB = get_from_env('MONGODB_DB', 'yummybox')
    MONGODB_PORT = get_from_env('MONGODB_PORT', '27017')
    MONGODB_READ_PREFERENCE = read_preferences.ReadPreference.PRIMARY