import socket
import threading

HEADER = 8
PORT = 5000
FORMAT = 'utf-8'
SERVER = "192.168.1.83"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msgSize = len(message)
    sendSize = str(msgSize).encode(FORMAT)
    sendSize += b' ' * (HEADER - len(sendSize))

    client.send(sendSize)
    client.send(message)


send("Hello there!")