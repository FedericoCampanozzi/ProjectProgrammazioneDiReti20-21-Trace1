import os

SERVER_IP = "10.10.10.1"
SERVER_MAC = "11:55:AB:2E:FF:EF"
ROUTER_IP = "192.168.1.1"
ROUTER_MAC = "EE:12:1B:25:0F:00"
ROUTER_UDP_PORT = 8085
ROUTER_TCP_PORT = 8086
LOCALHOST = "127.0.0.1"
BUFFER_SIZE = 4096
N_TEST_CLIENT = 4 # Numero di client attivi che invieranno messaggi
N_TEST_MESSAGE = 2 # Numero di messaggi che invia un singolo client al router
N_TEST_WAIT_SERVER_CON = 3 # Numero di secondi da aspettare per l'invio del prossimo messaggio
FILE_LOG_FOLDER = "Log"
FILE_LOG_FILE = "Log.txt"
FILE_LOG_PATH = os.path.join(os.getcwd(), FILE_LOG_FOLDER , FILE_LOG_FILE)
EXIT_DAEMON = None