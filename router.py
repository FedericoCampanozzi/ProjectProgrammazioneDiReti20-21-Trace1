#!/usr/bin/env python3
import socket
import commons
from threading import Thread

class Router:
    
    SERVER_CON = None
    CLIENT_CON = None
    isServerReady = False
    
    def __init__ (self):
        
        self.CLIENT_CON = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.CLIENT_CON.bind((commons.LOCALHOST, commons.ROUTER_UDP_PORT))
        
        self.SERVER_CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER_CON.bind((commons.LOCALHOST, commons.ROUTER_TCP_PORT))
        self.SERVER_CON.listen(1)
        
        print('\n\r router is online')
        
        tClient = Thread(target = self.WaitToReceiveClientsData)
        tServer = Thread(target = self.WaitToServerConnect)
        
        tClient.start()
        tServer.start()
        
        tClient.join()
        tServer.join()
        
        print('\n\r router is offline')
       
    def WaitToReceiveClientsData(self) :       
        print('\n\r waiting to receive message from clients ...')
        
        while True:
            
            data, address = self.CLIENT_CON.recvfrom(4096)
            
            if (self.isServerReady):
                self.SERVER_CON.send(data)
                
    def WaitToServerConnect(self):
        print('\n\r waiting to server connect ...')
          
        connectionSocket, addr = self.SERVER_CON.accept()
        self.isServerReady = True
        self.SERVER_CON = connectionSocket
        
        print('\n\r server connect ...')
        
router = Router()