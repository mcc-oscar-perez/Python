#%%
# obtenemos la ruta de la carpeta en la que estamos con OS
# Get the path of the folder we are in with OS

import os 
ruta = os.getcwd()
print(ruta)

#%%
# Buscamos un archivo en una ruta especifica con OS 
# Search a file in a specific path with OS

import os 
ruta = os.chdir("C:\\Users\\OSKR-\\Downloads")

archivo = open("otro_archivo.txt")
print(archivo.read())

archivo.close()

#%%
# Buscar archivo en una ruta especifica sin OS 
# Find file in a specific path without OS

mi_archivo = open("C:\\Users\\OSKR-\\Downloads\\otro_archivo.txt")
print(mi_archivo.read())



# %%
# Crear un archivo en una ruta
# Create a file in a path

import os 
ruta = os.makedirs("C:\\Users\\OSKR-\\Downloads\\otra")



#%%
# Eliminar una carpeta 
# Delete folder

import os 
ruta = os.rmdir("C:\\Users\\OSKR-\\Downloads\\otra")


#%%
# Buscar el nombre del elemento que deseamos abrir 
# Search for the name of the item to open

import os 
ruta = "C:\\Users\\OSKR-\\Downloads\\otro_archivo.txt"

elemento = os.path.basename(ruta)
print(elemento)
# %%
# Abrimos archivo con Path
# Open file with Path 

from pathlib import Path

carpeta = Path("C:/Users/OSKR-/Downloads")
archivo = carpeta / "otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())
mi_archivo.close()
# %%
# Abrimos un archivo con Path 
# Abrimos archivo con Path

from pathlib import Path

carpeta = Path("C:/Users/OSKR-/Downloads/otro_archivo.txt")
print(carpeta.read_text())

# %%
# Extraemos el nombre con Path
# Extract the name with Path

from pathlib import Path

carpeta = Path("C:/Users/OSKR-/Downloads/otro_archivo.txt")
print(carpeta.name)
# %%
# Extraemos el tipo de archivo con Path 

from pathlib import Path

carpeta = Path("C:/Users/OSKR-/Downloads/otro_archivo.txt")
print(carpeta.suffix)
# %%
# Extraemos el nombre sin la terminacion con Path 
# Extract the file type with Path

from pathlib import Path

carpeta = Path("C:/Users/OSKR-/Downloads/otro_archivo.txt")
print(carpeta.stem)
# %%
# Realizar acciones si un archvo existe o no con Path
# Actions if a file exists or not with Path

from pathlib import Path

carpeta = Path("C:/Users/OSKR-/Downloads/otro_archivo.txt")

if not carpeta.exists():
    print("Lo siento no existe el archivo que buscas")
else:
    print("Genial tu archivo si existe")
# %%
