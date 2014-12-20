# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from bs4 import BeautifulSoup
from xml.dom.minidom import parse
import xml.dom.minidom
from mongodb import MongoDB
from Tools.extra_methods import ExtraMethods


class RSSReader(object):

	def __init__(self):
		self.info = []
		self.config = {'pravda.com.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'fulltext', 'link1':'pdalink','link2':'link'},
'tyzhden.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'fulltext', 'link1':'pdalink','link2':'link'},
'censor.net':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'fulltext', 'link1':'link','link2':'guid'},
'eizvestia.com':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'fulltext', 'link1':'link','link2':'guid'},
'nbnews.com.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'non','content':'description', 'link1':'link','link2':'guid'},
'vchaspik.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'non', 'link1':'link','link2':'guid'},
'radiosvoboda.org':{'items':'item','pubdate':'pubdate','title':'title','description':'non','content':'description', 'link1':'link','link2':'guid'},
'kp.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'ultramir.net':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'yandex:full-text', 'link1':'link','link2':'NON'},
'cursorinfo.co.il':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'yandex:full-text', 'link1':'link','link2':'NON'},
'intell.in.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'yandex:full-text', 'link1':'link','link2':'NON'},
'racurs.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'unian.net':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'galinfo.com.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'zik.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'guid'},
'24tv.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'guid'},
'obozrevatel.com':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'vkulake.com':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'yandex:full-text', 'link1':'link','link2':'NON'},
'newsoboz.org':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'fulltext', 'link1':'link','link2':'NON'},
'galnet.org':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'content:encoded', 'link1':'link','link2':'guid'},
'gazeta.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'description', 'link1':'link','link2':'guid'},
'dsnews.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'fulltext', 'link1':'link','link2':'guid'},
'1.crimea.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'yandex:full-text', 'link1':'link','link2':'guid'},
'politica-ua.com':{'items':'item','pubdate':'pubdate','title':'title','description':'yandex:full-text','content':'NON', 'link1':'link','link2':'NON'},
'real-vin.com':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'guid','link2':'link'},
'charter97.org':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'gazetavv.com':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'fulltext', 'link1':'link','link2':'NON'},
'vesti-ukr.com':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'yandex:full-text', 'link1':'link','link2':'NON'},
'rbc.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'fulltext', 'link1':'link','link2':'guid'},
'glavnoe.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'yandex:full-text', 'link1':'link','link2':'NON'},
'glavcom.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'NON','content':'fulltext', 'link1':'link','link2':'guid'},
'unn.com.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'joinfo.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'NON'},
'focus.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'yandex:full-text', 'link1':'link','link2':'guid'},
'comments.ua':{'items':'item','pubdate':'pubdate','title':'title','description':'description','content':'NON', 'link1':'link','link2':'guid'},

}

	def read_rss(self, link, configs):
		config = self.config[configs]
		data_available = {'pubtime':False,'title':False,'content':False,'link':False, 'link1':False}
		content = ''.encode('utf8')
		soup = BeautifulSoup(requests.get(link).content)
		items = soup.findAll(config["items"])
		for i in items:
			data = []
			new_soup = BeautifulSoup(str(i))
			
			#reading publication time
			try:
				pubtime = new_soup.find(config['pubdate']).text
				data_available['pubtime'] = True
			except AttributeError:
				pubtime = "".encode('utf8')
		
			#reading article title
			try:
				title = new_soup.find(config['title']).text
				data_available['title'] = True
			except AttributeError:
				title = "".encode('utf8')
			#reading artile description
			try:
				content = new_soup.find(config['description']).text
			except AttributeError:
				content = ''.encode('utf8') 
			#reading article content
			try:
				content = content + new_soup.find(config['content']).text
				data_available['content'] = True
			except AttributeError:
				content = content + ''.encode('utf8') 
			#reading article link
			try:
				link = new_soup.find(config['link1']).text
				data_available['link'] = True
			except AttributeError:
				link = ''.encode('utf8')
			try:
				link2 = new_soup.find(config['link2']).text
				data_available['link1'] = True
			except AttributeError:
				link2 = ''.encode('utf8')


			data = [pubtime,title,content,link,link2,data_available]
			# print 'pubtime: '.encode('utf8') + str(data[0].encode('utf8'))
			# print 'title: '.encode('utf8') + str(data[1].encode('utf8'))
			# print 'content: '.encode('utf8') + str(data[2].encode('utf8'))
			# print 'link: '.encode('utf8') + str(data[3].encode('utf8'))
			# print 'link1: '.encode('utf8') + str(data[4].encode('utf8'))
			# print data_available
			self.info.append(data)
		return self.info

