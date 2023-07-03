import socket, pickle
from art import tprint

host = "localhost"
port = 5000

ADDRESS = (host, port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDRESS)

    s.listen(1)
    print("Waiting for connection....")


    (client_host, client_address) = s.accept()
    cart = []
    tprint("Online Store")
    path = "/home/midev/Desktop/Python/CST1510/week19_M00931468/Excellent/order.txt"

    client_host.send("Welcome to the Local Grocery Store\n".encode())
    
    while True:
        client_host.send("What do you want to do: Buy or Remove\n".encode())
        command = client_host.recv(1024).decode()

        print(command)
        if command  == "Buy":
            client_host.send("What do you want to buy? \n".encode())
            order = pickle.loads(client_host.recv(4096))

            cart.append(order)

        elif command == "Remove":
            client_host.send("What do you want to remove? \n".encode())
            order = pickle.loads(client_host.recv(4096))

            cart.remove(order)

        with open(path, "w") as f:
            for item in cart:
                f.writelines(f"{item}\n")


