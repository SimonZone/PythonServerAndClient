from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

keep_communicating = True

while keep_communicating:
    sentence = input('Input sentence: ')
    if sentence == "close":
        keep_communicating = False
    else:
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024).decode().strip()
        print('From server: ', modifiedSentence)
        if modifiedSentence == "close":
            print("here")
            keep_communicating = False
clientSocket.close()