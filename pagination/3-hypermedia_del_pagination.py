#!/usr/bin/env python3
"""
Nginx logs stats printer.

Connects to MongoDB (logs.nginx) and prints:
- total logs count
- count per HTTP method (GET, POST, PUT, PATCH, DELETE)
- count of status checks (method=GET and path=/status)
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # total logs
    total = collection.count_documents({})
    print(f"{total} logs")

    # per method
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # status check
    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")
