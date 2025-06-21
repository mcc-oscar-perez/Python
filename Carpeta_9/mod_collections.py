"""Aqui ponderemos a prueba algunas librerias"""
#%%
from collections import Counter

numeros = [8,2,5,2,1,6,3,5,4,8,2,0,3,9,8,8,5,7,1,3]
frase = " al pan pan y al vino vino"

print(Counter(numeros))
print(Counter("mississippi"))
print(Counter(frase.split()))

print(" ")
serie = Counter([1,2,2,3,4,4,6,4,2,1,1,2,4,3,5,6,7,7,6,7,6,5,4,3])
print(serie.most_common(1))
print(list(serie))

#%%
from collections import defaultdict

diccionario = {'uno': 'verde','dos': 'azul','tres': 'rojo' }
print(diccionario['dos'])

diccionario2 = defaultdict(lambda: 'nada')

diccionario2['uno'] = 'verde'
print(diccionario2['dos'])
print(diccionario2)
# %%
from collections import namedtuple

mi_tupla =(500,18,65)
print(mi_tupla[1])

persona = namedtuple('Persona',['nombre','altura', 'peso'])
ariel = persona('Kevin', 1.75, 75)
print(ariel.altura)
# %%
# Practical excercise 

#1 
from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)

#2
from collections import defaultdict

mi_diccionario = defaultdict(lambda:"Valor no hallado")
mi_diccionario["edad"] = 44

#3
from collections import deque
lista_ciudades= deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])