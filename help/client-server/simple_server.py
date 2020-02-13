# -*- coding: utf-8 -*-
"""
title: How to Write a Server with Python
link: https://www.wikihow.com/Write-a-Server-with-Python
date: Tue Jun 26 20:49:28 2018
@author: Arkadiusz
"""

# import socket

from socket import *
import threading

class roomThread(threading.Thread):
    """ Create a new **thread**.
    This will handle matching 2 clients up with each other.
    Threads are processes that can be running while the main program runs.
    This will set up the variables in the thread so that they can be called later.
    """
    def __init__(self, name, client1IP, client1P, client2IP, client2P, port):
        threading.Thread.__init__(self)
        self.name = name
        self.client1 = (client1IP, client1P)
        self.client2 = (client2IP, client2P)
        self.port = port
        self.done = 0


    def run(self):
        """ Create thread process.
        For clients to communicate directly you need to send to each the other’s information,
        which includes their IP address and which port they are using.
        To do this you must create a **socket** object which can be done with
            variableName = socket(AF_NET, SOCK_DGRAM).
        This will create a socket object that uses the UDP protocol.
        Next **bind** the socket to your IP address with a certain **port** number with
            roomSocket.bind((‘ ‘, self.port))
        The blank area stands for your own pc IP address within your local area network
        and `self.port` assigns the port number that is included when you call this thread.
        The last thing you have to do with this socket is send information through it.
        Since this is a UDP socket you simply must know
        the IP and port of the computer you are sending information to,
        the syntax for sending is
            socketName.sendto(IP, port)
        """
            strServerPort = str(self.port)
            playerNum = 1
            sequence = 0

            roomSocket = socket(AF_INET, SOCK_DGRAM)
            roomSocket.bind(('', self.port))

            roomSocket.sendto(strServerPort, self.client1)
            roomSocket.sendto(strServerPort, self.client2)

            roomSocket.sendto(self.client2[0], self.client1)
            roomSocket.sendto(str(self.client2[1]), self.client1)

            roomSocket.sendto(self.client1[0], self.client2)
            roomSocket.sendto(str(self.client1[1]), self.client2)

            print("done")


""" Create the global variables.
For this step you will need to define several variables, which includes:
    a user list,
    port numbers,
    client count,
    clients for the thread,
    and the room ID.
You will also need to create a socket so that your server can interact with the internet.
This is done by creating a new socket object and binding it to your IP address with a certain port number.
(The port number can be anything but it is usually something high
to avoid having either another process using it or using reserved port numbers.)
"""
userID = 1
userList = ()
userPort = ()
roomID = 1
count = 0
client1 = ()
client2 = ()
done = 0
portNum = 12000
port = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind('', portNum)


""" Create the main server process.
This will take in client address as well as start the thread created earlier.
This includes waiting to receive data from the buffer and getting the client address
and saving it to be used in the thread.
The way to get information from your socket is to call by
    socketName.recvfrom(1024)
the number here is just the amount of bytes that gets read at a time.
In this example we are storing it into a variable called `userAddr`,
and once this happens you can save this address in the list that was created in step 4.
The if statement will create a room thread if two people connect
and will only create a room when two different connections happen.
"""
while True:
    connectReq, userAddr = serverSocket.recv(1024)
    userList += userAddr
    serverSocket.sendto(str(userID), userAddr)
    if userID % 2 == 0 and userID / 2 == roomID:
        pList = list(userList)
        port += 1
        room = roomThread(roomID, pList[count], pList[count+1],
                                  pList[count+2], pList[count+3], port)
        room.start()  #?
        count += 4
        roomID += 1
        print "room created"
    userID += 1

