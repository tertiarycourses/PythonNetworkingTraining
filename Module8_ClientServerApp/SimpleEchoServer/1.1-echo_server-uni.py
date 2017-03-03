import socket

HOST = ''
PORT = 4040

def recv_msg(sock):
    #Wait for data to arrive on the socket, then parse into messages using
    #b'\0' as message delimiter

    data = bytearray()
    msg = ''
    # Repeatedly read 4096 bytes off the socket, storing the bytes
    # in data until we see a delimiter
    while not msg:
        recvd = sock.recv(4096)
        if not recvd:
            # Socket has been closed prematurely
            raise ConnectionError()
        data = data + recvd
        if b'\0' in recvd:
            # we know from out protocol rules that we only send
            # one message per connection, so b'\0' will always be
            # the last character
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg



def send_msg(sock, msg):
    """ Send a string over a socket, preparing it first """
    msg += '\0'
    sock.sendall( msg.encode('utf-8'))

def handle_client(sock, addr):
    """ Receive data from the client via sock and echo it back """
    try:
        # Blocks until received complete message
        msg = recv_msg(sock)
        print('{}: {}'.format(addr, msg))
        # Blocks until sent
        send_msg(sock, msg)
    except (ConnectionError, BrokenPipeError):
        print('Socket error')
    finally:
        print('Closed connection to {}'.format(addr))
        sock.close()

if __name__ == '__main__':
    """ Setup the sockets our server will receive connection requests on """
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind((HOST, PORT))
    listen_sock.listen(100)
    addr = listen_sock.getsockname()
    print('Listening on {}'.format(addr))

    while True:
        client_sock,addr = listen_sock.accept()
        print('Connection from {}'.format(addr))
        handle_client(client_sock, addr)
