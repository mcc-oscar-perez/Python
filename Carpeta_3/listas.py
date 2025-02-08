mi_lista = ["a", "b", "c"]
otra_lista = ["hola",55,6.1]
mi_ultima_lista = mi_lista + otra_lista
lista_desordenada = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
mi_ultima_lista[0] = "alfa"
mi_ultima_lista.append("beta")
eliminado = mi_ultima_lista.pop(0)
lista_desordenada.sort()
lista_desordenada.reverse()

print(type(mi_lista))
print(len(mi_lista))
print(mi_ultima_lista)
print(eliminado)
print(lista_desordenada)




