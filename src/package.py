#!/usr/bin/env python3
from networkComponents import NetWorkComponents

class Package ():
    
    __SOURCE = NetWorkComponents.EmptyNetWorkComponents()
    __DESTINATION = NetWorkComponents.EmptyNetWorkComponents()
    __PROTOCOL = ""
    __MESSAGE = ""
    
    def __init__(self):
        self.__PROTOCOL = ""
        self.__MESSAGE = ""
    
    def GetSource(self) :
        return self.__SOURCE
    
    def SetSource(self, source):
        self.__SOURCE = source
        
    def GetDestination(self) :
        return self.__DESTINATION
    
    def SetDestination(self, destination):
        self.__DESTINATION = destination
        
    def SetProtocol(self, protocol):
        self.__PROTOCOL = protocol
        
    def GetProtocol(self):
        return self.__PROTOCOL
    
    def SetMessage(self, message):
        self.__MESSAGE = message
        
    def GetMessage(self):
        return self.__MESSAGE
    
    def Encode(self) :
        return (
                self.__SOURCE.GetIP() + ";" + 
                self.__DESTINATION.GetIP() + ";" + 
                self.__SOURCE.GetMAC() + ";" + 
                self.__DESTINATION.GetMAC() +  ";" + 
                str(self.__SOURCE.GetPort()) + ";" +
                str(self.__DESTINATION.GetPort()) + ";" + 
                self.__PROTOCOL + ";" + 
                self.__MESSAGE
            ).encode('utf8')
    
    @staticmethod  
    def DecodePackage(data) :
        vet = data.decode('utf8').split(";")
        p = Package()
        p.GetSource().SetIP(vet[0])
        p.GetDestination().SetIP(vet[1])
        p.GetSource().SetMAC(vet[2])
        p.GetDestination().SetMAC(vet[3])
        p.GetSource().SetPort(int(vet[4]))
        p.GetDestination().SetPort(int(vet[5]))
        p.SetProtocol(vet[6])
        p.SetMessage(vet[7])
        return p
    
    def __str__(self) :
        return ("\n\t\t SOURCE : " + str(self.__SOURCE) +
                "\n\t\t DESTINATION : " + str(self.__DESTINATION) +
                "\n\t\t DATA : " + self.__MESSAGE + 
                "\n\t\t PROTOCOL : " +  self.__PROTOCOL )