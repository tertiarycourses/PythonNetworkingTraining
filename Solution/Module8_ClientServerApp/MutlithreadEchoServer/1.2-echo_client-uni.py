import sys, socket


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


HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = 4040

if __name__ == '__main__':
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print('\nConnected to {}:{}'.format(HOST, PORT))
            print("Type message, enter to send. 'q' to quit")
            msg = input()
            if msg == 'q': break
             # Blocks until sent
            send_msg(sock, msg)
            print('Sent message: {}'.format(msg))
            # Blocks until recent complete message
            msg = recv_msg(sock)
            print('Received echo: ' + msg)
        except ConnectionError:
            print('Socket error')
            break
        finally:
            sock.close()
            print('Closed connection to server\n')

