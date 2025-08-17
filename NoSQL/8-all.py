#!/usr/bin/env python3
"""
Module that provides a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    List all documents in the given collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection.

    Returns:
        list: A list of documents (empty list if no document is found).
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
