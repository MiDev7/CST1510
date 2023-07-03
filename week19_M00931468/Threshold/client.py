import socket               
     
host = "localhost" 
port = 5000                

with socket.socket() as s:
    s.connect((host, port))
    print(s.recv(1024).decode())
    name= input("")
    s.send(name.encode())