#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    
    # Köhnə count() metodu
    total_logs = collection.count()
    print("{} logs".format(total_logs))
    
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.find({"method": method}).count()
        print("method {}: {}".format(method, count))
    
    status_check = collection.find({"method": "GET", "path": "/status"}).count()
    print("{} status check".format(status_check))
