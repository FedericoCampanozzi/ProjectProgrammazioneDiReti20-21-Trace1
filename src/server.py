#!/usr/bin/env python3
import socket
import commons
import sys 
import signal
from package import Package

class ServerTCP:
    
    CON = None
    
    def __init__ (self):  
        self.CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.CON.connect((commons.LOCALHOST, commons.ROUTER_TCP_PORT))
        print('\n\r server is online')
        
        signal.signal(signal.SIGINT, self.KillServer)
        while True:
            data = self.CON.recv(1024)
            
            if len(data) > 0 :
                print("Receive from router " + str(Package.DecodePackage(data)))
    
    def KillServer(self, signal, frame):
        print('Server killed')
        sys.exit(0) 

server = ServerTCP()