# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import sqlite3 as lite
import codecs
from get_links_ukr_net import GetLinksUkrNet, GetNewsItemsUkrNet




class ParseResults(object):
	def __init__(self):
		self.resulting_array = []


	def getLinks(self, link, title_for_sources=None):
		items = GetNewsItemsUkrNet()
		get_items = items.getNewsItems(link)
		get_links_from_items = GetLinksUkrNet()

		for i in get_items:
			if len(BeautifulSoup(str(i)).findAll('div', {"class":"dublicates"})) > 0:
				self.resulting_array.append(get_links_from_items.getInfoArrayFromMultipleSources(str(i), title_for_sources))
			elif len(BeautifulSoup(str(i)).findAll('a', {"class":"amount"})) > 0 :
				new_link = get_links_from_items.getLinkForMultipleNews(str(i))
				title_for_sources = get_links_from_items.getTitleForMultipleNews(str(i))
				self.getLinks(new_link, title_for_sources)
			else:
				self.resulting_array.append(get_links_from_items.getInfoArray(str(i), title_for_sources))
		return self.resulting_array			

	def writeLinksToFile(self,res_array,file_name):
		# ff =open('res_array.txt', "w")
		# ff.write(str(res_array))
		# open(file_name, "w")
		f = open(file_name,"a")
		for i in range(0,len(res_array)):
			if type(res_array[i][1]) == list:
				for j in range(1, len(res_array[i])):
					# print str(res_array[i][0])
					f.write(str(res_array[i][0]) + ';'.encode('utf8'))
					for k in range(0, len(res_array[i][j])):
						# print res_array[i][j][k]
						f.write(str(res_array[i][j][k]) + ';'.encode('utf8'))
					f.write('\n')
			else:
				for j in range(0,len(res_array[i])):
					# print res_array[i][j]
					f.write(str(res_array[i][j]) + ';'.encode('utf8'))
				f.write('\n')

	def write_to_db(self, db_name, res_array):
		conn = lite.connect(db_name)
		with conn:
			cursor = conn.cursor()
			
			cursor.execute("SELECT MAX(id) FROM Topic")
			max_topic_id = cursor.fetchall()[0][0]
			if max_topic_id:
				topic_id = int(max_topic_id) + 1
			else:
				topic_id = 1

			cursor.execute("SELECT MAX(id) FROM Source")
			max_article_id = cursor.fetchall()[0][0]
			if max_article_id: 
				article_id = int(max_article_id) + 1
			else:
				article_id = 1
			
			for i in range(len(res_array)):
				if type(res_array[i][1]) == list:
					# print "1st: {0}:".format(str(res_array[i][0].decode('utf8')))
					# r_a = str(res_array[i][0]).replace("'","\'")
					query = "INSERT INTO Topic VALUES({0}, '{1}')".format(topic_id, res_array[i][0])
					# query = "INSERT INTO Topic VALUES(".encode('utf8') + str(topic_id).encode('utf8') + ", \'".encode('utf8') + str(res_array[i][0].encode('utf8')) + "\')".encode('utf8')
					cursor.execute(query)
					for j in range(1, len(res_array[i])):
						query = "INSERT INTO Source VALUES({0}, {1}, '{2}', '{3}', '{4}')".format(article_id, topic_id, res_array[i][j][1], res_array[i][j][2], res_array[i][j][0])
						cursor.execute(query)
						article_id+=1
					topic_id +=1
				else:
					# print "2nd: {0}".format(str(res_array[i][0].decode('utf8')))
					# r_a = str(res_array[i][0]).replace("'","\'")
					query = "INSERT INTO Topic VALUES({0}, '{1}')".format(topic_id, res_array[i][0])
					# query = "INSERT INTO Topic VALUES(".encode('utf8') + str(topic_id).encode('utf8') + ", \'".encode('utf8') + str(res_array[i][0].encode('utf8')) + "\')".encode('utf8')
					cursor.execute(query)
					query = "INSERT INTO Source VALUES({0}, {1}, '{2}', '{3}', '{4}')".format(article_id, topic_id, res_array[i][0], res_array[i][2], res_array[i][1])
					cursor.execute(query)
					article_id+=1
					topic_id+=1
			conn.commit()


link = "https://www.ukr.net/news/politika.html"
res = ParseResults()
links = res.getLinks(link)
res.writeLinksToFile(links, "test_results.csv")










# res.write_to_db('parse_results_lol.db',links)

# conn = lite.connect('parse_results_lol.db')
# cursor=conn.cursor()
# # cursor.execute("delete from Topic")
# # cursor.execute('Delete from Source')
# # conn.commit()
# cursor.execute('Select * from Topic')
# rows = cursor.fetchall()
# print "Topic:"
# for row in rows:
# 	print row

# print '\n\nSource:'

# cursor.execute('Select * from Source')
# rows = cursor.fetchall()
# for row in rows:
# 	print row