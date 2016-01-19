import json

class FileChunk():

    def __init__(self, id, fileId, user, data, position):
        self._id = id
        self.fileId = fileId
        self.user = user
        self.data = data
        self.position = position

    def to_json(self):
        return json.loads(json.dumps(self.__dict__))

    def __cmp__(self, other):
        if hasattr(other, 'position'):
            return self.position.__cmp__(other.position)