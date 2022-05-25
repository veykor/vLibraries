#!/usr/bin/python3

import time, sys, traceback, inspect, re

LOGLEVEL = 1
LOGERRORLEVEL = 2
LOGLEVELS = ['DEBUG', 'INFO', 'WARN', 'ERROR']
LOGTRACE = True


def strMultireplace(strIn, listOfTuplesReplacers):
        strOut=strIn
        for replacer in listOfTuplesReplacers:
                strOut=strOut.replace(replacer[0], replacer[1])
        return strOut

def getStrMilliseconds():
    return str(round(time.time()%1,3))[1:]
    
def getTimeFormatted():
    return time.strftime('%Y-%m-%dT%H:%M:%S')

def getTimeFormattedWithMilliseconds():
        return time.strftime(f'%Y-%m-%dT%H:%M:%S{getStrMilliseconds()}')

def getTimeFormattedForFile():
        return time.strftime('%Y-%m-%dT%H-%M-%S')
        
def getHeartbit(frequency): #could not work in high frequency rates
        return bool((int(2*time.time()*frequency)%2))
        
def getFunctionRoute():
    stackExecData = inspect.stack()[:2:-1] #exclude log function for function route
    return formatExecData(stackExecData)
    
def loggerTraceback(enableTb, outToStderr=False): #traceback enable and select out (stdout or stderr)
    if enableTb==True:
        tb=sys.exc_info()
        if outToStderr==True:
            traceback.print_exception(tb[0], tb[1], tb[2], file=sys.stderr)
        else:
            traceback.print_exception(tb[0], tb[1], tb[2])
    return

def logger(level, msg, logtb=False):
    #print(f'test logger:{LOGLEVEL}')
    if level < LOGLEVEL:
        return
    msgLog=getTimeFormattedWithMilliseconds() + "\t[" + LOGLEVELS[level] + "]\t"  + msg
    print(msgLog)
    loggerTraceback(logtb)
    if level >= LOGERRORLEVEL: #write to stderr
        print(msgLog, file=sys.stderr)
        loggerTraceback(logtb, True)
        
def setLogLevel(level):
    if not isinstance(level, int):
        logger(2, 'level is not integer')
        return
    LOGLEVEL=level
