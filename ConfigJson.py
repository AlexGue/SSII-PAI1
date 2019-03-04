import json

#Cambiar contenido de fichero de configuración y ruta de archivos

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

def leeTiempoComprobacion(file):
    f = open (file, "r",encoding='utf-8')
    data = json.load(f)
    tiempoComprobacion=data['tiempoComprobacion']
    return tiempoComprobacion

ej=leeFicheros("Config.json")
print(ej)

ej2=leeAlgoritmo("Config.json")
print(ej2)

ej3=leeFicheroIncidencias("Config.json")
print(ej3)

ej4=leeTiempoComprobacion("Config.json")
print(ej4)

