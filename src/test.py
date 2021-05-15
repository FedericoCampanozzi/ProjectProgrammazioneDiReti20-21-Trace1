from threading import Thread
import time
import commons
from utilities import Utilities
from server import ServerTCP
from client import ClientUDP
from router import Router
from networkComponents import NetWorkComponents

def RunRouter(myBase, server_nc):
    Router(myBase, server_nc)

def RunServer(myBase):
    ServerTCP(myBase)
    
def RunTest():
    
    Utilities.Reset()
    commons.EXIT_DAEMON = False
    Utilities.PrintAndWrite(" {TEST} -- inizio TEST")
    
    server_nc = NetWorkComponents(commons.SERVER_IP, commons.ROUTER_TCP_PORT, commons.SERVER_MAC)
    router_nc = NetWorkComponents(commons.ROUTER_IP, commons.ROUTER_TCP_PORT, commons.ROUTER_MAC)
    clients = []
    
    Utilities.Write("\n {TEST} -- Create Router : " + str(router_nc))
    Utilities.Write("\n {TEST} -- Create Server : " + str(server_nc))
    
    tRouter = Thread(target = RunRouter, args = [router_nc, server_nc])
    tServer = Thread(target = RunServer, args = [server_nc])
    
    tRouter.start()
    tServer.start()

    time.sleep(commons.N_TEST_WAIT_SERVER_CON)
    
    Utilities.Write("\n {TEST} -- Create Clients ")
    
    for i in range(commons.N_TEST_CLIENT) :
        myBase = NetWorkComponents.RandomNetWorkComponentsWithoutPort(commons.ROUTER_UDP_PORT)
        Utilities.Write("\n {TEST} -- Create Client" + str(i) + " -> " + str(myBase))
        clients.append(ClientUDP(myBase, router_nc))
         
    for i in range(commons.N_TEST_MESSAGE) :
        
        for c in range(commons.N_TEST_CLIENT) :
            clients[c].SendData()
            
    commons.EXIT_DAEMON = True
    
    tRouter.join()
    tServer.join()
    
    for i in range(commons.N_TEST_CLIENT) :
        clients[i].Close()
        
    Utilities.PrintAndWrite("\n {TEST} -- end TEST")

RunTest()