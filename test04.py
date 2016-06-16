# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
request=urllib2.Request("http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=1000&format=xml")
response=urllib2.urlopen(request)
html=response.read()
soup=BeautifulSoup(html)
for data in soup.select('data'):
	
	print data.select('sitename')[0].text
	print data.select('county')[0].text
	print data.select('pm2.5')[0].text
