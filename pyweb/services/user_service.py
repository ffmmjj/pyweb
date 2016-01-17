from ..models.user import User

class UserService():
	db = None

	def __init__(self, database):
		self.db = database

	def load_user_by_login(self, login):
		collection = self.db.Users.find({'id': login})
		if collection.count() > 0:
			document = collection[0]
			user = User(document['id'])
			user.first_name = document['first_name']
			user.last_name = document['last_name']
			user.email = document['email']
			user.password = document['password']
			return user
		else:
			return None
	
	def load_all_users(self):
		users = [u for u in self.db.Users.find()]
		return users

	def initialize_users(self):
		users = self.db.Users

		if users.count() == 0:
			user = User('valid_user')
			user.first_name = 'system'
			user.last_name = 'admin'
			user.email = 'admin@yummybox.com'
			user.password = 'valid_password'
			json_data = user.to_json()
			self.db.Users.insert(json_data)