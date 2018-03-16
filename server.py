from  _thread import start_new_thread
from threading import Thread
from time import sleep
import socket, sys, pafy, os, vlc, struct, traceback

PORT = 8000
_host = 'localhost'

def packSize(msg):
    size = struct.pack('!I', len(msg))
    return size

def playYT(url):
    global player
    global trackList
    print("creating video object")
    video = pafy.new(url)
    title = video.title
    track = video.getbestaudio()
    trackList.append(track.url)

def runVLC():
    global trackList
    instance = vlc.Instance('--input-repeat=-1')
    player = instance.media_player_new()
    
    for song in trackList:
        player=instance.media_player_new()
        media=instance.media_new(song)

        media.get_mrl()
        player.set_media(media)
        player.play()
        playing = set([1,2,3,4])
        sleep(1)

        trackList.remove(song)

        while True:
            state = player.get_state()
            if state not in playing:
                break
            continue

def createSocket(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_name = socket.gethostbyname(host)
    server_address = (server_name, PORT)
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
            title = pafy.new(url).title.encode()
            size = packSize(title)
            print("launch playYT")
            playYT(url)
            connection.send(size)
            connection.send(title)
        
        finally:
            connection.close()


serversocket = createSocket(_host)
trackList = []
isempty = True

#start_new_thread(slisten, (serversocket,))
t2 = Thread(target=runVLC)
start_new_thread(slisten,(serversocket,))

while True:
    if not trackList:
        continue
    runVLC()
