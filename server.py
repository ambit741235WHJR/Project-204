import socket
from threading import Thread

# Global variables
SERVER = None
IP_ADDRESS = "127.0.0.1"
PORT = 8000

# List to keep track of clients
CLIENTS = {}

def setup():
    # Printing the header
    print("\n\t\t\t\t\t*** Welcome to Tambola Game ***\n")

    # Declaring the global variables
    global SERVER
    global IP_ADDRESS
    global PORT

    # Setting up the server
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    # Listening for incoming connections
    SERVER.listen(10)

    # Printing the waiting message
    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")

    # Accepting connections
    acceptConnections()

def acceptConnections():
    # Declaring the global variables
    global CLIENTS
    global SERVER

    # Accepting connections
    while True:
        player_socket, addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
        print(player_name)
        if(len(CLIENTS.keys()) == 0):
            CLIENTS[player_name] = {'player_type': 'player1'}
        else:
            CLIENTS[player_name] = {'player_type': 'player2'}
        
        CLIENTS[player_name]['player_socket'] = player_socket
        CLIENTS[player_name]['address'] = addr
        CLIENTS[player_name]['player_name'] = player_name
        CLIENTS[player_name]['turn'] = False

        print(f"Connection established with {player_name} : {addr}")

setup()