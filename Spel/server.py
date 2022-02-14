from socket import *
import json, random
HOST = "127.0.0.1"
PORT = 8080

def startServer():
    s = socket();
    s.bind((HOST, PORT));
    s.listen();

    return s;

def threaded_client(connection):
    for c in connections:
        data = json.dumps(c[1])
        c[0].send(data.encode())

    while True:
        data = connection.recv(1024);
        print(data)



from _thread import *
s = startServer()
threadCount = 0;
ids = 0;

connections = []

while True:
    print("Waiting for client to connect")
    conn, address = s.accept();
    print("Client added with address: " +  address[0])
    start_new_thread(threaded_client, (conn,))

    
    
    client = {
        "id": ids + 1,
        "type": "newConnection",
        "coords" : {
            "x": random.randrange(0, 300),
            "y": random.randrange(0, 300),
        }
    }

    ids += 1
    
    connections.append([conn, client])
    threadCount += 1

