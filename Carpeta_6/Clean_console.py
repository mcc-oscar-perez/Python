# Ejemplo de como limpiar consola en Windows
# Exaple of how to clean console in Windows

from os import system

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('cls')

print(f"Tu nombre es {nombre} y tu edad es {edad}")

