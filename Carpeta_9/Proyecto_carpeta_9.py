#first descompress the file Proyecto_carpeta_9.zip

# import librraries 
#import shutil

# Descompress the zip file into a folder named 'carpeta_9'
"""shutil.unpack_archive('Carpeta_9/Proyecto+Dia+9.zip', 'carpeta_9')"""

#-------------------------------------------------------------------------------

# import libraries
import re
import os 
import time
import datetime
import pathlib as path 
import math

inicio = time.time()

ruta = 'carpeta_9/Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []

# Function to search for files in a directory
def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        for a in archivos:
            resultado = buscar_numero(path.Path(carpeta, a), mi_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('.'* 50)
    print(f'fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('Archivo \t\t\t NRO. SERIE')
    print('________\t\t\t___________')
    for a in archivos_encontrados:
        print(f'{a}.\t{numeros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numero encontrados: {len(numeros_encontrados)}')
    
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('.'* 50)
    
# Main function to execute the search
crear_listas()
mostrar_todo()
#-------------------------------------------------------------------------------
    