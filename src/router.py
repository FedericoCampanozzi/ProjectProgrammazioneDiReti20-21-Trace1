#!/usr/bin/env python3
import socket
import commons
from threading import Thread
from package import Package
from networkComponents import NetWorkComponents

class Router(NetWorkComponents):
    
    SERVER_CON = None
    CLIENT_CON = None
    
    SERVER_NC = None
    
    def __init__ (self, myBase, server):
        
        self.IP = myBase.GetIP()
        self.MAC = myBase.GetMAC()
        self.PORT = myBase.GetPort()
        
        self.CLIENT_CON = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.CLIENT_CON.bind((commons.LOCALHOST, commons.ROUTER_UDP_PORT))
        
        self.SERVER_CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER_CON.bind((commons.LOCALHOST, commons.ROUTER_TCP_PORT))
        self.SERVER_CON.listen(1)
        
        self.SERVER_NC = server
        
        print('\n\r ROUTER -- Router is Online')
        
        tClient = Thread(target = self.WaitToReceiveClientsData)
        tServer = Thread(target = self.WaitToServerConnect)
        
        tClient.start()
        tServer.start()
        
        tClient.join()
        tServer.join()
        
        print('\n\r ROUTER -- Router is Offline')
       
    def WaitToReceiveClientsData(self) :       
        print('\n\r ROUTER -- Waiting to receive message from clients ...')
        
        while True :
            try :
                data, address = self.CLIENT_CON.recvfrom(4096)
                
                package = Package.DecodePackage(data)
                package.SetSource(NetWorkComponents(self.IP, self.PORT, self.MAC))
                package.SetDestination(self.SERVER_NC)
                package.SetProtocol("TCP")
                
                self.SERVER_CON.send(package.Encode())
            except Exception as e :
                print('\n\r ROUTER -- Error Message : ' + str(e))
                break
                
    def WaitToServerConnect(self):
        print('\n\r ROUTER -- waiting to server connect ...')
          
        connectionSocket, addr = self.SERVER_CON.accept()
        self.SERVER_CON = connectionSocket
        
        print('\n\r ROUTER -- Server Connect ...')