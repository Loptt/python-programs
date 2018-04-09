import socket
import threading

class Client:
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    server_address = "b8:27:eb:0c:22:3f"
    port = 5
    message = ""

    def __init__(self):
        try:
            self.s.connect((self.server_address,self.port))
        except socket.error as e:
            print(str(e))

    def send_message(self):

        while True:
            self.message = input("Message: ")
            self.s.sendall(message.encode())

            if self.message == "exit":
                break

    def run(self):

        thread = threading.Thread(target=self.send_message)

        while True:
            data = self.s.recv(1024)

            if not data:
                break

            print("\n",data.decode())

            if self.message == "exit":
                break

client = Client()
client.run()