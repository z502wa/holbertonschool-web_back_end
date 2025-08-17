#!/usr/bin/env python3
"""
Nginx logs stats printer.

Connects to MongoDB (logs.nginx) and prints:
- total logs count
- count per HTTP method (GET, POST, PUT, PATCH, DELETE)
- count of status checks (method=GET and path=/status)

Output format must match the project example exactly.
"""

from pymongo import MongoClient


def print_nginx_stats() -> None:
    """
    Print stats for the 'logs.nginx' collection exactly as required.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total = collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        cnt = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {cnt}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    print_nginx_stats()
