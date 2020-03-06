import socket
import time
import threading
from pynput.keyboard import Listener
#from audio_stream import audio_stream

HEADER = 10
HOST = socket.gethostname()
PORT = 1234

class Server():
    def __init__(self, header, addr, data):
        #super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.h = header
        self.a = addr
        self.d = data

    def start_server(self):
        def server_socket_running(HEADER, addr, op):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(addr)
            s.listen(5)
            nonlocal THREAD_START
            data = data_selector(op)
            HEADER_BUFF = f'{len(data):<{HEADER}}'
            data = bytes(HEADER_BUFF, 'utf-8') + data
            print("\nPress 'q' for stopping the server.")
            while True:
                THREAD_START = True
                conn, address = s.accept()
                print(f"new connection formed at address: {address}")
                conn.send(data)
                conn.close()

        def audio_socket_running(HEADER, addr, op):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(addr)
            s.listen(5)
            nonlocal THREAD_START
            HEADER_BUFF = f'{len(data):<{HEADER}}'
            //START_FROM_HERE


        def data_selector(data):
            if data == "text":
                while True:
                    text = input("\nEnter text to be Broadcasted : ")
                    l = input(f"\nEntered Text : {text}\n\nEnter 'Y' to CONFIRM 'N' to CHANGE : ")
                    if(l.lower() == 'y'):
                        break
                return bytes(text, 'utf-8')
            if data == "audio":
                print("\nStart Broadcasting through your microphone : ")
                while True:
                    l = input("\nEnter 'Y' to CONFIRM 'N' to CANCEL : ")
                    if(l.lower() == 'y'):
                        break

        def is_pressed(key):
            nonlocal SERVER_EXIT
            try:
                if key.char == 'q':
                    SERVER_EXIT = True
            except AttributeError:
                pass

        if(self.d == "text" or self.d == "text"):
            x = threading.Thread(target=server_socket_running, args=(self.h, self.a, self.d), daemon=True)
        else:
            x = threading.Thread(target=audio_socket_running, args=(self.h, self.a, self.d), daemon=True)

        k = Listener(on_press=is_pressed, daemon=True)
        THREAD_START = False
        SERVER_EXIT = False
        FIRST = False
        j=0
        k.start()
        while True:
            if not FIRST:
                x.start()
                FIRST = True
            if THREAD_START:
                print('Server running for : '+str(j)+' seconds', end='\r')
                time.sleep(1)
                j += 1
            if SERVER_EXIT:
                break
