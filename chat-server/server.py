import socket
import sys
from _thread import *

host = ""
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAdress = (host, port)

try:
	s.bind(serverAdress)

except socket.error as e:
	print(str(e))

s.listen(5)

print("Waiting for connections...")

def threadedClient(conn):
	conn.send(str.encode("Welcome! Type your message\n"))

	while True:
		data = conn.recv(2048)
		reply = "Server output: " + data.decode()

		if not data:
			break

		conn.sendall(str.encode(reply))

	conn.close()

while True:

	conn, address = s.accept()
	print("Connected to: "+address[0]+":"+str(address[1]))

	start_new_thread(threadedClient, (conn,))

