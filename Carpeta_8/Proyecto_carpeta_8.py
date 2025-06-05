
def numeros_perfumeria():
    """Esta funcion genera los turnos del dia para el area de perfumeria"""
    for n in range(1,10000):
        yield f"P - {n}"

def numeros_farmacia():
    """Esta funcion genera los turnos del dia para el area de farmacia"""
    for n in range(1,10000):
        yield f"F- {n}"

def numeros_cosmetica():
    """Esta funcion genera los turnos del dia para el area de cosmetica"""
    for n in range(1,10000):
        yield f"C - {n}"

#Guardamos en variables estos generadores de numeros
P = numeros_perfumeria()
F = numeros_farmacia()
C = numeros_cosmetica()

#Creamos el decorador del numero para darle apariencia de tiket

def decorador(catergoria):
    
    print("\n"+"*" *40) 
    print("Su numero es: ") 
    
    if catergoria == "P":
        print(next(P))
    elif catergoria == "F":
        print(next(F))
    else:
        print(next(C))
    print("Espere un momento y sera atendido")
    print( "*" * 23 + "\n")
