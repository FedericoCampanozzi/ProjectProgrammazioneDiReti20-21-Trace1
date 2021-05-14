#!/usr/bin/env python3
import socket
import commons
from threading import Thread
from package import Package

class Router:
    
    SERVER_CON = None
    CLIENT_CON = None
    
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
        while True :
            try :
                data, address = self.CLIENT_CON.recvfrom(4096)
                package = Package.DecodePackage(data)
                package.SetDestinationMAC("00:00:00:00:00:00")
                package.SetDestinationIP("10.10.10.0")
                package.SetDestinationPort(commons.ROUTER_TCP_PORT)
                package.SetProtocol("TCP")
                self.SERVER_CON.send(package.Encode())
            except Exception as e :
                print('\n\r server disconnect')
                print('Error Message : ' + str(e))
                break
                
    def WaitToServerConnect(self):
        print('\n\r waiting to server connect ...')
          
        connectionSocket, addr = self.SERVER_CON.accept()
        self.SERVER_CON = connectionSocket
        
        print('\n\r server connect ...')
        
router = Router()