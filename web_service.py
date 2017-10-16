import socket
import re

# WAN IP: 72.76.113.192

class Server:
	HOST = '192.168.1.155' # LAN IP address, use WAN IP adress when communicating from client side
	PORT = 8111 # WAN will use port 80 by default
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Configure the server
	response = """\
HTTP/1.1 200 OK

%s"""
	
	def __init__(self):
		self.socket.bind((self.HOST, self.PORT)) # bind to socket
		self.socket.listen(1) # listen to socket
		print("Listening on port %s" % self.PORT)

	# handle connections
	def run(self):
		while True:
			client_connection, client_address = self.socket.accept()
			request = client_connection.recv(1024)

			if "Ping" in request:
				http_response = (self.response % "OK")

			elif "Name" in request:
				http_response = (self.response % "Zachary Winters")
			
			elif "Email+Address" in request:
				http_response = (self.response % "zachwinters1@gmail.com")

			elif "Resume" in request:
				http_response = (self.response % "http://zwinters.com/static/images/zachary_winters_resume.pdf")

			elif "Status" in request:
				http_response = (self.response % "Yes")

			elif "Degree" in request:
				http_response = (self.response % "Electrical Engineering")

			elif "Years" in request:
				http_response = (self.response % "2 years")

			elif "Referrer" in request:
				http_response = (self.response % "I was referred by an Engine Media employee, Beth Stirling.")

			elif "Position" in request:
				http_response = (self.response % "Software Engineer")

			elif "Puzzle" in request:
				print(request)
				LF = "%0A"
				puzzle = []

				pairs = {0:'A', 1:'B', 2:'C', 3:'D'}
				percent_pairs = {"%3E": ">", "%3C": "<", "%3D": "="}

				scores = {'A':0, 'B':0, 'C':0, 'D':0}

				# turn the request into a readable format
				LFindices = [i.start() for i in re.finditer(LF, request)] # finds all iterations of %0A
				
				for i in LFindices:
				    puzzle.append(request[(i+4):(i+10)]) # add the PE lines to puzzle, ie A--%3E-
				puzzle = puzzle[1:5]

				print(puzzle)

				l1 = []
				l2 = []
				l3 = []
				l4 = []

				l_total = []

				letter = 0

				# format [[C < A], [B < D], D < B]]
				for i in puzzle:
				    if letter == 0:
				        if "%3C" in puzzle[letter]:
				            l1.append(letter)
				            other_letter = puzzle[letter].index("%3C")
				            l1.append(other_letter)
				        elif "%3E" in puzzle[letter]:
				            other_letter = puzzle[letter].index("%3E")
				            l1.append(other_letter)
				            l1.append(letter)
				        elif "%3D" in puzzle[letter]:
				            l1 = []
				        letter += 1
				    if letter == 1:
				        if "%3C" in puzzle[letter]:
				            l2.append(letter)
				            other_letter = puzzle[letter].index("%3C")
				            l2.append(other_letter)
				        elif "%3E" in puzzle[letter]:
				            other_letter = puzzle[letter].index("%3E")
				            l2.append(other_letter)
				            l2.append(letter)
				        elif "%3D" in puzzle[letter]:
				            l2 = []
				        letter += 1
				    if letter == 2:
				        if "%3C" in puzzle[letter]:
				            l3.append(letter)
				            other_letter = puzzle[letter].index("%3C")
				            l3.append(other_letter)
				        elif "%3E" in puzzle[letter]:
				            other_letter = puzzle[letter].index("%3E")
				            l3.append(other_letter)
				            l3.append(letter)
				        elif "%3D" in puzzle[letter]:
				            l3 = []
				        letter += 1
				    if letter == 3:
				        if "%3C" in puzzle[letter]:
				            l4.append(letter)
				            other_letter = puzzle[letter].index("%3C")
				            l4.append(other_letter)
				        elif "%3E" in puzzle[letter]:
				            other_letter = puzzle[letter].index("%3E")
				            l4.append(other_letter)
				            l4.append(letter)
				        elif "%3D" in puzzle[letter]:
				            l4 = []
				        letter += 1

				l_total.append(l1)
				l_total.append(l2)
				l_total.append(l3)
				l_total.append(l4)

				# get rid of item that doesnt tell us anything
				for i in l_total:
				    if i == []:
				        l_total.remove(i)
				        
				# A=0, B=1, C=2, D=3

				# initialize final list as the first pair in l_total
				final_list = l_total[0]

				print(l_total)

				loops = 0
				not_in = 0

				# while len(final_list) < 4:
				while loops < 10:
					# enumerate creates keys for each value
					# iterate over each sublist (ie [0,3]) in the list of lists
				    for IDX, VAL in enumerate(l_total):
				    	# iterate over each element in our output list (the list that will have all 4 letters together)
				        for idx, val in enumerate(final_list):
				        	# prevent error when index of final list gets > 1 (using idx to reference VAL)
				            if idx < 2:
				            	# if neither of the values of the sublist are in final_list, skip and put
				            	# the sublist at the end of the list to check again
				            	for i in VAL:
				            		if i not in final_list:
				            			not_in += 1
				            	if not_in == 2:
				            		l_total.append(VAL)
				                if VAL[idx] in final_list:
				                	pass
				                # iterating over final list, if the element is in the second position
							    # in an l_total list, add the element that is less than that to the front of 
							    # final list
				                elif final_list[idx] == l_total[IDX][1]:
				                    final_list.insert((idx),l_total[IDX][0])
				                # if the element is in the first position (ie less than the 2nd position) add the
							    # second position to the end of final_list
				                elif final_list[idx] == l_total[IDX][0]:
				                    final_list.append(l_total[IDX][1])
				            # need to keep filling final_list after it gets its third value
				            elif idx >= 2:
				            	for i in range(2):
									if VAL[i] in final_list:
										pass
									elif final_list[idx] == l_total[IDX][1]:
										final_list.insert((idx), l_total[IDX][0])
									elif final_list[idx] == l_total[IDX][0]:
										final_list.append(l_total[IDX][1])
					loops += 1

				print(final_list)

				answers = ''

				# order final_list in A, B, C, D
				values = [final_list.index(0), final_list.index(1), final_list.index(2), final_list.index(3)]
				values_top = values

				# use values as a key to build answer
				for i in values:
					for j in values_top:
						if i == j:
							answers += '='
						if i < j:
							answers += '<'
						if i > j:
							answers += '>'

				response_string = " ABCD\nA%s\nB%s\nC%s\nD%s" % (answers[0:4], answers[4:8], answers[8:12], answers[12:16])
				http_response = (self.response % response_string)

			elif "Source" in request:
				http_response = http_response = (self.response % "https://github.com/zdw001/bRT/blob/master/web_service.py")

			elif "Phone" in request:
				http_response = http_response = (self.response % "(609)744-1172")			

			else:
				http_response = http_response = (self.response % "Sorry I don't understand that question")

			client_connection.sendall(bytes(http_response.encode('utf-8')))
			client_connection.close()

# instantiate server
server = Server()
server.run()






   

    
