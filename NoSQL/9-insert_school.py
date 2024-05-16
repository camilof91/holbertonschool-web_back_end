#!/usr/bin/env python3
''' inserts a new document in a collection based on kwargs
'''
import pymongo


def insert_school(mongo_collection, **kwargs):
  """
  Inserts a new document into the provided pymongo collection object based on keyword arguments.

  Args:
      mongo_collection (pymongo.collection.Collection): The pymongo collection object.
      **kwargs (dict): Keyword arguments representing the document fields.

  Returns:
      ObjectId: The ObjectId of the newly inserted document, or None if insertion fails.
  """
  return mongo_collection.insert_one(kwargs).inserted_id
