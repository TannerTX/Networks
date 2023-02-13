from socket import * #import socket module
import sys  # In order to terminate the program
import errno
import os

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        # The Server will be terminated if the client tries /stop
        # Loop will break, the connection is broken
        if filename == "/stop":
            break

        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:

        #Send response message for file not found
        #Fill in start
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

    # This will trigger if the server encounters ^c as input from it's operator
    # Terminate the server
    except KeyboardInterrupt:
        serverSocket.close()
        sys.exit()


serverSocket.close()
sys.exit()
