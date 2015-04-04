from flask_login import UserMixin

class User(UserMixin):
    id = ""
    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, id):
        self.id = id