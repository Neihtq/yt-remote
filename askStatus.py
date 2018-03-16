import socket, sys, struct

PORT = 8020

def askStatus():
    sock = socket.create_connection(('localhost', PORT))
    try:        
        size = struct.unpack('!I', sock.recv(4))[0]
        data = sock.recv(size)       

        status = "Currently playing: " + data.decode()
        print(status)
    finally:
        sock.close()


askStatus()
