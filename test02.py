# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
request = urllib2.Request("http://140.127.218.250:44/david/")
response = urllib2.urlopen(request)
html = response.read()

soup=BeautifulSoup(html)
#print "soup.title:",soup.title
#print "soup.center:",soup.center
#print "soup.title.string:",soup.title.string
#print "soup.title.parent.name:",soup.title.parent.name
#print "soup.a:",soup.a
#print "soup.find_all:",soup.find_all('a')
#for link in soup.find_all('a'):
       	#print(link.get('href'))
print soup.text
print(soup.prettify())
