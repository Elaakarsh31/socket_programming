import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.105"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '*(HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello Bro!")
input()
send("Hello DUNIYA BC")
input()
send("YO Yo Hnoney")
send(DISCONNECT_MESSAGE)