# Metodos
# Methods

# metodo para combertir a mayusculas
texto = "Este es el texto de Federico"
resultado = texto[2].upper() # podemos decirle que nos muestre la posición 2 en mayusculas
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.lower() # podemos decirle que nos muestre todo en minusculas
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.split("t") # podemos hacer que nos muestre una lista con las palabras separadas tomo por separador a los espacios pero esto se puede modificar
print(resultado)

a = "aprender"
b = "Python"
c = "es"
d = "genial"
e = " "

resultado = e.join([a,b,c,d]) # aqui estamos pidiendo que nos muestre las variables unidas por un espacio
print(resultado)

texto = "Este es el texto de Federico"
resultado = texto.find("S") # aqui estamos pidiendo que nos muestre la posición de la letra S
print(resultado)
# cuando find no encuentra la letra nos devuelve un -1

texto = "Este es el texto de Federico"
resultado = texto.replace("Federico", "todos") # aqui estamos pidiendo que nos muestre el texto pero que cambie la palabra Federico por todos
print(resultado)