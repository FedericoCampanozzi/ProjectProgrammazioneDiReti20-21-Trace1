ROUTER_IP = "192.168.1.1"
LOCALHOST = "127.0.0.1"
ROUTER_UDP_PORT = 7879
ROUTER_TCP_PORT = ROUTER_UDP_PORT + 2
N_TEST_CLIENT = 4 # Numero di client attivi che invieranno messaggi
N_TEST_MESSAGE = 10 # Numero di messaggi che invia un singolo client al router
N_TEST_WAIT = 1 # Numero di secondi da aspettare per l'invio del prossimo messaggio