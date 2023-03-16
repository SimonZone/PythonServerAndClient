from socket import *
from threading import *

def handleClient(connectionSocket, addr):
    print(addr)
    keepcommunicating = True
    # Uses connection make a socket connection and recieve
    # decode() function decodes data

    while keepcommunicating:
        sentence = connectionSocket.recv(1024).decode()
        print(addr[0])
        print(sentence)
        processedSentence = processString(sentence)
        
        if processedSentence == "close;":
            keepcommunicating = False
            break
            
        if validSentance(processedSentence):
            if processedSentence.startswith("upper:"):
                processedSentence = toUpper(processedSentence)
            elif processedSentence.startswith("lower:"):
                processedSentence = toLower(processedSentence)
            elif processedSentence.startswith("reverse:"):
                processedSentence = toReverse(processedSentence)

        connectionSocket.send(processedSentence.encode())
    
    closeMessage = "close"        
    connectionSocket.send(closeMessage.encode())
    print("Connection stopped")
    connectionSocket.close()

def processString(sentance):
    sentance = sentance.strip()
    sentance = sentance.lower()
    return sentance
    
def toUpper(sentance):
    sentance = message(sentance)
    sentance = sentance.upper()
    return sentance

def toLower(sentance):
    sentance = message(sentance)
    sentance = sentance.lower()
    return sentance

def toReverse(sentance):
    sentance = message(sentance)
    sentance = sentance[::-1]
    return sentance

def validSentance(sentance):
    if sentance.find(";") >= 1:
        return True
    else: False

def message(sentance):
    sentance = sentance.split(": ")
    sentance = sentance[1]
    sentance = sentance.split(";")
    return sentance[0]
    
# Port that client needs
serverPort = 12000
# AF_INET: IPv4
# SOCK_STREAM: stream of content
serverSocket = socket(AF_INET,SOCK_STREAM)
# "": IP address, blank = all ip can access in my server
# serverPort: port of my server
serverSocket.bind(("",serverPort))
# waiting for client
serverSocket.listen(1)
print("The server is ready to receive")
while True:
    # Wait for connected client
    connectionSocket, addr = serverSocket.accept()
    Thread(target=handleClient, args=(connectionSocket, addr)).start()