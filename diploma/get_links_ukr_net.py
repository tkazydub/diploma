# -*- coding: utf-8 -*-


from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import sqlite3 as lite
import codecs


class GetLinksUkrNet(object):

	#when we have multiple sources
	def getInfoArrayFromMultipleSources(self, html, title_for_sources = None):
		soup = BeautifulSoup(html)
		duplicates = soup.findAll('div', {"class":"dublicates"})

		if len(duplicates)>0:
			overal_info = []
			if title_for_sources:
				new_title = title_for_sources
			else:
				new_title = soup.findAll('a')[0].text.encode('utf8')
			overal_info.append(new_title)
			for i in duplicates:
				info = []
				new_soup = BeautifulSoup(str(i))
				for j in new_soup.findAll('span', {"class":"date"}):
					title = j.text
					info.append(title.encode('utf8'))
				for j in new_soup.findAll("a", title=True):
					info.append(j['title'].encode('utf8'))
				for j in new_soup.findAll("a", href=True):
					info.append(j['href'].encode('utf8'))
				overal_info.append(info)
		return overal_info


	# for single article
	def getInfoArray(self, html, title_for_sources=None):
		soup = BeautifulSoup(str(html))
		parse_data = []
		if title_for_sources:
			new_title = title_for_sources
		else:
			new_title = soup.findAll('div',{"class":"item-title"})[0].text.encode('utf8')
		parse_data.append(new_title)
		for i in soup.findAll('div', {"class":"tabele-cell"}):
			parse_data.append(i.text.encode('utf8'))
		parse_data.append(soup.findAll('div',{"class":"item-title"})[0].text.encode('utf8'))
		for i in soup.findAll('a', href = True):
			parse_data.append(i['href'].encode('utf8'))
		return parse_data


	#when we have multiple news from different sources
	def getLinkForMultipleNews(self, html):
		soup = BeautifulSoup(html)
		amount = soup.findAll('a', {"class":"amount"})
		if len(amount)>0:
			link = soup.findAll("a", href=True)[0]['href']
			if '//www.' not in str(link):
				link = 'http://www.' + str(link)[2:]
			elif 'http:' not in str(link):
				link = 'http:' + str(link)
				print "Link:" + str(link)
			else:
				link = str(link)
		return link

	def getTitleForMultipleNews(self, html):
		soup = BeautifulSoup(html)
		amount = soup.findAll('a', {"class":"amount"})
		if len(amount)>0:
			title = soup.findAll("a")[0].text
		return title.encode('utf8')

class GetNewsItemsUkrNet(object):
	
	def getNewsItems(self,link):
		r = requests.get(link)
		response = str(r.content)
	
		new_response = BeautifulSoup(response).findAll('div', {"class": "news-items"})
		soup = BeautifulSoup(str(new_response))
		divs = soup.findAll('div', {"class":"item"})
		return divs