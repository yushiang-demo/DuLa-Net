import pymongo
from bson import ObjectId
from api.constant import TASK_STATUS

class DB():
    def __init__(self, url):
        client = pymongo.MongoClient(url)
        db = client.dulanet
        self.task_collection = db.task

    def getTask(self, id):
        try:
            filter_criteria = {
                '_id': ObjectId(id),
                "status": {"$ne": TASK_STATUS.REMOVED}
            }
            result = self.task_collection.find_one(filter_criteria)
            return result
        except:
            return None

    def createTask(self, path):
        object_id = ObjectId()
        self.task_collection.insert_one({
            '_id': object_id,
            'status': TASK_STATUS.PROCESSING,
            'images': {
                'origin': f'{path}/{object_id}/image.jpg',
                'preview': f'{path}/{object_id}/vis.jpg',
                'aligned': f'{path}/{object_id}/raw.jpg',
            },
            'layout':{
                'data': None
            }
        })
        return str(object_id)
        
    def updateTask(self, id, data):
        try:
            filter_criteria = {'_id': ObjectId(id)}
            update_data = {
                '$set': data
            }
            result = self.task_collection.update_one(filter_criteria, update_data)
            return result.modified_count > 0
        except:
            return None

    def getTasks(self):
        all_documents = self.task_collection.find({})
        return list(all_documents)


db = DB('mongodb://root:example@mongo:27017/')