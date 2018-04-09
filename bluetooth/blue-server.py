import socket
import threading

class Server:

	s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

	#Server unique MAC address
	server_address = "ec:35:86:2e:b9:1c"
	port = 5

	#List of active connections
	connections = []

	def __init__(self):

		try:
			self.s.bind((self.server_address, self.port))
			self.s.listen(5)

		except socket.error as e:
			print(str(e))

	def handle_connection(self, conn, conn_address):

		while True:

			data = conn.recv(1024)

			if not data:
				conn.close()
				self.connections.remove(conn)
				break

	def run(self):
		print("Initializing server...")

		while True:
			conn, conn_address = self.s.accept()
			thread = threading.Thread(target=self.handle_connection, args=(conn,address))
			thread.daemon = True
			thread.start()

			self.connections.append(conn)


server = Server()
server.run()

		