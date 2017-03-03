#Requests with urllib
from urllib.request import urlopen

response = urlopen('http://www.google.com')

print(response)

text=str(response.read())
print(text)

with open("output.html", "w") as f:
        f.write(text) 




#with open("output.txt", "w") as f: 
        #for x in response:
                #f.write(str(x).replace('\\n','\n')) 








#page = urlopen('http://crypto-bot.hopto.org/server/list.php')

#f = open("test.txt", "w")
#f.write(str(page.read()))
#f.close()

#print(page.read())

##response object
#print(response.url)

#response = urlopen('http://www.debian.org')
#print(response.read(50))

#response = urlopen('http://www.debian.org')
#print(response.read())

#print(response.read())

##Status Code
#print(response.status)