# Loop for
#%%
# Ejemplo 1 del uso del loop for
lista = ["a", "b", "c", "d", "e"]

for x in lista:
    inidice  = lista.index(x)
    print(f"En el indice {inidice} esta el la letra {x}")
#%%
# Ejemplo 2 del uso del loop for
lista2 = ["pablo", "juan", "pedro", "maria", "luis"]

for i in lista2:
    if i.startswith("p"):
        print(i)
    else:
        print("No empieza con p")
#%%   
# Ejemplo 3 del uso del loop for
lista3 = [1, 2, 3, 4, 5]
mi_valor = 0 

for y in lista3:
    mi_valor = mi_valor + y
    print(mi_valor)
    
#%%
# Ejemplo 4 del uso del loop for

palabra = "hola"

for letra in palabra:
    print(letra)
    
#%%
# Ejemplo 5 del uso del loop for

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
    
for a in [[1,2],[3,4],[5,6]]:
    print(a)

#%%
#ejemplo 6 de uso del loop for

dic = {"a":1, "b":2, "c":3}

for item in dic.values():
    print(item)

for item in dic.keys():
    print(item)
# %%
