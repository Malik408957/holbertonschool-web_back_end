#!/usr/bin/env python3
"""
Python function that returns the list of school having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Find all schools that have a specific topic
    
    Args:
        mongo_collection: pymongo collection object
        topic: topic to search for
    
    Returns:
        List of schools that have the specified topic
    """
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
