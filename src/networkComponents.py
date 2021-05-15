#!/usr/bin/env python3
import random
from utilities import Utilities

class NetWorkComponents():
    IP = None
    PORT = None
    MAC = None
    
    def __init__ (self, ip, port, mac):
        self.IP = ip
        self.MAC = mac
        self.PORT = port
    
    @staticmethod
    def EmptyNetWorkComponents ():
        return NetWorkComponents("0.0.0.0", -1, "00:00:00:00:00:00")
        
    @staticmethod
    def RandomNetWorkComponentsWithoutPort (port):
        mac = ""        
        for i in range(0, 6) :
            mac += (Utilities.Hex(random.randint(0, 15)) + Utilities.Hex(random.randint(0, 15)) + ":")       
        mac = mac[:-1]        
        ip = "192.168.1." + str(random.randint(10, 35))       
        return NetWorkComponents(ip, port, mac)
        
    def GetIP(self):
        return self.IP
    
    def SetIP(self , ip):
        self.IP = ip
    
    def GetPort(self):
        return self.PORT
    
    def SetPort(self, port):
        self.PORT = port
    
    def GetMAC(self):
        return self.MAC
     
    def SetMAC(self, mac):
        self.MAC = mac
    
    def __str__(self):
        return (
                "[ IP=" + self.IP + " " +
                "MAC=" + self.MAC + " " +
                "PORT=" + str(self.PORT) + " ]"
            )