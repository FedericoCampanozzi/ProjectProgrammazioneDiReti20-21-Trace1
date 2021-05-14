#!/usr/bin/env python3
from networkComponents import NetWorkComponents

class Package ():
    
    SOURCE = NetWorkComponents.EmptyNetWorkComponents()
    DESTINATION = NetWorkComponents.EmptyNetWorkComponents()
    PROTOCOL = ""
    MESSAGE = ""
    
    def __init__(self):
        self.PROTOCOL = ""
        self.MESSAGE + ""
    
    def GetSource(self) :
        return self.SOURCE
    
    def SetSource(self, source):
        self.SOURCE = source
        
    def GetDestination(self) :
        return self.DESTINATION
    
    def SetDestination(self, destination):
        self.DESTINATION = destination
        
    def SetProtocol(self, protocol):
        self.PROTOCOL = protocol
        
    def GetProtocol(self):
        return self.PROTOCOL
    
    def SetMessage(self, message):
        self.MESSAGE = message
        
    def GetMessage(self):
        return self.MESSAGE
    
    def Encode(self) :
        return (
                self.SOURCE.GetIP() + ";" + 
                self.DESTINATION.GetIP() + ";" + 
                self.SOURCE.GetMAC() + ";" + 
                self.DESTINATION.GetMAC() +  ";" + 
                str(self.SOURCE.GetPort()) + ";" +
                str(self.DESTINATION.GetPort()) + ";" + 
                self.PROTOCOL + ";" + 
                self.MESSAGE
            ).encode('utf8')
    
    @staticmethod  
    def DecodePackage(data) :
        vet = data.decode('utf8').split(";")
        p = Package()
        p.SOURCE.SetIP(vet[0])
        p.DESTINATION.SetIP(vet[1])
        p.SOURCE.SetMAC(vet[2])
        p.DESTINATION.SetMAC(vet[3])
        p.SOURCE.SetPort(int(vet[4]))
        p.DESTINATION.SetPort(int(vet[5]))
        p.SetProtocol(vet[6])
        p.SetMessage(vet[7])
        return p
    
    def __str__(self) :
        return (
                "\n\r\r SOURCE_IP -> " + self.SOURCE.GetIP()  + ""
                "\n\r\r DEST_IP -> " + self.DESTINATION.GetIP() + ""
                "\n\r\r SOURCE_MAC -> " + self.SOURCE.GetMAC()  + ""
                "\n\r\r DEST_MAC -> " + self.DESTINATION.GetMAC() + ""
                "\n\r\r SOURCE_PORT -> " + str(self.SOURCE.GetPort()) + ""
                "\n\r\r DEST_PORT -> " + str(self.DESTINATION.GetPort()) + ""
                "\n\r\r PROTOCOL -> " + self.PROTOCOL + ""
                "\n\r\r MESSAGE -> " + self.MESSAGE
            )