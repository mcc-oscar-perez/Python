# Ejecicios practicos de funciones 
# Practical exercises on functions

#%%
# Ejercicio practico 1 
def devolver_distintos(a,b,c):

    suma = a+b+c
    lista = [a,b,c]
    
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort() 
        return lista[1]
    
print(devolver_distintos(8,1,0))
#%%
# Ejercicio practico 2
def x (texto):
    lista = list(texto)
    lista2 = list(set(lista))
    lista2.sort()
    return lista2
    

texto = "cascarrabias"
print(x(texto))

#%%
# Ejercicio practico 3
def vecinos(*args):
    
    for i in range(len(args)-1):
        if args[i] == 0 and args[i+1] == 0:
            return True
        
    return False
        
print(vecinos(1, 0, 0, 2, 3))  
print(vecinos(1, 2, 3, 4)) 

#%%   
# Ejercicio practico 4
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(n):
    primos = []
    for num in range(2, n + 1):  # Empezamos en 2 porque 0 y 1 no son primos
        if es_primo(num):
            primos.append(num)
    
    # Imprimir todos los números primos encontrados
    print(f"Números primos entre 0 y {n}: {primos}")
    
    # Devolver la cantidad de números primos encontrados
    return len(primos)

# Ejemplo de uso
numero = 36
cantidad_primos = contar_primos(numero)
print(f"Cantidad de números primos entre 0 y {numero}: {cantidad_primos}")

# %%
