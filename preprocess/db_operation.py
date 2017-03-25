# encoding=utf-8
from pymongo import MongoClient


class Mongo:

    def __init__(self):
        client = MongoClient()
        self.db = client.referee_system

    def set_collection(self, name):
        self.collection = self.db[name]

    def insert_data(self, data):
        self.collection.insert_many(data)

    def find_data(self, condition):
        return self.collection.find(condition)