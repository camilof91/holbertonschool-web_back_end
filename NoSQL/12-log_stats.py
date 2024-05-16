#!/usr/bin/env python3
"""
Analyzes Nginx logs stored in MongoDB and displays statistics.
"""

import pymongo


def analyze_logs(mongo_client, db_name, collection_name):
  """
  Analyzes the provided MongoDB collection 
  containing Nginx logs and displays statistics.

  Args:
      mongo_client (MongoClient): The MongoClient 
      object for interacting with MongoDB.
      db_name (str): The name of the database containing 
      the logs collection.
      collection_name (str): The name of the collection 
      containing the Nginx logs.
  """

  # Connect to the database and collection
  db = mongo_client[db_name]
  collection = db[collection_name]

  # Get total number of logs
  total_logs = collection.count_documents({})

  # Print total logs stat
  print(f"{total_logs} logs")

  # Define methods to count (considering case-insensitivity)
  methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
  method_counts = {method.lower(): collection.count_documents(
      {"method": {"$regex": method, "$options": "i"}}
  ) for method in methods}

  # Print method stats
  print("Methods:")
  for method, count in method_counts.items():
    print(f"\tmethod {method.upper()}: {count}")

  # Count status checks (specifically for path="/status")
  status_checks = collection.count_documents({"path": "/status"})

  # Print status check stat
  print(f"{status_checks} status check")


if __name__ == "__main__":
  # Replace with your MongoDB connection details
  mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
  # Modify connection string as needed
  db_name = "logs"
  collection_name = "nginx"

  analyze_logs(mongo_client, db_name, collection_name)