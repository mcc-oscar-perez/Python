"""
Ejercicio:  Juego del ahorcado 
Hacer un programa que le permita al usuario adivinar una palabra secreta que 
el programa ya tiene guardado, dandole solo 5 vidas para acertar la palabra correcta,
de lo contrario se pierde el juego.

Reglas:
1- si acierta, dar las felicitaciones y decir cuantas vidas le quedaban.
2- si no acierta, decirle cual era la palabra correcta.
3- solo permitir letras, no numeros y si una letra ya usada, avisar al usuario que ya uso esa letra.


Exercise: Hangman game
Make a program that allows the user to guess a secret word that the program
already has saved, giving him only 5 lives to guess the correct word,
otherwise the game is lost.

Rules:
1- if he guesses correctly, congratulate him and tell him how many lives he had left.
2- if he doesn't guess correctly, tell him what the correct word was.
3- only allow letters, not numbers, and if a letter has already been used, tell the user that he has already used that letter.

"""

from random import choice

palabras = ['panadero', 'dinosaurio', 'helipuerto', 'tiburon']
letras_correctas = []
letras_incorrectas = []
intentos = 5
aciertos = 0
juego_terminado = False


def elegir_palbra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input("Elige una letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print("No has elegido una letra correcta")

    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))


def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra!!!")

    return True


palabra, letras_unicas = elegir_palbra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)

    juego_terminado = terminado
