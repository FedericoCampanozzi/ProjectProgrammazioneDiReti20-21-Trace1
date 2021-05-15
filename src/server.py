#!/usr/bin/env python3
import socket
import threading
import commons
from package import Package
from networkComponents import NetWorkComponents
from utilities import Utilities

class ServerTCP(NetWorkComponents):
    
    CON = None
    
    def __init__ (self, myBase):
        
        self.IP = myBase.GetIP()
        self.MAC = myBase.GetMAC()
        self.PORT = myBase.GetPort()
        
        self.CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.CON.connect((commons.LOCALHOST, commons.ROUTER_TCP_PORT))
        
        tServer = threading.Thread(target = self.WaitToReceiveRouterData)
        tServer.start()
        
        Utilities.PrintAndWrite('\n SERVER -- Server is Online')
        
        tServer.join()
        
    def WaitToReceiveRouterData(self) : 
        while not commons.EXIT_DAEMON:
            try:
                data = self.CON.recv(commons.BUFFER_SIZE)
                
                if len(data) > 0 :
                    package =  Package.DecodePackage(data)
                    Utilities.Write("\n SERVER -- " + str(package))
                    
            except Exception as e :
                Utilities.PrintAndWrite('\n SERVER -- Error Message : ' + str(e))
                self.Close()
                break
            
        self.Close()
        
    def Close(self):
        Utilities.PrintAndWrite('\n SERVER -- Close Connections')
        self.CON.close()