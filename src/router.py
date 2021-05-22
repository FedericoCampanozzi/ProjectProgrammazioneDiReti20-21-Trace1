#!/usr/bin/env python3
import socket
import threading
from datetime import datetime
from utilities import Utilities
from package import Package
from networkComponents import NetWorkComponents

class Router(NetWorkComponents):
    
    __SERVER_CON = None
    __CLIENT_CON = None
    __SERVER_NC = None

    def __init__ (self, myBase, server):
        
        self.IP = myBase.GetIP()
        self.MAC = myBase.GetMAC()
        self.PORT = myBase.GetPort()
        
        self.__CLIENT_CON = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__CLIENT_CON.bind((Utilities.LOCALHOST, Utilities.ROUTER_UDP_PORT))
        
        self.__SERVER_CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__SERVER_CON.bind((Utilities.LOCALHOST, Utilities.ROUTER_TCP_PORT))
        self.__SERVER_CON.listen(1)
        
        self.__SERVER_NC = server
        
        Utilities.PrintAndWrite('\n ROUTER -- Router is Online')
        
        tClient = threading.Thread(target = self.__WaitToReceiveClientsData__)
        tServer = threading.Thread(target = self.__WaitToServerConnect__)
        
        tClient.start()
        tServer.start()
        
        tClient.join()
        tServer.join()
        
        Utilities.PrintAndWrite('\n ROUTER -- Router is Offline')
       
    def __WaitToReceiveClientsData__(self) :       
        Utilities.PrintAndWrite('\n ROUTER -- Waiting to receive message from clients ...')

        while not Utilities.EXIT_DAEMON :
            try :
                
                data, address = self.__CLIENT_CON.recvfrom(Utilities.BUFFER_SIZE)
                package = Package.DecodePackage(data)
                
                Utilities.Write("\n ROUTER -- " + str(package) +
                                "\n\t\t DELTA TIME : " + Utilities.DateDifference(package.GetDeltaTime(), datetime.today()))       
                
                package.SetSource(NetWorkComponents(self.IP, self.PORT, self.MAC))
                package.SetDestination(self.__SERVER_NC)
                package.SetProtocol("TCP")
                package.SetDeltaTime(datetime.today())
                
                self.__SERVER_CON.send(package.Encode())
                
            except Exception as e :
                Utilities.PrintAndWrite('\n ROUTER -- Error Message : ' + str(e))
                self.__Close__()
                break
            
        self.__Close__()
        
    def __WaitToServerConnect__(self):
        Utilities.PrintAndWrite('\n ROUTER -- waiting to server connect ...')
          
        connectionSocket, addr = self.__SERVER_CON.accept()
        self.__SERVER_CON = connectionSocket
        
        Utilities.PrintAndWrite('\n ROUTER -- Server Connect ...')
        
    def __Close__(self) :
        Utilities.PrintAndWrite('\n ROUTER -- Close Connections')
        self.__SERVER_CON.close()
        self.__CLIENT_CON.close()