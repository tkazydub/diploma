# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pymongo import MongoClient
from Tools.extra_methods import ExtraMethods

class MongoDB(object):

	def __init__(self):
		client = MongoClient('localhost', 27017)
		self.db = client.test_database
		## creating indexes
		self.db['article_info'].create_index(
			[
				('title','text'),
				('content','text'),
				('link1','text')
			]
			)


	# Info format: [pubtime, title, content, link1, link2, completeness]
	def makeArticleInfoQuery(self,info):
		insert_query = {}
		try:
			insert_query['pubdate'] = info[0]
		except IndexError:
			insert_query['pubdate'] = False
		try:
			insert_query['title'] = info[1]
		except IndexError:
			insert_query['title'] = False
		try:
			insert_query['content'] = ExtraMethods().remove_tags(info[2].encode('utf8'))
		except IndexError:
			insert_query['content'] = False
		try:
			insert_query['link1'] = info[3]
		except IndexError:
			insert_query['link1'] = False
		try:
			insert_query['link2'] = info[4]
		except IndexError:
			insert_query['link2'] = False
		try:
			insert_query['completeness'] = info[5]
		except IndexError:
			insert_query['completeness'] = False
		return insert_query

	def verifyQueryIsReady(self,query):
		if len(query)>0:
			is_ready = True
			for key in query:
				if not query[key]:
					is_ready = False
		else:
			is_ready = False
		return is_ready

	def writeArticleInfo(self, art_info):
		self.db.article_info.insert(art_info)

	def printDB(self):
		for i in self.db.article_info.find():
			result_string = ''.encode('utf8')
			for key in i:
				if key != '_id' and key != 'completeness':
					result_string += str(i[key].encode('utf8')) + "; ".encode('utf8')
			print result_string
			# print [key for key in i]

			# print str(i['pub_date'].encode('utf8')) + "; ".encode('utf8') + str(i['article'].encode('utf8')) + "; ".encode('utf8') + str(i['name'].encode('utf8'))


	def findElementFromAI(self, val):
		collection = self.db.article_info
		return collection.find_one(val)

	def getNumberOfMatchingElemets(self,val=None):
		collection = self.db.article_info
		return collection.find(val).count()

	def findElements(self, collection, val=None):
		coll = self.db[collection]
		return coll.find(val)

	def findElemetByWord(self,collection,word):
		coll = self.db[collection]
		return coll.find({'$text':{'$search':word}})	

		# for i in collection.find({'$text':{'$search':word}}):	
		# 	result_string = ''.encode('utf8')
		# 	for key in i:
		# 		if key != '_id' and key != 'completeness':
		# 			result_string += str(i[key].encode('utf8')) + "; ".encode('utf8')
		# 	print result_string	


# data_base = MongoDB()
# print data_base.findElementFromAI({'link1':'http://focus.ua/country/321326/'})
# print data_base.getNumberOfMatchingElemets()
# el = data_base.findElementsFromAI({'link1':'http://focus.ua/country/321326/'})
# for i in el:
# 	print i

# res = data_base.findElemetByWord('article_info','ДНР'.encode('utf8'))
# print res
# for i in res:
# 	print i
# data_base.printDB()