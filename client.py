import socket
import sys

sock = socket.create_connection(('localhost', 8081))

url = sys.argv[1]

try:
    message = url.encode()
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(43)
        amount_received += len(data)
        txt = data.decode()
        print(txt)

finally:
    print('closing socket')
    sock.close()