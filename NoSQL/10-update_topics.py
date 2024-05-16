#!/usr/bin/env python3
"""changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
  """
  Updates the "topics" field for all documents in the provided pymongo collection object
  that match the specified "name".

  Args:
      mongo_collection (pymongo.collection.Collection): The pymongo collection object.
      name (str): The name of the school document to update.
      topics (list): The new list of topics to set for the matching documents.

  Returns:
      int: The number of documents that were updated.
  """
  # Update many documents with the specified filter and update criteria
  update_result = mongo_collection.update_many(
      {"name": name},
      {"$set": {"topics": topics}}
  )

  # Return the number of updated documents (modified_count)
  return update_result.modified_count