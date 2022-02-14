from logging import PlaceHolder
import socketio
import tkinter as tk
from tkinter import ttk
from tkinter import *

sio = socketio.Client()
root = tk.Tk()
root.geometry("800x500")



tabs = ttk.Notebook(root)
tabs.pack(fill=BOTH, expand=TRUE)
frame1 = ttk.Frame(tabs)
frame2 = ttk.Frame(tabs)
tabs.add(frame1, text="Tab One")
tabs.add(frame2, text="Tab Two")

def get_value():
    e_text=entry.get()
    e_username = nameEntry.get()
    sio.emit('message_client', {'name': e_username, 'message': e_text})
    @sio.event
    def message_server(data):
        print(data)
        t.insert(END, f'\n {data["name"]}: {data["message"]}')
        t.pack(side=TOP, fill=X)
        



textFrame = tk.Frame(frame1, highlightthickness=1, highlightbackground="black", height=100, width=300)
textFrame.pack(side="top", fill="both", expand=True)
textFrame.grid_rowconfigure(0, weight=1, uniform="x")
textFrame.grid_columnconfigure(0, weight=1, uniform="x")


v = Scrollbar(textFrame)
v.pack(side = RIGHT, fill = Y)

t = Text(textFrame, width = 15, height = 15, wrap = NONE,
                 yscrollcommand = v.set)


nameEntry = tk.Entry(root,font=('Century 12'),width=20)
nameEntry.insert(0, "Username")
nameEntry.pack(pady=10)


entry= tk.Entry(root,font=('Century 12'),width=40)
entry.insert(0, "Message")
entry.pack(pady=10)

button= tk.Button(root, text="Submit", command= get_value)
button.pack()











sio.connect('http://localhost:8080')

root.mainloop()