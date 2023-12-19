#!/usr/bin/env python3
"""update documents in mongodb collection"""


def update_topics(mongo_collection, name, topics):
    """update documents in collection"""
    mongo_collection.update_one({"name": name}, {'$set': {"topics": topics}})
