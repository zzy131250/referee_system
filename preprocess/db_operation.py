# encoding=utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId


class Mongo:

    def __init__(self):
        client = MongoClient()
        self.db = client.referee_system

    def set_collection(self, name):
        self.collection = self.db[name]

    def insert_one(self, data):
        self.collection.insert_one(data)

    def insert_many(self, data):
        self.collection.insert_many(data)

    def find_data(self, condition, no_cursor_timeout=False):
        return self.collection.find(condition, no_cursor_timeout=no_cursor_timeout)

    def delete_by_id(self, id):
        self.collection.delete_one({'_id': ObjectId(id)})

    def delete_by_key_value(self, condition):
        self.collection.delete_one(condition)