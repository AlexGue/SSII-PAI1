
import sys
import hashlib
import time
import datetime
import json
import requests


# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
configFile = "Config.json"

def leeFicheros(file):
    f = open (file, "r",encoding='utf-8')
    data = json.load(f)
    ficheros=data['ficheros']
    return ficheros

def leeAlgoritmo(file):
    f = open (file, "r",encoding='utf-8')
    data = json.load(f)
    algoritmo=data['algoritmo']
    return algoritmo

def leeFicheroIncidencias(file):
    f = open (file, "r",encoding='utf-8')
    data = json.load(f)
    ficheroIncidencias=data['ficheroIncidencias']
    return ficheroIncidencias

def leeServer(file):
    f = open (file, "r",encoding='utf-8')
    data = json.load(f)
    server=data['server']
    return server

def leeTiempoComprobacion(file):
    f = open (file, "r",encoding='utf-8')
    data = json.load(f)
    tiempoComprobacion=data['tiempoComprobacion']
    return int(tiempoComprobacion)


filesToCheck = leeFicheros(configFile)
repeatTime = leeTiempoComprobacion(configFile)
now = datetime.datetime.now()
algorithm = leeAlgoritmo(configFile)
server = leeServer(configFile)
statusURL = server + "/sendStatus/" 



def storeInLogFile(line):
    fn = "results/logs/" + str(now.day) + "-" + str(now.month) + "-" + str(now.year)  + ".log"
    fileLog = {}
    try:
        fileLog = open(fn, 'a')
    except IOError:
        fileLog = open(fn, 'a')
    fileLog.write(line + '\n')
    
def checkFiles(): 
    hashes = []
    nowTime = datetime.datetime.now()
    storeInLogFile("Starting file check |" + str(nowTime) )
    for fileH in filesToCheck:
        hashR = getattr(hashlib, algorithm)()
        with open(fileH, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                hashFile = hashR.update(data)
        lineLog = ("{0}|{2}|{1}".format(hashR.hexdigest(), fileH, algorithm))
        hashes.append(hashR.hexdigest())
        print(lineLog)
        storeInLogFile(lineLog)
    finalLog = str(hashes)+ str(nowTime)
    hashAlg = getattr(hashlib, algorithm)()
    hashAlg.update(finalLog.encode('utf-8'))
    hashFinal = hashAlg.hexdigest()
    storeInLogFile("Finished file check | " + hashFinal)
    try:
        r = requests.get(statusURL + hashFinal)
        print("Response from server: " + r.status_code)
    except:
        print("Error connecting to the server.")
        storeInLogFile("Error connecting to the server.|" + str(nowTime))


def startChecks():
    starttime=time.time()
    print("Starting")
    while True:
        checkFiles()
        time.sleep(repeatTime - ((time.time() - starttime) % repeatTime))

#Cambiar contenido de fichero de configuraci�n y ruta de archivos



startChecks()

ficherosToCheck=leeFicheros("Config.json")
