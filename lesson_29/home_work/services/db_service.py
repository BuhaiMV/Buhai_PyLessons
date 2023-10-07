from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Maks:123456Pass@cluster0.sfxhonn.mongodb.net/?retryWrites=true&w=majority"


class DataBase:
    def __init__(self):
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.weather_db = self.client.get_database('sample_weatherdata')
        self.data_collection = self.weather_db.get_collection('data')

    def get_data_from_db(self, data_id):
        return self.data_collection.find_one(data_id)

    def add_to_db(self, data):
        return self.data_collection.insert_one(data)

    def update_in_db(self, data_id, data):
        return self.data_collection.replace_one({'_id': data_id}, data)
