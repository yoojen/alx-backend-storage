#!/usr/bin/env python3

def schools_by_topic(mongo_collection, topic):
    """returns list of documents which matches the topic"""
    return mongo_collection.find({"topics": {"$in": [topic]}})
