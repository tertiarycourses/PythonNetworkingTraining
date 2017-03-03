import socket
from time import ctime
import datetime

HOST = 'localhost'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)


def GetResult(Cmd):
    
    retValue=""
    
    if Cmd == "time":
    	retValue="time"
    elif Cmd=="date":
    	retValue="date"
    else:
    	retValue="date time"
	
    return retValue
	


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen(5)
server_socket.setsockopt( socket.SOL_SOCKET,socket.SO_REUSEADDR, 1 )
retData=""
while True:
    print('Server waiting for connection...')
    client_sock, addr = server_socket.accept()
    print('Client connected from: ', addr)
    while True:
    	data = client_sock.recv(BUFSIZ)
    	if not data or data.decode('utf-8') == 'END':
    		break
    	#retData=""
    	getData = data.decode('utf-8')
    	print("Received from client: %s" % getData)
    	#retData=GetResult(getData)
    	#print("Sending the Server to client ", retData)
    	if getData == "time":
    		print("Sending the server time to client: %s"%datetime.datetime.now().time())
    		retData = str(datetime.datetime.now().time())
    		#retData="time"
    	elif (getData == "date"):
    		print("Sending the server date to client: %s"%datetime.datetime.now().date())
    		retData =str(datetime.datetime.now().date())
    		#retData="date"
    	else: 
    		print("Sending the server date to client: {}".format(ctime()))
    		retData = ctime()
    		#retData = "data time"
    	try:
    		client_sock.send(bytes(retData, 'utf-8'))
    	except KeyboardInterrupt:
    		print("Exited by user")
    client_sock.close()
server_socket.close()