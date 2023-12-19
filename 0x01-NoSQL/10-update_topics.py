#!/usr/bin/env python3

def update_topics(mongo_collection, name, topics):
    """update documents in collection"""
    mongo_collection.update_one({"name": name}, {'$set': {"topics": topics}})
