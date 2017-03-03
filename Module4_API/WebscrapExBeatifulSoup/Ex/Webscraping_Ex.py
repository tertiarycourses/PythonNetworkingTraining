
import requests
import pprint
from bs4 import BeautifulSoup

from urllib.request import urlopen

redditFile =urlopen('http://www.google.com')
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml, "lxml")
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))

