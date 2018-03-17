import socket, sys, struct, pickle

PORT = 8002
HOST = "localhost"
def askStatus():
    sock = socket.create_connection((HOST, PORT))
    try:        
        size = struct.unpack('!I', sock.recv(4))[0]
        data = pickle.loads(sock.recv(size))
        print(str(data))
    finally:
        sock.close()


askStatus()
