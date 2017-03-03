##import urllib
##from urllib.request import urlopen
##
##uri = 'http://localhost:8000'
##name = "Mark"
## Encode data in base64 string
##encode = name.encode('utf-8')
##encode = name
##params = { 'name' : encode }
## Pack key-value pairs in form of url-encode format
##data = urllib.parse.urlencode(params)
##
## urlopen with data will use POST method by default
##p = urlopen(uri, params.encode('utf-8'))
##print(p.read())


import http.client, urllib.parse
params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
#conn = http.client.HTTPConnection("bugs.python.org")
conn = http.client.HTTPConnection("127.0.0.1:8000")
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
#302 Found
data = response.read()
print(data)
#b'Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>'
conn.close()
