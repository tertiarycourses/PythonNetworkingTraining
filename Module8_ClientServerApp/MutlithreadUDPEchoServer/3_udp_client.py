from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST,SO_REUSEADDR

MAX_SIZE = 4096
PORT = 6060
server_address = ('127.0.0.1', PORT)



if __name__ == '__main__':
    

    while True:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        sock.bind(server_address)

    	msg = input()
    	if msg == "q":
    		break
    	sock.sendto(bytes(msg, 'utf-8'),server_address)
    	data, addr = sock.recvfrom(MAX_SIZE)
    	if data:
    		print("Server says-")
    		print(data.decode('utf-8'))
