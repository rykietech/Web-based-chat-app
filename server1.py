# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from _thread import *

def post(sock,message):
	for socket in List_of_clients:
		if socket != server and socket != sock:
			try:
				socket.send(message).encode()
			except:
				socket.close()
				List_of_clients.remove(socket)

if __name__ == "__main__":
	List_of_clients =[]
	RECV_BUFFER = 4096
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
	IP_address = str(sys.argv[1])
	Port = int(sys.argv[2]) 
	server.bind((IP_address, Port)) 
	server.listen(100)
	List_of_clients.append(server)
	print(f"Chat server started on port {str(Port)}")

	while 1:
		read_sockets,write_socket,error_socket = select.select(List_of_clients,[],[])

		for sock in read_sockets:
			if sock == server:
				sockfd,addr = server.accept()
				List_of_clients.append(sockfd)
				print(f"Client {sockfd} connected {addr}")
				post(sockfd,f" someone entered the room\n {addr}" )

			else:
				try:
					msg = sock.recv(RECV_BUFFER)
					if msg:
						post(sock,"\r"+'<'+str(sock.getpeername())+'>'+msg)
				
				except:
					post(sock,f"Client {sock} is offline { addr}" )
					print(f"Client {sock} is offline {addr}" )
					sock.close()
					List_of_clients.remove(sock)
					continue
	server.close()
			


