#!/usr/bin/env python3
import socket
from datetime import datetime
import random
import commons

class ClientUDP :
    ROUTER_CON = None
    
    def __init__(self) :
        self.ROUTER_CON = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ROUTER_CON.connect((commons.LOCALHOST, commons.ROUTER_UDP_PORT))
        
    def SendData(self) :
        data = "DateTime : " + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " Temperature: " + str(random.randint(-1, 30)) + " gradi Humidity : " + str(random.randint(0, 50)) + " %"
        self.ROUTER_CON.send(data.encode("utf-8"))
        print("DATA SENT")
        
client1 = ClientUDP()
client1.SendData()