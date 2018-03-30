import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ('192.168.11.113', 5000)

while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(server_adress)
		message = input("Message: ")

		s.sendall(message.encode())

		if message=="quit":
			break
	except:
		print("An error has ocurred")
		break
sleep(1)


s.close()