import socket, sys, struct

PORT = 8001
HOST = 'localhost'
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
        data = sock.recv(size).decode('utf-8')
        print("Now playing: " + data)

    finally:
        print('closing socket')
        sock.close()


url = "https://www.youtube.com/watch?v=mkgl_f-DpXc" # Anevo- Waiting on your call
#url = "https://www.youtube.com/watch?v=BXyksv9M8pU"
message = url.encode()
connectAndSend(message)
