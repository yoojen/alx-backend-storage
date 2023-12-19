#!/usr/bin/env python3
"""Operates on imported mongodb dump file"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ prints some stats from Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collections = client.logs.nginx

    total_docs = nginx_collections.count_documents({})
    print(f"{total_docs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('Methods:')
    for method in methods:
        count = nginx_collections.count_documents({"method": method})
        print(f'\tmethod {method} : {count}')
    status = nginx_collections.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f'{status} status check')
