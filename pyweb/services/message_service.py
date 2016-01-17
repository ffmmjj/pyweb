from ..models.message import Message

class MessageService():
	db = None

	def __init__(self, database):
		self.db = database

	def load_messages_by_login(self, login):
		collection = self.db.Messages.find({'user': login})
		if collection.count() > 0:
			document = collection[0]
			user = Message(document['id'])
			user.first_name = document['first_name']
			user.last_name = document['last_name']
			user.email = document['email']
			user.password = document['password']
			return user
		else:
			return User('')

	def create(self, message):
			json_data = message.to_json()
			self.db.Messages.insert(json_data)			