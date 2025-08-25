# Diccionarios
# Dictionaries

#%%
diccionario = {'c1': 'valor1', 'c2': 'valor2', 'c3': 'valor3'}
print(diccionario)

#%%
restultado = diccionario['c2']
print(restultado)

#%%
cliente = {"nombre": "Juan", "edad": 28, "direccion": "Calle 13 # 12-34"}
restultado2 = cliente['edad']
print(restultado2) 

#%%
dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1":100, "s2":200}}
print(dic['c2'][1])

#%%
dic2 = {"c1": ["a", "b","c"], "c2": ["d", "e","f"]}
print(dic2["c2"][1].upper())

#%%
diccionario['c4'] = 'valor4'
print(diccionario)

#%%
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
# %%
