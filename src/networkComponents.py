#!/usr/bin/env python3
import random

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
    def RandomNetWorkComponents ():
        mac = ""
        
        for i in range(0,6) :
            mac += str(random.randint(0, 255)) + ":"
        
        mac = mac[:-1]
        
        ip = "192.168.1." + str(random.randint(1, 25))
        port = random.randint(10_000, 65_536)
        
        print("\n\r NC -- MAC : " + mac + " IP : " + ip + " PORT : " + str(port) )
        
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
                "IP : " + self.IP + " " +
                "MAC : " + self.MAC + " " +
                "PORT : " + str(self.PORT)
            )