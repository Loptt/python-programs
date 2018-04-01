import socket
from time import sleep

def welcome():
	print("Welcome, please enter the adress of the connection you want to reach")

	address = input("Address: ")
	port = input("Port: ")

	print("Connecting to "+address+":"+port+"...")

	return (address, int(port))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = welcome()

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(server_address)
except:
	print("An error has ocurred")
	sleep(2)

while True:
	serverMessage = s.recv(2048)
	print(serverMessage.decode())

	message = input("Message: ")
	s.sendall(message.encode())

	if message=="quit":
		break

sleep(1)

s.close()
