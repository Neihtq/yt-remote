import socket, sys, struct

PORT = 8001
HOST = '192.168.2.206'
def packSize(msg):
    size = struct.pack('!I', len(msg))
    return size

def connectAndSend(msg):
    sock = socket.create_connection((HOST, PORT))
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
url = "https://soundcloud.com/marshmellomusic/friends"
message = url.encode()
connectAndSend(message)
