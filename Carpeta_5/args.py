def suma_cuadrados(*args):
    
    total = 0
    for numero in args:
        total += numero**2
    return total 
    


def suma_absolutos(*args):
    total = 0
    for numero in args:
        total += abs(numero)
    return total 

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'   