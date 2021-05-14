from server import ServerTCP
from client import ClientUDP
from router import Router
from networkComponents import NetWorkComponents
import commons
import time
from threading import Thread
import random

def RunRouter(myBase, server_nc):
    Router(myBase, server_nc)

def RunServer(myBase):
    ServerTCP(myBase)
    
def RunTest():
    
    commons.ROUTER_UDP_PORT = random.randint(10_000, 65_536)

    server_nc = NetWorkComponents(commons.SERVER_IP, commons.ROUTER_TCP_PORT, commons.SERVER_MAC)
    router_nc = NetWorkComponents(commons.ROUTER_IP, commons.ROUTER_TCP_PORT, commons.ROUTER_MAC)
    clients = []
    
    print("\n\r TEST -- Create Router : " + str(router_nc))
    print("\n\r TEST -- Create Server : " + str(server_nc))
    
    tRouter = Thread(target = RunRouter, args = [router_nc, server_nc])
    tServer = Thread(target = RunServer, args = [server_nc])
    
    tRouter.start()
    tServer.start()

    time.sleep(commons.N_TEST_WAIT_SERVER_CON)
    
    print("\n\r TEST -- Create Clients ")
    
    for i in range(commons.N_TEST_CLIENT) :
        myBase = NetWorkComponents.RandomNetWorkComponents()
        clients.append(ClientUDP(myBase, router_nc))
    
    print("\n\r TEST -- inizio test")
    
    for i in range(commons.N_TEST_MESSAGE) :
        
        for c in range(commons.N_TEST_CLIENT) :
            clients[c].SendData()
            time.sleep(commons.N_TEST_WAIT)
            
        time.sleep(2 * commons.N_TEST_WAIT)
    
    
    print("\n\r TEST -- end test")

RunTest()