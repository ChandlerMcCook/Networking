import socket
import threading

PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

HEADER = 8
FORMAT = 'utf-8'

print("Server staring on port ", PORT)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msgSize = conn.recv(HEADER).decode(FORMAT)
        if (msgSize): 
            msgSize = int(msgSize)
            msg = conn.recv(msgSize).decode(FORMAT)

            if msg == "#":
                break

            print(f"[{addr}] {msg}")
    
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
