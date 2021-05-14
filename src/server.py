#!/usr/bin/env python3
import socket
import commons
from package import Package
from networkComponents import NetWorkComponents

class ServerTCP(NetWorkComponents):
    
    CON = None
    
    def __init__ (self, myBase):
        
        self.IP = myBase.GetIP()
        self.MAC = myBase.GetMAC()
        self.PORT = myBase.GetPort()
        
        self.CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.CON.connect((commons.LOCALHOST, commons.ROUTER_TCP_PORT))
        print('\n\r SERVER -- Server is Online')
    
        while True:
            data = self.CON.recv(1024)
            
            if len(data) > 0 :
                print("\n\r SERVER -- Receive from router " + str(Package.DecodePackage(data)) )