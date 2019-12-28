import socket
import time
import threading
from pynput.keyboard import Listener

HEADER = 10
HOST = socket.gethostname()
PORT = 1234

class Server():
    def __init__(self, header, addr):
        self.h = header
        self.a = addr

    def start_server(self):
        def server_socket_running(HEADER, addr):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(addr)
            s.listen(5)
            msg = "Welcome to server!!"
            msg = f'{len(msg):<{HEADER}}' + msg
            while True:
                conn, address = s.accept()
                print(f"new connection formed at address: {address}")
                conn.send(bytes(msg,'utf-8'))
                conn.close()

        def is_pressed(key):
            nonlocal SERVER_EXIT
            try:
                if key.char == 'q':
                    SERVER_EXIT = True
            except AttributeError:
                pass

        x = threading.Thread(target=server_socket_running, args=(self.h, self.a), daemon=True)
        k = Listener(on_press=is_pressed, daemon=True)

        SERVER_EXIT = False
        FIRST = False
        j=0
        k.start()
        while True:
            if not FIRST:
                x.start()
                print("Press 'q' for stopping the server.")
                FIRST = True
            print('Server running for : '+str(j)+' seconds', end='\r')
            time.sleep(1)
            j += 1
            if SERVER_EXIT:
                break
