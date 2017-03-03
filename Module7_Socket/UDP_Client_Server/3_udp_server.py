from socket import socket, AF_INET, SOCK_DGRAM
maxsize = 4096
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))
while True:
    data, addr = sock.recvfrom(maxsize)
    if data:
    	print("recv data from Client %s"%(data.decode('utf-8'))) 
    	resp = "UDP server sending data"
    	sock.sendto(bytes(resp, 'utf-8'),addr)