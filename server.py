#!/usr/bin/env python3
import socket
import commons

class ServerTCP:
    
    CON = None
    
    def __init__ (self):  
        self.CON = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.CON.connect((commons.LOCALHOST, commons.ROUTER_TCP_PORT))
        print('\n\r server is online')
        
        while True:
            message = self.CON.recv(1024)
            
            if len(message) > 0 :
                print("Receive from router " + message.decode('utf8'))
            
server = ServerTCP()