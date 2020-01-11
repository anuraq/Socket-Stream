from server import Server, HEADER, HOST, PORT
import pyfiglet
import random


def server_selected():
    while(True):
        i = input('''\nSelect Option from below : \n
    1. Broadcast a text.\n
    2. Broadcast audio. [STREAM]\n
    3. Broadcast a file.\n
input> ''')
        if i == "1" or i.lower == "text":
            serv = Server(HEADER, (HOST, PORT), "text")
            serv.start_server()
            #SERVER_TEXT
            break
        elif i == "2" or i.lower == "audio":
            serv = Server(HEADER, (HOST, PORT), "audio")
            serv.start_server()
            #SERVER_AUDIO
            break
        elif i == "3" or i.lower == "file":
            serv = Server(HEADER, (HOST, PORT), "file")
            serv.start_server()
            #SERVER_FILE
            break
        else:
            print("\n!!Error Acceptable Inputs : 1, 2, 3, text, audio, file.\n")
            continue


def client_selected():
    while(True):
        i = input('''\nSelect Option from below : \n
    1. Recieve a text.\n
    2. Stream audio.\n
    3. Recieve a file.\n
input> ''')
        if i == "1" or i.lower == "text":
            #SERVER_TEXT
            break
        elif i == "2" or i.lower == "audio":
            #SERVER_AUDIO
            break
        elif i == "3" or i.lower == "file":
            #SERVER_FILE
            break
        else:
            print("\n!!Error Acceptable Inputs : 1, 2, 3, text, audio, file.\n")
            continue


if __name__ == '__main__':
    fonts = ["banner3-D","basic","block","bulbhead","coinstak","colossal","computer","cosmic","lean","letters","o8","roman","rowancap","rozzo","speed","univers"]
    FONT = int(random.random() * len(fonts))
    fig = pyfiglet.figlet_format("Socket_Stream", font=fonts[FONT],width=200)
    print(fig)
    print("This can be used to transfer data between devices connected accross a network.\n\n")
    while(True):
        i = input('''Select Option from below : \n
    1. Server\n
    2. Client\n
input> ''')
        if i == "1" or i.lower == "server":
            server_selected()
            break
        elif i == "2" or i.lower == "client":
            client_selected()
            break
        else:
            print("\n!!Error Acceptable Inputs : 1, 2, Server, Client.\n")
            continue
