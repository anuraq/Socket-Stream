import socket
import time
import threading
import keyboard

HEADER = 10

HOST = socket.gethostname()
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)
msg = "Welcome to server!!"
msg = f'{len(msg):<{HEADER}}' + msg

def server_socket_running():
    global STOP_SERVER
    while True:
        if STOP_SERVER:
            print("server break")
            break
        conn, address = s.accept()
        print(f"new connection formed at address: {address}")
        conn.send(bytes(msg,'utf-8'))
        conn.close()

STOP_SERVER = False
x = threading.Thread(target=server_socket_running, args=())

FIRST = False
j=0
while True:
    if not FIRST:
        x.start()
        FIRST = True
    print('waiting : '+str(j), end='\r')
    time.sleep(1)
    j += 1
    if keyboard.is_pressed('q'):
        STOP_SERVER = True
        break
