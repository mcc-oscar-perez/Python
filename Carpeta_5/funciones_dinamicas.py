# def chequear_3_cifras(numero):
#     return numero in range(100,1000)

# resultado = chequear_3_cifras(658)
# print(resultado)


# def chequear_3_cifras(lista):
#     for n in lista:
#         if n in range(100,1000):
#             return True
#         else:
#             pass
#     return False
        
# resultado = chequear_3_cifras([55,99,6000])
# print(resultado)

def chequear_3_cifras(lista):
    
    lista_vacia = []
    
    for n in lista:
        if n in range(100,1000):
            lista_vacia.append(n)
        else:
            pass
    return lista_vacia
        
resultado = chequear_3_cifras([555,99,600])
print(resultado)


