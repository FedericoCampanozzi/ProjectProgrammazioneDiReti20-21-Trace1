#!/usr/bin/env python3
import socket
from datetime import datetime
import random
import commons
from package import Package

class ClientUDP :
    ROUTER_CON = None
    PACKAGE = Package()
    
    def __init__(self, sim_ip, sim_mac) :
        self.ROUTER_CON = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ROUTER_CON.connect((commons.LOCALHOST, commons.ROUTER_UDP_PORT))
        self.PACKAGE.SetProtocol("UDP")
        self.PACKAGE.SetSourceIP(sim_ip)
        self.PACKAGE.SetSourceMAC(sim_mac)
        self.PACKAGE.SetSourcePort(commons.ROUTER_UDP_PORT)
         
    def SendData(self) :
        data = "DateTime : " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " Temperature: " + str(random.randint(-1, 30)) + " gradi Humidity : " + str(random.randint(0, 50)) + " %"
        self.PACKAGE.SetMessage(data)
        self.ROUTER_CON.send(self.PACKAGE.Encode())
        #print("DATA SENT")
        print("DATA SENT " + str(self.PACKAGE))

        
client1 = ClientUDP("192.168.1.113", "AA:AA:BB:BB:CC:CC")
client1.SendData()