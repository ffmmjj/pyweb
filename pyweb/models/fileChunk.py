import json

class FileChunk():

    def __init__(self, id, fileId, fileUser, fileData):
        self._id = id
        self.fileId = fileId
        self.user = fileUser
        self.data = fileData

    def to_json(self):
        return json.loads(json.dumps(self.__dict__))