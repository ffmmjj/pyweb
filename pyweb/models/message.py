import json

class Message():    

    def __init__(self, id, fileId, content, subject, sender, to, user):
        self._id = id
        self.fileId = fileId
        self.content = content
        self.subject = subject
        self.sender = sender
        self.to = to
        self.user = user

    def to_json(self):
        return json.loads(json.dumps(self.__dict__))