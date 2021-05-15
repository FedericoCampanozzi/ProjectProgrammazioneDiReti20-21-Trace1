#!/usr/bin/env python3
import socket
import threading
import commons
from utilities import Utilities
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
        
        Utilities.PrintAndWrite('\n ROUTER -- Router is Online')
        
        tClient = threading.Thread(target = self.WaitToReceiveClientsData)
        tServer = threading.Thread(target = self.WaitToServerConnect)
        
        tClient.start()
        tServer.start()
        
        tClient.join()
        tServer.join()
        
        Utilities.PrintAndWrite('\n ROUTER -- Router is Offline')
       
    def WaitToReceiveClientsData(self) :       
        Utilities.PrintAndWrite('\n ROUTER -- Waiting to receive message from clients ...')

        while not commons.EXIT_DAEMON :
            try :
                
                data, address = self.CLIENT_CON.recvfrom(commons.BUFFER_SIZE)
                package = Package.DecodePackage(data)
                
                Utilities.Write("\n ROUTER -- " + str(package))                    
                
                package.SetSource(NetWorkComponents(self.IP, self.PORT, self.MAC))
                package.SetDestination(self.SERVER_NC)
                package.SetProtocol("TCP")
                
                self.SERVER_CON.send(package.Encode())
                
            except Exception as e :
                Utilities.PrintAndWrite('\n ROUTER -- Error Message : ' + str(e))
                self.Close()
                break
            
        self.Close()
        
    def WaitToServerConnect(self):
        Utilities.PrintAndWrite('\n ROUTER -- waiting to server connect ...')
          
        connectionSocket, addr = self.SERVER_CON.accept()
        self.SERVER_CON = connectionSocket
        
        Utilities.PrintAndWrite('\n ROUTER -- Server Connect ...')
        
    def Close(self) :
        Utilities.PrintAndWrite('\n ROUTER -- Close Connections')
        self.SERVER_CON.close()
        self.CLIENT_CON.close()