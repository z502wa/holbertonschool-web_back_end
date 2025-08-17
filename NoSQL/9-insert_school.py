#!/usr/bin/env python3
"""
Module that provides a function to insert a new document
into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.
        **kwargs: Key-value pairs representing the document fields.

    Returns:
        ObjectId: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
