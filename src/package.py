#!/usr/bin/env python3

class Package ():
    
    SOURCE_IP = ""
    DEST_IP = ""
    SOURCE_MAC = ""
    DEST_MAC = ""
    SOURCE_PORT = 0
    DEST_PORT = 0
    PROTOCOL = ""
    MESSAGE = ""
    
    def __init__(self):
        self.SOURCE_IP = ""
        self.DEST_IP = ""
        self.SOURCE_MAC = ""
        self.DEST_MAC = ""
        self.SOURCE_PORT = 0
        self.DEST_PORT = 0
        self.PROTOCOL = ""
        self.MESSAGE + ""
        
    def SetSourceIP(self, ip):
        self.SOURCE_IP = ip
    def GetSourceIP(self):
        return self.SOURCE_IP
    
    def SetDestinationIP(self, ip):
        self.DEST_IP = ip
    def GetDestinationIP(self):
        return self.DEST_IP
    
    def SetSourceMAC(self, mac):
        self.SOURCE_MAC = mac
    def GetSourceMAC(self):
        return self.SOURCE_MAC
    
    def SetDestinationMAC(self, mac):
        self.DEST_MAC = mac
    def GetDestinationMAC(self):
        return self.DEST_MAC
    
    def SetSourcePort(self, port):
        self.SOURCE_PORT = port
    def GetSourcePort(self):
        return self.SOURCE_PORT
    
    def SetDestinationPort(self, port):
        self.DEST_PORT = port
    def GetDestinationPort(self):
        return self.DEST_PORT
    
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
            self.SOURCE_IP + ";" + 
            self.DEST_IP + ";" + 
            self.SOURCE_MAC + ";" + 
            self.DEST_MAC +  ";" + 
            str(self.SOURCE_PORT) + ";" +
            str(self.DEST_PORT) + ";" + 
            self.PROTOCOL + ";" + 
            self.MESSAGE ).encode('utf8')
    
    @staticmethod  
    def DecodePackage(data) :
        vet = data.decode('utf8').split(";")
        #print("vettore splittato : " + str(vet))
        p = Package()
        p.SetSourceIP(vet[0])
        p.SetDestinationIP(vet[1])
        p.SetSourceMAC(vet[2])
        p.SetDestinationMAC(vet[3])
        p.SetSourcePort(int(vet[4]))
        p.SetDestinationPort(int(vet[5]))
        p.SetProtocol(vet[6])
        p.SetMessage(vet[7])
        return p
    
    def __str__(self) :
        return (
            "\nSOURCE_IP -> " + self.SOURCE_IP  + ""
            "\nDEST_IP -> " + self.DEST_IP + ""
            "\nSOURCE_MAC -> " + self.SOURCE_MAC  + ""
            "\nDEST_MAC -> " + self.DEST_MAC + ""
            "\nSOURCE_PORT -> " + str(self.SOURCE_PORT) + ""
            "\nDEST_PORT -> " + str(self.DEST_PORT) + ""
            "\nPROTOCOL -> " + self.PROTOCOL + ""
            "\nMESSAGE -> " + self.MESSAGE )