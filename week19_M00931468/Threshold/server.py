import socket 
HOST = "localhost"
PORT = 5000

ADDRESS = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind(ADDRESS)

    s.listen(5)

    while True:
        print('weighting for connection...')

        (client, address) = s.accept()

        client.send('What is your name  '.encode())
        print(client.recv(1024))
