# loop while 

#%%
# Ejemplo 1 del loop while 
vidas  = 5 

while vidas > 0:
    print(f"Te quedan {vidas} vidas")
    vidas -= 1
print("Se acabaron las vidas")

#%%
# Ejemplo 2 del loop while 
respuesta = "s"

while respuesta == "s":
    respuesta  = input("Quieres seguir jugando? s/n")
print("Gracias por jugar")

#%%
# Ejemplo 3 del loop while 
respuesta = "s"

while respuesta == "s":
    pass 

print("hola")

#%%
# Ejemplo 4 del loop while 
nombre  = input("Cual es tu nombre?")

for letra in nombre:
    if letra == "a":
        break 
    print(letra) 


# %%
