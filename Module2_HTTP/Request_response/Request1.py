from urllib.request import urlopen

#response = urlopen('http://www.debian.org')
#print(response.getheaders())
#print(response.info())


import urllib.request
local_filename, headers = urllib.request.urlretrieve('http://python.org/')
html = open(local_filename)
print(html)
print("-----------------------------\n")
print(headers)
