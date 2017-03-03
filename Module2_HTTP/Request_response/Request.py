#Requests with urllib
# from urllib.request import urlopen
# from urllib.request import Request


# response = urlopen('http://www.debian.org')
# print(response)
# print(response.readline())

# ##response object
# print(response.url)
# print(response.status)
# print(response.headers['content-type'])


#response = urlopen('http://www.debian.org')
#print(response.read(50))

#response = urlopen('http://www.debian.org')
#print(response.read())

##print(response.read())

##Status Code
#print(response.status)

#-------------------------------------
#custom request
#req = Request('http://www.debian.org')
#req.add_header('Accept-Language', 'sv')
#response = urlopen(req)
#print(response.readlines()[:5])

#----------------------------------------
#Content Compression

#with decompression cannot see data
#from urllib.request import Request
#from urllib.request import urlopen
#req = Request('http://www.debian.org')
#req.add_header('Accept-Encoding', 'gzip')
#response = urlopen(req)
#print(response.getheader('Content-Encoding'))
#print(response.read())

#With Decompression can view data
#from urllib.request import Request
#from urllib.request import urlopen
#import gzip

#req = Request('http://www.debian.org')
#req.add_header('Accept-Encoding', 'gzip')
#response = urlopen(req)
#content = gzip.decompress(response.read())
#result=content.splitlines()[:5]
#print(result)

#--------------------------------------
#Content Negotiation
#from urllib.request import urlopen
#import gzip

#req = Request('http://www.debian.org')
#req.add_header('Accept-Content-Type', 'text/plain')
#response = urlopen(req)
#content = response.read()
#result=content.splitlines()[:5]
#print(result)

#-------------------------------------------
#User Agent
#from urllib.request import Request
#from urllib.request import urlopen
#req = Request('http://www.debian.org')
#req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64;rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')
#response = urlopen(req)
#print(response.readline())

#---------------------------------------------
#Cookie
#from http.cookiejar import CookieJar
#cookie_jar = CookieJar()

#from urllib.request import build_opener, HTTPCookieProcessor
#opener = build_opener(HTTPCookieProcessor(cookie_jar))
#opener.open('http://www.github.com')

#print(len(cookie_jar))
#cookies = list(cookie_jar)
#print(cookies)

#---------------------------------------------\
#Redirect
#from urllib.request import Request
#from urllib.request import urlopen

#req = Request('http://www.gmail.com')
#response = urlopen(req)
#print(response.url)
#print(req.redirect_dict)

#---------------------------------------
#HTTP Methods

#GET
import requests
response = requests.get('http://www.debian.org')
print(response.content)
print(response.status_code)

#POST
# import requests
# r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
# print(r.status_code, r.reason)

# print(r.text)
