#!/usr/bin/env python3
"""
Finds schools that offer a specific topic.
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
  """
  Retrieves a list of documents (schools) from the 
  provided pymongo collection object
  that have the specified "topic" in their "topics" list.

  Args:
      mongo_collection (pymongo.collection.Collection): 
      The pymongo collection object.
      topic (str): The topic to search for in 
      the schools' "topics" lists.

  Returns:
      list: A list of dictionaries representing 
      the matching school documents.
  """
  # Find documents with the topic in their "topics" list (case-insensitive)
  cursor = mongo_collection.find({"topics": {"$regex": topic, "$options": "i"}})

  # Convert the cursor to a list for easier iteration
  return list(cursor)
