from socket import socket, AF_INET, SOCK_DGRAM
MAX_SIZE = 4096
PORT = 12345
server_address = ('localhost', PORT)

if __name__ == '__main__':
    sock = socket(AF_INET,SOCK_DGRAM)
    msg = "Hello UDP server"
    #sock.sendto(msg.encode(),('127.0.0.1', PORT))
    sock.sendto(bytes(msg, 'utf-8'),server_address)
    data, addr = sock.recvfrom(MAX_SIZE)
    print("Server says:")
    print(data.decode('utf-8'))