import socket, sys, struct
from time import sleep

def packSize(msg):
    size = struct.pack('!I', len(msg))
    return size

def connectAndSend(msg):
    sock = socket.create_connection(('localhost', 8800))
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


url = "https://www.youtube.com/watch?v=wuGt8wanfhE" # Anevo- Waiting on your call
message = url.encode()
connectAndSend(message)
