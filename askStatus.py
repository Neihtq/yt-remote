import socket, sys, struct

PORT = 8020

def askStatus():
    print("connect " + str(PORT))
    sock = socket.create_connection(('localhost', PORT))
    print("connected")
    try:        
        size = struct.unpack('!I', sock.recv(4))[0]
        data = sock.recv(size)       

        status = "Currently playing: " + data.decode()
        print(status)
    finally:
        print('closing socket')
        sock.close()


askStatus()
