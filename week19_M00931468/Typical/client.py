import socket, time

host = "localhost" 
port = 5002  

ADDRESS = (host, port)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect(ADDRESS)

    receiver_name = input("Enter the receiver name: ")
    s.send(receiver_name.encode())
    recipient =s.recv(1024).decode()

    time.sleep(2)
    while True:
        reply = s.recv(1024).decode()
        print(f"{recipient}: {reply}")

        if reply.lower() == "bye":
            print(reply)
            break


        message = input(f"{receiver_name}: ")
        
        if message.lower() == "bye"  :
            break

        s.send(message.encode())
        

        
        