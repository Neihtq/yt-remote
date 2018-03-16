import socket, sys, struct
from time import sleep

PORT = 8000

def packSize(msg):
    size = struct.pack('!I', len(msg))
    return size

def connectAndSend(msg):
    sock = socket.create_connection(('localhost', PORT))
    try:        
        size = packSize(msg)
        sock.send(size)
        sock.send(msg)

        size = sock.recv(4)
        size = struct.unpack('!I', size)[0]        
        data = sock.recv(size).decode()
        print("Now playing: " + data)

    finally:
        print('closing socket')
        sock.close()


url = "https://www.youtube.com/watch?v=mkgl_f-DpXc" # Anevo- Waiting on your call
message = url.encode()
connectAndSend(message)
