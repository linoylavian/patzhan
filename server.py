import socket
import time
server_socket=socket.socket()
server_socket.bind(("0.0.0.0",13370))
server_socket.listen()

(client_socket, client_address) = server_socket.accept()
data = client_socket.recv(1024).decode()
if data=="Howdy":
    client_socket.send("1".encode())

server_socket.close()
client_socket.close()
time.sleep(3)
client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 13371))
client_socket.send("aaaaaaaa,baaababz,dc825b4a3b4b683007382218e18c05a4".encode())
time.sleep(0.5)
client_socket.send("bbbbbbbb,dbbbbbbz,07cba382559e7304802600384b83a589".encode())
time.sleep(5)
client_socket.send("finish,07cba382559e7304802600384b83a589".encode())
data =''
while not data:
    data = client_socket.recv(1024).decode()
print(data)
