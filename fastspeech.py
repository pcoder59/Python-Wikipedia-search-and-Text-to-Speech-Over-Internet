import playsound
import pyttsx3
import socket
import threading

HEADER = 64
PORT = 5051
FORMAT = 'utf-8'
SERVER = "172.105.62.42"
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

search = input("Search Anything: ")

def speech(msg):
    msgobj = pyttsx3.init()
    msgobj.say(msg)
    msgobj.runAndWait()

def fetchData(search):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    message = search.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    success = client.recv(HEADER).decode(FORMAT)
    success = int(success)
    data = client.recv(success).decode(FORMAT)
    if data == DISCONNECT_MESSAGE:
        print("No Search Results")
        data = "No Results"
    print(data)
    speech(data)
    
fetchData(search)