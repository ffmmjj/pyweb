from ..models.fileChunk import FileChunk
import uuid

class FileService():
    db = None

    def __init__(self, database):
        self.db = database

    def load_files_by_login(self, user):
        collection = self.db.Files.find({'user': user})
        if collection.count() > 0:
            document = collection[0]
            fileChunk = File(document['_id'])            
            return user
        else:
            return User('')

    def getChunksByFileId(self, fileId):
        collection = self.db.FileChunks.find({'fileId': fileId})
        if collection.count() > 0:
            result = []
            for document in collection:
                result.append(FileChunk(document['_id'], document['fileId'], document['user'], document['data'], document['position']))
            return result
        else:
            return None

    def __save(self, fileChunk):                
        if fileChunk._id is None:
            fileChunk._id = str(uuid.uuid1())
            json_data = fileChunk.to_json()
            self.db.FileChunks.insert_one(json_data)
        else:
            json_data = fileChunk.to_json()
            self.db.FileChunks.replace_one({'_id': fileChunk._id}, json_data)

    def processFileChunk(self, id, fileId, fileUser, chunkData, chunkPosition):
        fileChunk = FileChunk(id, fileId, fileUser, chunkData, chunkPosition)

        self.__save(fileChunk)

        return fileChunk