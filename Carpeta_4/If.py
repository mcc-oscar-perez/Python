# # ejemplo 1
# if 5 == 2:
#     print("Es verdad")
# else:
#     print("Es falso")
    
# # ejemplo 2 
# mascota = "perro"

# if mascota == "gato":
#     print("tienes un gato")
# elif mascota == "perro":
#     print("tienes un perro")
# else:
#     print("No se que animal tienes")
    
# # ejemplo 3 anidadno IF

# edad = 35

# if edad >= 18:
#     print("Eres mayor de edad")
#     if edad >= 50:
#         print("Eres un adulto mayor")
#     else:
#         print("Eres un adulto joven")
# else: 
#     print("Eres menor de edad")
    
    
# num1 = input("Ingresa un número:")
# num2 = input("Ingresa otro número:")

# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num1 == num2:
#     print(f"{num1} y {num2} son iguales")
# else:
#     print(f"{num2} es mayor que {num1}")


edad = 16
tiene_licencia = False


if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad >= 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
    

