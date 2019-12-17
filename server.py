import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    conn, address = s.accept()
    print(f"new connection formed at address: {address}")
    conn.send("Welcome to server!!")
