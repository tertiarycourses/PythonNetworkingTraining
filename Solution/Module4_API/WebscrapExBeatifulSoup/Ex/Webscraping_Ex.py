import requests
import pprint
from bs4 import BeautifulSoup

#download HTML doc
#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get("http://www.google.com")

print(page)
print(page.status_code)
#print(page.content)
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(page.content)

#parse the html doc using beatifulsoup4
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

list(soup.children)

print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))

