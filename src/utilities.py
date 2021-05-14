#!/usr/bin/env python3
import commons
import os

class Utilities :
    
    @staticmethod
    def Print(log, carry = True, indendation = 1):
        
        ind = ""
        
        if carry :
            ind += "\r"
        
        for i in range(indendation):
            ind += "\t"
        log = ind + log
        
        print(log)
        
        f = None
        
        try:
            if os.path.exists(commons.FILE_LOG_PATH):
                mode = 'a'
            else :
                os.mkdir(commons.FILE_LOG_FOLDER, 0o666)
                mode = 'w'
            f = open(commons.FILE_LOG_PATH, mode)
            f.write(log)
        except:
            f.close()
        finally:
            f.close()