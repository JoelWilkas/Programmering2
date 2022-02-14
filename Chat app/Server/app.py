import socketio

sio = socketio.Server()

app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print(sid, "connected")
    sio.emit("message", {'data': 'foobar'})

@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

@sio.on('message_client')
def message_client(sid, data):
    print(data)
    sio.emit('message_server', data)


