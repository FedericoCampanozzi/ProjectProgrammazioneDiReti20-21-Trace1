from threading import Thread
import time
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
    Utilities.EXIT_DAEMON = False
    Utilities.PrintAndWrite(" TEST   -- inizio TEST")
    
    server_nc = NetWorkComponents(Utilities.SERVER_IP, Utilities.ROUTER_TCP_PORT, Utilities.SERVER_MAC)
    router_nc = NetWorkComponents(Utilities.ROUTER_IP, Utilities.ROUTER_TCP_PORT, Utilities.ROUTER_MAC)
    clients = []
    
    Utilities.Write("\n TEST   -- Create Router : " + str(router_nc))
    Utilities.Write("\n TEST   -- Create Server : " + str(server_nc))
    
    tRouter = Thread(target = RunRouter, args = [router_nc, server_nc])
    tServer = Thread(target = RunServer, args = [server_nc])
    
    tRouter.start()
    tServer.start()

    time.sleep(Utilities.N_TEST_WAIT_SERVER_CON)
    
    Utilities.Write("\n TEST   -- Create Clients ")
    
    for i in range(Utilities.N_TEST_CLIENT) :
        myBase = NetWorkComponents.RandomNetWorkComponentsWithoutPort(Utilities.ROUTER_UDP_PORT)
        Utilities.Write("\n TEST   -- Create Client" + str(i) + " -> " + str(myBase))
        clients.append(ClientUDP(myBase, router_nc))
         
    for i in range(Utilities.N_TEST_MESSAGE) :
        
        for c in range(Utilities.N_TEST_CLIENT) :
            clients[c].SendData()
            
    Utilities.EXIT_DAEMON = True
    
    tRouter.join()
    tServer.join()
    
    for i in range(Utilities.N_TEST_CLIENT) :
        clients[i].Close()
        
    Utilities.PrintAndWrite("\n TEST   -- end TEST")

RunTest()