from socket import *

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

running = True
while running:
    message = input("Masukkan kata")
    
    if message.lower() == "exit":
        # Kirim "exit" ke server dulu
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        running = False
        continue

    clientSocket.sendto(message.encode(), (serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("pesan dari server:", modifiedMessage.decode())

clientSocket.close()