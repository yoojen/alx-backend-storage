#!/usr/bin/env python3
"""list all documents from mongodb collection"""
from typing import List


def list_all(mongo_collection) -> List:
    """list all documents from mongo collection"""
    if mongo_collection.count_documents({}) == 0:
        return []
    return mongo_collection.find()
