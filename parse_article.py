# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from bs4 import BeautifulSoup


#Getting article text and publication date
class ParseArticleInfo(object):

	#get publication date, article name and artilce text from telegraf.com.ua
	def fromTelegraf(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))
		
		date_published = soup.findAll('span', {'itemprop':'datePublished'})[0].text.encode('utf8')
		article_name = soup.findAll('h2')[0].text.encode('utf8')
		article_content = soup.findAll('div',{"class":"article-content"})[1].text.encode('utf8')
		
		return [str(date_published),str(article_name), str(article_content)]	
	
	#get publication date, article name and artilce text from unian.ua
	def fromUnian(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))
		
		date_published = soup.findAll('div', {'class':'date'})[0].text.encode('utf8')
		article_name = soup.findAll('h1', {'itemprop':'headline'})[0].text.encode('utf8')
		article_content = soup.findAll('h2')[0].text.encode('utf8')
		for i in soup.findAll('p'):
			article_content += i.text.encode('utf8')
		
		return [str(date_published),str(article_name),str(article_content)]
	
	#get publication date, article name and artilce text from glavnoe.ua
	def fromGlavnoe(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.findAll('div', {'class':'newsdate'})[0].text.encode('utf8') + '|'.encode('utf8') + soup.findAll('div', {'class':'newstime'})[0].text.encode('utf8')
		article_name = soup.findAll('div', {'class':'newstitle'})[0].text.encode('utf8')
		article_content = soup.findAll('div', {'class':'newstext'})[0].text.encode('utf8')
		
		return [str(date_published),str(article_name),str(article_content)] 


	#get publication date, article name and artilce text from obozrevatel.com
	def fromObozrevatel(self,link):
		#need to resolve encoding issue
		pass


	#get publication date, article name and artilce text from 24tv.ua
	def from24TV(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.findAll('span', {'class':'news-date'})[0].text.encode('utf8')
		article_name = soup.findAll('h1', {'class':'title-news'})[0].text.encode('utf8')		
		article_content = soup.findAll('h3')[0].text.encode('utf8')
		for i in soup.findAll('p'):
			article_content += i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#get publication date, article name and artilce text from statuspress.com.ua
	def fromStatuspress(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))
				#!!!need to review this part
		date_published = soup.findAll('div', {'class':'postFooter'})[0].text.encode('utf8')
		#!!!need to review this part
		article_name = soup.findAll('h1')[0].text.encode('utf8')
		article_content = soup.findAll('div', {'class':'post _ga1_on_'})[0].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#get publication date, article name and artilce text from pravda.com.ua
	def fromPravda(self,link):
		#available for pda links only!!! (e.g. http://pda.pravda.com.ua/news/id_7043643/)
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.findAll('div', {'class':'date1'})[0].text.encode('utf8')
		article_name = soup.findAll('b')[0].text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in soup.findAll('p'):
			article_content += i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 
	
	#get publication date, article name and artilce text from censor.net.ua
	def fromCensor(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('time', {'class':'published dateline'}).text.encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		article_content = soup.findAll('div', {'class':'text'})[0].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 	
	
	#get publication date, article name and artilce text from unn.com.ua
	def fromUNN(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('span', {'itemprop':'datePublished'})['content'].encode('utf8')
		article_name = soup.find('h1', {'class':'title'}).text.encode('utf8')
		article_content = soup.find('div', {'itemprop':'articleBody'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#get publication date, article name and artilce text from interfax.com.ua
	def fromInterfax(self,link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('span', {'itemprop':'datePublished'}).text.encode('utf8')
		article_name = soup.find('h1', {'class':'article-content-title'}).text.encode('utf8')
		article_content = soup.find('div', {'class':'article-content'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#get publication date, article name and artilce text from segodnya.ua
	def fromSegodnya(self,link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('span', {'itemprop':'datePublished'}).text.encode('utf8')
		article_name = soup.find('span', {'itemprop':'name'}).text.encode('utf8')
		article_content = soup.find('h2').text.encode('utf8') + '\n'.encode('utf8') + soup.find('span', {'class':'_ga1_on_'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 
		
	#get publication date, article name and artilce text from zaxid.net
	def fromZaxid(self,link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('span', {'class':'date'}).text.encode('utf8')
		article_name = soup.find('h1', {'class':'title'}).text.encode('utf8')
		article_content = soup.find('span',{'id':'newsSummary'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#get publication date, article name and artilce text from espreso.tv
	def fromEspreso(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.findAll('div', {'class':'date'})[0].text.encode('utf8') + '|'.encode('utf8') +  soup.findAll('div', {'class':'time date'})[0].text.encode('utf8')
		article_name = soup.findAll('title')[0].text.encode('utf8')
		article_content = soup.find('div',{'class':'first text-page'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 
	
	#get publication date, article name and artilce text from gordonua.com
	def fromGordon(self,link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('div', {'class':'a_footer'}).text.encode('utf8')
		article_name = soup.findAll('h1', {'class': 'a_head'})[0].text.encode('utf8')
		article_content = soup.findAll('div',{'class':'a_description'})[0].text.encode('utf8') + soup.find('div',{'class':'text _ga1_on_'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	def fromTSN(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('span', {'class':'date'}).text.encode('utf8')
		article_name = soup.findAll('h1', {'class': 'title'})[0].text.encode('utf8')
		article_content = soup.findAll('h2', {'itemprop':'alternativeHeadline'})[0].text.encode('utf8') +soup.findAll('div',{'id':'news_text'})[0].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 
		
	#expres.ua
	def fromExpres(self,link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('div', {'class':'field-item odd'}).text.encode('utf8')
		article_name = soup.findAll('h1', {'class': 'title'})[0].text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in BeautifulSoup(str(soup.findAll('div', {'class':'node-content'}))).findAll('p'):
			article_content +=i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#tvi.ua
	def fromTVI(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('div', {'class':'date'}).text.encode('utf8')
		article_name = soup.findAll('h1', {'class': 'article-title'})[0].text.encode('utf8')
		article_content = soup.findAll('div', {'class':'article-description'})[0].text.encode('utf8')
		for i in BeautifulSoup(str(soup.findAll('div', {'class':'article-content'}))).findAll('p'):
			article_content +=i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 
		
	#glavred.info
	def fromGlavred(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('span', {'class':'date_time'}).text.encode('utf8')
		article_name = soup.findAll('h1', {'class': 'title'})[0].text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in BeautifulSoup(str(soup.findAll('div', {'class':'article_body'}))).findAll('p'):
			article_content +=i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#rbc.ua
	def fromRBC(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('time', {'itemprop':'datePublished'}).text.encode('utf8')
		article_name = soup.findAll('h1', {'itemprop': 'name'})[0].text.encode('utf8')
		article_content = soup.findAll('div', {'class': 'text _ga1_on_'})[0].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#focus.ua
	def fromFocus(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('div', {'class':'author-date-holder'}).text.encode('utf8')
		article_name = soup.findAll('title')[0].text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in BeautifulSoup(str(soup.findAll('div', {'class':'content-card'}))).findAll('p'):
			article_content +=i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#Gazeta.ua
	def fromGazetaUA(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))

		date_published = soup.find('div', {'class':'pull-right news-date'}).text.encode('utf8')
		article_name = soup.findAll('h1')[0].text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in BeautifulSoup(str(soup.findAll('section', {'class': 'article-content clearfix'}))).findAll('p'):
			article_content +=i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#fakty.ictv.ua
	def fromICTV(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))
		date_published = soup.find('div', {'class':'date'}).contents[2].encode('utf8')
		article_name = soup.findAll('h1')[0].text.encode('utf8')
		article_content = soup.findAll('div', {'class': 'text'})[0].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#tyzhden.ua
	def fromTyzhden(self,link):
		r = requests.get(link)	
		soup = BeautifulSoup(r.text.encode('utf8'))
		date_published = soup.find('div', {'class':'bf4'}).contents[0].text.encode('utf8')
		article_name = soup.findAll('h1', {'class':'ap5'})[0].text.encode('utf8')
		article_content = soup.findAll('div', {'class': 'bf1'})[0].text.encode('utf8')
		for i in BeautifulSoup(str(soup.findAll('div', {'class': 'bf3 ap2 _ga1_on_'}))).findAll('p'):
			article_content +=i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#ukrinform.ua
	def fromUkrinform(self, link):
		r = requests.get(link)	
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		
		date_published = soup.find('div', {'class':'date'}).text.encode('utf8')
		article_name = soup.findAll('h1')[0].text.encode('utf8')
		html = html[:html.find('<div class="article_info">'.encode('utf8'))]
		soup = BeautifulSoup(html)
		article_content = ''.encode('utf8')
		for i in soup.findAll('p'):
			article_content += i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 
		

	#kp.ua
	def fromKP(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('a', {'class':'meta__date'}).text.encode('utf8')
		article_name = soup.findAll('h1')[0].text.encode('utf8')
		article_content = soup.find('div', {'class':'content'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#day.kiev.ua
	def fromDayKiev(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('div', {'class':'node_date'}).text.encode('utf8')
		article_name = soup.findAll('h1', {'class':'title'})[0].text.encode('utf8')
		article_content = soup.find('div', {'class':'field-item even'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#bbc.co.uk
	def fromBBCUkraine(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = 'No time!'
		article_name = soup.findAll('h1', {'class':'story-body__h1'})[0].text.encode('utf8')
		article_content = soup.find('div', {'class':'story-body__inner'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#joinfo.ua
	def fromJoinfo(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('meta', {'property':'article:published_time'})['content'].encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		article_content = soup.find('div', {'class':'content _ga1_on_'}).contents[0].encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#vchaspik.ua
	def fromVchaspik(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('span', {'class':'submitted'}).contents[2].encode('utf8')
		article_name = soup.find('h1',{'class':'title'}).text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in BeautifulSoup(str(soup.find('div',{'class':'content clearfix _ga1_on_'}))).findAll('p'):
			article_content += i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#depo.ua
	def fromDepoUA(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		new_soup = BeautifulSoup(str(soup.find('div',{'class':'publication'})))

		date_published = new_soup.find('span', {'class':'metadate'}).contents[0].encode('utf8')
		article_name = new_soup.find('h1').text.encode('utf8')
		article_content = new_soup.find('div', {'class':'publication-text'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#ipnews.in.ua
	def fromIPnews(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		# new_soup = BeautifulSoup(str(soup.find('div',{'class':'publication'})))

		date_published = soup.find('div', {'class':'blog-date'}).text.encode('utf8')
		article_name = soup.find('h1', {'class':'blog-title'}).text.encode('utf8')
		article_content = soup.find('div', {'class':'blog-content'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#newsoboz.org
	def fromNewsOboz(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		new_soup = BeautifulSoup(str(soup.find('div',{'class':'articl'})))

		date_published = new_soup.find('div', {'class':'data'}).contents[0].encode('utf8')
		article_name = new_soup.find('h1', {'class':'title-block'}).text.encode('utf8')
		new_soup = BeautifulSoup(str(soup.find('div',{'class':'pubBody _ga1_on_'})))
		article_content = ''.encode('utf8')
		for i in new_soup.findAll('p'):
			article_content += i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#eizvestia.com
	def fromEizvestia(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('div', {'id':'postDate'}).text.encode('utf8')
		article_name = soup.find('h1', {'id':'postTitle'}).text.encode('utf8')
		html = str(r.text.encode('utf8'))
		html = html[html.find('<div class="border">'.encode('utf8')):]
		new_html = html[html.find('<div class="border">'.encode('utf8')):html.find('<div class="postFooter">'.encode('utf8'))]
		new_soup = BeautifulSoup(str(new_html))
		article_content = ''.encode('utf8')
		for i in new_soup.findAll('p'):
			article_content += i.text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#pic.com.ua
	def fromPIC(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published =  "No time!"#soup.find('div', {'class':'tdate'}).text.encode('utf8')
		article_name = soup.find('h2', {'class':'title'}).text.encode('utf8')
		article_content = soup.find('div', {'class':'entry _ga1_on_'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#news.finance.ua
	def fromNewsFinance(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('time', {'pubdate':'pubdate'})['datetime'].encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		article_content = soup.find('div', {'class':'news-body'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#capital.ua
	def fromCapital(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('div', {'class':'b-news-stat'}).contents[0].text.encode('utf8')
		article_name = soup.find('h1', {"class":"title"}).text.encode('utf8')
		article_content = soup.find('div', {'class':'b-static-text b-newsfull-text clear'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

		
	#radiosvoboda.org
	def fromRadiosvoboda(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('p', {'class':'article_date'}).text.encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		html = str(r.text.encode('utf8'))
		html = html[:html.find('<tbody>'.encode('utf8'))]
		article_content = BeautifulSoup(str(html)).find('div', {'class':'zoomMe'}).text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#nr2.com.ua
	def fromNR2(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('time')['datetime'].encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		article_content = soup.find('h2').text.encode('utf8')
		for i in range(1, len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#uainfo.org
	def fromUAInfo(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		soup = BeautifulSoup(str(soup.find('article', {'class':'article'})))

		date_published = soup.find('time').text.encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in range(1, len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#slovoidilo.ua
	def fromSlovoiDilo(self, link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		soup = BeautifulSoup(str(soup.find('div', {'class':'publish-info'})))

		date_published = soup.find('div', {'class':'date'}).text.encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#btbtv.com
	def fromBtbTv(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		soup = BeautifulSoup(str(soup.find('div', {'class':'b-static-text'})))

		date_published = soup.find('div', {'class':'b-news-date'}).text.encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#7dniv.info
	def from7Dniv(self,link):
		r=requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		date_published = soup.find('meta', {'property':'article:published_time'})['content'].encode('utf8')
		article_name = soup.find('h1',{'class':'title'}).text.encode('utf8')
		
		new_soup = BeautifulSoup(str(soup.findAll('div',{'class':'field-items'})[1]))
		article_content = ''.encode('utf8')
		for i in range(len(new_soup.findAll('p'))-1):
			article_content+= ' '.encode('utf8') + new_soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#politica-ua.com
	def fromPoliticaUA(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('span', {'class':'meta_date'}).text.encode('utf8')
		date_published = date_published[30:]
		article_name = soup.find('h1',{'class':'entry-title'}).text.encode('utf8')
		soup = BeautifulSoup(str(soup.find('div',{'class':'post_content entry-content'})))
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))-2):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#nvua.net
	def fromNVUA(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		soup = BeautifulSoup(str(soup.find('article', {'class':'article'})))

		date_published = soup.find('time')['datetime'].encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		soup = BeautifulSoup(str(soup.find('div',{'class':'body'})))
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#forbes.ua
	def fromForbesUA(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('div',{'class':'time2'}).text.encode('utf8')
		article_name = soup.find('h1',{'class':'title2'}).text.encode('utf8')
		soup = BeautifulSoup(str(soup.find('div',{'class':'text_box'})))
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#gazetavv.com
	def fromGazetaVV(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('div',{'class':'data'}).contents[2].encode('utf8')
		article_name = soup.find('h1',{'class':'title-block'}).text.encode('utf8')
		soup = BeautifulSoup(str(soup.find('div',{'class':'text'})))
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))-3):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#novosti.dn.ua
	def fromNovostiDN(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('span',{'class':'dt_title'}).text.encode('utf8')
		article_name = soup.find('h1',{'class':'content_news_h1'}).text.encode('utf8')
		soup = BeautifulSoup(str(soup.find('font',{'class':'content_detail'})))
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


	#dailylviv.com
	def fromDailyLviv(self,list):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))
		date_published = soup.find('p',{'class':'date'}).text.encode('utf8')
		article_name = soup.find('h1').text.encode('utf8')
		soup = BeautifulSoup(str(soup.find('div',{'class':'description'})))
		article_content = ''.encode('utf8')
		for i in range(len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 

	#112.ua
	def from112UA(self,link):
		r = requests.get(link)
		soup = BeautifulSoup(str(r.text.encode('utf8')))

		date_published = soup.find('span',{'class':'date'}).text.encode('utf8')
		article_name = soup.find('h1',{'class':'title'}).text.encode('utf8')
		article_content = soup.find('h2',{'class':'descr'}).text.encode('utf8')
		soup = BeautifulSoup(str(soup.find('div',{'id':'news_text'})))
		for i in range(len(soup.findAll('p'))):
			article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
		return [str(date_published),str(article_name),str(article_content)] 


link = 'http://ua.112.ua/golovni-novyni/sogodni-v-zoni-ato-zaginuv-1-viyskovosluzhbovec-i-4-poraneno-atc-144947.html'

# r = requests.get(link)
# soup = BeautifulSoup(str(r.text.encode('utf8')))
# # # # # # soup = BeautifulSoup(str(soup.find('article', {'class':'article'})))

# date_published = soup.find('span',{'class':'date'}).text.encode('utf8')
# print date_published

# article_name = soup.find('h1',{'class':'title'}).text.encode('utf8')
# print article_name

# article_content = soup.find('h2',{'class':'descr'}).text.encode('utf8')
# soup = BeautifulSoup(str(soup.find('div',{'id':'news_text'})))
# for i in range(len(soup.findAll('p'))):
# 	article_content+=' '.encode('utf8') + soup.findAll('p')[i].text.encode('utf8')
# print article_content

# html = str(r.text.encode('utf8'))
# html = html[html.find('<div class="border">'.encode('utf8')):]
# new_html = html[html.find('<div class="border">'.encode('utf8')):html.find('<div class="postFooter">'.encode('utf8'))]
# new_soup = BeautifulSoup(str(new_html))
# article_content = ''.encode('utf8')
# for i in new_soup.findAll('p'):
# 	article_content += i.text.encode('utf8')
# print article_content




# article_content = ''.encode('utf8')
# for i in BeautifulSoup(str(soup.find('div',{'class':'content clearfix _ga1_on_'}))).findAll('p'):
# 	article_content += i.text.encode('utf8')
# print article_content



# html = html[:html.find('<div class="article_info">'.encode('utf8'))]
# soup = BeautifulSoup(html)
# article_content = ''.encode('utf8')
# for i in soup.findAll('p'):
# 	article_content += i.text.encode('utf8')
# print article_content


# article_content = soup.findAll('div', {'class': 'bf1'})[0].text.encode('utf8')
# for i in BeautifulSoup(str(soup.findAll('div', {'class': 'bf3 ap2 _ga1_on_'}))).findAll('p'):
# 	article_content +=i.text.encode('utf8')
# print article_content



# with open('result.txt', 'w') as f:
# 	f.write(r.text.encode('utf8'))

# res = GetArticleInfo().from112UA(link)
# print res[0]
# print res[1]
# print res[2]