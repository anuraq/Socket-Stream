import socket

HEADER = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 1234))

SIZE = int(s.recv(HEADER).decode('utf-8'))

msg = s.recv(SIZE).decode('utf-8')

print(msg)
