# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 3001  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hola soy un el CLIENTE PYTHON")
    data = s.recv(1024)

print(f"Mensaje del Servidor: {data.decode('ascii')}")