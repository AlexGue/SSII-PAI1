import os
from datetime import datetime, timedelta

#NOTA: Igual hay que cambiar:
# el datetime.now() por datetime.datetime.now()
# y el timedelta(...) por datetime.timedelta(...)
#dependiendo de los imports
def compruebaLog(ruta, tiempoComprobacion):


    for filename in os.listdir(ruta):
        now = datetime.now()
        if not filename == str(now.day) + "-" + str(now.month) + "-" + str(now.year)  + ".log":
            ficheroC = rutaAnalysis + "/" + filename  + "_" + str(now.day) + "-" + str(now.month) + "-" + str(now.year)  + ".log"
            fileFicheroC = {}
            try:
                fileFicheroC = open(ficheroC, 'a')
            except IOError:
                fileFicheroC = open(ficheroC, 'a')
            ficheroNombre = 'Fichero: '+filename
            fileFicheroC.write("================ INICIALIZANDO COMPROBACION DE LOG: " + ficheroNombre +  " ===============  " +'\n' )
            rutafich = ruta+'\\' + filename
            f = open (rutafich, "r",encoding='utf-8')

            lines = [line.rstrip('\n') for line in f]
            files = {}
            currentTime = ""
            for n in lines:
                if (not n.startswith('Starting')) & (not n.startswith('Finished')) & (not n.startswith('Error')) :
                    split = n.split('|')
                    if (not split[2] in files):
                        files[split[2]] = []
                    logData = {
                    "hash": split[0],
                    "algorithm": split[1],
                    "currentTime": currentTime
                    }
                    files[split[2]].append(logData)
                else:
                    if (n.startswith('Starting')):
                        split = n.split('|')
                        currentTime = split[1]
            for key in files:
                print("Analizando fichero: " + key)
                fileFicheroC.write("== Analizando fichero == | " + key + '\n')
                log = files[key]
                dataAnterior = {}
                for x in log:
                    if dataAnterior != {}:
                        hashAnterior = dataAnterior["hash"]
                        timeAnterior = dataAnterior["currentTime"]
                        if hashAnterior != x["hash"]:
                            print("Cambio detectado: " + x["currentTime"])
                            fileFicheroC.write("Cambio detectado: " + x["currentTime"] + '\n')
                        timeDate= datetime.strptime(timeAnterior, '%Y-%m-%d %H:%M:%S.%f')
                        timeDate2= datetime.strptime(x["currentTime"], '%Y-%m-%d %H:%M:%S.%f')
                        if timeDate2 > (timeDate + timedelta(0,tiempoComprobacion+0.5)):
                            ErrorTiempo = 'El tiempo de comprobacion fue mayor del esperado, en la fecha: ' + str(timeDate2)
                            print(ErrorTiempo)
                            fileFicheroC.write(ErrorTiempo +'\n')
                    dataAnterior = x
            f.close()
            os.rename(rutaLogs + '/' + filename, rutaFinishedLogs + '/' + filename)

                
        

baseRuta = r'C:\Users\Ale\Desktop\Universidad\SSII\PAI 1\results'
rutaLogs = baseRuta + r'\logs'
rutaFinishedLogs = baseRuta + r'\logs-finished'
rutaAnalysis = baseRuta + r'\analysis'

#Se le pasa como parametros la ruta del directorio de los logs,
#el numero de ficheros que se comprueban (cuyo numero se obtiene con las funciones mas abajo)
#y el tiempo de comprobacion
compruebaLog(rutaLogs,10)

#number_files devuelve el numero de ficheros que estan en la ruta definida en listaFicheros
rutaFicheros = r'C:\Users\Ale\Desktop\Universidad\SSII\PAI 1\ficheros'
listaFicheros = os.listdir(rutaFicheros)
number_files = len(listaFicheros)