import re

Texto =  "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in Texto
print(palabra)

# If i want to find the word "ayuda" using regular expressions
patron = 'ayuda'
busqueda = re.search(patron, Texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

#%%
import re

Texto =  "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
patron = 'ayuda'

# If we want to find words repeated more than once
busqueda = re.findall(patron, Texto)
print(busqueda)


# %%
# If we want to find the 2 ubications of both words "ayuda"

import re

Texto =  "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
patron = 'ayuda'

for hallazgo in re.finditer(patron, Texto):
    print(hallazgo.span())
# %%

import re 

texto = "llama al 564-525-6588 ya mismo"
patron =  r'\d\d\d-\d\d\d-\d\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{4}'
patron3 = r'(\d{3})-(\d{3})-(\d{4})'


resultado = re.search(patron3, texto)
print(resultado)
print(resultado.group(2))

# %%

# if we want to do a pasword validation using regular expressions
import re

clave = input("Introduce una clave: ")
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)
print(chequear)

# %%
# if we want to search one of two words using regular expressions

import re

texto = "No atendemos los lunes por la terde"

buscar  =re.search(r'lunes|martes',texto)  
print(buscar) 
# %%

# Practical excercise 

# 1 

import re

def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

#%%
# 2

import re

def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")
        
#%%
# 3

import re

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")