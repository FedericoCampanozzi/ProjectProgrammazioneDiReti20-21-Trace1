#!/usr/bin/env python3
import os

class Utilities :
    
    SERVER_IP = "10.10.10.1"
    SERVER_MAC = "11:55:AB:2E:FF:EF"
    ROUTER_IP = "192.168.1.1"
    ROUTER_MAC = "EE:12:1B:25:0F:00"
    ROUTER_UDP_PORT = 8091
    ROUTER_TCP_PORT = 8092
    LOCALHOST = "127.0.0.1"
    BUFFER_SIZE = 4096
    N_TEST_CLIENT = 4 # Numero di client attivi che invieranno messaggi
    N_TEST_MESSAGE = 2 # Numero di messaggi che invia un singolo client al router
    N_TEST_WAIT_SERVER_CON = 3 # Numero di secondi da aspettare per l'invio del prossimo messaggio
    FILE_LOG_FOLDER = "Log"
    FILE_LOG_FILE = "Log.txt"
    FILE_LOG_PATH = os.path.join(os.getcwd(), FILE_LOG_FOLDER , FILE_LOG_FILE)
    EXIT_DAEMON = None
    DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
    
    @staticmethod
    def Hex(number):
        if(number < 10) : 
            return str(number)
        if(number == 10): return "A"
        if(number == 11): return "B"
        if(number == 12): return "C"
        if(number == 13): return "D"
        if(number == 14): return "E"
        if(number == 15): return "F"
        
    @staticmethod
    def Reset():
        f = None
        
        try:
            if not os.path.exists(Utilities.FILE_LOG_PATH):
                os.mkdir(Utilities.FILE_LOG_FOLDER, 0o666) 
            f = open(Utilities.FILE_LOG_PATH, 'w')
        except:
            f.close()
        finally:
            f.close()
            
    @staticmethod
    def PrintAndWrite(log):
        print(log)        
        f = None        
        try:
            mode = 'a'
            if not os.path.exists(Utilities.FILE_LOG_PATH):
                os.mkdir(Utilities.FILE_LOG_FOLDER, 0o666) 
                mode = 'w'
            f = open(Utilities.FILE_LOG_PATH, mode)
            f.write(log)
        except:
            f.close()
        finally:
            f.close()
    
    @staticmethod
    def Write(log):
        f = None
        try:
            mode = 'a'
            if not os.path.exists(Utilities.FILE_LOG_PATH):
                os.mkdir(Utilities.FILE_LOG_FOLDER, 0o666) 
                mode = 'w'
            f = open(Utilities.FILE_LOG_PATH, mode)
            f.write(log)
        except:
            f.close()
        finally:
            f.close()
    
    @staticmethod
    def DateDifference(data1, data2) :
        delta = 0.0
        if (data1 > data2):
            delta = (data1 - data2).total_seconds()
        else:
            delta = (data2 - data1).total_seconds()
        delta = round(delta * 1000.0, 3)
        return str(delta) + " MS"
        