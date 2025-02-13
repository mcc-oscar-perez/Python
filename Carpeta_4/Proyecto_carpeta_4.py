"""
Ejercicio:  juego de adivinar el numero 
Programar un juego que te de 8 intentos para adivinar u numero secreto que este pensando el programa 

Exercise: guess the number game
Program a game that gives you 8 attempts to guess the secret number that the program is thinking of

"""


nombre =  input("¿Cual es tu nombre? ")
print("\nHola", nombre, "Estoy pensando en un número entre 1 y 100. Intenta adivinarlo en solo 8 intentos.")

numero = 10
intentos = 8
numero_del_usuario = int(input("\n¿Cual es el numero en que pienso? "))

while intentos >= 1:

    if (numero_del_usuario > 100) or (numero_del_usuario < 1):
        print("Este numero excede el rango de 1 a 100")
        intentos -= 1
        if intentos <1:
            break
        else :
            numero_del_usuario = int(input(f"te quedan {intentos} intentos. ¿Cual es el numero en que pienso? ")) 
        
    elif (numero_del_usuario < numero) and (0 < numero_del_usuario <= 100):
        print("Mi número es mayor que", numero_del_usuario)
        intentos -= 1 
        if intentos <1:
            break
        else :
            numero_del_usuario = int(input(f"te quedan {intentos} intentos. ¿Cual es el numero en que pienso? ")) 
        
    elif (numero_del_usuario > numero) and (0 < numero_del_usuario <= 100):
        print("Mi número es menor que", numero_del_usuario)
        intentos -= 1
        if intentos <1:
            break
        else :
            numero_del_usuario = int(input(f"te quedan {intentos} intentos. ¿Cual es el numero en que pienso? ")) 
        
    elif numero_del_usuario == numero:
        print(f"¡Felicidades! ¡Adivinaste el número! y tu quedaron {intentos -1} intentos")
        break

if numero_del_usuario != numero:
    print(f"¡Lo siento! No adivinaste el número. El número era {numero}")

