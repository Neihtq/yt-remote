from  _thread import start_new_thread
from threading import Thread
from time import sleep
import socket, sys, pafy, os, vlc, struct, traceback

_host = 'localhost'
txt = "Can't read title from soundcloud"

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

def runVLC2():
    global currplaying
    global trackList
    playlist = ""
    for track in trackList:
        playlist += track[0] + " "
        currplaying = track[1]
        trackList.remove(track)
    os.system("cvlc --novideo --play-and-exit " + playlist)

def runVLC():
    global currplaying
    global trackList
    instance = vlc.Instance('--input-repeat=-1')
    player = instance.media_player_new()
    
    for song in trackList:
        currplaying = song[1]
        media=instance.media_new(song[0])

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
trackList = []
isempty = True
currplaying= "Nothing"


t2 = Thread(target=runVLC2)
start_new_thread(slisten,(serversocket,))
start_new_thread(currentlyPlaying,(statusSocket,))
while True:
    if not trackList:
        currplaying = "Nothing"
        continue
    runVLC2()