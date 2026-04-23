from socket import *

serverName = "localhost"
serverPort = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)

#koneksi ke server
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase Sentence: ")

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(2048)
print("From Server: ", modifiedSentence.decode())

clientSocket.close()