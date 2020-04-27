import socket
import threading
import requests
import bs4
import wikipedia

HEADER = 64
PORT = 5051
SERVER = "172.105.62.42"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    connected = True
    while connected:
        name = conn.recv(HEADER).decode(FORMAT)
        if name:
            name = int(name)
            msg_name = conn.recv(name).decode(FORMAT)
            print(f"[NEW CONNECTION] {msg_name} connected.")
            try:
                res = wikipedia.summary(msg_name, sentences=1)
                senddata = res
            except:
                senddata = DISCONNECT_MESSAGE
                message = senddata.encode(FORMAT)
                msg_length = len(message)
                send_length = str(msg_length).encode(FORMAT)
                send_length += b' ' * (HEADER - len(send_length))
                conn.send(send_length)
                conn.send(message)
                continue
            message = senddata.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            conn.send(send_length)
            conn.send(message)

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()
        print(f"[ACTIVE CONNECTIONS]")

print("[STARTING] server is starting...")
start()