#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def insert_school(mongo_collection, **kwargs):
    """Insert new data in school collection"""
    return mongo_collection.insert(kwargs)
