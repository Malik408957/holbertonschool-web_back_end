#!/usr/bin/env python3
"""
Python function that changes all topics of a school document
"""

def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name
    
    Args:
        mongo_collection: pymongo collection object
        name: school name to update
        topics: list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},  # Filter: name-ə görə tap
        {"$set": {"topics": topics}}  # Update: topics-i dəyiş
    )
