#%%
# Leer un archivo almacenado en la mismca carpeta en la que estamos trabajando 
# Read a file stored in the same folder we are working in


mi_archivo = open('Prueba.txt')
print(mi_archivo.read())


mi_archivo.close()

#%%
# Leer el mismo archivo pero linea por linea
# Read the same file but line by line

mi_archivo = open('Prueba.txt')

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)


mi_archivo.close()
# %%
# Crear un loop for para leer linea por linea  
# Create a for loop to read line by line

mi_archivo = open('Prueba.txt')

for i in mi_archivo:
    print("Aqui dice : " + i)

mi_archivo.close()

#%% 
# Leer todo el archivo con readlines
# Read the entire file with readlines

mi_archivo = open('Prueba.txt')

todas  = mi_archivo.readlines()

print(todas)

mi_archivo.close()


# %%

