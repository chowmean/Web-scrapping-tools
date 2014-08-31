from bs4 import BeautifulSoup
import urlparse
import cookielib
from cookielib import CookieJar
import urllib2 as urllib

cj=CookieJar()
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))
opener.addheader= [('User-agent','Mozilla/5.0')]

html= urllib.urlopen("http://nytimes.com")
soup= BeautifulSoup(html)

for tags in soup.findAll('h2',href=False):  #add tags you want to read
	print str(tags)
