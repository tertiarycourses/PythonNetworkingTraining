import socket
HOST = 'www.google.org' # or 'localhost'
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)


client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(ADDR)

data = 'GET / HTTP/1.0\r\n\r\n'
client_sock.send(data.encode('utf-8'))
data = client_sock.recv(BUFSIZ)
print(data.decode('utf-8'))
client_sock.close()

text_file = open("Output.html", "w")
text_file.write(data.decode('utf-8'))
text_file.close()
