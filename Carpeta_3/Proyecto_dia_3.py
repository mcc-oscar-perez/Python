a = input("\n\nIngrea el texto que deseas analizar: ")
b = input("Ingresa 3 letras de tú elección SIN ESPACIOS: ")

proceso1 = a.lower()
proceso2 = b.lower()

print(f"\n\ntu texto procesado es: {proceso1}\ny tus palabras procesadas son: {proceso2}\n")

lista1 = list(proceso1)
lista2 = list(proceso2)    

contador1 = lista1.count(lista2[0])
contador2 = lista1.count(lista2[1])
contador3 = lista1.count(lista2[2]) 

print('CANTIDAD DE LETRAS:')

print(f"La letra '{lista2[0]}' se repite {contador1} veces en tu texto \nLa letra '{lista2[1]}' se repite {contador2} veces en tu texto \nLa letra '{lista2[2]}' se repite {contador3} veces en tu texto\n")  

print('CANTIDAD DE PALABRAS:')
proceso3 = proceso1.split(" ")
print(f"hemos encontrado {len(proceso3)} palabras en tu texto\n")

print("LETRAS DE INICIO Y FINAL")

letra_inicial = proceso1[0]
letra_final = proceso1[-1]

print(f"La letra con la que inicia tu texto es: '{letra_inicial}'\nLa letra con la que finaliza tu texto es: '{letra_final}'\n")  

print("TEXTO INVERTIDO")

lista1.reverse()
texto_invertido = " ".join(lista1)

print(f"Tu texto invertido es: {texto_invertido}\n")

print("Buscando la plabra 'hola' en tu texto")







