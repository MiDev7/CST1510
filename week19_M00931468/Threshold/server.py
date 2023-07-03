from socket import *

HOST = 'localhost'
PORT = 5000

ADDRESS = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)

s.bind(ADDRESS)

s.listen(5)

while True:
    print('weighting for connection...')

    (client, address) = s.accept()

    client.send('What is your name  '.encode())

    print(client.recv(1024).decode())

    client.close()
