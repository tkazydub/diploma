# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urlparse, xml.etree.ElementTree
import re
from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.encode('utf8').join(self.fed)


class ExtraMethods(object):
	def get_link_body(self, link):
		return urlparse.urlparse(link).hostname

	def remove_tags(self,html):
		s = MLStripper()
		try:
			s.feed(html)
		except UnicodeDecodeError:
			pass
		return s.get_data()



# text = '''<p>Доллар США вечером в пятницу, 28 ноября, впервые в истории превысил отметку в 50 рублей.</p> <p>На единой тарифной сессии Московской межбанковской валютной биржи (ММВБ) вечером за американскую валюту давали 50,28 рубля. Тем самым доллар по сравнению с уровнем закрытия торгов накануне подорожал на 1,5 рубля, пишет <a href="http://www.dw.de/9/a-18100927" target="_blank">DW</a>.</p> <p>В свою очередь евро подорожал на 1,6 рубля - до 62,52 рубля.</p> <p>С начала текущего года курс доллара США к рублю вырос в полтора раза. За последние три месяца рубль ослаб более чем на 25% по отношению к доллару. Эксперты прямо связывают обвал курса рубля с падением цен на нефть. Последние резко упали после того, как 27 ноября страны-участницы ОПЕК решили оставить квоту на добычу этого сырья на прежнем уровне, составляющем 30 млн баррелей в сутки.</p>'''
# print ExtraMethods().remove_tags(text.encode('utf8'))