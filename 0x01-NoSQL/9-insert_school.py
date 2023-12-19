#!/usr/bin/env python3
    """Insert new data in school collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert new data in school collection"""
    return mongo_collection.insert_one(kwargs)
