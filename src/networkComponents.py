#!/usr/bin/env python3
import random
from utilities import Utilities

class NetWorkComponents():
    __IP = None
    __PORT = None
    __MAC = None
    
    def __init__ (self, ip, port, mac):
        self.__IP = ip
        self.__MAC = mac
        self.__PORT = port
    
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
        return self.__IP
    
    def SetIP(self , ip):
        self.__IP = ip
    
    def GetPort(self):
        return self.__PORT
    
    def SetPort(self, port):
        self.__PORT = port
    
    def GetMAC(self):
        return self.__MAC
     
    def SetMAC(self, mac):
        self.__MAC = mac
    
    def __str__(self):
        return (
                "[ IP=" + self.__IP + " " +
                "MAC=" + self.__MAC + " " +
                "PORT=" + str(self.__PORT) + " ]"
            )