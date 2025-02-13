
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

# Palabra secreta que marque la cantidad de lineas que conforman esa palabra

palabra = 'Tucana'
palabra_secreta=palabra.lower()
palbara_lista = list(palabra_secreta)

# creamos la imprecion de la cantidad de lineas que hay en la palabra

lista_vacia = []
cadena = " "
vidas = 5
letras_adivinadas = []


for i in palbara_lista:
    lista_vacia.append("-")
x = print(cadena.join(lista_vacia))

# pedimos al usuario una letra

while vidas > 0:
    letra =  input("Dime una letra: ")
        
    if len(letra) >= 2:
        print("Por favor solo propocrione una letra")
        continue
        
    if letra not in 'abcdefghijklmnñopqrstuvwwxyz':
        print("por favor ingrese una letra no un numero")
        continue
        
    if letra in letras_adivinadas:
        print(f"Ya has usado la letra '{letra}'. Intenta con otra.")
        continue
        
    encontrada = False

    for i in range(len(palbara_lista)):
        if palbara_lista[i] == letra:
            lista_vacia[i]=letra
            encontrada = True
            
    print(cadena.join(lista_vacia))
    
    if encontrada == False:
        vidas = vidas -1
        print(f"Ahora te quedan '{vidas}' vidas")
    else:
        letras_adivinadas.append(letra)
    
    
    if "-" not in lista_vacia:
        print("Felicidades lograste completar la plabra")
        break

if vidas < 1:
    print(f"Has perdido, la palabra secreta era {palabra}")




