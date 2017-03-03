import http.client
conn = http.client.HTTPConnection("127.0.0.1:8081")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)