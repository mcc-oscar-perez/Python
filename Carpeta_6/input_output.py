# Leer un archivo almacenado en la mismca carpeta en la que estamos trabajando 

mi_archivo = open('Prueba.txt')
print(mi_archivo.read())
mi_archivo.close()

#%%

# Leer el mismo archivo pero linea por linea
mi_archivo = open('Prueba.txt')
una_linea = mi_archivo.readline()
print(una_linea)

# %%
