from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("server siap digunakan")

running = True
while running:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodeMessage = message.decode()

    if decodeMessage.lower() == "exit":
        print("Server Dimatikan")
        running = False
        continue

    modifiedMessage = decodeMessage.upper()
    print("Server diterima dari ", clientAddress, " Message: ", decodeMessage)

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

# Pindahkan close ke sini, setelah loop selesai
serverSocket.close()