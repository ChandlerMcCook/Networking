import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5000
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

HEADER = 8
FORMAT = 'utf-8'
MAX_SIZE = 1024

print("Server staring on port ", PORT)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    msg = conn.recv(MAX_SIZE).decode(FORMAT)
    print(msg)
    conn.send("hi".encode(FORMAT))
    
    conn.close()

def start():
    server.listen()
    print(f"SERVER LISTENING ON {SERVER}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[{threading.active_count() - 1} ACTIVE CONNECTIONS]")


start()
