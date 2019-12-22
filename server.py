import socket
import time
import threading
#import keyboard
from pynput.keyboard import Listener

HEADER = 10

HOST = socket.gethostname()
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)
msg = "Welcome to server!!"
msg = f'{len(msg):<{HEADER}}' + msg

def server_socket_running():
    while True:
        conn, address = s.accept()
        print(f"new connection formed at address: {address}")
        conn.send(bytes(msg,'utf-8'))
        conn.close()


def is_pressed(key):
    global EXIT
    try:
        if key.char == 'q':
            EXIT = True
    except AttributeError:
        pass


x = threading.Thread(target=server_socket_running, args=(), daemon=True)
k = Listener(on_press=is_pressed, daemon=True)
k.start()

EXIT = False
FIRST = False
j=0
while True:
    if not FIRST:
        x.start()
        print("Press 'q' for stopping the server.")
        FIRST = True
    print('Server running for : '+str(j)+' seconds', end='\r')
    time.sleep(1)
    j += 1
    if EXIT:
        break
