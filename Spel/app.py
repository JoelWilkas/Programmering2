from tkinter import *
from socket import *
from _thread import *


import json, random
HOST = '127.0.0.1'
PORT = 8080

ws = Tk();
ws.title('Game')
currentId = 0;

players = []


playerCharacters = []


def connect():
            s = socket();
            s.connect((HOST, PORT))
            return s

gameCanvas = Canvas(ws, width=1000, height=700)
gameCanvas.pack()

def getThreads():
    while True:
        data = s.recv(1024)
        loadedData = json.loads(data)
        if(loadedData["type"] == 'newConnection'):
            print("new")
            global currentId
            currentId = loadedData['id']
            
            data = gameCanvas.create_oval(
                    loadedData["coords"]["x"], loadedData["coords"]["y"], 
                    loadedData["coords"]["x"] + 10, loadedData["coords"]["y"] + 10,  
                 )
            s.send(json.dumps(data).encode())


            
        


def keyPressed(event):
    print(currentId)
    gameCanvas.move(playerCharacters[currentId - 1], -50, 0)
    data = {
        "id": currentId,
        "type": "move",
        "coords" : {
            "x": random.randrange(0, 300),
            "y": random.randrange(0, 300),
        }
    }

    s.send(json.dumps(data).encode())

s = connect();
start_new_thread(getThreads, ())


ws.bind_all('<Key>', keyPressed)

ws.resizable(False, False)




ws.mainloop()