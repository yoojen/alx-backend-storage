#!/usr/bin/env python3
"""returns sorted list of students according to average scores"""


def top_students(mongo_collection):
    """returns sorted list of students according to average scores"""
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name", "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
