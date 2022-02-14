from tkinter import *

import socket, json
HOST = '127.0.0.1'
PORT = 8080


players = []

def toDict(data):
    result = dict((a.strip(), int(b.strip()))  
                     for a, b in (element.split('-')  
                                  for element in data.split(', ')))  
    return result

class game(Canvas):
    def __init__(self):
        super().__init__(
            width=1000,
            height=700,
            background='#f1f1f1'
        )



        self.pack()

    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024)
            print(data)

ws = Tk();
ws.title('Game')
ws.resizable(False, False)

game = game()
game.connect()
ws.mainloop()