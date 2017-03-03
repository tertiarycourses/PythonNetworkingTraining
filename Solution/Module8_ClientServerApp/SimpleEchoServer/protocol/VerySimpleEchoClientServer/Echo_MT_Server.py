#Mutlithreaded echo server
import socket
import sys
import _thread

def handle(client_socket, address):
    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = client_socket.recv(16)
            print('received "%s"' % data.decode('utf-8'))
            if data:
                print('sending data back to the client')
                client_socket.sendall(data)
            else:
                print('no more data from', address)
                break
                
    finally:
        # Clean up the connection
        client_socket.close()  



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)
    
    # spawn a new thread that run the function handle()
    _thread.start_new_thread(handle, (connection, client_address))     
       