import os
from datetime import datetime, timedelta

#NOTA: Igual hay que cambiar:
# el datetime.now() por datetime.datetime.now()
# y el timedelta(...) por datetime.timedelta(...)
#dependiendo de los imports
def compruebaLog(ruta, numeroFicheros, tiempoComprobacion):
    ficheroC = "results/ficheroComprobacion.log"
    fileFicheroC = {}
    try:
        fileFicheroC = open(ficheroC, 'a')
    except IOError:
        fileFicheroC = open(ficheroC, 'a')

    for filename in os.listdir(ruta):
        ficheroNombre = 'Fichero: '+filename
        fileFicheroC.write(ficheroNombre + '\n')
        rutafich = ruta+'\\' + filename
        f = open (rutafich, "r",encoding='utf-8')

        lines = [line.rstrip('\n') for line in f]
        fichs = []
        starts = []
        for n in lines:
            if ('Starting' not in n) & ('Finished' not in n):
                fichs.append(n)
            else:
                if ('Starting' in n):
                    starts.append(n)
                    
        hashes = []
        for fich in fichs:
            split1 = fich.split()
            hashYAlgoritmo = split1[0]
            hashh = hashYAlgoritmo.split('|')[0]
            hashes.append(hashh)

        times = []
        for time in starts:
            timeSplit = time.split('| ')[1]
            times.append(timeSplit)
        
        errores = 0
        for index in range(0,len(hashes)-numeroFicheros):
            if hashes[index] != hashes[index+numeroFicheros]:
                lineaCambio = 'Cambio: '+str(datetime.now())+', Hash inicial: '+hashes[index]+', Hash final: '+hashes[index+numeroFicheros]
                fileFicheroC.write(lineaCambio + '\n')
                errores = errores +1
        if errores == 0:
            SinCambios = 'Sin cambios'
            fileFicheroC.write(SinCambios + '\n')
            
        for indexTime in range(0,len(times)-1):
            timeDate= datetime.strptime(times[indexTime], '%Y-%m-%d %H:%M:%S.%f')
            timeDate2= datetime.strptime(times[indexTime+1], '%Y-%m-%d %H:%M:%S.%f')
            if timeDate2 > (timeDate + timedelta(0,tiempoComprobacion+0.5)):
                ErrorTiempo = 'El tiempo de comprobacion fue mayor del esperado. '
                fileFicheroC.write(ErrorTiempo +str(datetime.now())+ '\n')
                
        


rutaLog = r'C:\Users\2aalf\Documents\Uni\SSII\Workspace SSII\PAI1\PAI1\Subido\results\logs'

#Se le pasa como parametros la ruta del directorio de los logs,
#el numero de ficheros que se comprueban (cuyo numero se obtiene con las funciones mas abajo)
#y el tiempo de comprobacion
compruebaLog(rutaLog,2,10)

#number_files devuelve el numero de ficheros que estan en la ruta definida en listaFicheros
rutaFicheros = r'C:\Users\2aalf\Documents\Uni\SSII\PAI1\ficheros'
listaFicheros = os.listdir(rutaFicheros)
number_files = len(listaFicheros)
print (number_files)