import time

def prueba_for (numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time()
print(prueba_for(100000))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fin = time.time() 
print(f"Tiempo de ejecución con for: {round(fin - inicio, 5)} segundos")

inicio = time.time()
print(prueba_while(100000))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fin = time.time()
print(f"Tiempo de ejecución con while: {round(fin - inicio, 5)} segundos")   

#%% 
import timeit


declaracion ="""
prueba_for(10)
"""

mi_setup = """
def prueba_for (numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista 
"""

duracion = timeit.timeit(declaracion, mi_setup, number=10000000)
print(f"Tiempo de ejecución con timeit: {round(duracion, 5)} segundos")

declaracion2 = """
prueba_while(10)"""

mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion2 = timeit.timeit(declaracion2, mi_setup2, number=10000000)
print(f"Tiempo de ejecución con timeit: {round(duracion2, 5)} segundos")


# %%
