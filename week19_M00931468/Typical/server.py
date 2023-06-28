import socket, time

host = "localhost" 
port = 5002

ADDRESS = (host, port)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(ADDRESS)

    s.listen(5)

    print("Waiting for connection.....")
    (client_host, client_address) = s.accept()

    sender_name = input("Enter sender name: ")
    client_host.send(sender_name.encode())

    recipient = client_host.recv(1024).decode()

    time.sleep(2)
    while True:
        message = input(f"{sender_name}: ")
        
        client_host.send(message.encode())
        
        if message.lower() == "bye"  :
            time.sleep(2)
            break
        
        reply = client_host.recv(1024).decode()
        print(f"{recipient}: {reply}")

        if reply.lower() == "bye":
            break
        



        

        
        
        