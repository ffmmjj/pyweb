import json

class Message():    

    def __init__(self, id, fileId, originalContent, content, subject, sender, date, user):
        self._id = id
        self.fileId = fileId
        self.originalContent = originalContent
        self.content = content
        self.subject = subject
        self.sender = sender
        self.date = date
        self.user = user

    def to_json(self):
        return json.loads(json.dumps(self.__dict__))