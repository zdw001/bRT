import socket

# WAN IP: 72.76.113.192
# ricky's 71.172.142.99

class Server:
	HOST = '192.168.1.172' # LAN IP address, use WAN IP adress when communicating from client side
	PORT = 8111 # WAN will use port 80 by default
	response = """\
HTTP/1.1 200 OK

%s"""

	# Configure the server
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __init__(self):
		self.socket.bind((self.HOST, self.PORT)) # bind to socket
		self.socket.listen(1) # listen to socket
		print("Listening on port %s" % self.PORT)

	# handle connections
	def run(self):
		while True:
			client_connection, client_address = self.socket.accept()
			request = client_connection.recv(1024)
			print(request)

			if "please+return+ok" in request:
				http_response = http_response = (self.response % "OK")

			elif "full+name" in request:
				http_response = (self.response % "Zachary Winters")
			
			elif "email+address" in request:
				http_response = http_response = (self.response % "zachwinters1@gmail.com")

			elif "provide+a+url" in request:
				http_response = http_response = (self.response % "http://zwinters.com/static/images/zachary_winters_resume.pdf")

			elif "proof+of+eligibility" in request:
				http_response = http_response = (self.response % "Yes")

			elif "relevant+university" in request:
				http_response = http_response = (self.response % "Electrical Engineering")

			else:
				http_response = http_response = (self.response % "OK")

			client_connection.sendall(bytes(http_response.encode('utf-8')))
			client_connection.close()

# instantiate server
server = Server()
server.run()


   

    
