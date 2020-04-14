from socket import * 
from datetime import datetime
from time import time

serverName = '10.0.0.161'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) #created a client side socket
clientSocket.settimeout(1)   # set the timeout at 1 second

counter = 0 #variable that tracks the sequence number
loss = 0 #variable that tracks the number of loss pkts

while (counter < 10):
    message = "sample text"
    sentTime = datetime.now() #assign current time to a variable 
    counter += 1
    try:
        clientSocket.sendto(bytes(message,"UTF-8"),(serverName,serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024) #receives msg from server
        elapsedTimeInSec = (datetime.now()-sentTime).microseconds/1000
        print('Ping ' + str(counter) + ': <Sent Message - ' + message + '>, <Recieved Message - ' + str(modifiedMessage) + '>, <RTT - ' + str(elapsedTimeInSec) + '>')

    except timeout:
        loss +=1
        print('*** Request Time Out. ***')

lossPercent = loss*10
print('Packet Loss:' +str(lossPercent)+ '%')


clientSocket.close()