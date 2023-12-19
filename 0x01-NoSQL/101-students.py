#!/usr/bin/env python3
"""returns sorted list of students according to average scores"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """returns sorted list of students according to average scores"""
    return mongo_collection.aggregate([
        {"$project": {
            "_id": "$name", "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
