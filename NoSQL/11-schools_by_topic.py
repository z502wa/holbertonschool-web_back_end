#!/usr/bin/env python3
"""
Module that provides a function to find all schools
having a specific topic in a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find all schools having a specific topic.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        topic (str): The topic to search for.

    Returns:
        list: A list of school documents matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
