"""Examples of how to use generators"""

def mi_funcion():
    """ This function generates all values immediately."""
    lista = []
    for i in range(1,5):
        lista.append(i*10)
    return lista

# In this way we can save memory space by doing the same thing.   
def mi_generador():
    """This function generates the values ​​as they are needed."""
    for i in range(1,5):
        yield i * 10 

print(mi_funcion())
print(mi_generador())

g =  mi_generador()
# Here we print as many outputs as we want
print(next(g))
print(next(g))
print(next(g))

#%%
"""More examples"""

# 1
def mi_generador():
    x = 1
    yield x
    
    x += 1
    yield x
    
    x += 1
    yield x  

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))

# 2
def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num

generador = secuencia_infinita()

# 3 

def multiplos_siete():
    num = 1
    while True:
        yield 7*num
        num += 1

generador = multiplos_siete()

# 4 
def mensaje():
    x = "Te quedan 3 vidas"
    yield x
    
    x = "Te quedan 2 vidas"
    yield x
    
    x = "Te queda 1 vida"
    yield x
    
    x = "Game Over"
    yield x
    
perder_vida = mensaje()

