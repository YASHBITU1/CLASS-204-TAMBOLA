from http import client
import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None

CLIENTS = {}




def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()

        playername = player_socket.recv(1024).decode().strip()
        if(len(CLIENTS.keys())==0):
            CLIENTS[playername] = {"playertype":"player1"}
        else:
            CLIENTS[playername] = {"playertype":"player2"}
        
        CLIENTS[playername]["player_socket"] = player_socket    
        CLIENTS[playername]["address"] = addr
        
        CLIENTS[playername]["playername"] = playername
        
        CLIENTS[playername]["turn"] = False
        print(f"CONNECTED WITH {playername}:{addr} :)")
                       







def setup():
    print("\n")
    print("\t\t\t\t\t\t*** -!!!TAMBOLA GAME!!!- ***")


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR PLAYERS...")
    print("\n")

    acceptConnections()


setup()
