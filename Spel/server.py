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
        data = json.dumps([c[1], "newConnection"])
        c[0].send(data.encode())

    while True:
        data = connection.recv(1024);
        loadedData = json.loads(data)
        
        if(loadedData[1] == "move"):
            for c in connections:
                c[0].send(data)




from _thread import *
s = startServer()
threadCount = 0;
ids = 0;
clients = []
colors = ["red", "blue"]
connections = []

while True:
    print("Waiting for client to connect")
    conn, address = s.accept();
    print("Client added with address: " +  address[0])
    start_new_thread(threaded_client, (conn,))

    
    
    client = {
        "id": ids + 1,
        "coords" : {
            "x": round(random.randrange(0, 1000)),
            "y": round(random.randrange(0, 700)),
        },
        "color": random.choice(colors)
    }
    clients.append(client)

    ids += 1
    print(clients)
    
    connections.append([conn, clients])
    threadCount += 1

