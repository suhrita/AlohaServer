from websocket_server import WebsocketServer
from APIManager import APIManager
import json

ClientConnections = []
PORT = 9001
api = APIManager()

def new_client(client, server):
	ClientConnections.append(client)

# Called for every client disconnecting
def client_left(client, server):
	ClientConnections.remove(client)

# Called when a client sends a message
def message_received(client, server, message):
	info = json.loads(message)
	msgType = info['type']
	if msgType == "authenticate":
		api.authenticate(message)
	elif msgType == "register":
		res = api.registerNewClient(message)
		print res
		server.send_message(client, res)


server = WebsocketServer(PORT)
print 'x'
server.set_fn_new_client(new_client)
print 'y'
server.set_fn_client_left(client_left)
print 'z'
server.set_fn_message_received(message_received)
print 't'
server.run_forever()
