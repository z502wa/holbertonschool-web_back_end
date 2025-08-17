#!/usr/bin/env python3
"""
Nginx logs stats.
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        # لازم tab بالضبط \t
        print(f"\tmethod {method}: {count}")

    # status check
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")
