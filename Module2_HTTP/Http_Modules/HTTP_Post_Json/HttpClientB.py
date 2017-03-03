##import http.client, urllib.parse
##params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
##headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
###conn = http.client.HTTPConnection("bugs.python.org")
##conn = http.client.HTTPConnection("127.0.0.1:80")
##conn.request("POST", "", params, headers)
##response = conn.getresponse()
##print(response.status, response.reason)
###302 Found
##data = response.read()
##print(data)
###b'Redirecting to <a href="http://bugs.python.org/issue12524">http://bugs.python.org/issue12524</a>'
##conn.close()


import urllib.request
import json      

body = {'ids': [12, 14, 50]}  

myurl = "http://127.0.0.1:80"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')
# needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes) 
print(response.content)
