from websocket_server import WebsocketServer

def new_message(client, server, message):
	print(f'new message received: {message}')

server = WebsocketServer(host='127.0.0.1', port=13254)
server.set_fn_message_received(new_message)
server.run_forever()