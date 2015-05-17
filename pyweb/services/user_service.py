from pymongo import MongoClient
from ..models.user import User

class UserService():
	db = None

	@staticmethod
	def connect_db():
		client = MongoClient('localhost')
		UserService.db = client.yummybox		

	@staticmethod
	def load_user_by_login(login):
		return {'username':'valid_user', 'password':'valid_password'}
	
	@staticmethod
	def load_all_users():
		UserService.connect_db()
		users = [u for u in UserService.db.Users.find()]
		return users

	@staticmethod
	def initialize_users():
		UserService.connect_db()
		users = UserService.db.Users

		if users.count() == 0:
			user = User('valid_user')
			user.first_name = 'system'
			user.last_name = 'admin'
			user.email = 'admin@yummybox.com'
			user.password = 'valid_password'
			json_data = user.to_json()
			UserService.db.Users.insert_one(json_data)