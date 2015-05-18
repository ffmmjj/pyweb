from pymongo import MongoClient
from config import Config

class MongoInit():

	def __init__(self):
		pass

	def initialize(self):
		if (Config.MONGODB_USERNAME and Config.MONGODB_PASSWORD):
			mongodb_uri = str.format('mongodb://{0}:{1}@{2}:{3}/{4}', Config.MONGODB_USERNAME, Config.MONGODB_PASSWORD, Config.MONGODB_HOST, Config.MONGODB_PORT, Config.MONGODB_DB)
		else:
			mongodb_uri = str.format('mongodb://{0}:{1}/', Config.MONGODB_HOST, Config.MONGODB_PORT)
		client = MongoClient(mongodb_uri)
		db = client[Config.MONGODB_DB]
		return db