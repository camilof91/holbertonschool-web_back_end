#!/usr/bin/env python3
''' Python function that lists all documents in a collection'''
import pymongo


def list_all(mongo_collection):
  """
  Lists all documents in a provided pymongo collection object.

  Args:
      mongo_collection (pymongo.collection.Collection): The pymongo collection object.

  Returns:
      list: A list containing all documents from the collection, or an empty list if the collection is empty.
  """
  if not mongo_collection:
    return []
  else:
    return list(mongo_collection.find())
