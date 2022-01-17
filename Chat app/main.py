import socketio
import tkinter as tk
from tkinter import *

sio = socketio.Client()
root = tk.Tk()
root.geometry("800x500")

def get_value():
    e_text=entry.get()
    sio.emit('message', e_text)
    Label(textCanvas, text=e_text).pack()




textCanvas = tk.Canvas(root, highlightthickness=1, highlightbackground="black", height=100, width=300)
textCanvas.pack()

entry= tk.Entry(root,font=('Century 12'),width=40)
entry.pack(pady=50)

button= tk.Button(root, text="Submit", command= get_value)
button.pack()











sio.connect('http://localhost:8080')

root.mainloop()