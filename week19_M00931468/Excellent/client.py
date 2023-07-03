import socket, pickle

host = "localhost"
port = 5000

ADDRESS = (host, port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ADDRESS)

    print(s.recv(1024).decode())

    while True:

        print(s.recv(1024).decode())

        command = input("Command: ")

        s.send(command.encode())

        print(s.recv(1024).decode())

        order = input("Order: ")

        s.sendall(pickle.dumps(order))