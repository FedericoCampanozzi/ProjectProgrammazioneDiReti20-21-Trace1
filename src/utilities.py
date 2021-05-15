#!/usr/bin/env python3
import os
import commons

class Utilities :
    
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
            if not os.path.exists(commons.FILE_LOG_PATH):
                os.mkdir(commons.FILE_LOG_FOLDER, 0o666) 
            f = open(commons.FILE_LOG_PATH, 'w')
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
            if not os.path.exists(commons.FILE_LOG_PATH):
                os.mkdir(commons.FILE_LOG_FOLDER, 0o666) 
                mode = 'w'
            f = open(commons.FILE_LOG_PATH, mode)
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
            if not os.path.exists(commons.FILE_LOG_PATH):
                os.mkdir(commons.FILE_LOG_FOLDER, 0o666) 
                mode = 'w'
            f = open(commons.FILE_LOG_PATH, mode)
            f.write(log)
        except:
            f.close()
        finally:
            f.close()