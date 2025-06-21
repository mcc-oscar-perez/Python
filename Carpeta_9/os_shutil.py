import os 
print(os.getcwd())  # get current working directory

#how to create a file
archivo = open("archivo.txt", "w")  # create a file
archivo.write("Hola, este es un archivo de prueba.")  # write to the file

#%%
print(os.listdir())
# %%
#How to move a file

import shutil
shutil.move("D:\\Cursos\\PYTHON\\archivo.txt", "D:\\Cursos\\PYTHON\\Carpeta_9")  # move the file to another directory

# %%
# send a file to the trash

import send2trash
send2trash.send2trash("D:\\Cursos\\PYTHON\\Carpeta_9\\archivo.txt")  # send the file to the trash
#%%

# How to see all files in a directory
import os

ruta = 'D:\Cursos\PYTHON\Carpeta_9'

for carpeta, subcarpetas,archivos in os.walk(ruta):
     print(f'Carpeta: {carpeta}')
     print(f'Las Subcarpetas son: ')
     for sub in subcarpetas:
         print(f'\t{sub}')
     print(f'Los Archivos son: ')
     for arch in archivos:
        print(f'\t{arch}')
     print('')  
# %%
