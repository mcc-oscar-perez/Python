# compresion de listas 
# list compression

palabra = "python"
lista = []

# sin comprension de listas
for letra in palabra:
    lista.append(letra)
print(lista)

# con comprension de listas
lista2 = [letra for letra in "matlab"]
print(lista2)   

