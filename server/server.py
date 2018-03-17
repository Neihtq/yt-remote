from  _thread import start_new_thread
from threading import Thread
from time import sleep
import socket, sys, pafy, os, struct, traceback, pickle

_host = 'localhost'
txt = "Can't read title from soundcloud"

def sendQueue(sock):
    while True:
        connection, client_address = sock.accept()
        try:
            data = pickle.dumps(trackList)
            size = packSize(data)
            connection.send(size)
            connection.send(data)
            print("sent status")
        
        finally:
            connection.close()


def currentlyPlaying(sock):
    while True:
        connection, client_address = sock.accept()
        try:
            print('client asking for status: ', client_address)
            msg = currplaying.encode()
            size = packSize(msg)
            connection.send(size)
            connection.send(msg)
            print("sent status")

        finally:
            connection.close()


def packSize(msg):
    size = struct.pack('!I', len(msg))
    return size


def addSong(url):
    global trackList
    title = txt
    if "youtube" in url:
        video = pafy.new(url)
        title = video.title
    trackList.append((url, title))


def runVLC():
    global currplaying
    global trackList
    playlist = ""
    for track in trackList:
        playlist += track[0] + " "
        currplaying = track[1]
        trackList.remove(track)
    os.system("cvlc --novideo --play-and-exit " + playlist)


def createSocket(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_name = socket.gethostbyname(_host)
    server_address = (server_name, port)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(5)
    return sock


def slisten(sock):
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('client connected: ', client_address)
            size = struct.unpack('!I', connection.recv(4))[0]
            data = connection.recv(size)
            print("received: " + str(data))

            url = data.decode()
            title = txt
            if "youtube" in url:
                title = pafy.new(url).title
            size = packSize(title)
            print("launch playYT")
            addSong(url)
            title = title.encode()
            connection.send(size)
            connection.send(title)
        
        finally:
            connection.close()


serversocket = createSocket(8001)
statusSocket = createSocket(8020)
queueSocket = createSocket(8002)
trackList = []
currplaying= "Nothing"

print("slisten")
threadL = Thread(target=slisten, args=(serversocket,))
threadL.start()

print("currPlaying")
threadS = Thread(target=currentlyPlaying, args=(statusSocket,))
threadS.start()

print("Queue")
threadQ = Thread(target=sendQueue, args=(queueSocket,))
threadQ.start()

print("Enter while loop")
while True:
    if not trackList:
        currplaying = "Nothing"
        continue
    runVLC()