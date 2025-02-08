from random import shuffle
import random

#Lista inicial 
palitos = ['-', '--', '---', '----']


#Mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ""
    
    while intento not in ['1','2','3','4']:
        intento = input ("Elige un numero del 1 al 4: ")
        
    return int(intento)

#comprobar intento 
def chequear_inento(lista,intento):
    if lista[intento -1] == '-':
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")
    
    print(f"te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_inento(palitos_mezclados,seleccion)


#ejercicio practico 1 --------------------------------------------------------------------

def lanzar_dados():
    lista = [1,2,3,4,5,6]
    dado1 = random.choice(lista)
    dado2 = random.choice(lista)

    return dado1 , dado2

def evaluar_jugada(dado1,dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif 6 < suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
        

lanzamiento = lanzar_dados()
print(lanzamiento)

evaluacion = evaluar_jugada(*lanzamiento)
print(evaluar_jugada)

#ejercicio practico 2 --------------------------------------------------------------------

lista_numeros = [1,2,15,7,2] 

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort
    lista.pop(-1)
    return lista

def promedio(lista):
    promedio = sum(lista)/len(lista)
    return promedio

modificacion = reducir_lista(lista_numeros)
print(modificacion)

resultado = promedio(modificacion)
print(resultado)

#ejercicio practico 3 --------------------------------------------------------------------

lista_numeros = [1,2,15,7,2,8]

import random

def lanzar_moneda():
    estado = ['Cara','Cruz']
    resultado = random.choice(estado)
    return resultado

def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        lista_eliminada = lista.clear()
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista

lanzamiento = lanzar_moneda()
print(lanzamiento)

suerte = probar_suerte(lanzamiento,lista_numeros)
print(suerte)