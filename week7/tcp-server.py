from socket import *

serverPort = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(5)
print("server Siap menerima koneksi client!! ")
print("Tekan Ctrl+C untuk menghentikan server.")

serverSocket.settimeout(1)

try: 
    while True:
        try:
            connectionSocket, addr = serverSocket.accept()
            print("Client Terhubung: ", addr)
            sentence = connectionSocket.recv(2048).decode()

            print("pesna di terima: ", sentence)

            modifiedSentence = sentence.upper()
            connectionSocket.send(modifiedSentence.encode())

            connectionSocket.close()
        except timeout:
            continue
except KeyboardInterrupt:
    print("Server di hentikan")

finally:
    serverSocket.close()