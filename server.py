import socket
import threading

#length or byte the message should be recieved from client,
#CAUTION: if the message is longer than 64 length, may throw error
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # getting local IP address
ADDR = (SERVER, PORT) #Binding Socket to a specific address needs to be in a tuple
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#AF_INET: type of network we are looking, SOCK_STREAM: streaming data through internet
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def Handle_Client(Conn, Addr): #Conn = connection, Addr= address
    print(f"[NEW Conn] {Addr} connected", "\n")
    connected =True
    while connected:
        msg_len = Conn.recv(HEADER).decode(FORMAT) #decode msg from byte to string using 'utf-8'
        if msg_len:
            msg_len = int(msg_len) #converting size in str to int
            msg = Conn.recv(msg_len).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                print(f"{Addr} [DISCONNECTED]")
                connected = False
            print(f"[{Addr}] {msg}")
            Conn.send("Msg recieved".encode(FORMAT))
    Conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        Conn, Addr = server.accept()
        thread = threading.Thread(target = Handle_Client, args = (Conn,Addr))
        thread.start()
        print(f"[ACTIVE Connections] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
