#!/usr/bin/env python3
"""
Module that provides a function to update the topics
of a school document in a MongoDB collection.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the school name.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        name (str): The school name to update.
        topics (list of str): The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
