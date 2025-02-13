# Enumerar
# Enumerate

#%%
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0 

for x in lista:
    print(indice, x) # Imprime el índice y el valor
    indice += 1 # Incrementa el índice
#%%

lista = ["a", "b", "c"]    

for indice, item in enumerate(lista):
    print(type(lista))
    print(lista)
    print(indice, item) # Imprime el índice y el valor
#%%
    
# explicacion 
# pasamos de un lista asi
nombres = ['Ana', 'Carlos', 'Beatriz', 'David']

# a un lista asi
[(0, 'Ana'), (1, 'Carlos'), (2, 'Beatriz'), (3, 'David')]

#ejemplo rapido 
lista_indices = list(enumerate("Python"))
print(lista_indices) 
# %%