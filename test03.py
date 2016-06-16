# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
request=urllib2.Request("http://www.im.nuk.edu.tw/zh-TW/professors/teachers.html")
response=urllib2.urlopen(request)
html=response.read()
soup=BeautifulSoup(html)
for pro in soup.select('.groupPrimary'):
	print pro.select('.catItemTitle')[0].text
	
