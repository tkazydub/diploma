# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)

db = client.test_database

db.countries.insert({"name": "Ukraine", "code":"UA", "lol":'asd'})
query = db.countries.find()
# eid = query.up_id
for post in query:
	print post
# print eid