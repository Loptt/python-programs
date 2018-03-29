import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '192.168.11.150'

# def pscan(port):
# 	try:
# 		s.connect((server,port))
# 		return True
# 	except:
# 		return False

# for x in range(1,81):
# 	if pscan(x):
# 		print("Port",x,"is open")
# 	else:
# 		print("Port",x,"is closed")


port = 1

request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

s.send(request.encode())

result = s.recv(4096)

while (len(result) > 0):
	print(result)
	result = s.recv(4096)