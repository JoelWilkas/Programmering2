from tkinter import *
from socket import *
from _thread import *


import json, random
from turtle import right
HOST = '127.0.0.1'
PORT = 8080

ws = Tk();
ws.title('Game')
currentId = 0;

players = []

moveSpeed = 10
playerList = []
currentX = 0
currentY = 0




def connect():
            s = socket();
            s.connect((HOST, PORT))
            return s

gameCanvas = Canvas(ws, width=1000, height=700)
gameCanvas.pack()

alreadyConnected = False

def getThreads():
    while True:
        data = s.recv(1024)
        loadedData = json.loads(data)
        if(loadedData[1] == 'newConnection'):
            global currentX, currentY, currentId, alreadyConnected
            for x in range(currentId, len(loadedData[0])):
                print("amogus")
                data = gameCanvas.create_oval(
                        loadedData[0][x]["coords"]["x"], loadedData[0][x]["coords"]["y"], 
                        loadedData[0][x]["coords"]["x"] + 10, loadedData[0][x]["coords"]["y"] + 10, fill=loadedData[0][x]["color"]
                )
                
                currentX = loadedData[0][x]["coords"]["x"]
                currentY = loadedData[0][x]["coords"]["y"]
                playerList.append(data)

            if(alreadyConnected == False):
                currentId = len(loadedData[0])
                alreadyConnected = True

            print(currentId)
        if(loadedData[1] == "move"):
            
            print(playerList[currentId - 1])

            if(loadedData[0]["dir"] == "left"):
                gameCanvas.move(playerList[loadedData[0]["id"] - 1], -moveSpeed, 0)
            if(loadedData[0]["dir"] == "right"):
                gameCanvas.move(playerList[loadedData[0]["id"] - 1], moveSpeed, 0)
            if(loadedData[0]["dir"] == "up"):
                gameCanvas.move(playerList[loadedData[0]["id"] - 1], 0, -moveSpeed)
            if(loadedData[0]["dir"] == "down"):
                gameCanvas.move(playerList[loadedData[0]["id"] - 1], 0, moveSpeed)
def keyPressed(event):
    
    global currentX, currentY
    

    print(event.keysym)
    if(event.keysym == "Left"):
        currentX -= moveSpeed
        data = {
            "id": currentId,
            "coords" : {
                "x": currentX,
                "y": currentY,
            },
            "dir": "left"
        }
        s.send(json.dumps([data, "move"]).encode())
    elif(event.keysym == "Right"):
        currentX += moveSpeed
        data = {
            "id": currentId,
            "coords" : {
                "x": currentX,
                "y": currentY,
            },
            "dir": "right"
        }
        s.send(json.dumps([data, "move"]).encode())
    elif(event.keysym == "Up"):
        currentY -= moveSpeed
        data = {
            "id": currentId,
            "coords" : {
                "x": currentX,
                "y": currentY,
            },
            "dir": "up"
        }
        s.send(json.dumps([data, "move"]).encode())
    elif(event.keysym == "Down"):
        currentY += moveSpeed
        data = {
            "id": currentId,
            "coords" : {
                "x": currentX,
                "y": currentY,
            },
            "dir": "down"
        }
        s.send(json.dumps([data, "move"]).encode())



    

s = connect();
start_new_thread(getThreads, ())


ws.bind_all('<Key>', keyPressed)

ws.resizable(False, False)




ws.mainloop()