#!/usr/bin/env python3
import socket
import random
from datetime import datetime
from utilities import Utilities
from networkComponents import NetWorkComponents
from package import Package

class ClientUDP(NetWorkComponents) :
    __ROUTER_CON = None
    __ROUTER_NC = None
    
    def __init__(self, myBase, router) :
        
        self.IP = myBase.GetIP()
        self.MAC = myBase.GetMAC()
        self.PORT = myBase.GetPort()
        
        self.__ROUTER_CON = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__ROUTER_CON.connect((Utilities.LOCALHOST, Utilities.ROUTER_UDP_PORT))
        self.__ROUTER_NC = router
        
    def SendData(self) :
        data = (
                " DateTime : " + datetime.today().strftime(Utilities.DATE_TIME_FORMAT) + 
                " Temperature: " + str(random.randint(-1, 30)) + 
                " gradi Humidity : " + str(random.randint(0, 50)) + " %"
            )
        
        package = Package()
        package.SetSource(NetWorkComponents(self.IP, self.PORT, self.MAC))
        package.SetDestination(self.__ROUTER_NC)
        package.SetProtocol("UDP")
        package.SetMessage(data)
        package.SetDeltaTime(datetime.today())
        self.__ROUTER_CON.send(package.Encode())
        Utilities.Write("\n CLIENT -- " + str(package))
    
    def Close(self) :
        Utilities.PrintAndWrite('\n CLIENT -- Close Connections')
        self.__ROUTER_CON.close()