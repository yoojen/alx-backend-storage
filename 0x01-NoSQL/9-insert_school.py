#!/usr/bin/env python3


def insert_school(mongo_collection, **kwargs):
    """Insert new data in school collection"""
    return mongo_collection.insert(kwargs)
