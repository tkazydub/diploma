# -*- coding: utf-8 -*-
from __future__ import unicode_literals


links = ['http://mediainfo.mk.ua/news/v_nikolaevskom_zooparke_rodilsja_malysh_amurskogo_tigra_foto/2014-10-21-25539',
'http://obozrevatel.com/politics/83425-blok-poroshenko-opredelilsya-s-kandidatom-po-okrugu-16.htm',
'http://nr2.com.ua/News/politics_and_society/Poroshenko-predlagaet-razreshit-otzyv-deputatov-82785.html',
'http://www.unn.com.ua/uk/news/1398276-o-novak-rosiya-ukrayina-i-yes-u-bryusseli-pidtverdili-milanski-domovlenosti-po-gazu']



import requests
re = requests.get(links[0])
response = re.text
with open('response_from_link.txt','w') as f:
	f.write(response.encode('utf8'))

a = ['<div style="float:right;font-size:9px;">21:59 </div>', '<time datetime="2014-10-21T21:50:20+03:00" pubdate>', '<time>21 Ð¾ÐºÑÑÐ±ÑÑ 2014, 21:42</time>','<span itemprop="datePublished" content="2014-10-21T21:50">Вівторок, 21 жовтня 2014, 21:50</span>'] 
