import socket, sys, pafy


def playYT(url):
    video = pafy.new(url)
    title = video.title
    audio = video.getbestaudio()
    dl = audio.download()


def createSocket(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_name = socket.gethostbyname(host)
    server_address = (server_name, 8081)
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
            while True:
                data = connection.recv(43)
                print('received {!r}'.format(data))
                if data:
                    url = data.decode()
                    print(url)
                    playYT(url)
                    connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break
        
        finally:
            connection.close()

_host = 'localhost'
serversocket = createSocket(_host)

slisten(serversocket)