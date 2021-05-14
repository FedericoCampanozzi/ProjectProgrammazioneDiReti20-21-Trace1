#!/usr/bin/env python3
import socket
from datetime import datetime
import random
import commons
from networkComponents import NetWorkComponents
from package import Package

class ClientUDP(NetWorkComponents) :
    ROUTER_CON = None
    ROUTER_NC = None
    
    def __init__(self, myBase, router) :
        
        self.IP = myBase.GetIP()
        self.MAC = myBase.GetMAC()
        self.PORT = myBase.GetPort()
        
        self.ROUTER_CON = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ROUTER_CON.connect((commons.LOCALHOST, commons.ROUTER_UDP_PORT))
        self.ROUTER_NC = router
        
    def SendData(self) :
        data = (
                "DateTime : " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + 
                " Temperature: " + str(random.randint(-1, 30)) + 
                " gradi Humidity : " + str(random.randint(0, 50)) + " %"
            )
        
        p = Package()
        p.SetSource(NetWorkComponents(self.IP, self.PORT, self.MAC))
        p.SetDestination(self.ROUTER_NC)
        p.SetProtocol("UDP")
        p.SetMessage(data)
        self.ROUTER_CON.send(p.Encode())
        print("\n\r CLIENT -- PC [" + p.GetSource().GetIP() + "] send data")