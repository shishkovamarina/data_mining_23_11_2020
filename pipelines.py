from pymongo import MongoClient


class GbParsePipeline:

    def __init__(self):
        self.db = MongoClient()['headhunters']

    def process_item(self, item, spider):

        collection = self.db[spider.name]
        collection.insert_one(item)
        return item