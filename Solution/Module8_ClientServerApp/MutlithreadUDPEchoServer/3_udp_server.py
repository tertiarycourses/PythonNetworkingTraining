from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST,SO_REUSEADDR
maxsize = 8192
dest = ('<broadcast>',6060)
sock = socket(AF_INET,SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.bind(('127.0.0.1',12345))
while True:
	sock = socket(AF_INET,SOCK_DGRAM)
	sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
	sock.bind(('127.0.0.1',12345))
    data, addr = sock.recvfrom(maxsize)
    if len(data) >0:
    	print("recv data from Client %s"%(data.decode('utf-8'))) 
    	resp = "UDP server sending data"+ data.decode('utf-8')
    	sock.sendto(bytes(resp, 'utf-8'),dest)