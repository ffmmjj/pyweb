import json

class Message():
    id = ""
    fileId = ""
    content = ""
    subject = ""
    sender = ""
    to = ""
    user = ""

    def __init__(self, id):
        self.id = id

    def to_json(self):
        return json.loads(json.dumps(self.__dict__))