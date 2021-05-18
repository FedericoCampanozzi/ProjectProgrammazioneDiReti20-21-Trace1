#!/usr/bin/env python3
import socket
import threading
from package import Package
from networkComponents import NetWorkComponents
from utilities import Utilities

class ServerTCP(NetWorkComponents):
    
    __CON = None
    
    def __init__ (self, myBase):
        
        self.IP = myBase.GetIP()
        self.MAC = myBase.GetMAC()
        self.PORT = myBase.GetPort()
        
        self.__CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__CON.connect((Utilities.LOCALHOST, Utilities.ROUTER_TCP_PORT))
        
        tServer = threading.Thread(target = self.__WaitToReceiveRouterData__)
        tServer.start()
        
        Utilities.PrintAndWrite('\n SERVER -- Server is Online')
        
        tServer.join()
        
    def __WaitToReceiveRouterData__(self) : 
        while not Utilities.EXIT_DAEMON:
            try:
                data = self.__CON.recv(Utilities.BUFFER_SIZE)
                
                if len(data) > 0 :
                    package =  Package.DecodePackage(data)
                    Utilities.Write("\n SERVER -- " + str(package))
                    
            except Exception as e :
                Utilities.PrintAndWrite('\n SERVER -- Error Message : ' + str(e))
                self.__Close__()
                break
            
        self.__Close__()
        
    def __Close__(self):
        Utilities.PrintAndWrite('\n SERVER -- Close Connections')
        self.__CON.close()