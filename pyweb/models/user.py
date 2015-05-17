from flask_login import UserMixin
import json

class User(UserMixin):
    id = ""
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, id):
        self.id = id

    def to_json(self):
    	return json.loads(json.dumps(self.__dict__))