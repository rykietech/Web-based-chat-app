import socket 
import select 
import string
import sys 
  
def show():
    sys.stdout.write("<You>")
    sys.stdout.flush()

if __name__ == "__main__":

    if (len(sys.argv)<3):
        print("Accepted")
        sys.exit()

    IP_address = sys.argv[1];
    Port = int(sys.argv[2])

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.settimeout(2)

    #Connecting to host
    try:
        server.connect((IP_address,Port))
    except:
        print("Unable to connect")
        sys.exit()

    print("Connected to host.")
    show()

    while 1:
        sockets_list = [socket.socket(),server]

        #Get readable list of sockets
        read_sockets,write_socket,error_socket = select.select(sockets_list,[],[])

        for sock in read_sockets:
            #incomming message
            if sock == server:
                message = sock.recv(4096)
                if not message:
                    print("\n Disconnected from server")
                    sys.exit()
                else:
                    #print the message
                    sys.stdout.write(message.decode('utf-8'))
                    show()
                    sys.stdout.flush()  
            else:
                #User entered a message
                msg = sys.stdin.readline().encode()
                server.send(msg)
                show()
                sys.stdout.flush()
  
  
  
  
"""  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 

while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [socket.socket(), server] 
  
   
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets: 
        if socks == server: 
            message = socks.recv(2048) 
            if not message:
                print("Connection closed")
                sys.exit()
        else: 
            message = sys.stdin.readline().encode()
            server.send(message) 
            sys.stdout.write("<You>") 
            sys.stdout.write(message.encode()) 
            sys.stdout.flush() 
T
server.close() """