import socket
import threading

HEADER = 8
PORT = 5000
FORMAT = 'utf-8'
SERVER = "192.168.96.1"
ADDR = (SERVER, PORT)

MAX_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    # message = msg.encode(FORMAT)
    # msgSize = len(message)
    # sendSize = str(msgSize).encode(FORMAT)
    # sendSize += b' ' * (HEADER - len(sendSize))

    # client.send(sendSize)
    # client.send(message)

    client.send(msg.encode(FORMAT))
    response = client.recv(MAX_SIZE).decode(FORMAT)
    print(response)


    

send("Hello there!")