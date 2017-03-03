import tincanchat

HOST = tincanchat.HOST
PORT = tincanchat.PORT

def handle_client(sock, addr):
	try:
		msg = tincanchat.recv_msg(sock)
		print('{}: {}'.format(addr, msg))
		msg1=""
		msg1= msg.split(":")
		result=0
		print(msg1)
		if(msg1[0] == "add"):
			result= int(msg1[1]) + int(msg1[2])
		elif(msg1[0] == "minus"):
			result= int(msg1[1]) - int(msg1[2])
		ans= str(result)
		print('{}: {}'.format(addr, ans))
		tincanchat.send_msg(sock, ans)  # Blocks until sent
	except (ConnectionError, BrokenPipeError):
		print('Socket error')
	finally:
		print('Closed connection to {}'.format(addr))
		sock.close()

if __name__ == '__main__':
	listen_sock = tincanchat.create_listen_socket(HOST, PORT)
	addr = listen_sock.getsockname()
	print('Listening on {}'.format(addr))
	
	while True:
		client_sock,addr = listen_sock.accept()
		print('Connection from {}'.format(addr))
		handle_client(client_sock, addr)
