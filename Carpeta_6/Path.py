#%%
# Otener la ruta del directiro sobre el que estamos trabajando 
# get the path of the directory we working on

from pathlib import Path
base = Path.home()
print(base)

#%% 
# Crear una ruta 
# Create a path 

from pathlib import Path
guia = Path("Barselona","otra_cosas.txt")
print(guia)

# %%
# Cambiamos el archivo que buscamos en la ruta 
# Change the file we are looking for in the path

from pathlib import Path
guia = Path("Mexico","Guadalajara","Guanajuato")
guia2 = guia.with_name("Monterrey")

print(guia)
print(guia2)



# %%
# Recorrer la ruta de derecha a izquiera 
# Navegate the folder path from right to left

from pathlib import Path
guia = Path("Mexico","Guadalajara","Guanajuato")

print(guia.parent.parent)
# %%
