import urllib2 as urllib
from bs4 import BeautifulSoup
import urlparse
import cookielib
from cookielib import CookieJar

cj=CookieJar()
opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))
opener.addheader= [('User-agent','Mozilla/5.0')]

html= urllib.urlopen("http://nytimes.com")
soup= BeautifulSoup(html)

for tags in soup.findAll('a',href=True):
	raw= tags['href']
	hostname= urlparse.urlparse(tags['href']).hostname
	path=urlparse.urlparse(tags['href']).path
	print "http://"+str(hostname)+str(path)
	#new= "http://"+str(hostname)+str(path)
	#page=str(new)
        #sourceCode=opener.open(page).read()
        #print (sourceCode)
	
	
