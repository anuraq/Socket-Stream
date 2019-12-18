import socket

HEADER = 10

HOST = socket.gethostname()
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)
msg = "Welcome to server!!"
msg = f'{len(msg):<{HEADER}}' + msg

while True:
    conn, address = s.accept()
    print(f"new connection formed at address: {address}")
    conn.send(bytes(msg,'utf-8'))
    conn.close()
