
import sys
import hashlib
import time
import datetime
# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


filesToCheck = ["C:/Users/Ale/Desktop/Universidad/SSII/test1.txt", "C:/Users/Ale/Desktop/Universidad/SSII/test2.txt"]
algorithm = "sha256"
repeatTime = 5.0
now = datetime.datetime.now()



def storeInLogFile(line):
    fn = "results/logs/" + str(now.day) + "-" + str(now.month) + "-" + str(now.year)  + ".log"
    fileLog = {}
    try:
        fileLog = open(fn, 'a')
    except IOError:
        fileLog = open(fn, 'a')
    fileLog.write(line + '\n')
    
def checkFiles():
    for file in filesToCheck:
        hashR = getattr(hashlib, algorithm)()
        with open(file, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                hashR.update(data)
        lineLog = ("SHA256: {0} of file {1}".format(hashR.hexdigest(), file))
        print(lineLog)
        storeInLogFile(lineLog)

def startChecks():
    starttime=time.time()
    print("Starting")
    while True:
        checkFiles()
        time.sleep(repeatTime - ((time.time() - starttime) % repeatTime))

startChecks()