# RSSReader().read_rss('http://www.pravda.com.ua/rss/view_news/','pravda.com.ua')
# RSSReader().read_rss('http://tyzhden.ua/RSS/News/','tyzhden.ua')
# RSSReader().read_rss('http://censor.net.ua/includes/news_ru.xml','censor.net')
# RSSReader().read_rss('http://eizvestia.com/rss/rss.xml','eizvestia.com')
# RSSReader().read_rss('http://nbnews.com.ua/ru/rss/','nbnews.com.ua')
# RSSReader().read_rss('http://r.vchaspik.ua/rss_news.xml','vchaspik.ua')
# RSSReader().read_rss('http://www.radiosvoboda.org/api/zrqiteuuir','radiosvoboda.org')
# RSSReader().read_rss('http://kp.ua/rss/feed.xml','kp.ua')
# RSSReader().read_rss('http://ultramir.net/rss.xml','ultramir.net')
# RSSReader().read_rss('http://cursorinfo.co.il/rss/index.rss','cursorinfo.co.il')
# RSSReader().read_rss('http://intell.in.ua/publ/rssya/','intell.in.ua')
#too many links on racurs
# RSSReader().read_rss('http://ua.racurs.ua/rss/ua/polityka.xml','racurs.ua')
# RSSReader().read_rss('http://ua.racurs.ua/rss/ua/ekonomika.xml','racurs.ua')
# RSSReader().read_rss('http://ua.racurs.ua/rss/ua/syspilstvo.xml','racurs.ua')
# RSSReader().read_rss('http://ua.racurs.ua/rss/ua/all.xml','racurs.ua')
# RSSReader().read_rss('http://rss.unian.net/site/news_ukr.rss','unian.net')
# RSSReader().read_rss('http://zik.ua/ua/rss/export.rss','zik.ua')
# RSSReader().read_rss('http://24tv.ua/rss/all.xml','24tv.ua')
# RSSReader().read_rss('http://obozrevatel.com/rss.xml','obozrevatel.com')
# RSSReader().read_rss('http://vkulake.com/feed/yandex/','vkulake.com')
# RSSReader().read_rss('http://newsoboz.org/static/rss/newsline.rss.xml','newsoboz.org')
# RSSReader().read_rss('http://galnet.org/feed','galnet.org')
# RSSReader().read_rss('http://gazeta.ua/rss','gazeta.ua')
# RSSReader().read_rss('http://www.dsnews.ua/static/rss/newsline.rss.xml','dsnews.ua')
# RSSReader().read_rss('http://1.crimea.ua/rss/blogs/all/feed.rss','1.crimea.ua')
# RSSReader().read_rss('http://politica-ua.com/?feed=news.yandex.ru','politica-ua.com')
# RSSReader().read_rss('http://real-vin.com/feed','real-vin.com')
# RSSReader().read_rss('http://www.charter97.org/ru/rss/all/','charter97.org')
# RSSReader().read_rss('http://static.gazetavv.com/rss/newsline.rss.xml','gazetavv.com')
# RSSReader().read_rss('http://vesti-ukr.com/feed/53-glavnye-vesti-strany.rss','vesti-ukr.com')
# RSSReader().read_rss('http://www.rbc.ua/static/rss/topnews.rus.rss.xml','rbc.ua')
# RSSReader().read_rss('http://www.rbc.ua/static/rss/topnews.economic.rus.rss.xml','rbc.ua')
# RSSReader().read_rss('http://www.rbc.ua/static/rss/topnews.politics.rus.rss.xml','rbc.ua')
# RSSReader().read_rss('http://glavnoe.ua/rss/newsall.xml','glavnoe.ua')
# RSSReader().read_rss('http://glavcom.ua/rss.xml','glavcom.ua')
# RSSReader().read_rss('http://www.unn.com.ua/rss/news_uk.xml','unn.com.ua')
# RSSReader().read_rss('http://joinfo.ua/rss/main.xml','joinfo.ua')
# RSSReader().read_rss('http://focus.ua/modules/rss.php','focus.ua')
# RSSReader().read_rss('http://comments.ua/export/rss_ru.xml','comments.ua')

data = RSSReader().read_rss('http://focus.ua/modules/rss.php','focus.ua')
# print '\n\ndata_received!!!\n\n'
# for i in data:
# 	# print "Original:".encode('utf8') + str(i[2].encode('utf8')) 
# 	print ExtraMethods().remove_tags(i[2].encode('utf8'))
# 	print '\n\n'



database = MongoDB()
for item in data:
	db_query = database.makeArticleInfoQuery(item)
	if database.verifyQueryIsReady(db_query):
		database.writeArticleInfo(db_query)
	else:
		print 'Error item#' + str(data.index(item))

database.printDB()



#need to resolve decode issue http://galinfo.com.ua/rss/export.rss

