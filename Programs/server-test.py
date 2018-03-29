import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ('192.168.11.113', 5000)

s.bind(server_adress)
s.listen(1)

while True:

	conn, cli_adress = s.accept()
	try:
		message = conn.recv(4096)

		if message.decode() == "quit":
			break
			
		print(message.decode())


	except:
		conn.close()
