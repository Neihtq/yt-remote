from  _thread import start_new_thread
from time import sleep
import socket, sys, pafy, os, vlc, struct, traceback


def _play(track, dur):
    global duration
    sleep(dur)
    media = instance.media_new(track)
    player.set_media(media)
    player.play()
    sleep(1)
    duration = player.get_length()
    print(duration)

def packSize(msg):
    size = struct.pack('!I', len(msg))
    return size

def playYT(url):

    print("creating video object")
    video = pafy.new(url)
    title = video.title
    track = video.getbestaudio()
    print(duration)
    start_new_thread(_play,(track.url, duration))


def createSocket(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_name = socket.gethostbyname(host)
    server_address = (server_name, 8800)
    print('starting up on {} port {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(5)
    return sock

def slisten(sock):
    while True:
        print(duration)
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

_host = 'localhost'
serversocket = createSocket(_host)
trackList = []
instance = vlc.Instance()
player = instance.media_player_new()

duration = 0;

slisten(serversocket)    